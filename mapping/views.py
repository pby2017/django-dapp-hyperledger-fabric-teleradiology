from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from django.urls import reverse, reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from mapping.models import *

import requests, json

class MedimageLV(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    model = Medimage
    template_name = 'mapping/medimage_all.html'
    context_object_name = 'medimages'

class BeforeLV(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    template_name = 'mapping/medimage_before.html'
    context_object_name = 'medimages'
    paginate_by = 7

    def get_queryset(self, *args, **kwargs):
        return Medimage.objects.filter(requesterID=self.request.user.id, progress=0)

class AfterLV(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    model = Medimage
    template_name = 'mapping/medimage_after.html'
    context_object_name = 'medimages'
    paginate_by = 7

    def get_queryset(self, *args, **kwargs):
        return Medimage.objects.filter(requesterID=self.request.user.id, progress=1)

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    model = Medimage
    template_name = 'mapping/medimage_form.html'
    fields = ['emr_file', 'dicom_jpg_file', 'pacs_file',
              'progress',
              'examination_name', 'examination_type',
              'examination_site', 'examination_regnum',
              'patient_id']
    # initial = {'slug': 'auto-filling-by-title'}
    success_url = reverse_lazy('mapping:index')
    
    def form_valid(self, form):  # self.request
        form.instance.owner = self.request.user
        form.instance.requesterID = self.request.user.id
        return super(PostCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['userid'] = self.request.user.id
        return context

class MedimageDV(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'

    model = Medimage
    template_name = 'mapping/medimage_detail.html'
    context_object_name = 'medimages'

    def render_to_response(self, context, **response_kwargs):
        context = {}
        medimage = None
        medimage_pk = self.kwargs['pk']

        try:
            medimage = Medimage.objects.get(pk=medimage_pk)
        except Medimage.DoesNotExist:
            print('objects.get DoesNotExist')
        except:
            print('objects.get except')

        try:
            url = "http://112.153.180.246:8000/get_tuna/"+str(medimage_pk)
            result = requests.get(url)
            context['medimage_opinion'] = json.loads(result.text)['opinion']
            context['medimages'] = medimage
            print(json.loads(requests.get(url).text)['opinion'])
        except ConnectionError:
            context['medimage_opinion'] = "서버 연결 실패"
            context['medimages'] = medimage
        except ValueError:
            print('ValueError')
            context['medimage_opinion'] = "현재 소견 없음"
            context['medimages'] = medimage
        except:
            print('other except')
            context['medimage_opinion'] = "서버 연결 실패"
            context['medimages'] = medimage

        return self.response_class(
        request = self.request,
        template = self.get_template_names(),
        context = context,
        **response_kwargs
        )
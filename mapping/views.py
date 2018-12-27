from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from django.urls import reverse, reverse_lazy

from mapping.models import *

import requests, json

#--- ListView


class MedimageLV(ListView):
    model = Medimage
    template_name = 'mapping/medimage_all.html'
    context_object_name = 'medimages'

class BeforeLV(ListView):
    template_name = 'mapping/medimage_before.html'
    context_object_name = 'medimages'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        return Medimage.objects.filter(requesterID=self.kwargs['requesterID'], progress=0)

class AfterLV(ListView):
    model = Medimage
    template_name = 'mapping/medimage_after.html'
    context_object_name = 'medimages'
    paginate_by = 3

    def get_queryset(self, *args, **kwargs):
        return Medimage.objects.filter(requesterID=self.kwargs['requesterID'], progress=1)

class PostCreateView(CreateView):
    model = Medimage
    template_name = 'mapping/medimage_form.html'
    fields = ['requesterID',
              'emr_file', 'dicom_jpg_file', 'pacs_file',
              'progress',
              'examination_name', 'examination_type',
              'examination_site', 'examination_regnum',
              'patient_id']
    # initial = {'slug': 'auto-filling-by-title'}
    success_url = reverse_lazy('mapping:index')

    def form_valid(self, form):  # self.request
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)

class MedimageDV(DetailView):
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
            url = "http://59.29.224.87:8000/get_tuna/"+str(medimage_pk)
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
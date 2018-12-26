from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from django.urls import reverse, reverse_lazy

from mapping.models import *

#--- ListView


class MedimageLV(ListView):
    # model = get_list_or_404(Medimage,)
    model = Medimage
    template_name = 'mapping/medimage_all.html'
    context_object_name = 'medimages'

#--- ListView

class BeforeLV(ListView):
    # model = Medimage.objects.filter(requesterID=1)
    # model = get_object_or_404(Medimage)
    # model = Medimage.objects.order_by('requesterID')
    # model = get_object_or_404(Medimage, pk=1)
    # model = Medimage
    template_name = 'mapping/medimage_before.html'
    context_object_name = 'medimages'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        return Medimage.objects.filter(requesterID=self.kwargs['requesterID'])

#--- ListView
class AfterLV(ListView):
    model = Medimage
    template_name = 'mapping/medimage_after.html'
    context_object_name = 'medimages'
    paginate_by = 5

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

    def form_valid(self, form): # self.request
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)
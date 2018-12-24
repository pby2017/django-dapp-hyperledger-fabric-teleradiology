from __future__ import unicode_literals # Python 2.x 지원용
from django.utils.encoding import python_2_unicode_compatible
from django.utils.text import slugify

from django.db import models
from django.urls import reverse

from mapping.fields import ThumbnailImageField

from django_unixdatetimefield import UnixDateTimeField

# Create your models here.

@python_2_unicode_compatible # Python 2.x 지원용
class Medimage(models.Model):
    requesterID = models.IntegerField('Requester ID')
    # request_time = models.DateTimeField('Request Date', auto_now_add=True)
    request_time = UnixDateTimeField('Request Date', auto_now_add=True)
    shooting_time = models.DateTimeField('Shooting Date', auto_now=True)
    emr_file = models.FileField('EMR File', blank=True)
    dicom_jpg_file = ThumbnailImageField('PACS File', upload_to='medimage/%Y/%m')
    pacs_file = models.FileField('PACS File', blank=True)
    progress = models.CharField('Viewing Progress', max_length=50)
    examination_name = models.CharField('Examination Name', max_length=50)
    examination_type = models.CharField('Examination Type', max_length=50)
    examination_site = models.CharField('Examination Site', max_length=50, blank=True)
    examination_regnum = models.IntegerField('Examination Register Number', unique=True)
    patient_id = models.CharField('Patient ID', max_length=50)

    def __str__(self):
        return self.examination_name
    
    def get_absolute_url(self):
        return reverse('mapping:medimage_detail', args=(self.id,))
    
    # def get_previous_post(self):
    #     return self.get_previous_by_modify_date()
    
    # def get_next_post(self):
    #     return self.get_next_by_modify_date()
        
    def save(self, *args, **kwargs):
        super(Medimage, self).save(*args, **kwargs)
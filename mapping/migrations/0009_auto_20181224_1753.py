# Generated by Django 2.1.4 on 2018-12-24 17:53

from django.db import migrations
import mapping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mapping', '0008_auto_20181224_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medimage',
            name='dicom_jpg_file',
            field=mapping.fields.ThumbnailImageField(upload_to='medimage/%Y/%m'),
        ),
    ]
# Generated by Django 2.1.7 on 2019-06-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='adhar_no',
            new_name='aadhar_no',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='adhar_image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='dl_image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='gstin_image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='other_image',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='pan_image',
        ),
        migrations.AddField(
            model_name='customer',
            name='aadhar_doc',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customer',
            name='dl_doc',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customer',
            name='gstin_doc',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customer',
            name='other_doc',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='customer',
            name='pan_doc',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]

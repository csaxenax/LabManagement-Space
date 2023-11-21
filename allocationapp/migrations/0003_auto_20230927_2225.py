# Generated by Django 3.2 on 2023-09-27 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocationapp', '0002_approverusermodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProjectsModel',
        ),
        migrations.AddField(
            model_name='allocationdetailsmodel',
            name='DeallocatedBy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='allocationdetailsmodel',
            name='DeallocatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='allocationdetailsmodel',
            name='approvedBy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
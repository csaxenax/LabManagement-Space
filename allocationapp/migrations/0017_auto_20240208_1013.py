# Generated by Django 3.2 on 2024-02-08 04:43

import allocationapp.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('allocationapp', '0016_boardallocationdatamodeltrackdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allocationdetailsmodel',
            name='DeallocatedDate',
        ),
        migrations.AddField(
            model_name='allocationdetailsmodel',
            name='RequestedBy',
            field=djongo.models.fields.ArrayField(blank=True, model_container=allocationapp.models.AllocatedToModel, null=True),
        ),
        migrations.AddField(
            model_name='allocationdetailsmodel',
            name='RequestedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='allocationdetailsmodel',
            name='deallocatedDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
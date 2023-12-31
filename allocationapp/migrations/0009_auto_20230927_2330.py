# Generated by Django 3.2 on 2023-09-27 18:00

from django.db import migrations, models

# def set_deallocated_fields(apps, schema_editor):
#     AllocationDetailsModel = apps.get_model('allocationapp', 'AllocationDetailsModel')
#     for allocation in AllocationDetailsModel.objects.all():
#         allocation.DeallocatedBy = {}  # Set the field to an empty dictionary
#         allocation.DeallocatedDate = {} # Set the field to the current datetime
#         allocation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('allocationapp', '0008_auto_20230927_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='allocationdetailsmodel',
            name='DeallocatedBy',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='allocationdetailsmodel',
            name='DeallocatedDate',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        # migrations.RunPython(set_deallocated_fields),
    ]

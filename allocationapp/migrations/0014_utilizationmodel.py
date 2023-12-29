# Generated by Django 3.2 on 2023-12-22 05:39

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('allocationapp', '0013_boardallocationdatamodel_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='UtilizationModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('WorkWeek', models.CharField(blank=True, max_length=20)),
                ('Lab', models.CharField(blank=True, max_length=255)),
                ('Lab_Details', models.CharField(max_length=50)),
                ('Bench', djongo.models.fields.JSONField(blank=True, null=True)),
                ('Program', models.CharField(blank=True, max_length=100)),
                ('SKU', models.CharField(blank=True, max_length=100)),
                ('Function', models.CharField(blank=True, max_length=255)),
                ('Vendor', models.CharField(blank=True, max_length=255)),
                ('Planned_Utilization', models.FloatField(default=0)),
                ('Actual_Utilization', models.FloatField(default=0)),
                ('Actual_utilization_in_percentage', models.CharField(blank=True, max_length=255, null=True)),
                ('Utilization_Percentage', models.CharField(blank=True, max_length=255, null=True)),
                ('Allocated_POC', models.CharField(max_length=100)),
                ('Remarks', models.CharField(blank=True, max_length=255)),
                ('Createdby', models.CharField(blank=True, max_length=255)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('Modifiedby', models.CharField(blank=True, max_length=255)),
                ('ModifiedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('Deletedby', models.CharField(blank=True, max_length=255)),
                ('DeletedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('isDeleted', models.BooleanField(default=False)),
            ],
        ),
    ]

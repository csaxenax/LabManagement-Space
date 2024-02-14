# Generated by Django 3.2 on 2024-02-13 07:11

import allocationapp.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('allocationapp', '0017_auto_20240208_1013'),
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Subject', models.CharField(blank=True, max_length=100, null=True)),
                ('Content', models.CharField(blank=True, max_length=100, null=True)),
                ('BroadCast_by', djongo.models.fields.ArrayField(blank=True, model_container=allocationapp.models.AllocatedToModel, null=True)),
                ('CreatedDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('User_mail_list', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

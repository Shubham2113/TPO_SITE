# Generated by Django 2.2.4 on 2021-05-30 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TPO_App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=10, unique=True)),
                ('passing_year', models.PositiveIntegerField()),
                ('branch', models.CharField(blank=True, choices=[('CS', 'computer_science'), ('ME', 'mechanical'), ('EE', 'electrical'), ('ECE', 'electronics_comm'), ('IT', 'information_technology')], default='CS', max_length=10)),
                ('course', models.CharField(choices=[('BTECH', 'bachelors_tech'), ('MTECH', 'masters_tech'), ('MBA', 'masters_management'), ('BBA', 'bachelors_business'), ('BCA', 'bachelors_application')], default='BTECH', max_length=5)),
                ('college', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=30)),
                ('father_number', models.PositiveSmallIntegerField()),
                ('mother_number', models.PositiveSmallIntegerField()),
                ('phone_number', models.PositiveSmallIntegerField()),
                ('address', models.CharField(max_length=80)),
                ('city', models.CharField(max_length=20)),
                ('pincode', models.PositiveSmallIntegerField()),
                ('state', models.CharField(max_length=20)),
                ('alternate_gmail', models.EmailField(max_length=254, unique=True)),
                ('gender', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

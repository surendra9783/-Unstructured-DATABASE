# Generated by Django 4.0.5 on 2022-06-02 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TA_ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ta_user', models.CharField(default='NV', max_length=200)),
                ('ta_entry', models.CharField(default='NV', max_length=200)),
                ('ta_course', models.CharField(default='NV', max_length=200)),
                ('reco_by', models.CharField(default='NV', max_length=200)),
                ('ldap_id', models.CharField(default='NV', max_length=200)),
                ('comments_by', models.CharField(default='NV', max_length=200)),
                ('supervisor_0', models.CharField(default='NV', max_length=200)),
                ('supervisor_1', models.CharField(default='NV', max_length=200)),
                ('supervisor_2', models.CharField(default='NV', max_length=200)),
                ('src_form', models.CharField(default='NV', max_length=200)),
                ('src_1', models.CharField(default='NV', max_length=200)),
                ('src_2', models.CharField(default='NV', max_length=200)),
                ('chair_name', models.CharField(default='NV', max_length=200)),
                ('topic_n', models.CharField(default='NV', max_length=200)),
                ('roll_nos', models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TA_shipnew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_data', models.JSONField(blank=True, null=True)),
            ],
        ),
    ]
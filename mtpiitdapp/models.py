from django.db import models
from djongo.models import JSONField, DjongoManager
import json
import uuid
class TA_shipnew(models.Model):
    ta_id = models.AutoField
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meta_data = models.JSONField(default={
      "name": "some",
      "age": "",
      "ta_entry": "",
      "courses": "some",
      "details": [
        {
          "grade": "",
          "year": "",
          "stauts":"",
          "roll_no": ""
        }
      ],
      "other_details": [
        {
          "TA_ship": "some",
          "TA_courses": "some"
        }
      ]
    },blank=True, null=True)

class MS_Student(models.Model):
    ms_id = models.AutoField
    meta_data = models.JSONField(default={
      "name": "some",
      "age": "",
      "ta_entry": "",
      "courses": "some",
      "details": [
        {
          "grade": "",
          "year": "",
          "stauts":"",
          "roll_no": ""
        }
      ],
      "other_details": [
        {
          "TA_ship": "some",
          "TA_courses": "some"
        }
      ]
    }, blank=True, null=True)

class PHD_Student(models.Model):
    phd_id = models.AutoField
    meta_data = models.JSONField(default={
      "name": "some",
      "age": "",
      "ta_entry": "",
      "courses": "some",
      "details": [
        {
          "grade": "",
          "year": "",
          "stauts":"",
          "roll_no": ""
        }
      ],
      "other_details": [
        {
          "TA_ship": "some",
          "TA_courses": "some"
        }
      ]
    }, blank=True, null=True)

class Mtech_Student(models.Model):
    mtech_id = models.AutoField
    meta_data = models.JSONField(default={
      "name": "some",
      "age": "",
      "ta_entry": "",
      "courses": "some",
      "details": [
        {
          "grade": "",
          "year": "",
          "stauts":"",
          "roll_no": ""
        }
      ],
      "other_details": [
        {
          "TA_ship": "some",
          "TA_courses": "some"
        }
      ]
    }, blank=True, null=True)

class Btech_Student(models.Model):
    btech_id = models.AutoField
    meta_data = models.JSONField(default={
      "name": "some",
      "age": "",
      "ta_entry": "",
      "courses": "some",
      "details": [
        {
          "grade": "",
          "year": "",
          "stauts":"",
          "roll_no": ""
        }
      ],
      "other_details": [
        {
          "TA_ship": "some",
          "TA_courses": "some"
        }
      ]
    }, blank=True, null=True)


class TA_ship(models.Model):
    # ta_id = models.AutoField
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ta_user = models.CharField(max_length=200,blank=True, null=True)
    ta_entry = models.CharField(max_length=200,blank=True, null=True)
    ta_course = models.CharField(max_length=200,blank=True, null=True)
    reco_by = models.CharField(max_length=200,blank=True, null=True)
    ldap_id = models.CharField(max_length=200,blank=True, null=True)
    comments_by = models.CharField(max_length=200,blank=True, null=True)
    supervisor_0 = models.CharField(max_length=200,blank=True, null=True)
    supervisor_1 = models.CharField(max_length=200,blank=True, null=True)
    supervisor_2 = models.CharField(max_length=200,blank=True, null=True)
    src_form = models.CharField(max_length=200,blank=True, null=True)
    src_1 = models.CharField(max_length=200,blank=True, null=True)
    src_2 = models.CharField(max_length=200,blank=True, null=True)
    chair_name = models.CharField(max_length=200,blank=True, null=True)
    topic_n = models.CharField(max_length=200,blank=True, null=True)
    roll_nos = models.JSONField(default={
        'new_data': 'some text',
        'new_data1': 'some text',
        'new_data2': 'some text',
        'new_data3': 'some text',
    },blank=True, null=True)

class TA_ship_i(models.Model):
    ta_id = models.AutoField
    ta_user = models.CharField(max_length=200)
    ta_entry = models.CharField(max_length=200)
    ta_course = models.CharField(max_length=200)

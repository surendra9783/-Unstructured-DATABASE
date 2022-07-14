import subprocess
from mtpiitdapp.models import TA_ship,TA_shipnew,MS_Student, PHD_Student,Mtech_Student,Btech_Student
from PyPDF2 import PdfFileReader
from bs4 import BeautifulSoup
import pandas
import json
import csv
import json
from django.shortcuts import render, redirect
from django.http import HttpResponse
from subprocess import run, PIPE
import sys
from django.conf import settings
# Create your views here.
def importtoxsl(request):
    if request.method =='POST':
        file = request.FILES['files']
        path = file.file
        print(f'{settings.BASE_DIR}/{path}')
        excel_data_df = pandas.read_excel(file)
        json_str = excel_data_df.to_json(orient='records')
        # print('Excel Sheet to JSON:\n', json_str)
        thisisjson_dict = json.loads(json_str)
        json_data = {"student_info": thisisjson_dict}
        # print('Excel Sheet to JSON:\n', json_data)
        for i in json_data['student_info']:
            if (i['ta_entry'] != None):
                p = TA_shipnew(meta_data=i)
                p.save()
                print(i)
                print("\n")
    print('succeses')
    return redirect("admin/mtpiitdapp/importintota_ship/")

def importtocsv(request):
    if request.method =='POST':
        file = request.FILES['files']
        path = file.file
        excel_data_df = pandas.read_csv(file)
        json_str = excel_data_df.to_json(orient='records')
        # print('Excel Sheet to JSON:\n', json_str)
        thisisjson_dict = json.loads(json_str)
        json_data = {"student_info": thisisjson_dict}
        # print('Excel Sheet to JSON:\n', json_data)
        for i in json_data['student_info']:
            if (i['ta_entry'] != None):
                p = TA_shipnew(meta_data=i)
                p.save()
                print(i)
                print("\n")

    print('succeses')
    return redirect("admin/mtpiitdapp/importintota_ship/")

def importtopdf(request):
    if request.method =='POST':
        file = request.FILES['files']
        path = file.file
    p = TA_shipnew(meta_data={
      "name": "HIMANI RAINA",
      "ta_entry": "2016CSY8515",
      "details":"The DRC approves the MS (R) full-time to part-time conversion of HIMANI RAINA(2016CSY8515)."
    })
    p.save()
    p = TA_shipnew(meta_data={
        "name": " PRAJNA UPADHYAY",
        "ta_entry": "2013CSZ8110",
        "details": "The DRC approves the request of Prof. Maya Ramanath to pay Ph.D. student PRAJNAUPADHYAY (2013CSZ8110) from her project RP03677F starting from June 1, 2019 to Dec. 31,2019."
    })
    p.save()
    p = TA_shipnew(meta_data={
        "name": "ABHISHEK ROSE",
        "ta_entry": "2017CSZ8584",
        "details": "The DRC approves the request for comprehensive deadline extension of ABHISHEK ROSE(2017CSZ8584) by 6 months"
    })
    p.save()
    p = TA_shipnew(meta_data={
        "name": "MADHUKAR YERRAGUNTLA",
        "ta_entry": "2016CSZ8230",
        "details": "The DRC approves the request for comprehensive deadline extension of MADHUKAR YERRAGUNTLA (2016CSZ8230) by 6 months. It was observed that this part-time students problem statement changed which has necessitated the extension"
    })
    p.save()
    p = TA_shipnew(meta_data={
        "name": "NIKHIL KUMAR ",
        "ta_entry": "2014CSZ8210",
        "details": "The DRC approves the request of NIKHIL KUMAR (2014CSZ8210) to convert from full-time to part-time."
    })
    p.save()
    p = TA_shipnew(meta_data={
        "name": "VINAYAK GUPTA",
        "ta_entry": "2017CSZ8063",
        "details": "VINAYAK GUPTA (2017CSZ8063) has completed the comprehensive requirements for Ph.D.in CSE and has passed both the oral and the written test"
    })
    p.save()
    p = TA_shipnew(meta_data={
        "name": "NITIN RAKHEJA",
        "ta_entry": "",
        "details": "The DRC approved the change in the primary supervisor of NITIN RAKHEJA () from Prof. Vinay Ribeiro to Prof. Huzur Saran. The DRC observed that Prof. Ribeiro continues to be a cosupervisor. "
    })
    p.save()
    print('succeses')
    return redirect("admin/mtpiitdapp/importintota_ship/")




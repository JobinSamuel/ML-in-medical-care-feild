from collections import defaultdict

from io import TextIOWrapper
import csv

from django.shortcuts import render
from django.http import HttpResponse
from patient.models import patientModel
from patient.forms import patientForm
from doctor.models import doctorModel, storedatamodel
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
from django_pandas.io import read_frame
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn import datasets


def logout(request):
    return render(request, "index.html")

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upasswd']
        if uname =='admin' and passwd=='admin':
            return render(request,"admin/adminloginentered.html")
        else:
            return HttpResponse("invalied credentials")
    return render(request, "admin/adminloginentered.html")

def doctordetails(request):
    qs=doctorModel.objects.all()
    return render(request,'admin/doctordetails.html',{"object":qs})

def patientdetails(request):
    qs=patientModel.objects.all()
    return render(request,'admin/patientdetails.html',{"object":qs})


def activatedoctor(request):
    if request.method == 'GET':
        uname = request.GET.get('pid')
        print(uname)
        status = 'Activated'
        print("pid=", uname, "status=", status)
        doctorModel.objects.filter(id=uname).update(status=status)
        qs = doctorModel.objects.all()
        return render(request,"admin/doctordetails.html", {"object": qs})

def activatepatient(request):
    if request.method == 'GET':
        uname = request.GET.get('pid')
        print(uname)
        status = 'Activated'
        print("pid=", uname, "status=", status)
        patientModel.objects.filter(id=uname).update(status=status)
        qs = patientModel.objects.all()
        return render(request, 'admin/patientdetails.html', {"object": qs})

def storecsvdata(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        csvfile =TextIOWrapper( request.FILES['file'])
        columns = defaultdict(list)

        storecsvdata =csv.DictReader(csvfile)

        for row1 in storecsvdata:
                Pregnancies = row1["Pregnancies"]
                Glucose = row1["Glucose"]
                BloodPressure = row1["BloodPressure"]
                SkinThickness = row1["SkinThickness"]
                Insulin = row1["Insulin"]
                DiabetesPedigreeFunction = row1["DiabetesPedigreeFunction"]
                Age = row1["Age"]
                BMI = row1["BMI"]
                Outcome = row1["Outcome"]

                storedatamodel.objects.create(Pregnancies=Pregnancies, Glucose=Glucose, BloodPressure=BloodPressure,
                                                SkinThickness=SkinThickness, Insulin=Insulin,BMI=BMI,DiabetesPedigreeFunction=DiabetesPedigreeFunction,Age=Age,Outcome=Outcome)

        print("Name is ",csvfile)
        return HttpResponse('CSV file successful uploaded')
    else:

        return render(request, 'admin/storecsvdata.html', {})

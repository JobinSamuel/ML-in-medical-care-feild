from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from doctor import views as doctor
from patient import views as patient
from Medicalcare import views as medical
from hsp import views as hsp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', doctor.index, name='index'),
    path('logout/',medical.logout,name='logout'),
    path('admin1/', medical.adminlogin, name='admin1'),
    path('adminloginentered/', medical.adminloginentered, name='adminloginentered'),
    path('doctordetails/', medical.doctordetails, name='doctordetails'),
    path('patientdetails/', medical.patientdetails, name='patientdetails'),
    path('activatedoctor/',medical.activatedoctor,name='activatedoctor'),
    path('activatepatient/',medical.activatepatient,name='activatepatient'),
    path('storecsvdata/',medical.storecsvdata,name='storecsvdata'),
    path('svm/',medical.svm,name='svm'),
    path('decision/',medical.decision,name='decision'),


    path('hsplogin/', hsp.hsplogin, name='hsplogin'),
    path('hsploginentered/', hsp.hsploginentered, name='hsploginentered'),
    path('uploadpatientdata/', hsp.uploadpatientdata,name='uploadpatientdata'),
    path('viewpatientdata/', hsp.viewpatientdata,name='viewpatientdata'),



    path('doctorlogin/',doctor.doctorlogin,name='doctorlogin'),
    path('doctorregister/',doctor.doctorregister,name='doctorregister'),
    path('doctorlogincheck/',doctor.doctorlogincheck,name='doctorlogincheck'),
    path('doctorviewpatientdata/',doctor.doctorviewpatientdata,name='doctorviewpatientdata'),
    path('addtreatment/',doctor.addtreatment,name='addtreatment'),


    path('patientlogin/',patient.patientlogin,name='patientlogin'),
    path('patientregister/',patient.patientregister,name='patientregister'),
    path('patientlogincheck/',patient.patientlogincheck,name='patientlogincheck'),
    path('treatment/',patient.treatment,name='treatment'),
    path('patienttreatmentresult/',patient.patienttreatmentresult,name='patienttreatmentresult'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

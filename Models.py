from django.db import models


class doctorModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    specialization = models.CharField(max_length=50, default="", editable=True)
    status = models.CharField(max_length=40, default="", editable=True)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='doctorregister'



class storedatamodel(models.Model):

    Pregnancies = models.CharField(max_length=500)
    Glucose = models.CharField(max_length=300)
    BloodPressure = models.CharField(max_length=300)
    SkinThickness = models.CharField(max_length=300)
    Insulin = models.CharField(max_length=255)
    BMI = models.CharField(max_length=255)
    DiabetesPedigreeFunction = models.CharField(max_length=255)
    Age = models.CharField(max_length=255)
    Outcome = models.CharField(max_length=255)


    def __str__(self):
        return self.Pregnancies,self.Glucose,self.BloodPressure,self.SkinThickness,self.Insulin,self.BMI,self.DiabetesPedigreeFunction,self.Age,self.Outcome

from django.db import models

# Create your models here.
class Report(models.Model):
    location=(('Corporate Headoffice','Corporate Headoffice'),
              ('Operations Department', 'Operations Department'),
              ('Work Station','Work Station'),
              ('Marketing Division','Marketing Division') )
    location=models.CharField(max_length=50, choices=location,default="Corporate Headoffice")
    department = models.TextField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    incidentlocation = models.TextField(max_length=500)
    saverity=(('Mild','Mild'),
              ('Moderate', 'Moderate'),
              ('Severe','Severe'),
              ('Fatal','Fatal') )
    saverity = models.CharField(max_length=50,choices=saverity,default="Mild")
    cause = models.TextField(max_length=500)
    actiontaken = models.TextField(max_length=500)
    enviromentalincident = models.BooleanField(default=False)
    injuryillness = models.BooleanField(default=False)
    propertydamage = models.BooleanField(default=False)
    vehicle = models.BooleanField(default=False)

# def __str__(self):
#     return self.location





    
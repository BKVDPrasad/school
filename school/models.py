from django.db import models

class PAS_S40_Institution(models.Model):
    S40_Instition_Id = models.BigAutoField(primary_key=True)
    S40_Instition_Name = models.CharField(max_length=100)
    S40_Instition_Type = models.CharField(max_length=30,null=True,blank=True)
    S40_Has_Branches_flag = models.BooleanField()
    S40_Email_Id = models.EmailField(blank=True,null=True)
    S40_Mobile_Number = models.PositiveBigIntegerField(blank=True,null=True)
    S40_Landline_Number = models.IntegerField(blank=True,null=True)
    S40_Tagline = models.CharField(max_length=50,blank=True,null=True)
    S40_Instition_Logo = models.FileField(blank=True,null=True,upload_to='InstitutionImages/')
    S40_Founder_Logo = models.FileField(blank=True,null=True,upload_to='InstitutionImages/')
    S40_Document_Path = models.FileField(upload_to='Alumbs/',blank=True,null=True)
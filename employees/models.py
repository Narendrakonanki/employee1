from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    dept=models.CharField(max_length=20)
    salary=models.DecimalField(max_digits=10,decimal_places=2)
    phone=models.IntegerField(null=True)

    def __str__(self):
        return(self.name)
        


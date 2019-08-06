from django.db import models

# Create your models here.

# small id is a reserved column for the auto incremented
# Always write variable name is small alphabet
class Equipment(models.Model):
    AutoId = models.AutoField(primary_key=True)
    Id = models.CharField(max_length=50,default="")
    Description = models.CharField(max_length=50,default="")
    ActiveStatus = models.BooleanField(default=False)


    def __str__(self):
        return self.Id


class EquipmentProp(models.Model):
    propId = models.CharField(max_length=50, default='')
    propDesc = models.CharField(max_length=50,default='')
    propValue = models.CharField(max_length=50,default='')
    propUOM = models.CharField(max_length=50,default='')
    propAS = models.BooleanField(default=False)
    equipId = models.ForeignKey(Equipment,on_delete=True)

    def __str__(self):
        return self.propId

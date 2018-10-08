from django.db import models

def upload_note_image(instance, filename):
    return "notes/{filename}".format(filename=filename)

#models are nothing but tables in django
#based upon the model, django creates the tables for you
#you have to specify all the fields in the table


# Create your models here.
class Notes(models.Model):
    title        = models.TextField(blank=False,null=False)
    content     = models.TextField(blank=False,null=False)
    image       = models.FileField(upload_to=upload_note_image,blank=False,null= False)

    def __str__(self):
        return self.title
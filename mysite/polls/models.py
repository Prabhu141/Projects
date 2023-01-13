from django.db import models
# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='pdfs/')

    
    def __str__(self):
        return self.description

    def delete(self, *args, **kwargs):
        if self.document:
            self.document.delete()
            super().delete(*args, **kwargs)
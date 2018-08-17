from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=140)
    image = models.ImageField(upload_to='images/')
    pub_date = models.DateTimeField(auto_now=True)
    text = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:30]

    def updatetime(self):
        return self.pub_date.strftime('%b %e %Y')

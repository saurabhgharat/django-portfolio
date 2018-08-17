from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    sender = models.EmailField()

    time = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return 'Message for {}'.format(self.sender)

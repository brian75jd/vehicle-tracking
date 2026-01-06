from django.db import models
from django.contrib.auth.models import User

class SendMessage(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    email = models.EmailField(blank=False,null=False,default='noemail@gmail.com')
    date_Sent = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return f"{self.sender.username} sent a message at {self.date_Sent}"

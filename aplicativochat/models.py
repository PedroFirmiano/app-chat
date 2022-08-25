from django.db import models
from django.contrib.auth.models import User

import uuid


class Group(models.Model):
  groupId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  lastModificated = models.DateTimeField()




class Message(models.Model):
  messageId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  message = models.TextField()
  date = models.DateTimeField()
  userSend = models.ForeignKey(User, on_delete=models.CASCADE)
  groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
  

class Contacts(models.Model):
  userId = models.ForeignKey(User, on_delete=models.CASCADE)
  groupId = models.ForeignKey(Group, on_delete=models.CASCADE)


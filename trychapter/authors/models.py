from django.db import models

class Author(models.Model):
    user = models.ForeignKey(User)

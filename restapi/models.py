from django.db import models


class User(models.Model):
    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)

    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    age = models.IntegerField()
    sex = models.IntegerField()
    email = models.CharField(max_length=40)

    class Meta:
        db_table = "user"

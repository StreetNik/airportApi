from django.db import models
from django.contrib.auth import get_user_model


class Order(models.Model):
    created_at = models.DateTimeField
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

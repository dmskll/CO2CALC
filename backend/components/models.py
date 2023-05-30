from django.db import models

class Component(models.Model):
    name            = models.TextField(default="pc")
    idle_use_cost   = models.IntegerField()
    max_use_cost    = models.IntegerField()
    build_cost      = models.IntegerField()

class Calculation(models.Model):
    user_name         = models.TextField()
    user_id              = models.IntegerField()
     


        

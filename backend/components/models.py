from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

# class Component(models.Model):
#     #owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
#     name                    = models.TextField()
#     description             = models.TextField(default="desc")
#     idle_power              = models.IntegerField(default=0)
#     bad_case_idle_power     = models.IntegerField(default=0)
#     good_case_idle_power    = models.IntegerField(default=0)
#     max_power               = models.IntegerField(default=0)
#     bad_case_max_power      = models.IntegerField(default=0)
#     good_case_max_power     = models.IntegerField(default=0)
#     cfp                     = models.IntegerField(default=0)
#     cfp_use_phase           = models.IntegerField(default=0)
#     cfp_deviation_standard  = models.IntegerField(default=0)

#     def __str__(self):
#         return f"{self.name}"


class Component(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="components")
    system_component        = models.BooleanField(default=False)
    is_server               = models.BooleanField(default=False)
    name                    = models.CharField(max_length=30)
    description             = models.CharField(max_length=200)
    worse_case               = models.DecimalField(max_digits=5, decimal_places=2,
                                                  validators=[MinValueValidator(0)])
    best_case      = models.DecimalField(max_digits=7, decimal_places=2,
                                                  validators=[MinValueValidator(0)])
    middle_case     = models.DecimalField(max_digits=7, decimal_places=2,
                                                  validators=[MinValueValidator(0)])
    cfp                     = models.DecimalField(max_digits=7, decimal_places=2,
                                                  validators=[MinValueValidator(0)])
    cfp_build_phase           = models.DecimalField(max_digits=7, decimal_places=2,
                                                  validators=[MinValueValidator(0)])
    cfp_deviation_standard  = models.DecimalField(max_digits=7, decimal_places=2,
                                                  validators=[MinValueValidator(0)])

    def __str__(self):
        if self.system_component == True:
            return f"System component - {self.name}"
        else:
            return f"Custom {self.name} by {self.owner.username}"
        
class Calculation(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE,
                              related_name="calculation")
    name                    = models.CharField(max_length=30)
    
    def __str__(self):
        return f"{self.name} by {self.owner.username} "

class ComponentUsage(models.Model):
    component = models.ForeignKey(Component,
                                  on_delete=models.CASCADE,
                                  related_name="usage")
    calculation = models.ForeignKey(Calculation,
                             on_delete=models.CASCADE, 
                             related_name="usage")  
    hours                   = models.IntegerField(validators=[MinValueValidator(0)])
    # use                     = models.IntegerField(validators=[MinValueValidator(0),
    #                                                           MaxValueValidator(100)])
    # Description             = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('component', 'calculation')
    def __str__(self):
        return f" Component {self.component.name} used by {self.calculation.owner.username} "


        

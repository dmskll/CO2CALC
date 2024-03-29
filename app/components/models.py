from django.conf import settings
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Component(models.Model):

    CUSTOM = "CU"
    PC = "PC"
    MONITOR = "MO"
    SERVER = "SE"
    EXTRA = "EX"

    TYPE_CHOICES = [
        (CUSTOM, "Custom"),
        (PC, "Pc"),
        (MONITOR, "Monitor"),
        (SERVER, "Server"),
        (EXTRA, "Extra"),
    ]
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="components"
    )
    system_component = models.BooleanField(default=False)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default=PC)
    description = models.CharField(max_length=200)
    is_server = models.BooleanField(default=False)
    hosted_apps = models.IntegerField(
        default=12, validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    worst_case = models.DecimalField(
        max_digits=5, decimal_places=2, validators=[MinValueValidator(0)]
    )
    best_case = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(0)]
    )
    middle_case = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(0)]
    )
    cfp_build_phase = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(0)]
    )
    cfp_deviation_standard = models.DecimalField(
        max_digits=7, decimal_places=2, validators=[MinValueValidator(0)]
    )

    def __str__(self):
        if self.system_component == True:
            return f"System component - {self.name}"
        else:
            return f"Custom {self.name} by {self.owner.username}"


class Calculation(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="calculation"
    )
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} by {self.owner.username} "


class ComponentUsage(models.Model):
    component = models.ForeignKey(
        Component, on_delete=models.CASCADE, related_name="usage"
    )
    calculation = models.ForeignKey(
        Calculation, on_delete=models.CASCADE, related_name="usage"
    )
    emissions = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1000)]
    )
    hours = models.IntegerField(validators=[MinValueValidator(0)])
    server_years = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(40)]
    )

    def __str__(self):
        return f" Component {self.component.name} used by {self.calculation.owner.username} "

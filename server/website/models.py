from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Profile(models.Model):
#     name = models.CharField(max_length=20)
#     password1 = models.CharField(max_length=20)
#     password2 = models.CharField(max_length=20)
#     email = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     SKI_EXPERIENCE={
#         "FT": "First Time",
#         "GZ": "Green Zone",
#         "BZ": "Blue Zone",
#         "EXZ": "Black Zone",
#     }
#     level = models.CharField(max_length=5, choices=SKI_EXPERIENCE, default="")

#     def __str__(self) -> str:
#         return (f"{self.name}")
    
class Tickets(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False
    )
    SKI_FACILITY={
        "F1": "FACILITY1",
        "F2": "FACILITY2",
        "F3": "FACILITY3",
        "F4": "FACILITY4",
    }
    facility = models.CharField(max_length=5, choices=SKI_FACILITY, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=10)
    quantity = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.facility

    
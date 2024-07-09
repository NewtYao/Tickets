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
# class Facilities(models.Model):
#     name = models.CharField(max_length=255)
#     image = models.ImageField(upload_to='static/facility_images/')


class Tickets(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False
    )
    # facility = models.ForeignKey(
    #     Facilities, 
    #     on_delete=models.CASCADE
    # )
    SKI_FACILITY={
        "F1": "神立雪場",
        "F2": "石打丸山雪場",
        "F3": "苗場雪場",
        "F4": "舞子雪場",
    }
    facility = models.CharField(max_length=5, choices=SKI_FACILITY, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.facility
    
class Facilities(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/facility_images/')

    
from django.db import models

# Create your models here.
class Profile(models.Model):
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)
    SKI_EXPERIENCE={
        "FT": "First Time",
        "GZ": "Green Zone",
        "BZ": "Blue Zone",
        "EXZ": "Black Zone",
    }
    level = models.CharField(max_length=5, choices=SKI_EXPERIENCE, default="FT")

    def __str__(self) -> str:
        return (f"{self.name}")
    
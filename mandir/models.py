from django.db import models
import uuid
import os
from django.core.validators import FileExtensionValidator


# Create your models here.
def upload_gallery_image_video(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join("gallery", filename)

class Gallery(models.Model):
    FILE_CATE = [
        ("video","Video"),
        ("image","Image"),
    ]

    title = models.CharField(max_length=100)
    file_type= models.CharField(max_length=10,choices= FILE_CATE, default= "image")
    
    file = models.FileField(
        upload_to= upload_gallery_image_video,
        validators=[
            FileExtensionValidator(
                allowed_extensions=[
                    "jpg", "jpeg", "png", "webp",
                    "mp4", "mov", "avi", "mkv", "webm"
                ]
            )
        ]
    )

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Event(models.Model):

    EVENT_TYPES = [
        ("festival", "Festival"),
        ("bhajan", "Bhajan Sandhya"),
        ("special", "Special"),
        ("weekly","Weekly")
    ]

    event_name_en = models.CharField(
        max_length=200
    )
    event_name_hi = models.CharField(
        max_length=200
    )
    event_time = models.CharField(
        max_length=200
    )


    event_date = models.DateField()

    event_type = models.CharField(
        max_length=20,
        choices=EVENT_TYPES,
        default="other"
    )

    def __str__(self):
        return f"{self.event_name_en} ({self.event_date})"


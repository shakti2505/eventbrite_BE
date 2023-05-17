from django.db import models

# Create your models here.


class Event(models.Model):
    user_id = models.EmailField(unique=True)
    event_name = models.CharField(max_length=100, help_text="Enter Event Name")
    event_date = models.DateTimeField(null=True, help_text="Enter event date")
    event_location = models.CharField(max_length=100, help_text="Enter event Location")
    event_img = models.ImageField(upload_to="uploads/images", null=False)

    def __str__(self):
        return self.event_name




class Like(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


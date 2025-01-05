from django.db import models


class ToDo(models.Model):
    STATUS_PENDING = 'Pending'
    STATUS_INPROGRESS = 'In-Progress'
    STATUS_COMPLETED = 'Completed'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_INPROGRESS, 'In-Progress'),
        (STATUS_COMPLETED, 'Completed')
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=11, choices=STATUS_CHOICES, default=STATUS_PENDING)

    def __str__(self) -> str:
        return self.title

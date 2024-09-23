from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    STATUS_CHOICES = (
        ("New", "New"),
        ("In Progress", "In Progress"),
        ("Done", "Done"),
    )

    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default = 'New')

    def __str__(self):
        return self.title
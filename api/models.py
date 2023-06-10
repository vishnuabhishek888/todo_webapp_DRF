from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


options = (
    ('open' , 'Open'),
    ('working' , 'Working'),
    ('done' , 'Done'),
    ('overdue' , 'Overdeue'),
)

class ToDo(models.Model):
    timestamp = models.DateField(auto_now=True)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    due_date = models.DateField(blank=True)
    tags = models.CharField( max_length=20, blank=True)
    status = models.CharField(max_length=20,
                              choices=options,
                              default='open',
                              null=False,
                              blank=False
                              )
    def clean(self):
        if self.due_date and self.due_date < self.timestamp:
            raise ValidationError("Due Date cannot be before Timestamp created.")
        
    
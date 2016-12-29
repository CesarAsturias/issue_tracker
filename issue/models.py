from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

STATUS_CODES = ((1, ('Open')),
                (2, ('Working')),
                (3, ('Closed')),)
PRIORITY_CODES = ((1, ('Very High')),
                  (2, ('High')),
                  (3, ('Medium')),
                  (4, ('Low')),)

class Ticket(models.Model):
    """ Trouble ticket class
    
    **Parameters**:
        
        .. data:: title
        
           Title of the ticket
           
        .. data:: asset
        
           Related asset
           
        .. data:: submitter
        
           Ticket creator
           
        .. data:: submitted_date
        
           Ticket creation date
           
        .. data:: modified_date
          
           Ticket modification date
           
        .. data:: closing_date
        
           Ticket closing date
           
        .. data:: assigned_to
        
           Technician in charge
           
        .. data:: description
        
           Trouble ticket description
           
        .. data:: status
        
           Ticket status
           
        .. data:: priority
        
           Ticket priority level
           
           
    """
    title = models.CharField(max_length=100)
    asset = models.ForeignKey('Asset', on_delete=models.CASCADE, )
    submitter = models.ForeignKey('User', on_delete=models.CASCADE, )
    submitted_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    assigned_to = models.ForeignKey('Technician', on_delete=models.CASCADE, )
    description = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS_CODES)
    priority = models.IntegerField(choices=PRIORITY_CODES)
    
                  
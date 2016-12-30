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

COUNTRIES = (('SP', ('Spain')),
             ('PT', ('Portugal')),
             ('FR', ('France')),
             ('IT', ('Italy')),
             ('BE', ('Belgium')),
             ('PO', ('Poland')),
             ('RO', ('Romania')),
             )
MANUFACTURERS = ((1, ('Vestas')),
                 (2, ('Gamesa')),
                 (3, ('Siemens')),
                 (4, ('Alstom')),
                 (5, ('Acciona')),
                 (6, ('GEWE')),
                 (7, ('Navantia')),
                 (8, ('Nordex')),
                 (9, ('Enercon')),)


    
    
class Technician(models.Model):
    """ Techniccian class
    
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    mobile_number = models.IntegerField()

class Asset(models.Model):
    """ Asset class
    
    """
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=2, choices=COUNTRIES)
    manufacturer = models.CharField(max_length=100, choices=MANUFACTURERS)
    windfarm_manager = models.ForeignKey(Technician, on_delete=models.CASCADE,
                                         related_name='windfarm_manager')
    area_manager = models.ForeignKey(Technician, on_delete=models.CASCADE,
                                     related_name='area_manager')
    operated = models.BooleanField()
    scada_support = models.ManyToManyField(Technician, related_name='scada_support')

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
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE, related_name='asset')
    submitter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='submitter')
    submitted_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    assigned_to = models.ManyToManyField(Technician, related_name='assigned_to')
    description = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS_CODES)
    priority = models.IntegerField(choices=PRIORITY_CODES)
    


    

from django.db import models
from django.utils import timezone

class register_club(models.Model):
    club_rep_number = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=50)
    club_address_street = models.CharField(max_length=50)
    club_address_street_num = models.CharField(max_length=50)
    club_address_city = models.CharField(max_length=50)
    club_address_postcode = models.CharField(max_length=50)
    club_contact_land_num = models.CharField(max_length=50)
    club_contact_mobile_num = models.CharField(max_length=50)
    club_rep_fname = models.CharField(max_length=50)
    club_rep_lname = models.CharField(max_length=50)
    club_rep_dob = models.DateField()
    club_rep_Pword = models.CharField(max_length=50)
    
    def __str__(self):
        return self.email
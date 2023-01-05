from django import forms
from UWEflix_APP.models import register_club

class RegisterClubForm(forms.ModelForm):
    class Meta:
        model = register_club
        fields =  ("club_name","club_address_street","club_address_street_num","club_address_city","club_address_postcode","club_contact_land_num","club_contact_mobile_num","club_rep_fname","club_rep_lname","club_rep_dob","club_rep_Pword",)
        labels = {
            'club_name': ('Club Name'),
            "club_address_street":(" Club street address"),
            "club_address_street_num" :("Club address number"),
            "club_address_city" : ("City"),
            "club_address_postcode":("Club Postcode"),
            "club_contact_land_num":("Club landline number"),
            "club_contact_mobile_num":("Club mobile number"),
            "club_rep_fname":("Club rep first name"),
            "club_rep_lname":("club rep last name"),
            "club_rep_dob":("club rep date of birth"),
            "club_rep_Pword":("Club password"),

        }

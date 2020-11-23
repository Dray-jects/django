from django.forms import ModelForm
from .models import contact

class contact_form(ModelForm):
    class Meta:
        model = contact
        fields= ['name','email','subject','message']
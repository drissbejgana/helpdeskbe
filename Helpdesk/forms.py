from django.forms import ModelForm
from .models import *

class Ticketform(ModelForm):
    class Meta:
        model=Ticket
        fields="__all__"




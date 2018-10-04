from .models import Qoute

from django.forms import ModelForm


class Qouteform(ModelForm):
    class Meta:
        model= Qoute
        fields=('title','author','text','picture','created_at','updated_at',)



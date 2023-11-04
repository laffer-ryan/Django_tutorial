from django.forms import ModelForm
from .models import Room


# creates form base on the model Room. Meaning all its required attributes
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participant']
from django.forms import ModelForm
from .models import ListPatPageOne


class ListPatPageOneForms(ModelForm):
    class Meta:
        model = ListPatPageOne
        fields = ('Date', 'OnStartDay', 'Receive', 'TransferFrom', 'TransferTo', 'ReleaseTotal',
                  'RelTotalTo', 'Die', 'Remain')

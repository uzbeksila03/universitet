from django import forms
class .models import *
# #- Vazifa
#     1. Muallif qo’shishni django form orqali qayta bajaring.
#     2. Record qo’shishni djangodagi ModelFormdan foydalanib qayta bajaring.
#     3. Admin qo’shishni django form orqali qayta bajaring.
#     4. Universitet loyihasida Fan qo’shishni django form orqali qayta bajaring.
#     5. Yo’nalish qo’shishni django form orqali qayta bajaring.
#     6. Ustoz qo’shishni django form orqali qayta bajaring.

class FanForm(forms.ModelForm):
    class Meta:
        model = Fan
        fields = '__all__'


class MuallifForm(forms.ModelForm):
    class Meta:
        model = Muallif
        fields = '__all__'

class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = '__all__'
class UstozForm(forms.Form):
    ism = forms.CharField(max_length=255)
    jins = forms.CharField(max_length=10, choices=JINS)
    yosh = forms.PositiveSmallIntegerField()
    daraja = forms.CharField(max_length=50, choices=DARAJA)
    fan = forms.ForeignKey(Fan)

class YonalishForm(forms.Form):
    nom = forms.CharField(max_length=255)
    aktiv = forms.BooleanField(required=False)
from django import forms
from cars.models import Brand,Car


class CarForm(forms.Form):
    model = forms.CharField(max_length=200)
    brand = forms.ModelChoiceField(Brand.objects.all())
    factor_year = forms.IntegerField()
    model_year=forms.IntegerField()
    value = forms.FloatField()
    photo = forms.ImageField()


class CarModelForm(forms.ModelForm):
	class Meta:
            model = Car
            fields ='__all__'

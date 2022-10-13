from django import forms
from .models import GeeksModel


# create a form
class InputForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(
                help_text="Enter 6 digit roll number"
                )
    password = forms.CharField(widget=forms.PasswordInput())


# create a ModelForm
class GeeksForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = GeeksModel
        # specify fields to be used
        fields = [
            "title",
            "description"
        ]

# class GeeksForm(forms.Form):
#     title = forms.CharField()
#     description = forms.CharField()
#     views = forms.IntegerField()
#     available = forms.BooleanField()


# creating a django form
class MyForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
    # views = forms.IntegerField()
    # available = forms.BooleanField()
    # date = forms.DateField(widget=forms.SelectDateWidget)

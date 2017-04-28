from django import forms     
from django.contrib.auth import get_user_model #my user model
from django.contrib.auth.forms import UserCreationForm      


class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)
    weather_id = forms.CharField(required=True, help_text='to get in www.openweathermap.com')
    #first_name = forms.CharField(required = False)
    #last_name = forms.CharField(required = False)


    class Meta:
        model = get_user_model() #i refer to my user model, so i get user model!
        fields = ('username', 'email', 'password1', 'password2','weather_id')        

    def save(self,commit = True):   
        user = super(MyRegistrationForm, self).save() #he look my model,thanks to get_user_model() and commit with my data form
        return user
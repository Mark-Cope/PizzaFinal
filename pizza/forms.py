from django import forms

from .models import Pizza, Topping, Comment

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['name']
        labels = {'name':''}

class ToppingForm(forms.ModelForm):
    class Meta:
        model = Topping
        fields = ['name']
        labels = {'name':''}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name']
        labels = {'name':''}

#A form is just like a model EXCEPT it is done by the user
#We must validate all the information entered to make sure it is not dangerous to our code
#MODELFORM from Django automatically build a from for us in the data
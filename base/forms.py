from django.forms import ModelForm
from .models import Food , Comment , Type

class FoodForm(ModelForm):
    class Meta:
        model=Food
        fields=['name','type']

class TypeForm(ModelForm):
    class Meta:
        model=Type
        fields=['name']

# class CommentForm(ModelForm):
#     class Meta:
#         model=Comment
#         fields='__all__'
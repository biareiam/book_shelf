from django import forms
from .models import Post, Category


choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','username','category','featured_image','body')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control' }),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            #'username': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user_name', 'type':'hidden'}),
            'username': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            #'featured_image':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Book Description'}),
            
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','featured_image','body')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            #'username': forms.Select(attrs={'class':'form-control'}),
            #'featured_image':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
        }
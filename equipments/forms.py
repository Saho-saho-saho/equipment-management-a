from .models import Equipment
from django import forms

class EquipmentForm(forms.ModelForm):
    class Meta:
      model = Equipment
      fields = ['name','category','status','location','description','image', 'quantity']
      widgets = {
          'name': forms.TextInput(attrs={'placeholder': 'Name'}),
          'category': forms.TextInput(attrs={'placeholder': 'Name'}),
          'status': forms.TextInput(attrs={'placeholder': 'Name'}),
          'location': forms.TextInput(attrs={'placeholder': 'Name'}),
          'description': forms.Textarea(attrs={'placeholder': 'Text', 'rows': 10}),
          'quantity': forms.TextInput(attrs={'placeholder': 'Name'}),
      }
      labels = {
         'name':'名前',
         'category': 'カテゴリ',
         'status': '状態',
         'location': '設置場所',
         'description': '説明',
         'image': '画像',
         'quantity': '在庫数',
      }
from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django.forms import ModelForm
from dashboard.models import Barang,Karyawan,Order
from django import forms

class FormBarang(ModelForm):
    class Meta :
        model=Barang
        fields='__all__'



        Widget =  {
            'Kodebrng': forms.TextInput({'class':'form-control'}),
            'Nama': forms.TextInput({'class':'form-control'}),
            'stock': forms.NumberInput({'class':'form-control'}),
            'haraga':  forms.NumberInput({'class':'form-control'}),
            'link_gbr': forms.TextInput({'class':'form-control'}),
            'jenis_id': forms.Select({'class':'form-control'}),
        }

class FormKaryawan(ModelForm):
    class Meta :
        model=Karyawan
        fields='__all__'

class FormOrder(ModelForm):
    class Meta :
        model=Order
        fields='__all__'
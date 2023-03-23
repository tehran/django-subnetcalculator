from django import forms

class SubnetCalculatorForm(forms.Form):
    ip_address = forms.GenericIPAddressField(label="IP Address")
    subnet_mask = forms.GenericIPAddressField(label="Subnet Mask")

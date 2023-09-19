from django import forms


class UploadJSONForm(forms.Form):
    json_file = forms.FileField(label='Select a JSON file')

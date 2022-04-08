from django import forms


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for bfield in self:
            bfield.field.widget.attrs['class'] = 'form-control'


class NewsfeedSearchForm(BootstrapFormMixin, forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'New Year'})
    )
    extended = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
    count = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'}),
        initial=3
    )
    latitude = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
    longitude = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
    start_time = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    end_time = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    start_id = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
    offset = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
    start_from = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
    fields = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )


class PhotosSearchForm(BootstrapFormMixin, forms.Form):
    q = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Nature'})
    )
    lat = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
    long = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
    start_time = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    end_time = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': ''})
    )
    sort = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
    offset = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
    count = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'}),
        initial=3
    )
    radius = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '0'})
    )
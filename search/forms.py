from django import forms


class SearchForm(forms.Form):
    search_request = forms.CharField(
        max_length=255,
        required=False,
        label='',
        widget=forms.TextInput(
            attrs={
                'class': 'rounded',
                'type': 'search',
                'placeholder': 'Search',

            }
        )
    )

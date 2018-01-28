from django import forms


class MusicianSortingForm(forms.Form):
    ordering = forms.ChoiceField(label="Sort",
                                 required=False,
                                 choices=[
                                     ["name", "A-Z"],
                                     ["-name", "Z-A"]])
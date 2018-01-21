from django import forms


class MusicianSortingForm(forms.Form):
    ordering = forms.ChoiceField(label="Sort",
                                 required=False,
                                 choices=[
                                     ["musician_name", "A-Z"],
                                     ["-musician_name", "Z-A"]])
from django import forms

class PatientForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        min_length=3,
        required=True,
        label="Patient Name"
    )

    email = forms.EmailField(
        required=True,
        label="Email"
    )

    age = forms.IntegerField(
        min_value=1,
        max_value=120,
        required=True,
        label="Age"
    )

    gender = forms.ChoiceField(
        choices=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other")
        ],
        required=True
    )
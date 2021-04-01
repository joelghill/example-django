from django import forms
from django.core.exceptions import ValidationError

from people.models import Person


class FirstNameForm(forms.Form):

    first_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        person_count = Person.objects.filter(email=email).count()

        if person_count == 0:
            return email
        else:
            raise ValidationError("A person with this email exists already!")

    def clean_first_name(self):
        """ Custom clean method following the patter clean_<YOUR FIELD NAME>
            Raise ValidationError to add error form
            Return clean field value if there is no error
        """

        if self.cleaned_data['first_name'] == 'Steve':
            raise ValidationError("Steve is a terrible name.")

        return self.cleaned_data['first_name']


    def clean(self):
        return self.cleaned_data

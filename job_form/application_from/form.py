from django import forms
from .models import *


optionfields = ["name", "value"]


class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = optionfields


class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = optionfields


class RelationStatusForm(forms.ModelForm):
    class Meta:
        model = RelationStatus
        fields = optionfields


class GenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = optionfields


class PreferedLocationForm(forms.ModelForm):
    class Meta:
        model = PreferedLocation
        fields = optionfields


class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = optionfields


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = optionfields


class BasicDetailForm(forms.ModelForm):
    class Meta:
        model = BasicDetail
        fields = [
            "first_name",
            "last_name",
            "designation",
            "address1",
            "address2",
            "email",
            "phone",
            "state",
            "city",
            "pincode",
            "gender",
            "rel_status",
            "date_of_birth",
        ]
        labels = {
            "first_name": "First Name: ",
            "last_name": "Last Name: ",
            "designation": "Designation: ",
            "address1": "Current Address: ",
            "address2": "Permanent Address: ",
            "email": "Email-Address: ",
            "phone": "Mobile Number: ",
            "state": "State: ",
            "city": "City: ",
            "pincode": "PIN Code: ",
            "gender": "Gender: ",
            "rel_status": "Relationship Status: ",
            "date_of_birth": "Date of Birth: ",
        }
        widgets = {
            "designation": forms.Select(),
            "gender": forms.Select(),
            "rel_status": forms.Select(),
            "address1": forms.Textarea(attrs={"rows": 2}),
            "address2": forms.Textarea(attrs={"rows": 2}),
            "date_of_birth": forms.DateInput(format=('%d/%m/%Y'), attrs={"type": "date"})
        }


class EducationDetailForm(forms.ModelForm):
    class Meta:
        model = EducationDetail
        fields = ["course", "board", "institute", "passing_year", "score"]
        labels = {
            "course": "Course: ",
            "board": "University/Board Name: ",
            "institute": "College/School Name: ",
            "passing_year": "Year of Passing: ",
            "score": "Result (in %)",
        }
        widgets = {"passing_year": forms.TextInput()}


class ExperienceDetailForm(forms.ModelForm):
    class Meta:
        model = ExperienceDetail
        fields = ["company", "designation", "from_date", "to_date"]
        labels = {
            "company": "'Company's Name: ",
            "designation": "Current Role: ",
            "from_date": "Date of Joining: ",
            "to_date": "Date of Leaving",
        }
        widgets = {
            "from_date": forms.DateInput(format=("%d/%m/%Y"), attrs={"type": "date"}),
            "to_date": forms.DateInput(format=("%d/%m/%Y"), attrs={"type": "date"}),
        }


lang_opts = ['Read', 'Write', 'Speak']


class LanguageDetailForm(forms.ModelForm):
    class Meta:
        model = LanguageDetail
        fields = ["language", "read", "write", "speak"]


class LanguageOptionForm(forms.ModelForm):
    class Meta:
        model = LanguageOption
        fields = optionfields


class TechDetailForm(forms.ModelForm):
    class Meta:
        model = TechDetail
        fields = ["technology", "status"]


class TechOptionForm(forms.ModelForm):
    class Meta:
        model = TechOption
        fields = optionfields


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ["name", "relation", "phone_number"]
        labels = {
            "name": "Name: ",
            "relation": "Relation",
            "phone_number": "Phone Number"
        }


class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ["notice_period", "expected_CTC", "current_CTC", "department"]
        labels = {
            "notice_period": "Notice Period: ",
            "expected_CTC": "Expected CTC: ",
            "current_CTC": "Current CTC: ",
            "department": "Department: "
        }
        widgets = {
            "notice_period": forms.NumberInput(attrs={
                "min": 0,
                "max": 12
            }),
            "department": forms.Select()
        }


class UserPreferenceLocationForm(forms.ModelForm):
    class Meta:
        model = UserPreferedLocation
        fields = ["location"]

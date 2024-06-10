from django import forms
from .models import *


optionfields = ['name', 'value']


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


class StateForm(forms.ModelForm):
    class Meta:
        model = State
        fields = optionfields


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = optionfields


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = optionfields


class BasicDetailForm(forms.ModelForm):
    class Meta:
        model = BasicDetail
        fields = ['first_name', 'last_name', 'designation', 'address1', 'address2', 'email',
                  'phone', 'city', 'state', 'pincode', 'gender', 'rel_status', 'date_of_birth']


class EducationDetailForm(forms.ModelForm):
    class Meta:
        model = EducationDetail
        fields = ['course', 'board', 'institute', 'passing_year', 'score']


class ExperienceDetailForm(forms.ModelForm):
    class Meta:
        model = ExperienceDetail
        fields = ['company', 'designation', 'from_date', 'to_date']


class LanguageDetailForm(forms.ModelForm):
    class Meta:
        model = LanguageDetail
        fields = ['language', 'read', 'write', 'speak']


class LanguageOptionForm(forms.ModelForm):
    class Meta:
        model = LanguageOption
        fields = optionfields


class TechDetailForm(forms.ModelForm):
    class Meta:
        model = TechDetail
        fields = ['technology', 'status']


class TechOptionForm(forms.ModelForm):
    class Meta:
        model = TechOption
        fields = optionfields


class ReferenceForm(forms.ModelForm):
    class Meta:
        model = Reference
        fields = ['name', 'relation', 'phone_number']


class PreferenceForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = ['notice_period', 'expected_CTC', 'current_CTC', 'department']


class UserPreferenceLocationForm(forms.ModelForm):
    class Meta:
        model = UserPreferedLocation
        fields = ['location']

from django.shortcuts import render, HttpResponse
from .form import *
from .models import Language, Technology, PreferedLocation

# Create your views here.
language = LanguageForm()
technology = TechnologyForm()
relation_status = RelationStatusForm()
gender = GenderForm()
prefered_location = PreferedLocationForm()
designation = DesignationForm()
department = DepartmentForm()
basic_detail = BasicDetailForm()
education_detail = EducationDetailForm()
experience_detail = ExperienceDetailForm()
language_detail = LanguageDetailForm()
language_option = LanguageOptionForm()
tech_detail = TechDetailForm()
tech_option = TechOptionForm()
reference = ReferenceForm()
preference = PreferenceForm()


context = {
    'k': basic_detail,
    'l': education_detail,
    'exper': experience_detail,
    'languages': Language.objects.all(),
    'techs': Technology.objects.all(),
    'n': language_detail,
    'p': tech_detail,
    'r': reference,
    'pref_loc': PreferedLocation.objects.all(),
    's': preference
}


def create_form(request):
    return render(request, 'form.html', context)


def show_form_data(request):
    if request.method == "POST":
        pass

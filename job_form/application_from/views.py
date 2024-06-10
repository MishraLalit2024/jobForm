from django.shortcuts import render, HttpResponse
from .form import *

# Create your views here.
language = LanguageForm()
technology = TechnologyForm()
relation_status = RelationStatusForm()
gender = GenderForm()
prefered_location = PreferedLocationForm()
designation = DesignationForm()
department = DepartmentForm()
state = StateForm()
city = CityForm()
course = CourseForm()
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
    'a': language,
    'b': technology,
    'c': relation_status,
    'd': gender,
    'e': prefered_location,
    'f': designation,
    'g': department,
    'h': state,
    'i': city,
    'j': course,
    'k': basic_detail,
    'l': education_detail,
    'm': experience_detail,
    'n': language_detail,
    'o': language_option,
    'p': tech_detail,
    'q': tech_option,
    'r': reference,
    's': preference
}


def create_form(request):
    return render(request, 'form.html', context)

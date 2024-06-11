from django.contrib import admin
from .models import Language, TechDetail, Technology
from .models import RelationStatus, Gender, PreferedLocation
from .models import Designation, Department, BasicDetail, UserPreferedLocation
from .models import EducationDetail, ExperienceDetail, LanguageDetail
from .models import LanguageOption, TechOption, Reference, Preference

# Register your models here.
admin.site.register(Language)
admin.site.register(Technology)
admin.site.register(RelationStatus)
admin.site.register(Gender)
admin.site.register(PreferedLocation)
admin.site.register(Designation)
admin.site.register(Department)
admin.site.register(BasicDetail)
admin.site.register(EducationDetail)
admin.site.register(ExperienceDetail)
admin.site.register(LanguageDetail)
admin.site.register(LanguageOption)
admin.site.register(TechDetail)
admin.site.register(TechOption)
admin.site.register(Reference)
admin.site.register(Preference)
admin.site.register(UserPreferedLocation)

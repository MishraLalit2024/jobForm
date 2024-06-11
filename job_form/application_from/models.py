from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class AbstractRecord(models.Model):
    user_id = models.IntegerField()
    created_at = models.DateTimeField(default=None)
    updated_at = models.DateTimeField(default=None)
    deleted_at = models.DateTimeField(default=None)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class AbstractOption(models.Model):
    name = models.CharField(max_length=50, blank=False)
    value = models.CharField(max_length=3)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Language(AbstractOption):
    pass


class Technology(AbstractOption):
    pass


class RelationStatus(AbstractOption):
    pass


class Gender(AbstractOption):
    pass


class PreferedLocation(AbstractOption):
    class Meta:
        verbose_name = __name__

    pass


class Designation(AbstractOption):
    pass


class Department(AbstractOption):
    pass


designation_choices = Designation.objects.all()
gender_choices = Gender.objects.all()
relstatus_choices = RelationStatus.objects.all()
desg_obj = {}
gender_obj = {}
relstatus_obj = {}

for i in designation_choices:
    desg_obj[i.value] = i.name
for i in gender_choices:
    gender_obj[i.value] = i.name
for i in relstatus_choices:
    relstatus_obj[i.value] = i.name
# print(gender_obj['NON'])


class BasicDetail(AbstractRecord):
    first_name = models.CharField("first-name", max_length=255, blank=False)
    last_name = models.CharField("last-name", max_length=255, blank=False)
    new_designation = models.CharField(
        "new-designation", max_length=50, choices=desg_obj, default=desg_obj["JDV"]
    )
    address1 = models.TextField(blank=False)
    address2 = models.TextField(blank=False)
    email = models.EmailField(unique=True, primary_key=True)
    phone = models.CharField(blank=False, unique=True, max_length=15)
    city = models.CharField(
        max_length=50,
        blank=False,
    )
    state = models.CharField(max_length=50, blank=False)
    pincode = models.CharField(max_length=6, blank=False)
    gender = models.CharField(max_length=3, choices=gender_obj, default=gender_obj["M"])
    rel_status = models.CharField(
        max_length=50, choices=relstatus_obj, default=relstatus_obj["SIN"]
    )
    date_of_birth = models.DateField(default="2001-01-01")

    class Meta:
        verbose_name_plural = "Basic Details"

    def __str__(self):
        return str(self.first_name + " " + self.last_name)


courses = {
    "ssc": "SSC",
    "hsc": "HSC",
    "bac": "Bachelor's",
    "mas": "Master's",
    "doc": "Doctorate",
}


class EducationDetail(AbstractRecord):
    courses = models.CharField("courses", max_length=50, blank=False, choices=courses)
    boards = models.CharField("boards", max_length=50, blank=False)
    institutes = models.CharField("institutes", max_length=100)
    passing_year = models.PositiveIntegerField(
        "pyear",
        default=2000,
        validators=[MinValueValidator(2000), MaxValueValidator(2025)],
    )
    scores = models.FloatField()


class ExperienceDetail(AbstractRecord):
    companies = models.CharField(max_length=100)
    designations = models.CharField(max_length=50)
    from_dates = models.DateField(default="2001-01-01")
    to_dates = models.DateField(default="2001-01-01")


class LanguageDetail(AbstractRecord):
    language = models.CharField(max_length=3)
    read = models.BooleanField()
    speak = models.BooleanField()
    write = models.BooleanField()


class TechDetail(AbstractRecord):
    technology = models.CharField(max_length=3)
    status = models.CharField(max_length=3)


class Reference(AbstractRecord):
    name = models.CharField(max_length=255)
    relation = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)


dept = Department.objects.all()
dept_choices = {}
for i in dept:
    dept_choices[i.value] = i.name


class Preference(AbstractRecord):
    notice_period = models.IntegerField()
    expected_CTC = models.FloatField()
    current_CTC = models.FloatField()
    department = models.CharField(max_length=3, choices=dept_choices)


class UserPreferedLocation(AbstractRecord):
    location = models.ManyToManyField(PreferedLocation)


class LanguageOption(AbstractOption):
    pass


class TechOption(AbstractOption):
    pass

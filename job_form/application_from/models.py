from django.db import models
from django.utils import timezone

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
    pass


class Designation(AbstractOption):
    pass


class Department(AbstractOption):
    pass


class State(AbstractOption):
    pass


class City(AbstractOption):
    pass


class Course(AbstractOption):
    pass


class BasicDetail(AbstractRecord):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    designation = models.CharField(max_length=3, null=True)
    address1 = models.TextField(blank=False)
    address2 = models.TextField(blank=False)
    email = models.EmailField(unique=True, primary_key=True)
    phone = models.CharField(blank=False, unique=True, max_length=15)
    city = models.CharField(max_length=3, blank=False)
    state = models.CharField(max_length=3, blank=False)
    pincode = models.CharField(max_length=6, blank=False)
    gender = models.CharField(max_length=3, null=True)
    rel_status = models.CharField(max_length=3)
    date_of_birth = models.DateField(default='2001-01-01')

    class Meta:
        verbose_name_plural = 'Basic Details'

    def __str__(self):
        return str(self.first_name+" "+self.last_name)


class EducationDetail(AbstractRecord):
    course = models.CharField(max_length=3, blank=False)
    board = models.CharField(max_length=50, blank=False)
    institute = models.CharField(max_length=100)
    passing_year = models.DateField(default='2001-01-01')
    score = models.FloatField()


class ExperienceDetail(AbstractRecord):
    company = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    from_date = models.DateField(default='2001-01-01')
    to_date = models.DateField(default='2001-01-01')


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


class Preference(AbstractRecord):
    notice_period = models.IntegerField()
    expected_CTC = models.FloatField()
    current_CTC = models.FloatField()
    department = models.CharField(max_length=3)


class UserPreferedLocation(AbstractRecord):
    location = models.CharField(max_length=3)


class LanguageOption(AbstractOption):
    pass


class TechOption(AbstractOption):
    pass

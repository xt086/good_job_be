from django.db import models
from django.utils.translation import gettext_lazy as _
class Gender(models.TextChoices):
    MALE = "M", _("Male")
    FEMALE = "F",_("Female")


class Level(models.TextChoices):
    INTERN = "IN", _("Intern")
    FRESHER = "FR", _("Fresher")
    JUNIOR = "JR", _("Junior")
    MIDDLE = "MD",_("Middle")
    SENIOR = "SR", _("Senior")
    MANAGER = "MG", _("Manager")
    CHIEF = "CH", _("Chief")

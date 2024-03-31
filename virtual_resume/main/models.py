from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    name = models.CharField(max_lenght=20, blank=True, null=True)
    score = models.IntegerField(default=80, blank=True, null=True)
    image = models.FileField(upload_to="skills", blank=True, null=True)
    is_key_skill = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Skills"
        verbose_name = "Skill"

    def __str__(self) -> str:
        return self.name

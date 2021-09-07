from django.db import models

# Create your models here.
from django.db.models import ForeignKey


class MovieStaffMember(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.DateField(null=True, blank=True)
    is_alive = models.BooleanField(default=True)

    class Career(models.TextChoices):
        DIRECTOR = "DRT", "Director"
        ACTOR = "ACT", "Actor"

    career = models.CharField(
        max_length=5, choices=Career.choices, default=Career.ACTOR
    )

    def __str__(self):
        return self.name


class MovieCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=512)
    year = models.DateField()
    director = models.ForeignKey(
        MovieStaffMember, related_name="director", on_delete=models.SET_NULL, null=True
    )
    actors = models.ManyToManyField(MovieStaffMember, related_name="actors")
    categories = models.ManyToManyField(MovieCategory, related_name="categories")
    box_office = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class MovieRole(models.Model):
    movie = ForeignKey(Movie, related_name="movie_roles", on_delete=models.CASCADE)
    actor = ForeignKey(MovieStaffMember, related_name="roles", on_delete=models.CASCADE)
    role = models.CharField(max_length=512)

    def __str__(self):
        return self.role

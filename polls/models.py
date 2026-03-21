import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __cl__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="questions", null=True, blank=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", default=timezone.now)

    def __str__(self):
        return self.question_text

    @property
    def total_votes(self):
        return sum(choice.votes for choice in self.choice_set.all())

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    trait = models.CharField(max_length=100, help_text="The personality trait this choice belongs to", null=True, blank=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class PersonalityResult(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="results")
    trait = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.category.name} - {self.trait}"

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=80)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", null=False, db_index=True, unique=True)

    def get_absolute_url(self):
        return reverse("book_outlet:book-detail", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Book(title="{self.title}", rating={self.rating}, author="{self.author}", is_bestselling={self.is_bestselling})'

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

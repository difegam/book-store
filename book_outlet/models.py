from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __repr__(self) -> str:
        return f'Author(first_name="{self.first_name}", last_name="{self.last_name}")'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=80)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    # author = models.CharField(max_length=100, null=True)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,  # Opt: PROTECT, SET_NULL, SET_DEFAULT, SET, DO_NOTHING
        null=True,
        related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", db_index=True, unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("book_outlet:book-detail", args=[self.slug])

    #! Added BookAdmin and prepopulated slug. see admin.py
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __repr__(self) -> str:
        return f'Book(title="{self.title}", rating={self.rating}, author="{self.author}", is_bestselling={self.is_bestselling}, slug="{self.slug}")'

    def __str__(self) -> str:
        return f"{self.title} ({self.rating})"

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __repr__(self) -> str:
        return f'Country(name="{self.name}", code="{self.code}")'

    def __str__(self) -> str:
        return f"{self.name} - ( {self.code.upper()} )"

    class Meta():
        verbose_name_plural = "Countries"
        ordering = ["name"]


class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=10)
    city = models.CharField(max_length=50)

    def __repr__(self) -> str:
        return f'Address(street="{self.street}", postal_code="{self.postal_code}", city="{self.city}")'

    def __str__(self) -> str:
        return f"{self.street}, {self.postal_code.upper()}, {self.city}"

    class Meta:
        # https://docs.djangoproject.com/en/4.2/ref/models/options/#verbose-name
        verbose_name_plural = "Addresses"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __repr__(self) -> str:
        return f'Author(first_name="{self.first_name}", last_name="{self.last_name}")'

    def __str__(self) -> str:
        return self.full_name


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
    published_countries = models.ManyToManyField(Country)

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

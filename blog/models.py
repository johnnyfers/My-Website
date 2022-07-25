from django.db import models
from django.core.validators import MinLengthValidator


class Tag(models.Model):
    caption = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.get_full_name()


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='skills', null=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=250)
    image = models.ImageField(upload_to='posts', null=True)
    date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    skills = models.ManyToManyField(Skill, null=True, related_name='posts')

    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
        return self.title

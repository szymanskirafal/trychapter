from django.db import models
from authors.models import Author

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add = True)
    modified = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Book(TimeStampedModel):
    author = models.ForeignKey(Author, on_delete = models.CASCADE, related_name='books')
    title = models.CharField(max_length = 50)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    slug = models.SlugField()

    def __str__(self):
        return self.title, self.author

    def get_absolute_url(self):
        #return reverse('company_details', kwargs={'pk': self.id})
        pass

from django.db import models
from common.models import TimeStampModel
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.utils.text import slugify

User = get_user_model()

# Create your models here.
class Post(TimeStampModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)
    thumbnail = models.ImageField(null=True, blank=True)
    body = models.TextField()
    slug = models.SlugField(default = '', unique=True, max_length=120)
    # tags = models.ManyToManyField('Tag', related_name='blogs')

    def __str__(self) -> str:
        return str(self.author_id) + "_" + self.title
    
    def save(self, *args, **kwargs):
        # Setting the slug
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.pk})
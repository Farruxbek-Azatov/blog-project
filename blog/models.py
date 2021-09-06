from django.db import models


class PublishedManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(publish=True)


class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique_for_date='created')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)
    objects = models.Manager()
    published = PublishedManager()

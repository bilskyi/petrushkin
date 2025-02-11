from django.db import models


class Gallery(models.Model):
    pass


class Album(models.Model):
    gallery = models.ForeignKey(
        Gallery,
        related_name='albums',
        on_delete=models.CASCADE
        )
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class Picture(models.Model):
    album = models.ForeignKey(
        Album,
        related_name='pictures',
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='pictures', null=True, blank=True)

    def __str__(self):
        return f'{self.image.url} - {self.album.title}'
    

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
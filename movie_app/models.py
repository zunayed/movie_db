from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=200, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '{} added to the database on {:%d, %b %Y}'.format(self.title, self.created_at)

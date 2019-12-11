from django.db import models


class Hero(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "heroes"

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        return super(Hero, self).save(*args, **kwargs)

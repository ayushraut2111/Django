from django.db import models

class details(models.Model):
    end_year=models.IntegerField(default=None,blank=True,null=True)
    intensity=models.IntegerField(default=None,blank=True,null=True)
    sector=models.TextField(blank=True,null=True)
    topic=models.TextField(blank=True,null=True)
    insight=models.TextField(blank=True,null=True)
    url=models.URLField(blank=True,null=True)
    region=models.TextField(blank=True,null=True)
    start_year=models.IntegerField(default=None,blank=True,null=True)
    impact=models.TextField(blank=True,null=True)
    added=models.TextField(blank=True,null=True)
    published=models.TextField(blank=True,null=True)
    country=models.TextField(blank=True,null=True)
    relevance=models.IntegerField(default=None,blank=True,null=True)
    pestle=models.TextField(blank=True,null=True)
    source=models.TextField(blank=True,null=True)
    title=models.TextField(blank=True,null=True)
    likelihood=models.IntegerField(default=None,blank=True,null=True)

    def __str__(self) -> str:
        return self.topic


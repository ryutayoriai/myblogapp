from django.db import models


class Tag(models.Model):
    tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=255)

class TagMap(models.Model):
    tag_id = models.IntegerField()
    post_id = models.IntegerField()

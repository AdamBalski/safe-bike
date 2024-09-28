from django.db import models
from users.models import User


# Create your models here.
class DangerCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    min_score = models.IntegerField()
    max_score = models.IntegerField()
    is_negative = models.BooleanField()

    def __str__(self):
        return self.name


class Route(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    segments = models.ManyToManyField("Segment")


class Segment(models.Model):
    id = models.AutoField(primary_key=True)
    src_x = models.FloatField()
    src_y = models.FloatField()
    dest_x = models.FloatField()
    dest_y = models.FloatField()


class Score(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    segment_id = models.ForeignKey("Segment", on_delete=models.CASCADE)
    danger_category_id = models.ForeignKey(
        "DangerCategory", on_delete=models.CASCADE
    )
    score = models.IntegerField()


# Route:
# route_id, owner_id, name and
#    segments (json as a string, contains src_x, src_y, dest_x, dest_y)

# Segment:
# src_x, src_y, dest_x, dest_y, segment_id

# Score:
# owner_id, segment_id, danger_category_id, score

# DangerCategory: as above

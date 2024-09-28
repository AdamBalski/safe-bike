from .models import DangerCategory, Route, Segment, Score
from users.models import User
from rest_framework import serializers


class DangerCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = DangerCategory
        fields = "__all__"


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = "__all__"


class SegmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Segment
        fields = "__all__"


class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = "__all__"

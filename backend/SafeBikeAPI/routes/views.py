from rest_framework import views
from .models import Route, Segment, Score, DangerCategory
from users.models import User
from .serializers import (
    RouteSerializer,
    SegmentSerializer,
    ScoreSerializer,
    DangerCategorySerializer,
)
from rest_framework.response import Response


# Create your views here.
class ListRoutesView(views.APIView):
    def get(self, request):
        user_id = request.user.id
        routes = Route.objects.filter(owner_id=user_id)
        serializer = RouteSerializer(routes, many=True)
        return Response(serializer.data)


class RateView(views.APIView):
    def post(self, request, route_id):
        user_id = request.user.id

        # TODO remove this line
        if not user_id:
            user_id = 1
        user = User.objects.get(id=user_id)
        route = Route.objects.get(id=route_id)
        segments_ratings = request.data["segment_ratings"]
        for segment_rating in segments_ratings:
            segment_id = segment_rating["segment_idx"]
            segment = Segment.objects.get(id=segment_id)
            danger_category_id = segment_rating["danger_category_idx"]
            danger_category = DangerCategory.objects.get(id=danger_category_id)
            score = segment_rating["value"]
            score = Score(
                owner_id=user,
                segment_id=segment,
                danger_category_id=danger_category,
                score=score,
            )
            route.segments.add(segment_id)
            score.save()

        return Response({"message": "Rating saved successfully"})


class ListDangerCategoriesView(views.APIView):
    def get(self, request):
        danger_categories = DangerCategory.objects.all()
        serializer = DangerCategorySerializer(danger_categories, many=True)
        return Response(serializer.data)


class CreateRouteView(views.APIView):
    def post(self, request):
        user_id = request.user.id
        # TODO remove this line
        if not user_id:
            user_id = 1
        user = User.objects.get(id=user_id)
        segments: list = request.data["segments"]
        route = Route.objects.create(owner_id=user, name=request.data["name"])
        for segment in segments:
            segment = Segment(**segment)
            segment.save()
            route.segments.add(segment)

        route.save()
        return Response({"message": "Route created successfully"})

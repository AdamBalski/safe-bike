from rest_framework import views
from .models import Route, Segment, Score, DangerCategory
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
    # POST /route/$route-id/rate
    # request body:
    #  {“route_id”: “$route_id”, segment_ratings: {“segment_idx”: number, “danger_category_idx”: number, “value”: number}[]}
    def post(self, request, route_id):
        user_id = request.user.id
        route = Route.objects.get(id=route_id)
        segments_ratings = request.data["segment_ratings"]
        for segment_rating in segments_ratings:
            segment_id = segment_rating["segment_idx"]
            danger_category_id = segment_rating["danger_category_idx"]
            score = segment_rating["value"]
            score = Score(
                owner_id=user_id,
                segment_id=segment_id,
                danger_category_id=danger_category_id,
                score=score,
            )
            route.segments.add(segment_id)
            score.save()

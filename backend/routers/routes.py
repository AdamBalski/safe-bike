from fastapi import APIRouter

router = APIRouter()

dummy_route = [
    {
        "id": 1,
        "owner_id": 1,
        "name": "Route 1",
        "points": [
            {"x": 0, "y": 0},
            {"x": 1, "y": 1},
            {"x": 2, "y": 2},
        ],
        "segments": [
            {"id": 1, "name": "Segment 1"},
            {"id": 2, "name": "Segment 2"},
        ],
    }
]


@router.get("/routes")
async def get_routes():
    return dummy_route


@router.post("/routes")
async def post_route(route: str):
    return {"route": route}


@router.post("/routes/{route_id}/score")
async def get_route_score(route_id: int, score: int):
    return {"route_id": route_id, "score": score}

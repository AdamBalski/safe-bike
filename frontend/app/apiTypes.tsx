type Route = {
    name: String,
    owner_id: String // (uuid);
    id: String //(uuid);
    points: Point[],
    segments: Segment[],
}

type Point = {
   coordinates: {x: number, y: number},
}

type Segment = {
    estimated_length: number, // (time/km idk)
    A: String, // maybe not
    B: String, // maybe not
    danger_estimates:  DangerEstimate[]
}

type DangerEstimate = {
    category: DangerCategory,
    value: number,
}

type DangerCategory = {
    name: String, 
    id: String,
    min: number,
    max: number,
    is_negative: boolean //(e.g. true for visual appeal),
}

type Account = {
     email: String,
     password_hash: String,
     id: String,
}

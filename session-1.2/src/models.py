from pydantic import BaseModel, Field

class Itinerary(BaseModel):
    destination: str = Field(min_length=1, description="Destination of the trip.")
    trip_duration: int = Field(gt=0, description="Duration of the trip in days.")
    budget_category: str = Field(min_length=1, description="Budget category for the trip (e.g., budget, mid-range, luxury).")
    top_attractions: list[str] = Field(min_length=1, description="List of top attractions to visit.")
    daily_plan: list[DailyPlan] = Field(description="Daily plan for the trip.")

class DailyPlan(BaseModel):
    day: int = Field(gt=0, description="Day number of the trip.")
    activities: list[str] = Field(min_length=1, description="List of activities planned for the day.")

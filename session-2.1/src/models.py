from pydantic import BaseModel, ConfigDict, Field


# Structured Output Models
class WeatherOutput(BaseModel):
    city: str = Field(..., description="The name of the city for which the weather is reported.")
    temperature: float = Field(..., description="The current temperature in Celsius.")
    condition: str = Field(..., description="A brief description of the weather condition.")
    humidity: int = Field(..., description="The current humidity percentage.")
    weather_summary: str = Field(..., description="A summary of the weather conditions in the city.")

# Tool Models
class WeatherToolOutput(BaseModel):
    temperature: float = Field(..., description="The current temperature in Celsius.")
    condition: str = Field(..., description="A brief description of the weather condition.")
    humidity: int = Field(..., description="The current humidity percentage.")

# API Models
class WeatherApiOutput(BaseModel):
    model_config = ConfigDict(extra="ignore")

    current_condition: list[CurrentCondition] = Field(..., description="The current weather conditions.")

class CurrentCondition(BaseModel):
    model_config = ConfigDict(extra="ignore")

    temp_C: float = Field(..., description="The current temperature in Celsius.")
    humidity: int = Field(..., description="The current humidity percentage.")
    weatherDesc: list[WeatherDescription] = Field(..., description="A list containing descriptions of the current weather conditions.")

class WeatherDescription(BaseModel):
    model_config = ConfigDict(extra="ignore")

    value: str = Field(..., description="A brief description of the weather condition.")

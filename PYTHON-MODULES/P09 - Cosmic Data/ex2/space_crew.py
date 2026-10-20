#!/usr/bin/env python3

from enum import Enum
from pydantic import BaseModel, Field, model_validator, ValidationError
from datetime import datetime


class CrewRank(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def validate_model(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        has_commander_or_captain = False
        for member in self.crew:
            if (member.rank is CrewRank.COMMANDER
                    or member.rank is CrewRank.CAPTAIN):
                has_commander_or_captain = True
        if not has_commander_or_captain:
            raise ValueError(
                "Mission must have at least one Commander or Captain"
                )
        if self.duration_days > 365:
            experienced_members = 0
            for member in self.crew:
                if not member.is_active:
                    raise ValueError("All crew members must be active")
                if member.years_experience >= 5:
                    experienced_members += 1
            if experienced_members < len(self.crew) / 2:
                raise ValueError(
                    "Long missions (> 365 days) need 50%"
                    "experienced crew (5+ years)"
                )
        return self


def main() -> None:
    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2026-01-01T14:00:00",
        duration_days=900,
        crew=[
            CrewMember(
                member_id="C001",
                name="Sarah Connor",
                rank=CrewRank.COMMANDER,
                age=35,
                specialization="Mission Command",
                years_experience=10
            ),
            CrewMember(
                member_id="C002",
                name="John Smith",
                rank=CrewRank.LIEUTENANT,
                age=30,
                specialization="Navigation",
                years_experience=5
            ),
            CrewMember(
                member_id="C003",
                name="Alice Johnson",
                rank=CrewRank.OFFICER,
                age=30,
                specialization="Engineering",
                years_experience=5
            )
        ],
        budget_millions=2500.0
    )
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value})"
            f" - {member.specialization}"
              )
    print()
    print("=========================================")
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2024_MOON",
            mission_name="Moon Colony Establishment",
            destination="Moon",
            launch_date="2026-01-01T14:00:00",
            duration_days=900,
            crew=[
                CrewMember(
                    member_id="C002",
                    name="John Smith",
                    rank=CrewRank.LIEUTENANT,
                    age=30,
                    specialization="Navigation",
                    years_experience=5
                ),],
            budget_millions=2500.0
        )
    except ValidationError as e:
        print(e.errors()[0]["msg"].removeprefix("Value error, "))


if __name__ == "__main__":
    main()

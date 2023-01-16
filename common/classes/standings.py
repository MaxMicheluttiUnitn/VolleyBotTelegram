from typing import List, TypedDict
from common.classes.game import Team, League, Country

class StandingsGroup(TypedDict): 
    name: str

class GamesStatsDetails(TypedDict):
    total: int
    percentage: str

class GameStats(TypedDict):
    played: int
    win: GamesStatsDetails
    lose: GamesStatsDetails

class GoalStats(TypedDict(
    "GoalStats",
    {'for': int},)):
    against: int

class StandingsItem(TypedDict): 
    position: int
    stage: str
    group: StandingsGroup
    team: Team
    league: League
    country: Country
    games: GameStats
    goals: GoalStats
    points: int
    form: str
    description: str

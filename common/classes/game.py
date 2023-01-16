from typing import List
from typing_extensions import TypedDict

class GameStatus(TypedDict):
    long: str
    short: str

class Country(TypedDict):
    id: int
    name: str
    code: str
    flag: str

class League(TypedDict):
    id: int
    name: str
    type: str
    logo: str
    season: int

class Team(TypedDict):
    id: int
    name: str
    logo: str

class GameTeams(TypedDict):
    home: Team
    away: Team

class GameScores(TypedDict):
    home: int
    team: int

class GamePeriod(TypedDict):
    home: int
    away: int

class GamePeriods(TypedDict):
    first: GamePeriod
    second: GamePeriod
    third: GamePeriod
    fourth: GamePeriod
    fifth: GamePeriod

class Game(TypedDict): 
  id: int
  date: str
  time: str
  timestamp: int
  timezone: str
  week: str
  status: GameStatus
  country: Country
  league: League
  teams: GameTeams
  scores: GameScores
  periods: GamePeriods

class GameResponse(TypedDict(
        "GameResponse",
        {'get': str},
    )):
    parameters: dict
    errors: List[str]
    results: int
    response: List[Game]
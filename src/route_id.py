from dataclasses import dataclass

@dataclass(frozen=True)
class RouteID:
    RED: int = 20
    BLUE: int = 21
    GREEN: int = 17
    GOLD: int = 29
    CLOUGH: int = 28
    ATLANTIC: int = 26
    EMORY: int = 18
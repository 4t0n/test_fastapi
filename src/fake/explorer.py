from model.explorer import Explorer


_explorers = [
    Explorer(
        name="Claude Hande",
        country="FR",
        description="Scarce during full moons",
    ),
    Explorer(
        name="Noah Weiser", country="DE", description="Myopic machete man"
    ),
]


def get_all() -> list[Explorer]:
    """Возврат всех исследователей"""
    return _explorers


def get_one(name: str) -> Explorer | None:
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
    return None


def create(explorer: Explorer) -> Explorer:
    """Добавление исследователя"""
    return explorer


def modify(explorer: Explorer) -> Explorer:
    """Частичное изменение записи исследователя"""
    return explorer


def replace(explorer: Explorer) -> Explorer:
    """Полная замена записи исследователя"""
    return explorer

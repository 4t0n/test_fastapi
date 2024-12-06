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


def modify(name: str, explorer: Explorer) -> Explorer:
    """Частичное изменение записи исследователя"""
    return explorer


def replace(name: str, explorer: Explorer) -> Explorer:
    """Полная замена записи исследователя"""
    return explorer


def delete(name: str) -> bool | None:
    """Удаление записи существа; возврат значения None,
    если запись существовала"""
    return None

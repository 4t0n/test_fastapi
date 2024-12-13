import pytest
from data import creature
from errors import Missing
from model.creature import Creature
from service import creature as code


sample = Creature(
    name="Yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman",
)


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one("Yeti")
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        creature.get_one("boxturtle")

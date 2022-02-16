import pytest

from solution import Marine, Marauder, TankBullet


@pytest.fixture
def getTankBullet():
    return TankBullet()


def test_visit_light(getTankBullet):
    light = Marine()
    light.accept(getTankBullet)
    assert light.health == 100 - 21


def test_visit_armored(getTankBullet):
    armored = Marauder()
    armored.accept(getTankBullet)
    assert armored.health == 125 - 32

# PatternCraft - Visitor
from abc import ABC, abstractmethod


class Unit(ABC):

    def __init__(self, health):
        self.health = health

    @abstractmethod
    def accept(self, visitor):
        pass


class Marine(Unit):

    def __init__(self, health=100):
        super().__init__(health)

    def accept(self, visitor):
        visitor.visit_light(self)


class Marauder(Unit):

    def __init__(self, health=125):
        super().__init__(health)

    def accept(self, visitor):
        visitor.visit_armored(self)


class TankBullet:

    def visit_light(self, unit: Marauder):
        unit.health -= 21

    def visit_armored(self, unit: Marine):
        unit.health -= 32

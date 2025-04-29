from test.bases import WorldTestBase
from .. import AnimalWellWorld


class AWTestBase(WorldTestBase):
    game = "Animal Well"
    world: AnimalWellWorld

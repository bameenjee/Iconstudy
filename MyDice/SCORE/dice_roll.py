from iconservice import *
from .customizedclass import DataClass

TAG = 'DiceRoll'

class DiceRoll(IconScoreBase):

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)

    def on_install(self) -> None:
        super().on_install()

    def on_update(self) -> None:
        super().on_update()
    
    @external(readonly=True)
    def diceRoll(self, data: str) -> int:
        data = DataClass(data, self.block.timestamp)
        return data.to_random()
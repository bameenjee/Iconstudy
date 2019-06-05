from iconservice import *

TAG = 'MEMO'

class Memo(IconScoreBase):
    _MEMO_ARRAY = "_MEMO_ARRAY"

    def __init__(self, db: IconScoreDatabase) -> None:
        super().__init__(db)
        self._memo_array = ArrayDB(self._MEMO_ARRAY, db, value_type=str)

    def on_install(self) -> None:
        super().on_install()
     
    def on_update(self) -> None:
        super().on_update()

    @external
    def add_memo(self, memo: str) -> None:
        self._memo_array.put(memo)

    @external(readonly=True)
    def get_memo_list(self) -> dict:
        array_data = []
        for memo in self._memo_array:
            array_data.append(memo)

        return {'memos': array_data}
¡

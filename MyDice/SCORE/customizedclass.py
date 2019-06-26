from iconservice import *


class DataClass:
    def __init__(self, data: str, timestamp: int):
        self.data = data
        self.timestamp = timestamp
 
    def to_random(self):
        input_data = f'{self.timestamp}, {self.data}'.encode()
        hash = sha3_256(input_data)
        return int.from_bytes(hash, 'big') % 6
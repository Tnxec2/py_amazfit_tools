import logging

class DrawingOrder:
    def __init__(self, flag):
        self._flag = flag

    def toJSON(self):
        return f"{hex(self._flag).split('x')[1]}"

    @staticmethod
    def fromJSON(strValue):
        v = int(strValue, 16)
        return v

import io
import logging


class BitWriter():

    def __init__(self, stream):
        self._masks = [128, 192, 224, 240, 248, 252, 254, 255]
        self._stream = stream
        self._currentBit = 0
        self._currentByte = 0
   
    def WriteBits(self, data, length):
        while (length > 0):
            freeBits = 8 - self._currentBit
            dataLength = min(freeBits, length)

            currentByteData = data >> (length - 8) if (length > 8) else data << (8 - length)
            appendData = (currentByteData & self._masks[dataLength - 1]) >> self._currentBit
            self._currentByte = self._currentByte | appendData
            self._currentBit += dataLength
            length -= dataLength
            if (self._currentBit != 8):
                continue

            self._stream.write(self._currentByte.to_bytes(1, 'little'))
            self._currentBit = 0
            self._currentByte = 0
            

    def Flush(self):
        if (self._currentBit > 0):
            self._stream.write(self._currentByte.to_bytes(1, 'little'))
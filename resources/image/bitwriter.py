import io
import math


class BitWriter():

    def __init__(self, stream):
        self._masks = [128, 192, 224, 240, 248, 252, 254, 255]
        self._stream = io.BytesIO(stream)
        self._currentBit = 0
        self._currentByte = ''

    def WriteInt(self, value):
        self.WriteBits(value, 8)

    def WriteBoolena(self, value):
        self.WriteBits( (1 if (value) else 0), 1)
    
    def WriteBits(self, binaryString):
        length = len(binaryString)
        data = self.Convert.ToUInt32(binaryString, 2)
        self.WriteBits(data, length)
    
    def WriteBits(self, data, length):
        while (length > 0):
            freeBits = 8 - self._currentBit
            dataLength = math.Min(freeBits, length)

            currentByteData = data >> (length - 8) if (length > 8) else data << (8 - length)
            appendData = (currentByteData & self._masks[dataLength - 1]) >> self._currentBit
            self._currentByte = self._currentByte | appendData
            self._currentBit += dataLength;
            length -= dataLength;
            if (self._currentBit != 8):
                continue

            self._stream.write(self._currentByte.to_bytes(1, byteorder='little'))
            self._currentBit = 0;
            self._currentByte = 0;
            

    def Flush(self):
        if (self._currentBit > 0):
            self._stream.write(self._currentByte.to_bytes(1, byteorder='little'))
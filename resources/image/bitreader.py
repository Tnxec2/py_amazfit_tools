import io


class BitReader():

    def __init__(self, stream):
        self._masks = [128, 192, 224, 240, 248, 252, 254, 255]
        self._stream = io.BytesIO(stream)
        self._bitsRemaining = 0
        self._currentByte = 0
        self._isDataPresent = True

    def IsDataPresent(self):
        if (self._bitsRemaining > 0):
            return True

        self.tryReadNext()
        return self._isDataPresent

    def ReadBit(self):
        return self.ReadBits(1) != 0
    
    def ReadBits(self, length):
        data = 0
        while length > 0:
            if (self._bitsRemaining == 0 and self._isDataPresent):
                self.tryReadNext()

            dataLength = min(length, self._bitsRemaining)

            currentData = self._currentByte & self._masks[dataLength - 1]
            if (length > 8):
                currentData = currentData << (length - 8)
            else:
                currentData = currentData >> (8 - length)
            data = data | currentData;

            self._currentByte = self._currentByte << dataLength
            length -= dataLength
            self._bitsRemaining -= dataLength
        return data

    def tryReadNext(self):
        self._currentByte = int.from_bytes(self._stream.read(1), 'little')
        self._isDataPresent = self._currentByte > -1
        if (self._isDataPresent):
            self._bitsRemaining = 8
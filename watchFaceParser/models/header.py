import logging
from watchFaceParser.config import Config

class Header:
    dialSignature = b"HMDIAL\0"

    headerSize = 40
    unknownPos = 32
    parametersSizePos = 36

    def __init__(self, unknown, parametersSize):
        self.signature = Header.dialSignature
        self.unknown = unknown
        self.parametersSize = parametersSize


    def isValid(self):
        return self.signature == Header.dialSignature


    def writeTo(self, stream):
        HeaderSize = 40
        buffer = bytearray(HeaderSize)
        for i in range(HeaderSize):
            buffer[i] = 0xff
        buffer[0:len(self.signature)] = self.signature
        t = self.unknown.to_bytes(4, byteorder='little')
        buffer[32:32+len(t)] = t
        t = self.parametersSize.to_bytes(4, byteorder='little')
        buffer[36:36+len(t)] = t

        self.hackBuffer(0, buffer)
        stream.write(buffer)


    # from genuine watchfaces
    def hackBuffer(self, index, buffer):
        data_0x10 = {
            0 : [0x0F, 0x00, 0xF8, 0x06, 0x00, 0x00, 0xD5, 0x3C],
        }

        p_0x10 = data_0x10[index]
        for i in range(len(p_0x10)):
            buffer[0x10 + i] = p_0x10[i]



    @staticmethod
    def readFrom(stream):
        sig_buffer = stream.read(16)

        bipMode = sig_buffer[0x0b] == 0xff
        if bipMode:
            Header.headerSize = 40 - 16
            Header.unknownPos = 32 - 16
            Header.parametersSizePos = 36 - 16
        else:
            Header.headerSize = 64 - 16
            Header.unknownPos = 52 - 16
            Header.parametersSizePos = 56 - 16

        buffer = stream.read(Header.headerSize)

        header = Header(
            unknown = int.from_bytes(buffer[Header.unknownPos:Header.unknownPos+4], byteorder='little'),
            parametersSize = int.from_bytes(buffer[Header.parametersSizePos:Header.parametersSizePos+4], byteorder='little'))
        header.signature = sig_buffer[0:7]
        return header
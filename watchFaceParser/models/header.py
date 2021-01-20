import logging
from watchFaceParser.config import Config

class Header:
    dialSignature = b"HMDIAL\0"

    deviceIdPos = 0
    headerSize = 40
    unknownPos = 32
    parametersSizePos = 36

    def __init__(self, unknown, parametersSize, deviceId = None):
        self.signature = Header.dialSignature
        self.unknown = unknown
        self.parametersSize = parametersSize
        self.deviceId = deviceId

    def isValid(self):
        return self.signature == Header.dialSignature


    def writeTo(self, stream): 
        if Config.isGtr2Mode() :
            Header.headerSize = 88
            Header.unknownPos = 76
            Header.parametersSizePos = 80
        else:
            Header.headerSize = 64
            Header.unknownPos = 52
            Header.parametersSizePos = 56  
        buffer = bytearray(Header.headerSize)
        for i in range(Header.headerSize):
            buffer[i] = 0xff
        buffer[0:len(self.signature)] = self.signature
        buffer[11] = 0x06 # verge
        t = self.unknown.to_bytes(4, byteorder='little')
        buffer[Header.unknownPos:Header.unknownPos+len(t)] = t
        t = self.parametersSize.to_bytes(4, byteorder='little')
        buffer[Header.parametersSizePos:Header.parametersSizePos+len(t)] = t

        self.hackBuffer(1, buffer)
        stream.write(buffer)


    # from genuine watchfaces
    # don't know why yet
    def hackBuffer(self, index, buffer):
        data_0x10 = {
            1 : [0x20, 0x00, 0x6e, 0xea, 0x00, 0x00, 0x01, 0xbc],
            2 : [0x20, 0x00, 0x6d, 0xea, 0x00, 0x00, 0x81, 0x77],
            3 : [0x20, 0x00, 0x6a, 0xea, 0x00, 0x00, 0xb1, 0xf3],
            4 : [0x20, 0x00, 0x69, 0xea, 0x00, 0x00, 0x74, 0xfa],
            5 : [0x20, 0x00, 0x6b, 0xea, 0x00, 0x00, 0x7c, 0x3e],
            6 : [0x20, 0x00, 0x6f, 0xea, 0x00, 0x00, 0x14, 0xde],
            7 : [0x20, 0x00, 0x70, 0xea, 0x00, 0x00, 0x35, 0xa1],
            8 : [0x20, 0x00, 0x6c, 0xea, 0x00, 0x00, 0x3f, 0x2c],
            40 : [0x2e, 0x00, 0xaa, 0xeb, 0x00, 0x00, 0x68, 0xf1], #gts 0xaa, 0x68, 0xf1 may vary
            47 : [0x28, 0x00, 0x8c, 0xea, 0x00, 0x00, 0x01, 0xbc], # gtr 47
            42 : [0x2a, 0x00, 0x72, 0xeb, 0x00, 0x00, 0x5c, 0xd3], # gtr 42
            50 : [0x34, 0x00, 0x1e, 0x1c, 0x00, 0x00, 0x49, 0xce], # trex
            53 : [0x35, 0x00, 0x09, 0x00, 0x00, 0x00, 0x4b, 0x9a], # AmazfitX
        }

        if Config.isGtrMode():
            index = Config.isGtrMode()
        if Config.isGtsMode():
            index = Config.isGtsMode()
        if Config.isTrexMode():
            index = Config.isTrexMode()
        if Config.isAmazfitXMode():
            index = Config.isAmazfitXMode()
        p_0x10 = data_0x10[index]
        for i in range(len(p_0x10)):
            buffer[0x10 + i] = p_0x10[i]
        # hard coding?
        buffer[60:60+4] = int(64).to_bytes(4, byteorder='little')


    @staticmethod
    def readFrom(stream):
        sig_buffer = stream.read(16)

        bipMode = sig_buffer[0x0b] == 0xff
        if bipMode:
            Header.headerSize = 40 - 16
            Header.unknownPos = 32 - 16
            Header.parametersSizePos = 36 - 16
        elif Config.isGtr2Mode() :
            Header.headerSize = 88 - 16
            Header.unknownPos = 76 - 16
            Header.parametersSizePos = 80 - 16
        else:
            Header.headerSize = 64 - 16
            Header.unknownPos = 52 - 16
            Header.parametersSizePos = 56 - 16 

        if Config.isGtr2Mode() and not Config._autodetect:
           Header.dialSignature = b"UIHH\x02\x00\xff"

        buffer = stream.read(Header.headerSize)
        header = Header(
            unknown = int.from_bytes(buffer[Header.unknownPos:Header.unknownPos+4], byteorder='little'),
            parametersSize = int.from_bytes(buffer[Header.parametersSizePos:Header.parametersSizePos+4], byteorder='little'),
            deviceId = int.from_bytes(buffer[Header.deviceIdPos:Header.deviceIdPos+1], byteorder='little'))
        header.signature = sig_buffer[0:7]
        return header

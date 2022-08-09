import logging
from watchFaceParser.config import Config
import io

class Header:
    dialSignature = b"HMDIAL\0"

    deviceIdPos = 0
    headerSize = 40
    unknownPos = 32
    parametersSizePos = 36

    basenamehash = ""

    def __init__(self, unknown, parametersSize, deviceId = None):
        self.signature = Header.dialSignature
        self.unknown = unknown
        self.parametersSize = parametersSize
        self.deviceId = deviceId

    def isValid(self):
        return self.signature == Header.dialSignature


    def writeTo(self, stream): 
        val_11= 0x06
        if Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode():
            Header.headerSize = 88
            Header.unknownPos = 76
            Header.parametersSizePos = 80 
            self.signature = b"UIHH\x02\x00\xff"
            val_11 = 0x01
        else:
            Header.headerSize = 64
            Header.unknownPos = 52
            Header.parametersSizePos = 56  
        buffer = bytearray(Header.headerSize)
        for i in range(Header.headerSize):
            buffer[i] = 0xff
        buffer[0:len(self.signature)] = self.signature
        buffer[11] = val_11 # verge
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
            59 : [0x3B, 0x00, 0x97, 0x04, 0x00, 0x00, 0x97, 0xD1, 0x02, 0x00], #gtr2
            65 : [0x41, 0x00, 0x51, 0x04, 0x00, 0x00, 0x43, 0x01, 0x02, 0x00], #gts2: 0x51, 0x04, 0x00, 0x00, 0x43, 0x01, 0x02, 0x00 - may vary
            83 : [0x53, 0x00, 0x36, 0x04, 0x00, 0x00, 0x1E, 0xAB, 0x03, 0x00], #gtr2
        }

        if Config.isGtrMode():
            index = Config.isGtrMode()
        elif Config.isGtr2Mode():
            index = 59
        elif Config.isGts2Mode():
            index = 65
        elif Config.isTrexProMode():
            index = 83
        elif Config.isGtsMode():
            index = Config.isGtsMode()
        elif Config.isTrexMode():
            index = Config.isTrexMode()
        elif Config.isAmazfitXMode():
            index = Config.isAmazfitXMode()
        p_0x10 = data_0x10[index]
        for i in range(len(p_0x10)):
            buffer[0x10 + i] = p_0x10[i]
        # hard coding?
        if Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode():
            buffer[12:12+4] = int(57305).to_bytes(4, byteorder='little') #some size??
            buffer[84:84+4] = int(48).to_bytes(4, byteorder='little')
            if Config._oldformat:
                buffer[75] = 0x00
            else:
                buffer[75] = 0x01
        else:
            buffer[60:60+4] = int(64).to_bytes(4, byteorder='little')


    @staticmethod
    def readFrom(stream):
        sig_buffer = stream.read(16)

        bipMode = sig_buffer[0x0b] == 0xff
        if bipMode:
            Header.headerSize = 40 - 16
            Header.unknownPos = 32 - 16
            Header.parametersSizePos = 36 - 16
        elif Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode() :
            Header.headerSize = 88 - 16
            Header.unknownPos = 76 - 16
            Header.parametersSizePos = 80 - 16
        else:
            Header.headerSize = 64 - 16
            Header.unknownPos = 52 - 16
            Header.parametersSizePos = 56 - 16 

        if Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode():
           Header.dialSignature = b"UIHH\x02\x00\xff"

        buffer = stream.read(Header.headerSize)
        header = Header(
            unknown = int.from_bytes(buffer[Header.unknownPos:Header.unknownPos+4], byteorder='little'),
            parametersSize = int.from_bytes(buffer[Header.parametersSizePos:Header.parametersSizePos+4], byteorder='little'),
            deviceId = int.from_bytes(buffer[Header.deviceIdPos:Header.deviceIdPos+1], byteorder='little'))
        header.signature = sig_buffer[0:7]

        if  Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode():
            if buffer[75-16] == 0x00:
                Config.setOldFormat(True)
                logging.info("Old json format for GTS2/GTR2")
                print("Old json format for GTS2/GTR2")
        return header
    
    @staticmethod
    def patchHeaderAfter( outputFileName ):
        if Config.isGtr2Mode() or Config.isGts2Mode() or Config.isTrexProMode(): 
            with open(outputFileName, 'rb+') as fileStream:
                logging.debug(f"Injecting additional header info") 
                header = bytearray( fileStream.read(40) )       
                data = bytearray( fileStream.read() )                 
                #write size
                size = len(data)
                header[32:32+4] = int(size).to_bytes(4, byteorder='little')
                logging.debug(f"Injected size: {size}")
                
                # write basename as 7 bit hash
                import hashlib, os
                baseName, _ = os.path.splitext(os.path.basename(outputFileName))
                basenamehash = bytearray(hashlib.shake_128(baseName.encode()).digest(7)) # 7 bit hash
                logging.debug(f"basename: {baseName}")
                logging.debug(f"hash lenght: {len(basenamehash)}")
                logging.debug("basename 7 byte hash " + "".join("%02x" % b for b in basenamehash))
                header[12:12+2] = basenamehash[0:2]#.to_bytes(2, byteorder='little')
                header[18:18+2] = basenamehash[2:4]#.to_bytes(2, byteorder='little')
                header[22:22+3] = basenamehash[4:7]#.to_bytes(3, byteorder='little')
                
                fileStream.seek(0)
                fileStream.write(header)
                fileStream.write(data)
                fileStream.flush()
    
    @staticmethod
    def crc16(data : bytearray, offset , length):
        if data is None or offset < 0 or offset > len(data)- 1 and offset+length > len(data):
            return 0
        crc = 0xFFFF
        for i in range(0, length):
            crc ^= data[offset + i] << 8
            for j in range(0,8):
                if (crc & 0x8000) > 0:
                    crc =(crc << 1) ^ 0x1021
                else:
                    crc = crc << 1
        return crc & 0xFFFF
     

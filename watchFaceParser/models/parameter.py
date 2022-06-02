import logging
import io
from watchFaceParser.config import Config
import struct

from watchFaceParser.models.parameterFlags import ParameterFlags

def ulong2long(n):
    if type(n) == int:
        if n >= 0x7fffffffffffffff:
            n = -(0xffffffffffffffff - n + 1)
    return n

def long2ulong(n):
    if type(n) == int:
        if n < 0:
            #n = (0xffffffffffffffff + n + 1) & 0xffffffff
            n = (0xffffffffffffffff + n + 1) #fix negative integers
    return n

def uint2int(n):
    if type(n) == int:
        if n >= 0x7fffffff:
            return -(0xffffffff - n + 1)
    return n

def int2uint(n):
    if type(n) == int:
        if n < 0: 
            n = (0xffffffff + n + 1) #fix negative integers
    return n
 

class Parameter:
    def __init__(self, _id, value, flags = None, pType = None):
        self._pType = pType
        if type(flags) == int:
            self._id = _id
            self._value = None
            self._children = None
            self._flags = flags 
        elif pType == 'int':
            self._id = _id
            self._value = uint2int(value)
            self._children = None
            self._flags = None
        elif type(value) == int:
            self._id = _id
            self._value = ulong2long(value)
            self._children = None
            self._flags = None
        elif type(value) == list:
            self._id = _id
            self._value = None
            self._children = value
            self._flags = None
        elif type(value) == float:
            self._id = _id
            self._value = value
            self._children = None
            self._flags = ParameterFlags.ModeFloatValue
        else:
            raise Exception(f'invalid type for parameter {value}:{type(value)}')

    def getId(self):
        return self._id


    def getType(self):
        return self._pType

    def getChildren(self):
        return self._children


    def getValue(self):
        return self._value

    def hasChildren(self):
        return self._children is not None
        #return self._children and len(self._children) > 0

    def hasFlags(self):
        return self._flags

    @staticmethod
    def writeByte(stream, v):
        stream.write(int(v).to_bytes(1, byteorder='little'))


    def write(self, stream, traceOffset = 0):
        assert(type(traceOffset) == int)
        size = 0
        flags = ParameterFlags.hasChildren if self.hasChildren() else 0
        flags |= self.hasFlags() if self.hasFlags() else 0
		
        rawId = 0xff & ((self.getId() << 3) + flags)
        #Parameter.writeByte(stream, rawId)
        self.writeValue(stream, rawId, traceOffset, self.getType())
        value = self.getValue()
        size += 1
        pflags = ParameterFlags(flags)
        if pflags.hasFlag(ParameterFlags.Unknown) and pflags.hasFlag(ParameterFlags.Unknown2):
            floatValArr = struct.pack('<f', value)  #little endian 
            stream.write(floatValArr)
            hex_string = "".join("%02x " % b for b in floatValArr)
            logging.info(Parameter.traceWithOffset(f"{self.getId()} ({rawId:2X}): %8.2f ({hex_string}) floatval" % value, traceOffset)) 
            return size + len(floatValArr)
        elif self.hasFlags():
    #        print ("EDDI %02x %x %x"% (rawId,flags,(ParameterFlags.Unknown | ParameterFlags.Unknown2| ParameterFlags.hasChildren)))
            logging.debug(("\t" * traceOffset) + f"{size} bytes")
            return size -1
        elif self.hasChildren():
            logging.debug(("\t" * traceOffset) + f"{self.getId()} ({rawId:02X}):")
            size += self.writeList(stream, traceOffset + 1)
            #logging.debug(("\t" * traceOffset) + f"{size} bytes")
            return size
        if value is None:
            value = 0
        size += self.writeValue(stream, value, traceOffset, self.getType())
        
        logging.debug(("\t" * traceOffset) + f"{self.getId()} ({rawId:02X}): {value} ({value:02X})")
        return size


    def writeList(self, stream, traceOffset):
        assert(type(traceOffset) == int)
        temporaryStream = io.BytesIO()
        for parameter in self.getChildren():
            parameter.write(temporaryStream, traceOffset)
        size = self.writeValue(stream, len(temporaryStream.getbuffer()), traceOffset, self.getType())
        temporaryStream.seek(0, 0)
        stream.write(temporaryStream.read())
        size += len(temporaryStream.getbuffer())
        return size


    def writeValue(self, stream, value, traceOffset, pType):        
        assert(type(value) == int)
        assert(type(traceOffset) == int)
        if (pType == 'int'):
            unsignedValue = int2uint(value)
        else:
            unsignedValue = long2ulong(value)
        size = 0
        currentByte = 0
        while unsignedValue >= 0x80:
            currentByte = 0xff & ((unsignedValue & 0x7f) | 0x80)
            Parameter.writeByte(stream, currentByte)
            size += 1
            unsignedValue = unsignedValue >> 7

        currentByte = 0xff & (unsignedValue & 0x7f)
        Parameter.writeByte(stream, currentByte)
        size += 1
        return size


    @staticmethod
    def readList(stream, traceOffset = 0):
        result = []
        try:
            while True:
                parameter = Parameter.readFrom(stream, traceOffset)
                result.append(parameter)
        except EOFError:
            pass
        except IndexError:
            pass
        except Exception as e:
            import traceback
            traceback.print_stack()
            logging.exception(e)
        return result


    @staticmethod
    def readFrom(fileStream, traceOffset = 0):
        #rawId = Parameter.readByte(fileStream, traceOffset)
        rawId = Parameter.readValue(fileStream, traceOffset) 
        _id = (rawId & 0xf8) >> 3
 #       print ("%03x" % rawId, rawId & 0x07)
        flags = ParameterFlags(rawId & 0x07)
        #logging.info("FLAGS %x" % (rawId & 0x07))

        if _id == 0:
            raise IndexError("Parameter with zero Id is invalid.") #ArgumentException
          
        #logging.info("DEBUG ID %d FLAGS %x VALUE %x" % (_id, rawId & 0x07, value))
#        if value == 1 and flags.hasFlag(ParameterFlags.hasChildren):
#            value = Parameter.readValue(fileStream, traceOffset)
#            logging.info("DEBUG                 %02x" % Parameter.readByte(fileStream, traceOffset))
#            pass 
        value = 0
        if flags.hasFlag(ParameterFlags.Unknown) and flags.hasFlag(ParameterFlags.Unknown2): 
            floatValArr = bytearray(fileStream.read(4)) 
            value = struct.unpack('<f', floatValArr)[0]   #little endian 
            hex_string = "".join("%02x " % b for b in floatValArr)
            logging.info(Parameter.traceWithOffset(f"{_id} ({rawId:2X}): %8.2f ({hex_string}) floatval" % value, traceOffset))
            return Parameter(_id, value)
        elif flags.hasFlag(ParameterFlags.Unknown2):
            value = Parameter.readValue(fileStream, traceOffset)
            value = flags.getValue()
            logging.info("Warning found Unknown2 flag")
        elif flags.hasFlag(ParameterFlags.hasChildren):
            value = Parameter.readValue(fileStream, traceOffset)
            if value == 0:
                logging.info("DEBUG                 %02x" % Parameter.readByte(fileStream, traceOffset))
                logging.info("DEBUG                 %02x" % Parameter.readByte(fileStream, traceOffset))
            logging.info(Parameter.traceWithOffset(f"{_id} ({rawId:2X}): {value} bytes", traceOffset))
            buffer = fileStream.read(value)
            stream = io.BytesIO(buffer)

            _list = Parameter.readList(stream, traceOffset + 1)
            return Parameter(_id, _list)
        else:
            value = Parameter.readValue(fileStream, traceOffset)
        logging.info(Parameter.traceWithOffset(f"{_id} ({rawId:2X}): {value} {value:2X}", traceOffset))
        return Parameter(_id, value)


    @staticmethod
    def readValue(fileStream, traceOffset = 0):
        bytesLength = 0
        value = 0
        offset = 0

        currentByte = Parameter.readByte(fileStream, traceOffset)
        bytesLength = bytesLength + 1

        while (currentByte & 0x80) > 0:
            if bytesLength > 9:
                raise Exception("Value of the parameter too long")
            value = value | ((currentByte & 0x7f) << offset)
            offset += 7
            currentByte = Parameter.readByte(fileStream, traceOffset)
            bytesLength = bytesLength + 1

        value = value | ((currentByte & 0x7f) << offset)
        return value


    @staticmethod
    def readByte(stream, traceoffset = 0):
        currentByte = int.from_bytes(stream.read(1), byteorder='little')
        return currentByte


    @staticmethod
    def traceWithOffset(message, offset):
        return '    ' * offset + message

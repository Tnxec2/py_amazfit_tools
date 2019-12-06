import logging
import os.path

from watchFaceParser.utils.elementsHelper import ElementsHelper
from watchFaceParser.utils.integerConverter import uint2int
from watchFaceParser.models.parameterFlags import ParameterFlags
from watchFaceParser.models.textAlignment import TextAlignment
from watchFaceParser.models.color import Color
from watchFaceParser.models.parameter import Parameter


class ParametersConverter:
    @staticmethod
    def getValue(propertyInfo, serializable):
        propertyInfoName = propertyInfo['Name']
        if not propertyInfoName in serializable:
            return None
        return serializable[propertyInfoName]


    @staticmethod
    def build(T, serializable, path = ""):
        result = []
        #print ("T",T)
        properties = ElementsHelper.sortedProperties(T)
#        print ("X",properties)
        for _id in properties:
            currentPath = str(_id) if path == None or path == '' else ''.join([path, '.', str(_id)])

            propertyInfo = properties[_id]
            #propertyType = propertyInfo['Type']
            if isinstance(propertyInfo['Type'],list):
                propertyType = propertyInfo['Type'][0]
            else:
                propertyType = propertyInfo['Type']
				
            propertyValue = ParametersConverter.getValue(propertyInfo, serializable)
#            print("QUI",propertyInfo['Name'],serializable,propertyValue)

            if propertyValue is None:
                continue

            if propertyType == 'long' or propertyType == 'long?' or propertyType == TextAlignment or propertyType == Color or propertyType == 'bool':
                value = propertyValue
                if propertyType == 'bool' or type(propertyValue) == bool:
                    value = 1 if propertyValue else 0
                elif propertyType == TextAlignment:
                    value = TextAlignment.fromJSON(propertyValue)
                elif propertyType == Color:
                    value = Color.fromJSON(propertyValue)
                elif propertyType == 'long' or propertyType == 'long?':
                    value = int(value)				

                logging.debug(f"{currentPath} '{propertyInfo['Name']}': {value}")
                result.append(Parameter(_id, value))
            #elif isinstance(propertyValue,list): 
            #    print ("e' una lista... fai qualcosa",propertyType)
            #    for i in propertyValue:
            #        print ("I1",i)
            #        innerParameters = ParametersConverter.build(propertyType, i, currentPath)
            #        print ("I2",i,innerParameters)
            #        if len(innerParameters) > 0:
            #            logging.debug(f"{currentPath} '{propertyInfo['Name']}'")
            #            result.append(Parameter(_id, innerParameters))
            #        else:
            #            logging.debug(f"{currentPath} '{propertyInfo['Name']}': Skipped because of empty(loop)")
            elif propertyType == ParameterFlags:
                flags = ParameterFlags.fromJSON(propertyValue)
                logging.debug(f"{currentPath} '{propertyInfo['Name']}': {flags}")
                result.append(Parameter(_id, None, flags = flags))

            else:

#                logging.debug ("childIsList "+str(childIsList)+" "+str(propertyType))
                if isinstance(propertyValue,list):
                    for i in propertyValue:
                        #d={}
                        #d[propertyInfo['Name']] = i
#                        print ("1propertyType",propertyType, d, currentPath )			
                        innerParameters = ParametersConverter.build(propertyType, i, currentPath)
                        #logging.debug(i)

                        if len(innerParameters) > 0:
                            #print ("I0",propertyType, propertyValue)
                            logging.debug(f"{currentPath} '{propertyInfo['Name']}'")
                            result.append(Parameter(_id, innerParameters))
                        else:
                            logging.debug(f"{currentPath} '{propertyInfo['Name']}': Skipped because of empty1")
                    continue
                innerParameters = ParametersConverter.build(propertyType, propertyValue, currentPath)
 #               print ("2propertyType",propertyType, propertyValue, currentPath )			
  #              logging.debug(propertyValue)
  #              logging.debug(propertyType)
#            if not childIsList:

                if len(innerParameters) > 0:
                    #print ("Ip",innerParameters)
                    logging.debug(f"{currentPath} '{propertyInfo['Name']}'")
                    result.append(Parameter(_id, innerParameters))
                else:
                    logging.debug(f"{currentPath} '{propertyInfo['Name']}': Skipped because of empty2")
 #                   print ("propertyType",propertyType, propertyValue )			
 #                   sys.exit(1)

        return result

    @staticmethod
    def childIsList(paramType, descriptor, path = ""):
        assert(type(descriptor) == type([]))
        assert(type(path) == type(""))
        properties = ElementsHelper.sortedProperties(paramType)
        currentType = paramType

        for parameter in descriptor:
            parameterId = parameter.getId()

            currentPath = str(parameterId) if not path else os.path.join(path, '.', str(parameterId))

            if parameterId not in properties:
                logging.warn(f"[ParamConv:parse] currentPath {currentPath} / Parameter {parameterId} isn't supported for {currentType}")
                raise IndexError(f"Parameter {parameterId} isn't supported for {currentType}")

            propertyInfo = properties[parameterId]

            if isinstance(propertyInfo['Type'],list):
                childIsList = True
            else:
                childIsList = False
        return childIsList

    @staticmethod
    def parse(paramType, descriptor, path = ""):
        assert(type(descriptor) == type([]))
        assert(type(path) == type(""))
        properties = ElementsHelper.sortedProperties(paramType)
        result = paramType()
        currentType = paramType

        prevPath = None
        artmp=[]

        for parameter in descriptor:
            parameterId = parameter.getId()

            currentPath = str(parameterId) if not path else os.path.join(path, '.', str(parameterId))

            if parameterId not in properties:
                logging.warn(f"[ParamConv:parse] currentPath {currentPath} / Parameter {parameterId} isn't supported for {currentType}")
                raise IndexError(f"Parameter {parameterId} isn't supported for {currentType}")

            propertyInfo = properties[parameterId]
            
            if isinstance(propertyInfo['Type'],list):
                propertyType = propertyInfo['Type'][0]
            else:
                propertyType = propertyInfo['Type']

            propertyInfoName = propertyInfo['Name']
            if propertyType == 'long' or propertyType == 'long?' or propertyType == TextAlignment or propertyType == ParameterFlags or propertyType == Color or propertyType == 'bool':
                if propertyType == TextAlignment:
                    setattr(result, propertyInfoName, TextAlignment(parameter.getValue()))
                elif propertyType == ParameterFlags:
                    setattr(result, propertyInfoName, ParameterFlags(parameter.getValue()))
                elif propertyType == Color:
                    setattr(result, propertyInfoName, Color(parameter.getValue()))
                elif propertyType == 'bool':
                    setattr(result, propertyInfoName, parameter.getValue() > 0)
                elif propertyType == 'long':
                    setattr(result, propertyInfoName, uint2int(parameter.getValue()))
                else:
                    setattr(result, propertyInfoName, uint2int(parameter.getValue() or None))
            elif propertyType == '[]':
                assert(False) # not tested yet
            else:		
                tmp = propertyType()	
                childIsList = False
                artmp = []
                for x in parameter.getChildren():
                    if not childIsList:
                        childIsList = ParametersConverter.childIsList(propertyType, [x], currentPath)

                    psd = ParametersConverter.parse(propertyType, [x], currentPath)
                    import json

                    for kk in psd.__dict__:
                        vv = psd.__dict__[kk]
                        if not childIsList:
                            setattr(tmp, kk, vv)
                        else:
                            artmp.append(vv)
                    if childIsList:
                        setattr(tmp, kk, artmp)
                setattr(result, propertyInfoName, tmp)
        return result

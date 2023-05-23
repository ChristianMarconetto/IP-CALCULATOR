from Utils import isNotValid
class Address:
    def __init__(self, inputValue):
        if isinstance(inputValue, str):
            #controllo [0-223].[0-255].[0-255].[0-255].
            if isNotValid(inputValue): raise ValueError("Invalid IP address.")
            self.__decimalDotted = inputValue
            self.__binary = self.__getBinaryFromDecimalDotted()
            self.__decimal = self.__getDecimalFromBinary()
        if isinstance(inputValue, int):
            self.__decimal = inputValue
            self.__binary = self.__getBinaryFromDecimal()
            self.__decimalDotted = self.__getDecimalDottedFromBinary()

    def __getBinaryFromDecimalDotted(self):
        binary = self.__decimalDotted.split(".")
        for i in range(4):
                binary[i] = bin(int(binary[i]))[2:]
                if len(binary[i])<8:
                    binary[i] = ((8- len(binary[i] )) * "0" ) + binary[i]
        return "".join(binary)

    def __getDecimalFromBinary(self):
        return int(self.__binary,2)
                   
    def __getBinaryFromDecimal(self):
        binary = bin(self.__decimal)[2:].zfill(32)
        octets = [binary[i:i+8] for i in range(0, len(binary), 8)]
        binary = ''.join(octets)
        return binary
    
    def __getDecimalDottedFromBinary(self):
        binary = self.__binary  # Ottiene la rappresentazione binaria senza punti
        octets = [binary[i:i+8] for i in range(0, len(binary), 8)]  # Divide il numero binario in ottetti
        decimal_dotted = '.'.join([str(int(octet, 2)) for octet in octets])  # Converte gli ottetti in decimali e li unisce con punti
        return decimal_dotted
    def getDecimalDotted(self):
        return self.__decimalDotted
    def getDecimal(self):
        return self.__decimal
    def getBinary(self):
        return self.__binary
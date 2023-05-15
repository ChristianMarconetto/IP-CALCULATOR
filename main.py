def clearConsole():
     print("\033c", end='')
def isNotValid(ipAddress):
    octets = ipAddress.split(".")
    if len(octets) != 4:
        return True
    if (octets[0].isdigit()) and (int(octets[0]) < 0 or int(octets[0]) > 223) :
        return True
    for octet in octets:
        if not octet.isdigit():
            return True
        value = int(octet)
        if value < 0 or value > 255:
            return True
    return False

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
    
clearConsole()
ipDiCasa = Address("192.168.0.1")
print("IP1 INFO")
print("Decimal dotted = "+ ipDiCasa.getDecimalDotted())
print("Binary = "+ipDiCasa.getBinary())
print("Decimal = "+ str(ipDiCasa.getDecimal()))
print("-------------")
ipDiScuola = Address(1361052929)
print("IP2 INFO")
print("Decimal dotted = "+ ipDiScuola.getDecimalDotted())#
print("Binary = "+ipDiScuola.getBinary())
print("Decimal = "+ str(ipDiScuola.getDecimal()))


import os

class Address:
    def __init__(self, inputValue):
        try:
            if isinstance(inputValue, str):
                self.decimalDotted = inputValue
                self.binary = self.getBinaryFromDecimalDotted()
                self.decimal = self.getDecimalFromBinary()
            elif isinstance(inputValue, int):
                self.decimal = inputValue
                self.binary = self.getBinaryFromDecimal()
                self.decimalDotted = self.getDecimalDottedFromBinary()
            else:
                raise ValueError("Invalid input type. Must be a string or an integer.")
        except ValueError as e:
            print("Error: " + str(e))
            self.decimalDotted = None
            self.binary = None
            self.decimal = None

    def getBinaryFromDecimalDotted(self):
        try:
            binary = [bin(int(octet))[2:].zfill(8) for octet in self.decimalDotted.split(".")]
            return "".join(binary)
        except ValueError as e:
            raise ValueError("Invalid decimal dotted format. " + str(e))

    def getDecimalFromBinary(self):
        try:
            return int(self.binary, 2)
        except ValueError as e:
            raise ValueError("Invalid binary format. " + str(e))

    def getBinaryFromDecimal(self):
        try:
            return bin(self.decimal)[2:].zfill(32)
        except ValueError as e:
            raise ValueError("Invalid decimal format. " + str(e))

    def getDecimalDottedFromBinary(self):
        try:
            octets = [str(int(self.binary[i:i+8], 2)) for i in range(0, 32, 8)]
            return ".".join(octets)
        except ValueError as e:
            raise ValueError("Invalid binary format. " + str(e))

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

ipDiCasa = Address("192.168.0.1")
print("IP1 INFO")
print("Decimal dotted = "+ ipDiCasa.decimalDotted)
print("Binary = "+ipDiCasa.binary)
print("Decimal = "+ str(ipDiCasa.decimal))
print("-------------")
ipDiScuola = Address(1361052929)
print("IP2 INFO")
print("Decimal dotted = "+ ipDiScuola.decimalDotted)#
print("Binary = "+ipDiScuola.binary)
print("Decimal = "+ str(ipDiScuola.decimal))

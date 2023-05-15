def clearConsole():
     print("\033c", end='')
class Address:
    def __init__(self, inputValue):
        if isinstance(inputValue, str):
            self.decimalDotted = inputValue
            self.binary = self.getBinaryFromDecimalDotted()
            self.decimal = self.getDecimalFromBinary()
        if isinstance(inputValue, int):
            self.decimal = inputValue
            self.binary = self.getBinaryFromDecimal()
            self.decimalDotted = self.getDecimalDottedFromBinary()

    def getBinaryFromDecimalDotted(self):
        binary = self.decimalDotted.split(".")
        for i in range(4):
                binary[i] = bin(int(binary[i]))[2:]
                if len(binary[i])<8:
                    binary[i] = ((8- len(binary[i] )) * "0" ) + binary[i]
        return "".join(binary)


        
    def getDecimalFromBinary(self):
        return int(self.binary,2)
                   
    def getBinaryFromDecimal(self):
        binary = bin(self.decimal)[2:].zfill(32)
        octets = [binary[i:i+8] for i in range(0, len(binary), 8)]
        binary_address = ''.join(octets)
        return binary_address
    
    def getDecimalDottedFromBinary(self):
        binary_address = self.binary  # Ottiene la rappresentazione binaria senza punti
        octets = [binary_address[i:i+8] for i in range(0, len(binary_address), 8)]  # Divide il numero binario in ottetti
        decimal_dotted = '.'.join([str(int(octet, 2)) for octet in octets])  # Converte gli ottetti in decimali e li unisce con punti
        return decimal_dotted
    
clearConsole()
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


from FileReader import FileReader
from Address import Address
def clearConsole():
     print("\033c", end='')


ip_List = FileReader("ip.txt").readLinesWithFourDots()

#clearConsole()
print(print(ip_List))
print("List of the addresses foundend in ip.txt: ")     
for ip in ip_List:
    print(ip)

for ip in ip_List:
    print("analisys of : ", end="")     
    print(ip)
    ipAddress = Address(ip)
    print("IP1 INFO")
    print("Decimal dotted = "+ ipAddress.getDecimalDotted())
    print("Binary = "+ipAddress.getBinary())
    print("Decimal = "+ str(ipAddress.getDecimal()))
    print("-------------")
#ipDiCasa = Address("192.168.0.1")
#print("IP1 INFO")
#print("Decimal dotted = "+ ipDiCasa.getDecimalDotted())
#print("Binary = "+ipDiCasa.getBinary())
#print("Decimal = "+ str(ipDiCasa.getDecimal()))
#print("-------------")
#ipDiScuola = Address(1361052929)
#print("IP2 INFO")
#print("Decimal dotted = "+ ipDiScuola.getDecimalDotted())#
#print("Binary = "+ipDiScuola.getBinary())
#print("Decimal = "+ str(ipDiScuola.getDecimal()))

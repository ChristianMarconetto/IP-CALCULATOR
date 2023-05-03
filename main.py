class Address:
    def __init__(self, input_value):
        if isinstance(input_value, str):
            self.__decimal_dotted_quad = input_value
            self.__binary_dotted = self.__decimal_to_binary(input_value)
            self.__decimal = self.__binary_to_decimal(self.__binary_dotted)
        elif isinstance(input_value, int):
            self.__decimal = input_value
            self.__binary_dotted = self.__decimal_to_binary(self.__decimal)
            self.__decimal_dotted_quad = self.__binary_to_decimal(self.__binary_dotted)

    def get_decimal_dotted_quad(self):
        return self.__decimal_dotted_quad

    def get_binary_dotted(self):
        return self.__binary_dotted

    def get_decimal(self):
        return self.__decimal

    def __decimal_to_binary(self, decimal_dotted_quad):
        binary_dotted = ""
        octets = str(decimal_dotted_quad).split(".")
        for octet in octets:
            binary_octet = bin(int(octet))[2:].zfill(8)
            binary_dotted += binary_octet + "."
        return binary_dotted[:-1]

    def __binary_to_decimal(self, binary_dotted):
        decimal_dotted = ""
        octets = binary_dotted.split(".")
        for octet in octets:
            decimal_octet = str(int(octet, 2))
            decimal_dotted += decimal_octet + "."
        return decimal_dotted[:-1]



ip = Address("192.168.0.1")
print("IP1:", ip.get_decimal_dotted_quad())
print("IP1 binario:", ip.get_binary_dotted())
print()

ip = Address(-1062731775)
print("IP2:", ip.get_decimal_dotted_quad())
print("IP2 binario:", ip.get_binary_dotted())

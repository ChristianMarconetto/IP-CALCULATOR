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
def bits_to_bytes(bitStr):
    bitStr = bitStr[::-1]
    s=i=0
    for b in bitStr:
        s = (s>>1|(0,0x80)[b])
        i+=1
        if i==8:
            #print (bin(s))
            yield s
            s = i = 0
    while i<8 and i>0:
        s>>=1
        i+=1
    #print (bin(s))
    yield s

def bits(string):
    bitArr = []
    for e in string:
        a = ord(e)
        i = 0
        while (i < 8):
            if ((a>>7)%2 == 1):
                bitArr.append(1)
            else: #((a>>7)%2 == 0):
                bitArr.append(0)
            a <<= 1
            i+=1
    return bitArr

print(bits("Quinn made a String->Bit code!"))
print(bits_to_bytes(bits("QuinnGates")))

s = input()
r=""
for char in s:
    a = ord(char)
    
    if(65<=a<= 90):
        r += chr(a+32)
    if(97 <= a<= 122):
        r += chr(a-32)
print(r)
    
    

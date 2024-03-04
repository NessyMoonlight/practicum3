raw = input('Enter number:')
if isinstance(raw, str) == True :
    num = raw
else:
    num = int(raw)
print(num)
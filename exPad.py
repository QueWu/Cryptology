keyArr = [90,121,109,97,110,111,119,115,107,105]
txtArr = [87,105,101,110,105,97,119,115,107,105]

for x in range(10):
    txtArr[x] = (txtArr[x] + keyArr[x])%127

for y in range(10):
    txtArr[y] = bin(txtArr[y])
print(txtArr)

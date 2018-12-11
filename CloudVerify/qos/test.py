y = [1,1,1,2,2,2,3,3,3,4,4,4,3,3,3,2,2,2,1,1,1]
datalen = len(y)
record = []
lastQ = curQ = y[0]
for i in range(datalen):
    curQ = y[i]
    if curQ != lastQ:
        record.append(i)
    lastQ = curQ
print record
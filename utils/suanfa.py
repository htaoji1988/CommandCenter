s = """
225.240.129.203~255.110.255.255
183.181.49.4~255.0.0.0
172.177.113.45~255.0.0.0
176.134.46.246~255.0.0.0
153.63.21.56~255.255.58.255
23.135.167.228~255.0.0.0
204.58.47.149~255.0.0.0
113.33.181.46~255.255.255.0
73.245.52.119~255.255.154.0
23.214.47.71~255.0.0.0
139.124.188.91~255.255.255.100
142.94.192.197~255.0.0.0
53.173.252.202~255.0.0.0
127.201.56.50~255.255.111.255
118.251.84.111~255.0.0.0
130.27.73.170~255.0.0.0
253.237.54.56~255.86.0.0
64.189.222.111~255.255.255.139
148.77.44.147~255.0.0.0
59.213.5.253~255.255.0.0
3.52.119.131~255.255.0.0
213.208.164.145~255.255.0.0
24.22.21.206~255.255.90.255
89.43.34.31~255.0.0.0
9.64.214.75~255.0.0.0
110.156.20.173~255.153.0.0
71.183.242.53~255.255.0.0
119.152.129.100~255.0.0.0
38.187.119.201~255.0.0.0
73.81.221.180~255.255.255.255
73.198.13.199~255.0.15.0
99.42.142.145~255.255.255.0
196.121.115.160~255.0.0.0
226.30.29.206~255.0.0.0
244.248.31.171~255.255.255.255
59.116.159.246~255.0.0.0
121.124.37.157~255.0.0.226
103.42.94.71~255.255.0.0
125.88.217.249~255.255.74.255
73.44.250.101~255.255.255.0
"""
def getlst(ip):
    lstip = []
    for i in ip.split('.'):
        if i.isdigit():
            lstip.append(int(i))
    return lstip
def checkip(ip):
    if len(ip) != 4:
        return False
    for x in ip:
        if x > 255 or x < 0 :
            return False
    return True
def checkmask(mask):
    bimask = ''
    for i in mask:
        bimask += bin(int(i)).split('b')[1].zfill(8)
    if '0' not in bimask or '1' not in bimask or '01'in bimask :
        return False
    return True
A, B, C, D, E, e, pip = 0, 0, 0, 0, 0, 0, 0
while True:
    try:
        ip, mask = input().split('~')
        lstip, lstmask = getlst(ip), getlst(mask)
        first = int(lstip[0])
        second = int(lstip[1])
        if first==0 or first==127:
            continue
        if not checkip(lstip) :
            e += 1
            continue
        elif not checkmask(lstmask):
            e += 1
            continue
        if first >= 1 and first <= 126:
            if first == 10:
                pip += 1
            A += 1
        elif first >= 128 and first <= 191:
            if first == 172 and second in range(16, 32):
                pip += 1
            B += 1
        elif first >= 192 and first <= 223:
            if first == 192 and second == 168:
                pip += 1
            C += 1
        elif first >= 224 and first <= 239:
            D += 1
        elif first >= 240 and first <= 255:
            E += 1
    except:
        break
print(A, B, C, D, E, e, pip)





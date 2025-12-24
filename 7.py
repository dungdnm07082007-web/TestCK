import math
N = int(input())
danh_sach_ucln = []
for i in range(N):
    print({i+1})
    a = int(input())
    b = int(input())
    ucln = math.gcd(a, b)
    danh_sach_ucln.append(ucln)
    print({ucln})
ket_qua = max(danh_sach_ucln)
print(ket_qua)
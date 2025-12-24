input_str = input()
arr = [int(x) for x in input_str.split()]
N = len(arr)
M = int(input("Nhập số M: "))
arr.sort()
tong = 0
print(arr)
for i in range(1, N):
    if i % M == 0:
        tong += arr[i]
        print({arr[i]})
print(tong)
input_str = input()
arr = [int(x) for x in input_str.split()]
N = len(arr)
M = int(input())
danh_sach_tong = []
for i in range(N - M + 1):
    tong_con = sum(arr[i : i + M])
    danh_sach_tong.append(tong_con)
tong_lon_nhat = max(danh_sach_tong)
tong_nho_nhat = min(danh_sach_tong)
chenh_lech = tong_lon_nhat - tong_nho_nhat
print(tong_lon_nhat)
print(tong_nho_nhat)
print(chenh_lech)
# 2884)
H, M = map(int,input().split())
if 0 <= H <= 23 and 0 <= M <= 59:
    if M >= 45:
        print(f'{H} {M-45}')
    elif H == 0:
        print(f'23 {M+15}')
    else:
        print(f'{H-1} {M+15}')
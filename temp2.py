# hyeondu
# branch test
H = int()
M = int(-1)

while ((0 >= H) or (H >= 23)):
    H = int(input("시간 입력"))

while ((0 > M) or (M > 59)):
    M = int(input("분 입력"))

def check(H, M):

    if(M-45<0):
        H-=1
        M=(60+(M-45))
    else:
        M=M-45
    print(f"{H} {M}")

check(H,M)
#  ================================================== 4 ==================================================

N, r, c = map(int, input().split())

def z(N, r, c, q):
    if N == 0:
        return q
    half = 2**(N-1)
    # 1사분면
    if r < half and c < half:
        return z(N-1,r,c,q)
    # 2사분면
    elif r < half and c >= half:
        return z(N-1, r, c-half, q + half**2)
    # 3사분면
    elif r >= half and c < half:
        return z(N-1, r-half, c, q + 2 * half**2)
    # 4사분면
    else:
        return z(N-1, r-half, c-half, q + 3 * half**2)
print(z(N, r, c, 0))
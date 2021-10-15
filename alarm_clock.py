h,m = map(int,input().split())

if h!=0 :
    if m>45 :
        M = m-45

    elif 0<m<45 :
        M = m+15
        H = h-1
elif h==0 :
    if m>45 :
        M = m-45

    elif 0<m<45 :
        M = m+15
        H = 23
print(f'{H} {M}')

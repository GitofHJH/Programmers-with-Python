def solution(n, m):
    a,b=n,m
    if n>m:
        n,m=m,n
    while n!=0:
        if m % n == 0:
            break
        n,m = m % n,n 
        
    return [n,a*b/n]
def dzielnik(n, m):
    if m == 0:
        return n
    else:
        return dzielnik(m, n % m)
    

    
print(dzielnik(27, 18))
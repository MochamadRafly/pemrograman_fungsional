print ('\nprogram triangular')
def triangular (n):
    if n==1:
        return (1)
    else :
        return (n + triangular (n-1))
jumlah = triangular (5)
print ("triangular ke-5 = ", jumlah)
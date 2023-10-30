m,n = map(int, input().split())
mat1 = []
mat2 = []
m *= 2
for i in range(m):
    if i >= (m//2):
        mat2.append(list(map(int, input().split())))
    else:
        mat1.append(list(map(int, input().split())))

for i in range(m//2):
    for j in range(n):
        print((mat1[i][j] + mat2[i][j]),end=" ")
    print()

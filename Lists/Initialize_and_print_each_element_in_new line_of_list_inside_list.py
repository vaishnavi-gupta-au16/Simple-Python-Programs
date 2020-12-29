"""
Initialize and print each element in new line of a list inside list.

"""
a = [[7,8,9] , [4,5,6]]
print(a)
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j])
        j += 1
    i += 1
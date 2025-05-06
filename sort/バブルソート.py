n = int(input())
a_list = list(map(int, input().split()))

for i in range(n-1):
    for j in range(n-1, i, -1):
        if a_list[j-1] > a_list[j]:
            a_list[j-1], a_list[j] = a_list[j], a_list[j-1]
            
    print(" ".join(map(str, a_list)))

n = int(input())
a_list = list(map(int, input().split()))

# リストの2番目（未整列の先頭）～最後までループ
for i in range(n-1):
    
    # 現在の要素を最小値とする
    min_index = i
    
    # 現在の要素の次の要素から最後までループ
    for j in range(i+1, n):
        
        # 現在の最小値より小さい要素が見つかったら
        if a_list[j] < a_list[min_index]:
            
            # 最小値のインデックスを更新
            min_index = j
            
    # 現在の要素と最小値を交換
    a_list[i], a_list[min_index] = a_list[min_index], a_list[i]
    
    print(" ".join(map(str, a_list)))

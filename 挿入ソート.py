n = int(input())
a_list = list(map(int, input().split()))

# リストの2番目～最後までループ
for i in range(1, n):
    
    # 現在の要素を一時的に保存
    tmp = a_list[i]
    
    # 現在の要素の1つ前の要素のインデックスをjに格納
    j = i - 1
    
    # jが0以上かつ、現在の要素(tmp)より前の要素が大きい間繰り返す
    while (j >= 0) and (tmp < a_list[j]):
        
        # 現在の要素(tmp)より前の要素を、1つ後ろにずらす
        a_list[j + 1] = a_list[j]
        
        # jを1つ前に進める
        j -= 1
        
    # tmpを適切な位置に挿入する
    a_list[j + 1] = tmp
    
    print(" ".join(map(str, a_list)))

# 昇順クイックソート
# リスト全体をクイックソートする場合は、quick_sort(A, 0, len(A))
def quick_sort(A: list, left: int, right: int):

    # ソートする範囲の長さが1以下の場合は何もしない
    if left + 1 >= right:
        return

    # データ列の末尾 A[right-1] をピボットとする
    pivot = A[right-1]

    # ピボット未満のデータを挿入する位置を保持する変数を用意
    cur_index = left

    for i in range(left, right - 1):
        if A[i] < pivot:
            A[cur_index], A[i] = A[i], A[cur_index]
            cur_index += 1

    # ピボットを A[cur_index] へ移動し、データ列を分割する
    A[cur_index], A[right-1] = A[right-1], A[cur_index]

    # 分割されたデータ列に対して再帰的にクイックソートを行う
    quick_sort(A, left, cur_index)
    quick_sort(A, cur_index+1, right)

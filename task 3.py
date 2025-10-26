def func3(index):  # index 是 0-based
    numbers = [25, 23, 20, 21, 23, 21, 18, 19, 21, 19, 16, 17]

    # Step 1：相鄰差值
    diffs = [numbers[i] - numbers[i-1] for i in range(1, len(numbers))]

    # Step 2：找最短循環差值
    def shortest_cycle(seq):
        n = len(seq)
        for L in range(1, n):
            unit = seq[:L]
            if all(seq[i] == unit[i % L] for i in range(n)):
                return unit
        return seq #沒有更短循環就回傳原序列
    
    # Step 3：找出規律 pattern
    pattern = shortest_cycle(diffs)  # [-2, -3, 1, 2]

    # Step 5：根據 pattern 自動補足到指定長度
    while len(numbers) <= index:
        step = pattern[(len(numbers) - 1) % len(pattern)]  # ★
        numbers.append(numbers[-1] + step)
    
    # Step 6：印出結果
    print(numbers[index])

func3(1) # print 23
func3(5) # print 21
func3(10) # print 16
func3(30) # print 6

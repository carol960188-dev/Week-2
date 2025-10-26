# task 1
def func1(name):
    # === Step 1. 定義角色座標 ===
    chars = [
        {"name": "悟空",     "x": 0,  "y": 0},
        {"name": "丁滿",     "x": -1, "y": 4},
        {"name": "辛巴",     "x": -3, "y": 3},
        {"name": "貝吉塔",   "x": -4, "y": -1},
        {"name": "特南克斯", "x": 1,  "y": -2},
        {"name": "弗利沙",   "x": 4,  "y": -1},
    ]

    # === Step 2. 定義斜線兩點（代表分隔線） ===
    line_p1 = {"x": -1, "y": 3}
    line_p2 = {"x":  3, "y": -2}

    # === Step 3. 定義輔助函式 ===
    def side_of_line(p, a=line_p1, b=line_p2):
        """回傳點在斜線哪一側（正 / 負 / 0）"""
        return (b["x"] - a["x"]) * (p["y"] - a["y"]) - (b["y"] - a["y"]) * (p["x"] - a["x"])

    def manhattan(a, b):
        """水平垂直距離"""
        return abs(a["x"] - b["x"]) + abs(a["y"] - b["y"])

    def is_across_line(a, b):
        """兩點是否在分隔線兩側"""
        sa = side_of_line(a)
        sb = side_of_line(b)
        return sa * sb < 0  # 一正一負代表不同側

    def distance_with_penalty(a, b):
        """計算距離，若跨線則 +2"""
        d = manhattan(a, b)
        if is_across_line(a, b):
            d += 2
        return d

    # === Step 4. 主計算 ===
    src = next((c for c in chars if c["name"] == name), None)
    if not src:
        raise ValueError(f"找不到角色：{name}")

    results = []
    for c in chars:
        if c["name"] == name:
            continue
        d = distance_with_penalty(src, c)
        results.append((c["name"], d))

    # === Step 5. 找最近與最遠 ===
    min_d = min(d for _, d in results)
    max_d = max(d for _, d in results)
    closest  = [n for n, d in results if d == min_d]
    farthest = [n for n, d in results if d == max_d]

    # === Step 6. 輸出結果 ===
    print(f"[基準：{name}] 最近距離={min_d} → {', '.join(closest)} | 最遠距離={max_d} → {', '.join(farthest)}")


func1("辛巴") # print 最遠弗利沙;最近丁滿、貝吉塔
func1("悟空") # print 最遠丁滿、弗利沙;最近特南克斯
func1("弗利沙") # print 最遠辛巴,最近特南克斯
func1("特南克斯") # print 最遠丁滿,最近悟空

#task 2


# task 3
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


#task 4
def func4(sp, stat, n):
    # 如果 stat 是字串，例如 "101000"，先轉成整數 list, 檢查變數 stat 是不是「字串」（str 型別）。
    if isinstance(stat, str):
        stat = [int(ch) for ch in stat]

    best_index = -1
    best_diff = float('inf')  # 越小越接近剛好

    # 逐一檢查每節車廂
    for i in range(len(sp)):
        # 只考慮可載客 (stat[i]==0) 且座位夠 (sp[i]>=n)
        if stat[i] == 0 and sp[i] >= n:
            diff = sp[i] - n
            # 找出差距最小（最剛好）的車廂
            if diff < best_diff:
                best_diff = diff
                best_index = i

    # 若沒找到符合條件的，就退而求其次：選可用車廂中座位最多的, 車廂可不可用與車廂剩幾個位置是獨立的兩件事情,要分開討論．如果可用的車廂的位置數都小於乘客數，那就選擇位置最多的那一個可用車廂.
    
    if best_index == -1:
        max_space = -1
        for i in range(len(sp)):
            if stat[i] == 0 and sp[i] > max_space:
                max_space = sp[i]
                best_index = i

    # 直接在函式內印出結果，不需要在function外面再包 print()
    print(best_index)

func4([3, 1, 5, 4, 3, 2], "101000", 2) # print 5
func4([1, 0, 5, 1, 3], "10100", 4) # print 4
func4([4, 6, 5, 8], "1000", 4) # print 2




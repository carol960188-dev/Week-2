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
def func2(ss, start, end, criteria):
    # 初始化或沿用預約紀錄（存在函式屬性上，符合「不改外部既有程式」）
    # hasattr(object, "屬性名") 是 Python 內建函式，用來檢查某個物件有沒有某個屬性。
    # 幫每個服務（service）建立一個空的預約清單,每一個 key（服務名稱）對應一個 list，用來記錄該服務的預約時段
    if not hasattr(func2, "booked"):
        func2.booked = {s["name"]: [] for s in ss}
    else:
        # 若第一次後有不同的服務清單，補上鍵
        for s in ss:
            if s["name"] not in func2.booked:
                func2.booked[s["name"]] = []

    # 解criteria
    if ">=" in criteria:
        field, value = criteria.split(">=")
        op = ">="
    elif "<=" in criteria:
        field, value = criteria.split("<=")
        op = "<="
    elif "=" in criteria:
        field, value = criteria.split("=")
        op = "="
    else:
        print("Sorry")
        return

    field = field.strip()
    value = value.strip()

    # 時段衝突檢查：有overlap則不可服務
    def available(name):
        for b_start, b_end in func2.booked.get(name, []):
            if not (end <= b_start or start >= b_end):
                return False
        return True

    chosen = None
    best_score = None  # 越小越好（距離門檻的差距）best match

    for s in ss:
        # 先比對條件
        if field == "name":
            if s["name"] != value:
                continue
            # 名稱符合，再看是否可預約
            if available(s["name"]):
                chosen = s  # 只有單一精確匹配，直接選
                best_score = 0
                break
            else:
                continue
        else:
            # 其他欄位預設為數值（r, c）
            try:
                v = float(value)
                sv = float(s[field])
            except Exception:
                # 欄位不存在或不是可轉浮點的值，略過
                continue

            # 檢查運算子與是否符合
            if op == ">=":
                if sv < v:
                    continue
                score = sv - v  # 越小越好（最接近門檻的最小符合者）
            elif op == "<=":
                if sv > v:
                    continue
                score = v - sv  # 越小越好（最接近門檻的最大符合者）
            else:
                # 題目規定其他欄位不使用等號
                continue

            # 時段可用才計分
            if not available(s["name"]):
                continue

            # 取最佳（分數小者；同分以先出現者優先）
            if best_score is None or score < best_score:
                chosen = s
                best_score = score

    if chosen is None:
        print("Sorry")
    else:
        func2.booked[chosen["name"]].append((start, end))
        print(chosen["name"])

services=[
    {"name":"S1", "r":4.5, "c":1000},
    {"name":"S2", "r":3, "c":1200},
    {"name":"S3", "r":3.8, "c":800}
]
func2(services, 15, 17, "c>=800") # S3
func2(services, 11, 13, "r<=4") # S3
func2(services, 10, 12, "name=S3") # Sorry
func2(services, 15, 18, "r>=4.5") # S1
func2(services, 16, 18, "r>=4") # Sorry
func2(services, 13, 17, "name=S1") # Sorry
func2(services, 8, 9, "c<=1500") # S2


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




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

// task 1
function func1(name){
const chars = [
  { name: "悟空",   x: 0,  y: 0 },
  { name: "丁滿",   x: -1, y:  4 },
  { name: "辛巴",   x: -3, y:  3 },
  { name: "貝吉塔", x: -4, y: -1 },
  { name: "特南克斯", x: 1, y: -2 },
  { name: "弗利沙", x:  4, y: -1 },
];
  
const lineP1 = { x: -1, y: 3 };
const lineP2 = { x:  3, y: -2 };

function sideOfLine(p, a = lineP1, b = lineP2) {
  return (b.x - a.x) * (p.y - a.y) - (b.y - a.y) * (p.x - a.x);
}
function manhattan(a, b) {
  return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
}
function isAcrossLine(a, b) {
  const sa = sideOfLine(a);
  const sb = sideOfLine(b);
  return sa * sb < 0;
}

function distanceWithPenalty(a, b) {
  let d = manhattan(a, b);
  if (isAcrossLine(a, b)) d += 2;   
  return d;
}

function closestAndFarthest(fromName) {
  const src = chars.find(c => c.name === fromName);
  if (!src) throw new Error(`找不到角色：${fromName}`);


  const list = chars
    .filter(c => c.name !== fromName)
    .map(c => ({ name: c.name, d: distanceWithPenalty(src, c) }));

  const ds = list.map(x => x.d);
  const minD = Math.min(...ds);
  const maxD = Math.max(...ds);

  const closest = list.filter(x => x.d === minD).map(x => x.name);
  const farthest = list.filter(x => x.d === maxD).map(x => x.name);

  return { minD, closest, maxD, farthest };
}

const res = closestAndFarthest(name);
  console.log(
    `[基準：${res.base}] 最近距離=${res.minD} → ${res.closest.join(", ")} | 最遠距離=${res.maxD} → ${res.farthest.join(", ")}`
  );
}
func1("辛巴"); // print 最遠弗利沙;最近丁滿、貝吉塔
func1("悟空"); // print 最遠丁滿、弗利沙;最近特南克斯
func1("弗利沙"); // print 最遠辛巴,最近特南克斯
func1("特南克斯"); // print 最遠丁滿,最近悟空


// task 2





// task 3
function func3(index){ // index 是 0-based
  const numbers = [25, 23, 20, 21, 23, 21, 18, 19, 21, 19, 16, 17];
  const pattern = [-2, -3, 1, 2];
  const predict = [...numbers];

  while (predict.length <= index) {
    const step = pattern[(predict.length - 1) % pattern.length];
    predict.push(predict[predict.length - 1] + step);
  }

  console.log(predict[index]);
}

func3(1); // print 23
func3(5); // print 21
func3(10); // print 16
func3(30); // print 6


// task 4
function func4(sp, stat, n){
    if (typeof stat === "string") {
    stat = Array.from(stat, ch => parseInt(ch));
    }
    let bestIndex = -1;
    let bestDiff = Infinity;  

    // step1：找可用且能容納所有乘客的車廂
    for (let i = 0; i < sp.length; i++) {
        if (stat[i] === 0 && sp[i] >= n) {      // 可用且位子夠
        const diff = sp[i] - n;
        if (diff < bestDiff) {                // 更接近剛好的
        bestDiff = diff;
        bestIndex = i;
      }
    }
  }
  // 若找到完全能容納的 → 直接印出
  if (bestIndex !== -1) {
    console.log(bestIndex);
    return;
  }

// step2：退而求其次 → 找可用車廂中座位最多者
  let fallbackIndex = -1;
  let maxSeats = -1;
  for (let i = 0; i < sp.length; i++) {
    if (stat[i] === 0 && sp[i] > maxSeats) {
      maxSeats = sp[i];
      fallbackIndex = i;
    }
  }
  console.log(fallbackIndex);
}
  
func4([3, 1, 5, 4, 3, 2], "101000", 2); // print 5
func4([1, 0, 5, 1, 3], "10100", 4); // print 4
func4([4, 6, 5, 8], "1000", 4); // print 2

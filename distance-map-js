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

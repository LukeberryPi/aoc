const file = Bun.file("./2023/7/input.txt");
const input = await file.text();

const lines = input.split("\n");

function cardBidMap(lines) {
  const dict = lines.reduce((acc, line) => {
    const [card, bid] = line.split(" ");
    acc[card] = bid;
    return acc;
  }, {});

  return dict;
}

function cardRankMap(cardBidMap) {
  let cardRankDict = new Map();
  let other = Object.keys(cardBidMap).map((key) => {
    const inside = key.split("").map((char) => {
      if (cardRankDict.has(char)) return;
      let count = key.match(new RegExp(char, "g") || []).length;
      return cardRankDict[char] = count;
    }).filter(Boolean);

    return inside;
  })

  return other;
}

function main() {
  return undefined;
}

console.log("cardRankMap(lines)", cardRankMap(cardBidMap(lines)));

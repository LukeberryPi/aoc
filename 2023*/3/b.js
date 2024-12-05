const file = Bun.file("./2023/3/input.txt");
const input = await file.text();

const lines = input.split("\n");

function discoverSymbols(lines) {
  const reg = /[\d.]/g;

  const symbols = lines.reduce((acc, line) => {
    const filteredLine = line.replace(reg, "").split("");
    for (const item of filteredLine) {
      acc.push(item);
    }
    return acc;
  }, []);

  return Array.from(new Set(symbols)).join("");
}

function areAdjacent(coord1, coord2) {
  const [x1, y1] = coord1;
  const [x2, y2] = coord2;

  const isHorizontallyAdjacent = Math.abs(x1 - x2) === 1 && y1 === y2;
  const isVerticallyAdjacent = x1 === x2 && Math.abs(y1 - y2) === 1;
  const isDiagonallyAdjacent =
    Math.abs(x1 - x2) === 1 && Math.abs(y1 - y2) === 1;

  return isHorizontallyAdjacent || isVerticallyAdjacent || isDiagonallyAdjacent;
}

function extractNumsAndPositions(listIndex = 0, line) {
  const result = [];
  let positions = [];
  let currentNumber = "";

  for (let i = 0; i < line.length; i++) {
    if (isNaN(line[i])) {
      continue;
    }

    if (isNaN(line[i + 1])) {
      currentNumber += line[i];
      positions.push([listIndex, i]);

      result.push({
        number: +currentNumber,
        positions,
      });

      positions = [];
      currentNumber = "";
      continue;
    }

    if (!isNaN(line[i])) {
      currentNumber += line[i];
      positions.push([listIndex, i]);
    }
  }

  return result;
}

function gearRatiosTwo(lines) {
  let result = 0;
  let asteriskPositions = [];
  let numberObjects = [];

  for (let i = 0; i < lines.length; i++) {
    numberObjects.push(extractNumsAndPositions(i, lines[i]));

    for (let j = 0; j < lines[i].length; j++) {
      if (lines[i][j] === "*") {
        asteriskPositions.push([i, j]);
      }
    }
  }

  const filteredNumberObjects = numberObjects.filter(item => item.length !== 0).flat();

  for (const asteriskPosition of asteriskPositions) {
    let adjacentNumberCount = 0;
    let product = 1;
    for (const obj of filteredNumberObjects) {
      const { number, positions } = obj;
      for (const pos of positions) {
        if (areAdjacent(asteriskPosition, pos)) {
          adjacentNumberCount++
          product *= number;
          break;
        }
      }
    } 
    if (adjacentNumberCount !== 2) continue;

    result += product;
  }

  return result;
}

console.log("gearRatiosTwo", gearRatiosTwo(lines));

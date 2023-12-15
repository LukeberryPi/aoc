const file = Bun.file("./2023/3/input.txt");
const input = await file.text();

const lines = input.split("\n");

function gearRatios(lines) {
  const matrix = lines.map((str) => str.split(""));
  return matrix;
}

console.log("gearRatios", gearRatios(lines));

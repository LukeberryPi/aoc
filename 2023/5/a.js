const file = Bun.file("./2023/3/input.txt");
const input = await file.text();

const lines = input.split("\n");

function gearRatios(lines) {
  return lines;
}

console.log("gearRatios", gearRatios(lines));

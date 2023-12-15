const file = Bun.file("./2023/4/input.txt");
const input = await file.text();

const lines = input.split("\n");

function scratchcardsTwo(lines) {
  let result = 0;

  for (let line of lines) {
    let count = -1;
    const winning = line
      .split(": ")[1]
      .split(" | ")[0]
      .split(" ")
      .filter(Boolean);
    const elected = line
      .split(": ")[1]
      .split(" | ")[1]
      .split(" ")
      .filter(Boolean);

    for (let elec of elected) {
      if (winning.includes(elec)) count++;
    }

    if (count === -1) continue;
    result += 2 ** count;
  }

  return result;
}

console.log("scratchcardsTwo", scratchcardsTwo(lines));

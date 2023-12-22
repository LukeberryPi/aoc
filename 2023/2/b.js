const file = Bun.file("./2023/2/input.txt");
const input = await file.text();

const games = input.split("\n");

function main(games) {
  let sumOfPower = 0;

  for (let game of games) {
    const draws = game.split(": ")[1].split(/, |; /g);
    let [minRed, minGreen, minBlue] = [0, 0, 0];

    for (let record of draws) {
      const [number, color] = record.split(" ");

      if (color === "red" && +number > minRed) {
        minRed = number;
      }

      if (color === "green" && +number > minGreen) {
        minGreen = number;
      }

      if (color === "blue" && +number > minBlue) {
        minBlue = number;
      }
    }

    sumOfPower += +minRed * +minBlue * +minGreen;
  }

  return sumOfPower;
}

console.log("main", main(games));

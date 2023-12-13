const file = Bun.file("./2023/2/input.txt");
const input = await file.text();

const games = input.split("\n");
const MAXIMUM_COLOR_VALUES = {
  red: 12,
  green: 13,
  blue: 14,
};

function cubeConundrum(games) {
  let sumOfPossibleGames = 0;

  for (let game of games) {
    let isPossible = true;
    const gameId = game.split(": ")[0].split(" ")[1];
    const draws = game.split(": ")[1].split(/, |; /g);

    for (let record of draws) {
      const [number, color] = record.split(" ");
      isPossible = number <= MAXIMUM_COLOR_VALUES[color];
      if (!isPossible) break;
    }

    if (isPossible) {
      sumOfPossibleGames += +gameId;
    }
  }

  return sumOfPossibleGames;
}

console.log("cubeConundrum", cubeConundrum(games));

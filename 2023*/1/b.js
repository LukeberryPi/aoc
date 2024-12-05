const file = Bun.file("./2023/1/input.txt");
const input = await file.text();

const lines = input.split("\n");

function sumCalibrationNumbersTwo(lines) {
  let sum = 0;

  const regex =
    /1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine/g;

  const dict = {
    one: "1",
    two: "2",
    three: "3",
    four: "4",
    five: "5",
    six: "6",
    seven: "7",
    eight: "8",
    nine: "9",
  };

  const filterString = (str) => {
    return str.match(regex);
  };

  for (let line of lines) {
    const filtered = filterString(line);
    const first = dict[filtered.at(0)] || filtered.at(0);
    const last = dict[filtered.at(-1)] || filtered.at(-1);

    const appendDigits = first + last;
    console.log(line, filtered, appendDigits);
    sum += Number(appendDigits);
  }

  return sum;
}

console.log("sumCalibrationNumbersTwo", sumCalibrationNumbersTwo(lines));

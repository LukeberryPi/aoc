const file = Bun.file("./2023/1/input.txt");
const input = await file.text();

const lines = input.split("\n");

function sumCalibrationNumbers(lines) {
  const nums = new Set(Array.from("1234567890"));
  let sum = 0;

  const findFirstDigit = (str) => {
    for (let i = 0; i < str.length; i++) {
      if (nums.has(str[i])) {
        return str[i];
      }
    }
  };

  const findLastDigit = (str) => {
    for (let i = str.length; i >= 0; i--) {
      if (nums.has(str[i])) {
        return str[i];
      }
    }
  };

  for (let line of lines) {
    let appendDigits = findFirstDigit(line) + findLastDigit(line);
    sum += Number(appendDigits);
  }

  return sum;
}

console.log("sumCalibrationNumbers", sumCalibrationNumbers(lines));

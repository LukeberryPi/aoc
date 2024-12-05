

const file = Bun.file("./2023/1/input.txt");
const input = await file.text();

const lines = input.split("\n");

function findFirstDigit(str) {
  for (let i = 0; i < str.length; i++) {
    if (!isNaN(parseInt(str[i]))) {
      return str[i];
    }
  }
};

function findLastDigit(str) {
  for (let i = str.length; i >= 0; i--) {
    if (!isNaN(parseInt(str[i]))) {
      return str[i];
    }
  }
};

function main(lines) {
  let sum = 0;

  for (let line of lines) {
    let digits = findFirstDigit(line) + findLastDigit(line);
    sum += +digits;
  }

  return sum;
}

console.log("main", main(lines));

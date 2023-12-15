const file = Bun.file("./2023/6/input.txt");
const input = await file.text();

// create (time, recordDistance) tuples
// iterate over them
// for each pair
// start with Math.floor(time / 2) and move down holdTimes until the record is no longer beat. count the combinations that beat the record.
// if time is even, the total combinations that beat the record will be 2x - 1
// if time is odd, the total combinations that beat the record will be 2x
// accumulate the value
// move to next value

const times = input.split("\n")[0].split(": ")[1].split(" ").filter(Boolean);
const recordDistances = input
  .split("\n")[1]
  .split(": ")[1]
  .split(" ")
  .filter(Boolean);
const tuples = [];

for (let i = 0; i < times.length; i++) {
  tuples.push([times[i], recordDistances[i]]);
}

function waitForIt(tuples) {
  let result = 1;

  for (let [time, recordDistance] of tuples) {
    const evenTime = time % 2 === 0;
    let attemptsThatBeatRecord = 0;
    
    for (let holdTime = Math.floor(time / 2); holdTime > 0; holdTime--) {
      const timeMoving = time - holdTime;
      const distance = timeMoving * holdTime;

      if (distance > recordDistance) {
        attemptsThatBeatRecord++;
      }
    }

    if (evenTime) {
      attemptsThatBeatRecord = attemptsThatBeatRecord * 2 - 1;
    } else {
      attemptsThatBeatRecord *= 2;
    }

    result *= attemptsThatBeatRecord;
  }

  return result;
}

console.log("waitForIt", waitForIt(tuples));

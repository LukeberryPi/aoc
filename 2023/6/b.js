const file = Bun.file("./2023/6/input.txt");
const input = await file.text();

const reg = /\D/g;
const time = input.split("\n")[0].replace(reg, "");
const recordDistance = input.split("\n")[1].replace(reg, "");

function waitForItTwo(time, recordDistance) {
  const evenTime = time % 2 === 0;
  let attemptsThatBeatRecord = 0;
  let result = 1;

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
  return result;
}

console.log("waitForItTwo", waitForItTwo(time, recordDistance));

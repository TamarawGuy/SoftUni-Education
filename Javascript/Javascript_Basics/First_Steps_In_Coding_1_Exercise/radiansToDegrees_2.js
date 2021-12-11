function fromRadiansToDegrees(input) {
    let radians = Number(input[0])
    let degrees = (radians * 180 / Math.PI).toFixed(0);
    console.log(degrees);
}
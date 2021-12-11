function aquarium(input) {
    let length = Number(input[0]);
    let width = Number(input[1]);
    let height = Number(input[2]);
    let p = Number(input[3]);

    let volume = length * width * height;
    let liters = volume * 0.001;
    let percent = p * 0.01;
    let total = liters * (1 - percent);
    console.log(total);
}
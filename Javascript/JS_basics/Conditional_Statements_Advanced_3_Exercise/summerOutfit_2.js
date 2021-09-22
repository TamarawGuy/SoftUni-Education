function summerOutfit(input) {
    let degrees = Number(input[0]);
    let time = input[1];

    if (degrees >= 10 && degrees <= 18) {
        if (time == 'Morning') {
            console.log(`It's ${degrees} degrees, get your Sweatshirt and Shoes.`)
        }
        else if (time == 'Afternoon') {
            console.log(`It's ${degrees} degrees, get your Shirt and Moccasins.`)
        }
        else if (time == 'Evening') {
            console.log(`It's ${degrees} degrees, get your Shirt and Moccasins.`)
        }
    }
    else if (degrees > 18 && degrees <= 24) {
        if (time == 'Morning') {
            console.log(`It's ${degrees} degrees, get your Shirt and Moccasins.`)
        }
        else if (time == 'Afternoon') {
            console.log(`It's ${degrees} degrees, get your T-Shirt and Sandals.`)
        }
        else if (time == 'Evening') {
            console.log(`It's ${degrees} degrees, get your Shirt and Moccasins.`)
        }
    }
    else if (degrees >= 25) {
        if (time == 'Morning') {
            console.log(`It's ${degrees} degrees, get your T-Shirt and Sandals.`)
        }
        else if (time == 'Afternoon') {
            console.log(`It's ${degrees} degrees, get your Swim Suit and Barefoot.`)
        }
        else if (time == 'Evening') {
            console.log(`It's ${degrees} degrees, get your Shirt and Moccasins.`)
        }
    }
}
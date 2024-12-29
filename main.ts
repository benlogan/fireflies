let random1 = 0
let strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
let strip2 = neopixel.create(DigitalPin.P1, 30, NeoPixelMode.RGB)
loops.everyInterval(10000, function () {
    strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
    basic.pause(500)
    strip.showColor(neopixel.colors(NeoPixelColors.Black))
})
basic.forever(function () {
    random1 = randint(0, 3000)
    basic.pause(random1)
    strip2.showColor(neopixel.colors(NeoPixelColors.White))
    basic.pause(500)
    strip2.showColor(neopixel.colors(NeoPixelColors.Black))
})

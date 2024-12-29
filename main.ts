let strip1on = false
let strip2on = false
let random1 = 0
let score = 0
let strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
let strip2 = neopixel.create(DigitalPin.P1, 30, NeoPixelMode.RGB)
basic.showNumber(score)
basic.forever(function on_forever() {
    
    random1 = randint(0, 3000)
    basic.pause(random1)
    strip2.showColor(neopixel.colors(NeoPixelColors.Indigo))
    strip2on = true
    basic.pause(500)
    strip2.showColor(neopixel.colors(NeoPixelColors.Black))
    strip2on = false
})
basic.forever(function on_forever2() {
    if (strip1on && strip2on) {
        
        score = score + 1
        basic.showNumber(score)
        console.log("MATCH new score : " + ("" + score))
    } else {
        
    }
    
})
loops.everyInterval(5000, function on_every_interval() {
    
    strip.showColor(neopixel.colors(NeoPixelColors.Yellow))
    strip1on = true
    basic.pause(500)
    strip.showColor(neopixel.colors(NeoPixelColors.Black))
    strip1on = false
})

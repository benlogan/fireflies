strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip2 = neopixel.create(DigitalPin.P1, 30, NeoPixelMode.RGB)

def on_every_interval():
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    basic.pause(200)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
loops.every_interval(10000, on_every_interval)

def on_every_interval2():
    random1 = randint(0, 3000)
    basic.pause(random1)
    strip2.show_color(neopixel.colors(NeoPixelColors.WHITE))
    basic.pause(200)
    strip2.show_color(neopixel.colors(NeoPixelColors.BLACK))

loops.every_interval(1000, on_every_interval2)

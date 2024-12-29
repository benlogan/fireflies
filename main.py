strip1on = False
strip2on = False
random1 = 0
score = 0
strip = neopixel.create(DigitalPin.P0, 30, NeoPixelMode.RGB)
strip2 = neopixel.create(DigitalPin.P1, 30, NeoPixelMode.RGB)
basic.show_number(score)

def on_forever():
    global random1, strip2on
    random1 = randint(0, 3000)
    basic.pause(random1)
    strip2.show_color(neopixel.colors(NeoPixelColors.INDIGO))
    strip2on = True
    basic.pause(500)
    strip2.show_color(neopixel.colors(NeoPixelColors.BLACK))
    strip2on = False
basic.forever(on_forever)

def on_forever2():
    if strip1on and strip2on:
        global score
        score = score + 1
        basic.show_number(score)
        print("MATCH new score : " + str(score))
    else:
        pass
basic.forever(on_forever2)

def on_every_interval():
    global strip1on
    strip.show_color(neopixel.colors(NeoPixelColors.YELLOW))
    strip1on = True
    basic.pause(500)
    strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
    strip1on = False
loops.every_interval(5000, on_every_interval)

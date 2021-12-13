Distance = 0

def on_forever():
    global Distance
    Distance = sonar.ping(DigitalPin.P0, DigitalPin.P1, PingUnit.CENTIMETERS)
    basic.show_number(Distance)
    basic.pause(1000)
basic.forever(on_forever)

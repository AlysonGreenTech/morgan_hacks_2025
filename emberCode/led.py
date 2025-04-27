import time
import board
import neopixel


def power_on():
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    for i in range(255):
        pixels.fill((i, i, i))
        pixels.show()
        time.sleep(0.01)
    time.sleep(0.5)
    for i in range(255, 0, -1):
        pixels.fill((i, i, i))
        pixels.show()
    pixels.fill((0, 0, 0))
    pixels.show()


def i2c_check(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "wait":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 0)
        pixels[10] = (0, 0, 255)
        pixels[0] = (255, 255, 0)
        pixels.show()
    elif status == "pass":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 0)
        pixels[10] = (0, 0, 255)
        pixels[0] = (0, 255, 0)
        pixels.show()
    elif status == "fail":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 0)
        pixels[10] = (0, 0, 255)
        pixels[0] = (255, 0, 0)
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


def gps_check(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "wait":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (255, 255, 0)
        pixels.show()
    elif status == "pass":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (0, 255, 0)
        pixels.show()
    elif status == "fail":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (255, 0, 0)
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


def wifi_check(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "wait":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 255)
        pixels[10] = (0, 255, 255)
        pixels[0] = (255, 255, 0)
        pixels.show()
    elif status == "pass":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 255)
        pixels[10] = (0, 255, 255)
        pixels[0] = (0, 255, 0)
        pixels.show()
    elif status == "fail":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 255, 255)
        pixels[10] = (0, 255, 255)
        pixels[0] = (255, 0, 0)
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


def py_check(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "wait":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 0)
        pixels[0] = (255, 255, 0)
        pixels.show()
    elif status == "pass":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 0)
        pixels[0] = (0, 255, 0)
        pixels.show()
    elif status == "fail":
        pixels.fill((0, 0, 0))
        pixels[9] = (0, 0, 255)
        pixels[10] = (255, 255, 0)
        pixels[0] = (255, 0, 0)
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


def client_check(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = .1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "wait":
        pixels.fill((0, 0, 0))
        pixels[9] = (255, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (255, 255, 0)
        pixels.show()
    elif status == "pass":
        pixels.fill((0, 0, 0))
        pixels[9] = (255, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (0, 255, 0)
        pixels.show()
    elif status == "fail":
        pixels.fill((0, 0, 0))
        pixels[9] = (255, 0, 255)
        pixels[10] = (255, 255, 255)
        pixels[0] = (255, 0, 0)
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()


def headlights(status):
    pixel_pin = board.D18
    num_pixels = 11
    brightness = 1

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=brightness, auto_write=False)

    if status == "OFF":
        pixels.fill((0, 0, 0))
        pixels.show()
    elif status == "ON":
        pixels.fill((255, 255, 255))
        pixels.show()
    else:
        pixels.fill((255, 0, 0))
        pixels.show()
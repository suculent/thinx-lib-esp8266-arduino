import ssd1306
import utime
from machine import I2C, Pin

i2c = I2C(sda=Pin(4), scl=Pin(5))
print("I2C scan: ", i2c.scan())
display = ssd1306.SSD1306_I2C(64, 48, i2c)

while True:
display.fill(0)

display.text('Hello',10,10)
display.show()
utime.sleep(1)
display.text('Martin',10,20)
display.show()
utime.sleep(2)

display.fill(0)
display.show()

# Use convert.py to generate the array below
pic = [
'111111111111111111111111111111111111111111111111',
'111111111111111111111110011111111111111111111111',
'111111111111111111111111111011111111111111111111',
'111111111111111111111110011101111111111111111111',
'111111111111111111111101100111111111111111111111',
'111111111111111111111011101011111111111111111111',
'111111111111111111111011111101111111111111111111',
'111111111111111111111010111101111111111111111111',
'111111111111111111110010101101111111111111111111',
'111111111111111111100001101101111111111111111111',
'111111111111111111100000011000111111111111111111',
'111111111111111111000000000000111111111111111111',
'111111111111111111000000000000111111111111111111',
'111111111111111111000000000000111111111111111111',
'111111111111111111000100000000111111111111111111',
'111111111111111111100100100001111111111111111111',
'111111111111111111100000100001111111111111111111',
'111111111111111111110000000001111111111111111111',
'111111111111111111111000000011111111111111111111',
'111111111111111111111000000011111111111111111111',
'111111111111111111111001100110001111111111111111',
'111111111111111000110101100100000001111111111111',
'111111111111100000000101000000001000111111111111',
'111111111111001000001001000000110000111111111111',
'111111111110000110011011000011000000111111111111',
'111111111110000001101110001100000001011111111111',
'111111111110100000010010000000000011011111111111',
'111111111110010000111110000000011100011111111111',
'111111111100010100011110001011011000001111111111',
'111111111100001110100010000111000000000111111111',
'111111111100000110111110000000000000000111111111',
'111111111100000000011110000000000000010111111111',
'111111110000000000001101000000000000110011111111',
'111111100000010000000011100110110110100001111111',
'111111101000001010101110001101101100000101111111',
'111111110110000001110001011101000000011011111111',
'111111100101100000000000000000000001101001111111',
'111111101001011000000000000000000110100101111111',
'111111011010010110000000000000011010010110111111',
'111111110110100101100000000001101001011011111111',
'111111111101101001011000000110100101101111111111',
'111111111111011010010110011010010110111111111111',
'111111111111110110100101101001011011111111111111',
'111111111111111101101000000101101111111111111111',
'111111111111111111011010010110111111111111111111',
'111111111111111111110111111011111111111111111111',
'111111111111111111111111111111111111111111111111',
'111111111111111111111111111111111111111111111111']

for x, row in enumerate(pic):
    for y, col in enumerate(row):
        if col == "1":
            display.pixel(x, y, 1)

display.show()

utime.sleep(3)
display.fill(0)
display.show()
utine.sleep(5)


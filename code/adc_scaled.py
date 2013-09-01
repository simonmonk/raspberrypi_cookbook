import spidev

R1 = 10000.0
R2 = 3300.0

spi = spidev.SpiDev()
spi.open(0,0)

def analog_read(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((r[1]&3) << 8) + r[2]
    return adc_out
 
reading = analog_read(0)
voltage_adc = reading * 3.3 / 1024
voltage_actual =  voltage_adc / (R2 / (R1 + R2))
print("Battery Voltage=" + str(voltage_actual))
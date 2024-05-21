# GPIO used GPIO23
###############################################################################
#                A Bink Led Example for GPIOD on Raspberrypi 5  
#                      Sensor Analytics Australia™ 2024
###############################################################################
import gpiod
import time

X=5
T=0.5
T2=0.1

chip=gpiod.Chip('gpiochip4') #chip4 selected for PI5 GPIOs ref gpioinfo

# Using gpiod.Line object method 
line = gpiod.find_line('GPIO23') # Pin16 on Rpi header with Led's +ve leg  
line.request(consumer='try line', type=gpiod.LINE_REQ_DIR_OUT)
for i in range(X):
    line.set_value(0)
    time.sleep(T2)
    line.set_value(1)
    time.sleep(T2)
line.release()

# Using gpiod.LineBulk object method
lines = chip.get_lines([line.offset()])
lines.request(consumer='try lines',type=gpiod.LINE_REQ_DIR_OUT,default_vals=[0])
for i in range(X):
    lines.set_values([0])
    time.sleep(T)
    lines.set_values([1])
    time.sleep(T)

lines.set_values([0]) #turn led off
lines.release()
chip.close()
# for more info on gpiod functions
# >>> help('gpiod')

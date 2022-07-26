from machine import Pin, PWM
import utime

servo = PWM(Pin(0))
servo.freq(50)

# 0 Deg - full left servo.duty_u16(1750)
# 90 Deg - front servo.duty_u16(4875)
# 180 Deg - full right servo.duty_u16(8000)

# Angle => 0 = left, 90 = front, 180 = right

# Convert def to servo.duty
# sd = 1750 + a * 34,7222

def zero_position():
    servo.duty_u16(4875)

def search_180(a1, a2, t):
    """
    Continuous mode, a1; a2 = extreme values of rot. in deg (min=0, max=180), t = sleep time
    """
    if a1 or a2 > 180:
        zero_position()
        print ("Servo imput value error: min andge=0, max angle=180")
        return 
    else:
        while True:
            sd1 = int(1750 + a1 * 34.7222)
            sd2 = int(1750 + a2 * 34.7222)
            servo.duty_u16(sd1)
            utime.sleep(t)
            servo.duty_u16(sd2)
            utime.sleep(t)

#zero_position()
search_180(0, 185, 1)
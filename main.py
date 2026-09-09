from machine import Pin, ADC, PWM
from time import sleep_ms

MIN_DUTY = 1638.0
MAX_DUTY = 8191.0

# Ograniczenia zakresu dla kazdego serwa osobno
SERVO1_MIN, SERVO1_MAX = MIN_DUTY, MAX_DUTY   # podstawa
SERVO2_MIN, SERVO2_MAX = MIN_DUTY, MAX_DUTY   # ramie1
SERVO3_MIN, SERVO3_MAX = MIN_DUTY, MAX_DUTY   # ramie2

def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))

servo1 = PWM(Pin(16)) # podstawa
servo1.freq(50)
servo2 = PWM(Pin(17)) # ramie1
servo2.freq(50)
servo3 = PWM(Pin(18)) # ramie2
servo3.freq(50)

# Joystick 1
joy1_x = ADC(Pin(27))  # ADC2, podstawa
joy1_y = ADC(Pin(28))  # ADC1, ramie1
# Joystick 2
joy2_y = ADC(Pin(26))  # ADC0, ramie2

average = (MAX_DUTY + MIN_DUTY) / 2
position1 = average
position2 = average
position3 = average

while True:
    target1 = MIN_DUTY + joy1_x.read_u16() * (MAX_DUTY - MIN_DUTY) // 65535 # przeskalowanie odczytu joysticka na zakres wypełnienia PWM
    position1 += (target1 - position1) // 4  # filtr wygladzajacy
    position1 = clamp(position1, SERVO1_MIN, SERVO1_MAX) # zabezpieczenie
    servo1.duty_u16(int(position1)) # wykonanie ruchu

    target2 = MIN_DUTY + joy1_y.read_u16() * (MAX_DUTY - MIN_DUTY) // 65535
    position2 += (target2 - position2) // 4
    position2 = clamp(position2, SERVO2_MIN, SERVO2_MAX)
    servo2.duty_u16(int(position2))

    target3 = MIN_DUTY + joy2_y.read_u16() * (MAX_DUTY - MIN_DUTY) // 65535
    position3 += (target3 - position3) // 4
    position3 = clamp(position3, SERVO3_MIN, SERVO3_MAX)
    servo3.duty_u16(int(position3))

    sleep_ms(15)

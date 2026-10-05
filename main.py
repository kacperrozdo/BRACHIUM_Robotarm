from machine import Pin, ADC, PWM
import time

pots = (
    ADC(Pin(32)), 
    ADC(Pin(35)), 
    ADC(Pin(36)), 
    ADC(Pin(39)), 
    ADC(Pin(34)), 
)

servos = (
    PWM(Pin(13)), 
    PWM(Pin(12)), 
    PWM(Pin(26)), 
    PWM(Pin(14)), 
    PWM(Pin(27)), 
)

NAMES = (
    "rotacja chwytaka",
    "chwytak",
    "platforma obrotowa",
    "ramie 1",
    "ramie 2",
)

N = len(servos)

REVERSED = (
    False,
    False, 
    False, 
    False,
    False,
)

ANGLE_LIMITS = (
    (0, 180), 
    (0, 180), 
    (0, 180), 
    (0, 180), 
    (0, 180), 
)

for servo in servos:
    servo.freq(50)

DEAD_ZONE = 2 
SAMPLES = 8 

def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def clamp_angle(angle, limits):
    min_angle, max_angle = limits
    if angle < min_angle:
        return min_angle
    if angle > max_angle:
        return max_angle
    return angle

def set_angle(servo, angle):
    min_duty = 1638
    max_duty = 8192
    duty = map_value(angle, 0, 180, min_duty, max_duty)
    servo.duty_u16(duty)

def read_pot_averaged(pot):
    total = 0
    for _ in range(SAMPLES):
        total += pot.read_u16()
    return total // SAMPLES

last_angles = [None] * N 
current_angles = [0] * N

while True:
    for i in range(N):
        pot_value = read_pot_averaged(pots[i])
        if REVERSED[i]:
            angle = map_value(pot_value, 0, 65535, 180, 0)
        else:
            angle = map_value(pot_value, 0, 65535, 0, 180)
        angle = clamp_angle(angle, ANGLE_LIMITS[i])
        current_angles[i] = angle

        if last_angles[i] is None or abs(angle - last_angles[i]) >= DEAD_ZONE:
            set_angle(servos[i], angle)
            last_angles[i] = angle

    print("  ".join("{}: {:>3}".format(NAMES[i], current_angles[i]) for i in range(N)))

    time.sleep(0.02)

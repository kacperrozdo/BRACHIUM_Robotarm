from machine import Pin, ADC, PWM
import time

pots = (
    ADC(Pin(32)), # 1
    ADC(Pin(35)), # 2
    ADC(Pin(36)), # 3
    ADC(Pin(34)), # 4
    ADC(Pin(39)), # 5
)

servos = (
    PWM(Pin(13)), # rotacja chwytaka
    PWM(Pin(12)), # chwytak
    PWM(Pin(26)), # platfroma obrotowa
    PWM(Pin(27)), # ramie 1
    PWM(Pin(14)), # ramie 2
)

N = len(servos)

# True = odwrócony kierunek ruchu serwa względem obrotu potencjometru
REVERSED = (
    True,  # rotacja chwytaka
    False, # chwytak
    False, # platforma obrotowa
    False, # ramie 1
    True,  # ramie 2
)

for servo in servos:
    servo.freq(50)

DEAD_ZONE = 3 # Minimalny kąt, który jeśli zostanie przekroczony to serwo wykona ruch (ograniczenie drgania)
SAMPLES = 8 # Liczba próbek uśrednianych przy odczycie z ADC (redukcja szumu pomiaru)

# Sklaowanie wartości między zakresami
def map_value(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

# Ustawienie kąta serwa
def set_angle(servo, angle):
    min_duty = 1638
    max_duty = 8192
    duty = map_value(angle, 0, 180, min_duty, max_duty) # Zamiana kąta (0-180) na wartość wypełnienia PWM (16-bitowa)
    servo.duty_u16(duty)

# Odczyt z potencometru + uśrednienie szumu
def read_pot_averaged(pot):
    total = 0
    for _ in range(SAMPLES):
        total += pot.read_u16()
    return total // SAMPLES

last_angles = [None] * N # Ostatni kąt wysłany do każdego serwa (None = jeszcze nie ustawiony)
current_angles = [0] * N # Bieżące kąty (do samego wyświetlania na konsoli)

while True:
    for i in range(N):
        pot_value = read_pot_averaged(pots[i])
        if REVERSED[i]:
            angle = map_value(pot_value, 0, 65535, 180, 0)
        else:
            angle = map_value(pot_value, 0, 65535, 0, 180)
        current_angles[i] = angle

        if last_angles[i] is None or abs(angle - last_angles[i]) >= DEAD_ZONE:
            set_angle(servos[i], angle)
            last_angles[i] = angle

    print("1: {}  2: {}  3: {}  4: {}  5: {}".format(*current_angles))

    time.sleep(0.02)

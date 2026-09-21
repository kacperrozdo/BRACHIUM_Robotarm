from machine import Pin, ADC, PWM
import time

pots = (ADC(Pin(28)), ADC(Pin(27)), ADC(Pin(26))) #ramie1, platforma obrotowa, ramie2 
servos = (PWM(Pin(18)), PWM(Pin(17)), PWM(Pin(16)))

for servo in servos:
    servo.freq(50)

DEAD_ZONE = 2 # Minimalny kąt, który jeśli zostanie przekroczony to serwo wykona ruch (ograniczenie drgania)
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

last_angles = [None, None, None] # Ostatni kąt wysłany do każdego serwa (None = jeszcze nie ustawiony)
current_angles = [0, 0, 0] # Bieżące kąty (do samego wyświetlania na konsoli)

while True:
    for i in range(3):
        pot_value = read_pot_averaged(pots[i])
        angle = map_value(pot_value, 0, 65535, 0, 180)
        current_angles[i] = angle

        if last_angles[i] is None or abs(angle - last_angles[i]) >= DEAD_ZONE:
            set_angle(servos[i], angle)
            last_angles[i] = angle

    print("Serwo 1: {}  Serwo 2: {}  Serwo 3: {}".format(*current_angles))

    time.sleep(0.02)
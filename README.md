[ENGLISH](#english)
[POLSKI](#polski)

# ENGLISH

## Description

A servo-based robotic arm, manually controlled with 5 potentiometers – each one drives a single motor. A gripper is mounted at the end of the arm. The project is based on the **ESP32-DevKitC** microcontroller.

This is my first robotic arm, so I'm aware of a few mistakes I made along the way. I'll be grateful for any tips and constructive feedback that will help me develop the project further.

Inspirations:

- [DIY Arduino Robot Arm with Smartphone Control](https://www.youtube.com/watch?v=_B3gWd3A_SI)
- [Brazo robótico con Arduino 💻 | Control desde PC, guarda y reproduce movimientos](https://www.youtube.com/watch?v=mH10h8SrDmM)

## Table of Contents

- [3D Model](#3d-model)
- [BOM](#bom)
    - [Electronics](#electronics)
    - [Screws and Bolts](#screws-and-bolts)
    - [Mechanical Parts](#mechanical-parts)
    - [Counterweight](#counterweight)
- [Printing Notes](#printing-notes)
- [Assembly](#assembly)
    - [Assembly Variants](#assembly-variants)
    - [Assembly Instructions](#assembly-instructions)
        - [1. Base](#1-base)
        - [2. Rotating Platform](#2-rotating-platform)
        - [3. Arm 1](#3-arm-1)
        - [4. Arm 2](#4-arm-2)
        - [5. Gripper](#5-gripper)
- [Wiring diagram](#wiring-diagram)
- [Power Supply](#power-supply)

---
## 3D Model

The 3D printable files are available on my MakerWorld profile at this link: [BRACHIUM - 5 DOF Robotarm](https://makerworld.com/pl/models/3395564-brachium-5-dof-robotarm?from=search#profileId-3865269)

---
## BOM

Every component I used has a link in its name to the store where I bought it.

### Electronics

|Component|Model|Qty|
|---|---|:-:|
|Microcontroller|[ESP32-DevKitC](https://botland.com.pl/moduly-esp32/8893-esp32-wifi-bt-42-platforma-z-modulem-esp-wroom-32-zgodny-z-esp32-devkit-5904422337438.html)|1|
|Servo|[MG996R](https://allegro.pl/produkt/serwo-tower-pro-mg996-arduino-metal-towerpro-30ce030f-85ea-4a96-a774-d2327b86bada?offerId=7441362868)|3|
|Servo|[MG90S](https://botland.com.pl/serwa-typu-micro/20435-serwo-mg-90s-micro-180-stopni-metalowa-przekladnia-5904422380915.html)|2|
|Potentiometer|any|5|
|Voltage regulator|[L7805CV](https://allegro.pl/produkt/stabilizator-nieregulowany-st-l7805cv-47b0abe2-182a-43d8-9404-100a03687be6?offerId=7400395364)|1|
|Jumper wires|–|–|
|Breadboard|[830 points](https://botland.com.pl/plytki-stykowe/19943-plytka-stykowa-justpi-830-otworow-5904422328610.html)|1|
|ESP32 adapter _(optional)_|[Terminal shield](https://elektroweb.pl/pl/plytki-rozszerzen-do-esp8266-i-esp32/1311-adapter-terminal-shield-esp32-esp8266-nodemcu-plytka-prototypowa.html)|_1_|

### Screws and Bolts

Kits used: [screws](https://allegro.pl/produkt/815x-wkrety-samowiercace-do-drewna-metali-stal-plaskie-krzyzowe-zestaw-duzy-53bdecd5-374e-49fa-bf9e-2ae12b0e7fb8?offerId=18832917865), [bolts](https://botland.com.pl/srubki-i-nakretki/23456-zestaw-srub-i-nakretek-m3m4m5m6-1000szt-5904257801784.html).

|Component|Size|Head|Qty|
|---|---|---|:-:|
|Screw|M5×18|pan|2|
|Screw|M4×16|pan|4|
|Screw|M4×16|flat|4|
|Screw|M4×12|pan|8|
|Screw|M3×10|pan|8|
|Screw|M3×10|flat|4|
|Bolt|M3×14|pan|2|
|Bolt|M3×10|pan|4|
|Bolt|M3×6|pan|3|
|Bolt|M2.5×6|pan|2|

### Mechanical Parts

|Component|Description|Qty|
|---|---|:-:|
|[Metal servo horn](https://allegro.pl/produkt/orczyk-serwa-avmarket-69-665-zta69665-71f7f07e-604f-4cff-84d0-a9700441dd16?offerId=18793103508)|for MG996R servo|3|

### Counterweight

|Component|Weight|Qty|
|---|---|:-:|
|[Steel weights](https://allegro.pl/produkt/ciezarki-klejone-do-felg-5g-10g-edgy-slim-50-szt-ocynkowane-stix-7e35ca66-2ed7-4c2c-b1ab-135471617335?offerId=14093125581)|10 g|12|

---
## Printing Notes

> **Pause at layer 78 (rotating platform)** 
> The rotating platform print will pause at layer 78. At that point, insert the twelve 10 g weights – 3 into each of the 4 slots – and resume printing.

---
## Assembly

### Assembly Variants

|Variant|Description|
|---|---|
|**Standard**|The base is screwed directly to the work table, with the rotating platform mounted on top of it.|
|**Alternative**|The rotating platform is screwed directly to the work table through its two holes. The arm loses one degree of freedom.|

These instructions cover the **standard variant**.

### Assembly Instructions

Screws and bolts without any annotation have a **pan** head. Flat heads are marked with **(flat)**.

#### 1. Base

1. Screw the base to the work table – 2× M5×18 screw.
2. Mount the MG996R servo (1) in the base – 4× M4×16 screw.
3. Attach the metal servo horn (1) to the MG996R servo (1) – 1× M3×6 bolt.

#### 2. Rotating Platform

4. Attach the rotating platform to the metal servo horn (1) – 2× M3×14 bolt.
5. Mount the MG996R servo (2) on the rotating platform – 4× M4×12 screw.

#### 3. Arm 1

6. Attach the metal servo horn (2) to arm 1 (2) – 2× M3×10 bolt.
7. Attach the metal servo horn (3) to arm 1 (2) – 2× M3×10 bolt.
8. Attach the metal servo horn (2) to the MG996R servo (2) – 1× M3×6 bolt.

#### 4. Arm 2

9. Mount the MG996R servo (3) in arm 2 – 4× M4×12 screw.
10. Attach the metal servo horn (3) to the MG996R servo (3) – 1× M3×6 bolt.
11. Mount the MG90S servo (1) in arm 2 – 2× M3×10 screw.
12. Attach the plastic servo horn to the MG90S servo (1) – 1× M2.5×6 bolt.

#### 5. Gripper

13. Attach the gripper mount to the plastic servo horn – 2× M3×10 screw.
14. Mount the MG90S servo (2) in the gripper – 2× M3×10 screw.
15. Attach the gear to the MG90S servo (2) – 1× M2.5×6 bolt.
16. Attach the gripper to the gripper mount – 4× M4×16 screw (flat).
17. Attach the cover to the gripper – 2× M3×10 screw.
18. Attach the jaws to the rails – 4× M3×10 screw (flat).

---
## Wiring diagram

<img src="Wiring%20diagram.png" alt="Wiring diagram" width="716">

---
## Power Supply

To power the circuit, I used a [Korad KA3005DS 0-30V 5A](https://botland.com.pl/zasilacze-laboratoryjne/23190-zasilacz-laboratoryjny-korad-ka3005ds-0-30v-5a-5904422384326.html) lab power supply.

> [!IMPORTANT]
> Under load, each MG996R servo can draw up to 2.5 A. The power supply must have enough current headroom to handle the load they create.


# POLSKI

## Opis

Ramię robotyczne oparte na serwomechanizmach, sterowane ręcznie za pomocą 5 potencjometrów – każdy odpowiada za jeden silnik. Na końcu ramienia znajduje się chwytak. Projekt bazuje na mikrokontrolerze **ESP32-DevKitC**.

To moje pierwsze ramię robotyczne, więc zdaję sobie sprawę z kilku popełnionych błędów. Będę wdzięczny za wszelkie porady i konstruktywne uwagi, które pomogą rozwinąć projekt w przyszłości.

Inspiracje:

- [DIY Arduino Robot Arm with Smartphone Control](https://www.youtube.com/watch?v=_B3gWd3A_SI)
- [Brazo robótico con Arduino 💻 | Control desde PC, guarda y reproduce movimientos](https://www.youtube.com/watch?v=mH10h8SrDmM)

## Spis treści

- [Model 3D](#model-3d)
- [BOM](#bom)
    - [Elektronika](#elektronika)
    - [Wkręty i śruby](#wkr%C4%99ty-i-%C5%9Bruby)
    - [Części mechaniczne](#cz%C4%99%C5%9Bci-mechaniczne)
    - [Przeciwwaga](#przeciwwaga)
- [Uwagi do druku](#uwagi-do-druku)
- [Montaż](#monta%C5%BC)
    - [Warianty montażu](#warianty-monta%C5%BCu)
    - [Instrukcja montażu](#instrukcja-monta%C5%BCu)
        - [1. Podstawa](#1-podstawa)
        - [2. Platforma obrotowa](#2-platforma-obrotowa)
        - [3. Ramię 1](#3-rami%C4%99-1)
        - [4. Ramię 2](#4-rami%C4%99-2)
        - [5. Chwytak](#5-chwytak)
- [Schemat połączeń](#schemat-po%C5%82%C4%85cze%C5%84)
- [Zasilanie](#zasilanie)

---
## Model 3D

Pliki do 3D do druku dostępne są na moim profilu Makerworld pod tym linkiem: [BRACHIUM - 5 DOF Robotarm](https://makerworld.com/pl/models/3395564-brachium-5-dof-robotarm?from=search#profileId-3865269)

---
## BOM

Wszystkie użyte przeze mnie elementy mają przy nazwie link do sklepu, w którym je kupiłem.

### Elektronika

|Element|Model|Ilość|
|---|---|:-:|
|Mikrokontroler|[ESP32-DevKitC](https://botland.com.pl/moduly-esp32/8893-esp32-wifi-bt-42-platforma-z-modulem-esp-wroom-32-zgodny-z-esp32-devkit-5904422337438.html)|1|
|Serwomechanizm|[MG996R](https://allegro.pl/produkt/serwo-tower-pro-mg996-arduino-metal-towerpro-30ce030f-85ea-4a96-a774-d2327b86bada?offerId=7441362868)|3|
|Serwomechanizm|[MG90S](https://botland.com.pl/serwa-typu-micro/20435-serwo-mg-90s-micro-180-stopni-metalowa-przekladnia-5904422380915.html)|2|
|Potencjometr|dowolny|5|
|Stabilizator napięcia|[L7805CV](https://allegro.pl/produkt/stabilizator-nieregulowany-st-l7805cv-47b0abe2-182a-43d8-9404-100a03687be6?offerId=7400395364)|1|
|Przewody połączeniowe|–|–|
|Płytka prototypowa|[830 otworów](https://botland.com.pl/plytki-stykowe/19943-plytka-stykowa-justpi-830-otworow-5904422328610.html)|1|
|Adapter ESP32 _(opcjonalnie)_|[Terminal shield](https://elektroweb.pl/pl/plytki-rozszerzen-do-esp8266-i-esp32/1311-adapter-terminal-shield-esp32-esp8266-nodemcu-plytka-prototypowa.html)|_1_|

### Wkręty i śruby

Użyte zestawy: [wkręty](https://allegro.pl/produkt/815x-wkrety-samowiercace-do-drewna-metali-stal-plaskie-krzyzowe-zestaw-duzy-53bdecd5-374e-49fa-bf9e-2ae12b0e7fb8?offerId=18832917865), [śruby](https://botland.com.pl/srubki-i-nakretki/23456-zestaw-srub-i-nakretek-m3m4m5m6-1000szt-5904257801784.html).

|Element|Rozmiar|Łeb|Ilość|
|---|---|---|:-:|
|Wkręt|M5×18|wypukły|2|
|Wkręt|M4×16|wypukły|4|
|Wkręt|M4×16|płaski|4|
|Wkręt|M4×12|wypukły|8|
|Wkręt|M3×10|wypukły|8|
|Wkręt|M3×10|płaski|4|
|Śruba|M3×14|wypukły|2|
|Śruba|M3×10|wypukły|4|
|Śruba|M3×6|wypukły|3|
|Śruba|M2,5×6|wypukły|2|

### Części mechaniczne

|Element|Opis|Ilość|
|---|---|:-:|
|[Orczyk metalowy](https://allegro.pl/produkt/orczyk-serwa-avmarket-69-665-zta69665-71f7f07e-604f-4cff-84d0-a9700441dd16?offerId=18793103508)|do serwa MG996R|3|

### Przeciwwaga

|Element|Masa|Ilość|
|---|---|:-:|
|[Stalowe ciężarki](https://allegro.pl/produkt/ciezarki-klejone-do-felg-5g-10g-edgy-slim-50-szt-ocynkowane-stix-7e35ca66-2ed7-4c2c-b1ab-135471617335?offerId=14093125581)|10 g|12|

---
## Uwagi do druku

> **Pauza na warstwie 78 (platforma obrotowa)** 
> Wydruk platformy obrotowej zatrzyma się na warstwie 78. Włóż wtedy 12 ciężarków po 10 g – po 3 do każdego z 4 slotów – i wznów druk.

---
## Montaż

### Warianty montażu

|Wariant|Opis|
|---|---|
|**Podstawowy**|Podstawa przykręcona bezpośrednio do stołu roboczego, a na niej platforma obrotowa.|
|**Alternatywny**|Platforma obrotowa przykręcona bezpośrednio do stołu roboczego przez dwa otwory w niej. Ramię traci jeden stopień swobody.|

Instrukcja opisuje **wariant podstawowy**.

### Instrukcja montażu

Wkręty i śruby bez dopisku mają łeb **wypukły**. Łeb płaski oznaczono dopiskiem **(płaski)**.

#### 1. Podstawa

1. Przykręć podstawę do stołu roboczego – 2× wkręt M5×18.
2. Zamocuj serwo MG996R (1) w podstawie – 4× wkręt M4×16.
3. Przykręć metalowy orczyk (1) do serwa MG996R (1) – 1× śruba M3×6.

#### 2. Platforma obrotowa

4. Przykręć platformę obrotową do metalowego orczyka (1) – 2× śruba M3×14.
5. Zamocuj serwo MG996R (2) na platformie obrotowej – 4× wkręt M4×12.

#### 3. Ramię 1

6. Przykręć metalowy orczyk (2) do ramienia 1 (2) – 2× śruba M3×10.
7. Przykręć metalowy orczyk (3) do ramienia 1 (2) – 2× śruba M3×10.
8. Przykręć metalowy orczyk (2) do serwa MG996R (2) – 1× śruba M3×6.

#### 4. Ramię 2

9. Zamocuj serwo MG996R (3) w ramieniu 2 – 4× wkręt M4×12.
10. Przykręć metalowy orczyk (3) do serwa MG996R (3) – 1× śruba M3×6.
11. Zamocuj serwo MG90S (1) w ramieniu 2 – 2× wkręt M3×10.
12. Przykręć plastikowy orczyk do serwa MG90S (1) – 1× śruba M2,5×6.

#### 5. Chwytak

13. Przykręć mocowanie chwytaka do plastikowego orczyka – 2× wkręt M3×10.
14. Zamocuj serwo MG90S (2) w chwytaku – 2× wkręt M3×10.
15. Przykręć zębatkę do serwa MG90S (2) – 1× śruba M2,5×6.
16. Przykręć chwytak do mocowania chwytaka – 4× wkręt M4×16 (płaski).
17. Przykręć nakładkę do chwytaka – 2× wkręt M3×10.
18. Przykręć szczypce do szyn – 4× wkręt M3×10 (płaski).

---
## Schemat połączeń

<img src="Wiring%20diagram.png" alt="Schemat połączeń" width="716">

---
## Zasilanie

Do zasilania układu użyłem zasilacza laboratoryjnego [Korad KA3005DS 0-30V 5A](https://botland.com.pl/zasilacze-laboratoryjne/23190-zasilacz-laboratoryjny-korad-ka3005ds-0-30v-5a-5904422384326.html).

> [!IMPORTANT]
> Serwa MG996R pod obciążeniem pobierają nawet do 2,5 A każde. Zasilacz musi mieć odpowiedni zapas prądu aby wytrzymać obciążenie pochodzące od nich.

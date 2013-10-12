EESchema Schematic File Version 2  date Sat 12 Oct 2013 22:07:52 CST
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:special
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:remote-240a-cache
EELAYER 25  0
EELAYER END
$Descr A4 11700 8267
encoding utf-8
Sheet 1 1
Title "noname.sch"
Date "12 oct 2013"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	5500 2000 5600 2000
Wire Wire Line
	5500 3400 5500 2300
Wire Wire Line
	5500 2300 5500 2000
Connection ~ 5900 2300
Connection ~ 5500 2300
Connection ~ 5900 2700
Wire Wire Line
	8300 3400 8300 2700
Wire Notes Line
	7400 2500 6200 2500
Wire Notes Line
	7400 2500 7400 3600
Wire Notes Line
	7400 3600 6200 3600
Wire Notes Line
	6200 3600 6200 2500
Wire Wire Line
	3750 3400 3600 3400
Wire Wire Line
	3600 3400 3600 3600
Wire Wire Line
	3600 3600 5900 3600
Wire Wire Line
	5900 2700 7700 2700
Wire Wire Line
	5900 3600 5900 2700
Wire Wire Line
	5900 2700 5900 2300
Wire Wire Line
	5900 2300 5900 2000
Wire Wire Line
	4550 3400 5500 3400
Wire Wire Line
	5500 3400 6450 3400
Connection ~ 5500 3400
Wire Wire Line
	7700 3400 7100 3400
Wire Wire Line
	5900 2000 5800 2000
Text Label 7100 3400 0    60   ~ 0
GND
Text Label 6450 3400 0    60   ~ 0
PCB
$Comp
L BATTERY BT?
U 1 1 52592F5A
P 8000 3400
F 0 "BT?" H 8000 3600 50  0000 C CNN
F 1 "BATTERY" H 8000 3210 50  0000 C CNN
	1    8000 3400
	-1   0    0    1   
$EndComp
$Comp
L BATTERY BT?
U 1 1 52592F4C
P 8000 2700
F 0 "BT?" H 8000 2900 50  0000 C CNN
F 1 "BATTERY" H 8000 2510 50  0000 C CNN
	1    8000 2700
	1    0    0    -1  
$EndComp
$Comp
L CONN_13X2 P?
U 1 1 52592F38
P 4150 2800
F 0 "P?" H 4150 3500 60  0000 C CNN
F 1 "CONN_13X2" V 4150 2800 50  0000 C CNN
	1    4150 2800
	1    0    0    -1  
$EndComp
$Comp
L LED D?
U 1 1 52592EF3
P 5700 2300
F 0 "D?" H 5700 2400 50  0000 C CNN
F 1 "LED" H 5700 2200 50  0000 C CNN
	1    5700 2300
	-1   0    0    1   
$EndComp
$Comp
L SPEAKER SP?
U 1 1 52592EEE
P 5700 1700
F 0 "SP?" H 5600 1950 70  0000 C CNN
F 1 "SPEAKER" H 5600 1450 70  0000 C CNN
	1    5700 1700
	0    -1   -1   0   
$EndComp
$EndSCHEMATC

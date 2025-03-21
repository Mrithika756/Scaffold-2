from machine import Pin, PWM
import time

# Define servo parameters
servo = PWM(Pin(2), freq=50)
led = Pin(5, Pin.OUT)
sensor = Pin(4, Pin.IN)

# Function to set servo angle
def set_servo_angle(angle):
    duty = int((angle / 180) * 102 + 26)
    servo.duty(duty)

# Very small oscillations to mimic vibration
def servo_vibrate():
    for _ in range(10):
        set_servo_angle(89.5)
        time.sleep(0.01)
        set_servo_angle(90.5)
        time.sleep(0.01)

# Main loop
while True:
    servo_vibrate()

    if sensor.value() == 1:
        led.value(1)
    else:
        led.value(0)

    time.sleep(0.1)# Write your code here :-)

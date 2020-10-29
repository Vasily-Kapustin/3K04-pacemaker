import time
import Serial

ser = Serial.Serial('COM4', 9600)


def send_email():
    print("Sending Email")

while True:
    message = ser.readline()
    print(message)
    if message[0] == 'M':
        send_email()
    time.sleep(0.5)
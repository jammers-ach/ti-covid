import serial
import RPi.GPIO as GPIO
import time
from covid_reporter import report_covid_status

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

def print_status():
    serialPort = serial.Serial(port="/dev/ttyAMA0",
                            timeout = 2,
                            baudrate=300,
                            parity=serial.PARITY_EVEN,
                            bytesize=serial.SEVENBITS,
                            stopbits=serial.STOPBITS_ONE)

    serialPort.flushInput()
    serialPort.flushOutput()
    report_covid_status(serialPort)
    serialPort.close()


def main():
    while True:
        print("Waiting for GPIO")
        GPIO.wait_for_edge(4, GPIO.RISING)
        print("GPIO activated")
        time.sleep(3)
        print("Printing message")
        print_status()
        time.sleep(5)


if __name__ == "__main__":
    main()


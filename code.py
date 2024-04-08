# maaaaaaaaaaaaaaaaaaaaaaasters
import board
import busio
import time
import digitalio

master_hc05 = busio.UART(board.GP16, board.GP17,baudrate=9600)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT


# CONSTANTS 
TIMEOUT = 1

def sendCMD_waitResp(cmd, uart=master_hc05, timeout=TIMEOUT):
    print("CMD: " + cmd)
    uart.write(cmd)
    waitResp(uart, timeout)
    print()

def waitResp(uart=master_hc05, timeout=TIMEOUT):
    prvMills = time.monotonic()
    resp = b""
    while (time.monotonic()-prvMills)<timeout:
        if uart.any():
            resp = b"".join([resp, uart.read(1)])
    print(resp)
i = 0

while True:
    led.value = True
    master_hc05.write(f'Comanda {i}\n\r')
    print(f'Comanda {i}\n\r')
    if i == 9:
        i = 0
    else:
        i = i + 1
    time.sleep(1)



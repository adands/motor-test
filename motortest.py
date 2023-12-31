#啟用RPI GPIO
import RPi.GPIO as GPIO

# 馬達接上A-、A+、B-、B+
# 另接12伏電壓供應
# 板子GND接RPI GND
# 連接PWM到腳位12
# 連接到任一腳位

GPIO.setmode(GPIO.BCM)

PWM_A = 12
PIN_A_PO = 5
PIN_A_NE = 6

PWM_B = 13
PIN_B_PO = 26
PIN_B_NE = 16

GPIO.setup(PWM_A, GPIO.OUT)
GPIO.setup(PWM_B, GPIO.OUT)

GPIO.setup(PIN_A_PO,GPIO.OUT)
GPIO.setup(PIN_A_NE,GPIO.OUT)
GPIO.setup(PIN_B_PO,GPIO.OUT)
GPIO.setup(PIN_B_NE,GPIO.OUT)

pwm_a = GPIO.PWM(PWM_A, 1000)  # 设置PWM_A引脚为PWM输出模式，频率为100Hz
pwm_b = GPIO.PWM(PWM_B, 1000)  # 设置PWM_B引脚为PWM输出模式，频率为100Hz



def setspeed(speed):
    pwm_a.start(speed)  # 启动PWM输出，初始占空比为0
    pwm_b.start(speed)
    return()

try:
    while True:
        GPIO.output(PIN_B_PO,GPIO.HIGH)
        GPIO.output(PIN_B_NE,GPIO.LOW)
        setspeed(100)
        usr_input = None
        usr_input = input("direction:")
        if usr_input == "forward" or "w":
            setspeed(0)
            # GPIO.output(PIN_A_PO,GPIO.HIGH)
            # GPIO.output(PIN_A_NE,GPIO.LOW)
            GPIO.output(PIN_B_PO,GPIO.HIGH)
            GPIO.output(PIN_B_NE,GPIO.LOW)
            usr_input = None
            setspeed(100)
        if usr_input == "reverse" or "s":
            setspeed(0)
            # GPIO.output(PIN_A_PO,GPIO.LOW)
            # GPIO.output(PIN_A_NE,GPIO.HIGH)
            GPIO.output(PIN_B_PO,GPIO.HIGH)
            GPIO.output(PIN_B_NE,GPIO.LOW)
            usr_input = None
            setspeed(10)
        elif usr_input == "right" or "a":
            pass
        elif usr_input == "left" or "d":
            pass
        elif usr_input == "stop" or "k":
            # GPIO.output(PIN_A_PO,GPIO.LOW)
            # GPIO.output(PIN_A_NE,GPIO.LOW)
            GPIO.output(PIN_B_PO,GPIO.LOW)
            GPIO.output(PIN_B_NE,GPIO.LOW)
            setspeed(0)
        else:
            GPIO.output(PIN_B_PO,GPIO.LOW)
            GPIO.output(PIN_B_NE,GPIO.LOW)
            setspeed(0)
except KeyboardInterrupt:
    pwm_a.stop()  # 停止PWM输出
    pwm_b.stop()
    GPIO.cleanup()
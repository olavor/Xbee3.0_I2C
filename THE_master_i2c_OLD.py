import time
from machine import I2C
import xbee

SLAVE_ADDRESS = 0x42
BAUDRATE = 100000
ad = 0x43
freq=400000

i2c_master = I2C(1, freq=400000)
i2c_master.scan()

data = i2c_master.readfrom(42, 4)
i2c_master.writeto(42, b'123')

for i in range(10):
    try:
        data = i2c_master.readfrom(42, 4)
    except OSError as exc:
        if exc.args[0] not in (5, 110):
            # 5 == EIO, occurs when master does a I2C bus scan
            # 110 == ETIMEDOUT
            print(exc)
    except KeyboardInterrupt:
        break
    else:
        print("RECV: %r" % data)




        #master
#for i in range(10):
#i2c_master.send(b"%04i" % i, addr=SLAVE_ADDRESS)
#time.sleep(0.5)
#i2c_master = I2C(1, I2C.MASTER,addr = ad, baudrate=BAUDRATE)
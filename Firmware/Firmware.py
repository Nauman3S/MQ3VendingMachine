import time
from gas_detection import GasDetection

detection = GasDetection()

BAC= 10000#1BAC(g/dL) is 10000ppm
PPM=1/BAC

def getAlcoholValue():
    global detection,PPM
    ppm = detection.percentage()

    print('ALCOHOL: {} ppm'.format(ppm[detection.ALCOHOL_GAS]))
    BACValue=PPM*ppm[detection.ALCOHOL_GAS]

    print('ALCOHOL BAC=',BACValue)

    return BACValue

while 1:
    time.sleep(1)
    getAlcoholValue()

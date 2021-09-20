from mq import *
import sys, time

BAC= 10000#1BAC(g/dL) is 10000ppm
PPM=1/BAC

mq = MQ()
def getAlcoholValue():
    global mq,BAC,PPM
    try:
    
        perc = mq.MQPercentage()
        print("ALCOHOL: %g ppm" % (perc["ALCOHOL"]))
        BACValue=(perc["ALCOHOL"])*PPM
        print('ALCOHOL BAC=',BACValue)
        return BACValue

    except:
        print("\nAbort by user")

while True:

    getAlcoholValue()

    time.sleep(1)
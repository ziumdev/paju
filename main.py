import snmpFunc
import trapReceiver
from multiprocessing import Process

loopProc = Process(target=snmpFunc.loop)
# receiverPro = Process(target=trapReceiver.run)

if __name__ == '__main__':
    loopProc.start()
    # receiverPro.start()
    # loopProc.join()
    # receiverPro.join()

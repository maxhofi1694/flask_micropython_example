# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
gc.collect()

# bis hier ist es ein standard micropython boot.py file

#wifi:
import network # network libary importieren

def do_connect(): # die standard verbindungsfunktion der library
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('WLANNAME, 'WLANPASSWORD') # hier den wlanname + password eingeben
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect() # hier wird die library aufgerufen, danach wird automatisch main.py ausgeführt

#import webrepl
#webrepl.start()



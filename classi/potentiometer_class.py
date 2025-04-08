"""classe per il potenziometro impostato a ATTN_11DB"""

from machine import ADC

class PTM:
    def __init__(self,sig_pin):
        self.adc = ADC(Pin(sig_pin,Pin.IN))
        self.adc.atten(ADC.ATTN_11DB)
        
    def read(self):
        return self.adc.read()
    
    def value(self):
        return self.read() * (3.3/4095)
    
    

from machine import ADC, Pin


class AdcSensor:
    def __init__(self, name, pin_id) -> None:
        self.name = name
        self.adc = ADC(Pin(pin_id))
        self.adc.atten(ADC.ATTN_11DB)
        self.adc.width(ADC.WIDTH_13BIT)
    
    def get(self):
        return {
            "name": self.name,
            "value": self.adc.read()
        }

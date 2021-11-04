import esp
import time
import json
import network
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

from adc import AdcSensor


CONFIG_FILE = "config.json"


esp.osdebug(None)


def load_config():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def configure_networking(net_ssid, net_password):
    print(f"Attempting to connect to {net_ssid}...")
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    time.sleep(1)
    wlan.active(True)
    wlan.connect(net_ssid, net_password)
    print("Connected.")
    return wlan


class Subscriber:
    def __init__(self, port) -> None:
        self.port = port
        self.sock = socket(AF_INET, SOCK_STREAM)
        self.sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", self.port))
        self.sock.listen(1)
        self.remote_sock = None

    def connect(self):
        self.remote_sock, _ = self.sock.accept()
    
    def close(self):
        self.sock.close()

    def send(self, obj):
        message = json.dumps(obj).encode()
        msg_len = len(message)
        if msg_len > 0xffff:
            raise OverflowError("Maximum packet size exceeded")
        message = bytes([msg_len >> 8 & 0xff, msg_len & 0xff]) + message
        self.remote_sock.send(message)
        print(".", end="")


def create_sensors():
    return [
        AdcSensor("anemometer", 4),
        AdcSensor("wind_direction", 5),
    ]


def main():
    while True:
        try:
            config = load_config()
            configure_networking(config["net_ssid"], config["net_password"])
            sensors = create_sensors()
        except Exception as e:
            print("Init failed:", e)
            continue

        while True:
            try:
                subscriber = Subscriber(config["port"])
                print("Awaiting subscriber...")
                subscriber.connect()
                print("Subscriber connected.")
                try:
                    while True:
                        sample = [sensor.get() for sensor in sensors]
                        subscriber.send(sample)
                        time.sleep(0.3)
                except Exception as e:
                    print("Error streaming data", e)
                    subscriber.close()
            except Exception as e:
                print("Error connecting to subscriber:", e)


main()

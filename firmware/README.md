## Weather station firmware

### Loading firmware (assumes device is on /dev/ttyUSB0):
```
./load.sh /dev/ttyUSB0
```

This assumes you have a MicroPython interpreter loaded on the chip. Working firmware for the ESP32-S2 can be found here:

[https://github.com/wangshujun-tj/mpy-Framebuf-boost/blob/main/esp12k_1.17_fb_boost_4M.bin](https://github.com/wangshujun-tj/mpy-Framebuf-boost/blob/main/esp12k_1.17_fb_boost_4M.bin)

This also assumes you have the ampy command. This can be installed with pip:
```
python3 -m pip install adafruit-ampy
```

Currently, the firmware (mainly in `boot.py`) connects to WiFi, then continuously attempts to accept a TCP connection and stream sample data to it.

WiFi credentials are currently managed in a config.json file on the ESP32 filesystem. It's not great, but
creating a method to accept WiFi credentials via a temporarily-hosted AP takes work. And transmitting that data securely and all that jazz is even more work. So for now, unencrypted config files will do.

The `config.json` should look something like:
```json
{
    "net_ssid": "<YOUR WiFi SSID>",
    "net_password": "<YOUR WiFi PASSWORD>",
    "port": 2149
}
```

*(The port field determines what TCP port the weather station will be accepting connections on.)*

The below command can upload the `config.json` to the ESP32:
```
ampy --port /dev/ttyUSB0 put config.json
```

### Adding new sensors

Sensors can be added in the returned list of the `create_sensors` function of `boot.py`.

Sensors should support the following interface:

```python
class Sensor:
    def get(): -> object
        # gather sensor data and return a JSON-friendly object
        pass
```

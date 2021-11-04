## Weather station firmware

### Loading firmware (assumes device is on /dev/ttyUSB0):
```
./load.sh /dev/ttyUSB0
```

Currently, the firmware (mainly in `boot.py`) connects to WiFi, then continuously attempts to accept a TCP connection and stream sample data to it.

WiFi credentials are currently managed in a config.json file on the ESP32 filesystem. It's not great, but
creating a method to accept WiFi credentials via a temporarily-hosted AP takes work.

The `config.json` should look something like:
```json
{
    "net_ssid": "<YOUR WiFi SSID>",
    "net_password": "<YOUR WiFi PASSWORD>",
    "port": 2149
}
```

*(The port field determines what TCP port the weather station will be accepting connections on.)*

### Adding new sensors

Sensors can be added in the returned list of the `create_sensors` function of `boot.py`.

Sensors should support the following interface:

```python
class Sensor:
    def get(): -> object
        # gather sensor data and return a JSON-friendly object
        pass
```

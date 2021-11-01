## Weather Station SW

This is the location for my particular take on the weather station's code.

### Overall design

Main components are:

- `firmware/` : runs on the ESP32-S2 on the weather station and provides a socket interface over WiFi.

- `ui/` : The webpage for interacting with the weather station. Currently build on React.

- `backend/` : An endpoint that hosts the weather station's UI and facilitates interaction between the UI and the firmware. While it could be argued that this is an unecessary element to add to the mix, websockets may be harder to integrate into the firmware, traditional sockets may be difficult to support in webpage JS, and since something already needs to host the UI, we might as well create a dedicated system to facilitate anything that we might not necessarily want to include into the weather station firmware.

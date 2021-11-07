import json
import websockets
import asyncio
from threading import Thread, Lock


class WebsocketServer:
    def __init__(self, port) -> None:
        self.port = port
        self.clients = []
        self.loop = None
        self.lock = Lock()

    def propagate(self, data):
        """
        Encodes the message and sends it to all active websockets
        """
        message = json.dumps(data)
        rm_clients = []
        for client in self.clients:
            try:
                asyncio.run_coroutine_threadsafe(client.send(message), self.loop)
            except Exception as e:
                print(f"Error sending update ({e}); disconnecting...")
                rm_clients.append(client)
        for client in rm_clients:
            self.disconnect(client)
    
    def disconnect(self, client):
        with self.lock:
            try:
                client.close()
            except:
                pass
            if client in self.clients:
                self.clients.remove(client)
    
    def start(self):
        loop = asyncio.new_event_loop()
        Thread(target=self.run_server, args=(loop,)).start()
    
    def run_server(self, loop: asyncio.AbstractEventLoop):
        self.loop = loop
        asyncio.set_event_loop(loop)
        loop.run_until_complete(websockets.serve(self.accept, "0.0.0.0", self.port))
        print("Listening for websocket connections...")
        loop.run_forever()
    
    async def accept(self, client, path):
        print("New ws connection")
        with self.lock:
            self.clients.append(client)
        try:
            while True:
                message = await client.recv()
                # NOTE: For now, the websocket server only propagates.
        except:
            print("Closing connection...")
            self.disconnect(client)

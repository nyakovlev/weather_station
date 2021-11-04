import json
import websockets
import asyncio


class WebsocketServer:
    def __init__(self) -> None:
        self.clients = []

    def propagate(self, data):
        """
        Encodes the message and sends it to all active websockets
        """
        message = json.dumps(data)
        for client in self.clients:
            # TODO: catch errors and disconnect
            client.send(message)
    
    def disconnect(self, client):
        client.close()
        if client in self.clients:
            self.clients.remove(client)
    
    def run_server():
        pass

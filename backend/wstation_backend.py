import argparse
from threading import Thread

import station_link
from websocket_server import WebsocketServer

__doc__ = """

"""


def main():
    parser = argparse.ArgumentParser(
        "server.py",
        description="Runs a webpage and manages interaction with weather stations"
    )
    parser.add_argument("--web-port", desc="TCP port to serve webpage", default=80)
    parser.add_argument("--backend-port", desc="TCP port to run backend", default=22149)
    
    wss = WebsocketServer()
    Thread(
        target=station_link.run,
        args=(
            "192.168.0.31",
            2149,
            wss.propagate
        )
    ).start()

    # TODO: Launch an nginx (or http-server) instance on a dist directory of the UI


if __name__ == "__main__":
    main()

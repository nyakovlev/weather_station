import argparse
from threading import Thread


def main():
    parser = argparse.ArgumentParser(
        "server.py",
        description="Runs a webpage and manages interaction with weather stations"
    )
    parser.add_argument("--web-port", desc="TCP port to serve webpage", default=80)
    parser.add_argument("--backend-port", desc="TCP port to run backend", default=2149)
    args = parser.parse_args()
    # TODO: Start the server core logic in a new thread
    # TODO: Launch an nginx instance on a dist directory of the UI


if __name__ == "__main__":
    main()

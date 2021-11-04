import socket
import json
import sys
import traceback
from select import select


TIMEOUT=5


def log_info(message):
    print(message)


def log_error(exc_type, exc_val, exc_tb):
    exc_msg = "\n".join(traceback.format_exception(exc_type, exc_val, exc_tb))
    print(f"\u001b[31m{exc_msg}\u001b[0m")


def run(address, port, on_update):
    """
    Keeps trying to connect to the weather station, then invokes on_update with 
    what it can receive from the connection.
    """
    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                log_info(f"Connecting to weather station at {address}:{port}...")
                sock.connect((address, port))
                log_info("Connected to weather station")
                sock.setblocking(0)
                while True:
                    ready = select([sock], [], [], TIMEOUT)
                    if not ready:
                        raise TimeoutError("Timeout waiting for header")
                    msg_hdr = sock.recv(2)
                    if not msg_hdr:
                        raise Exception("no msg_hdr")
                    msg_len = int.from_bytes(msg_hdr, "big")

                    ready = select([sock], [], [], TIMEOUT)
                    if not ready:
                        raise TimeoutError("Timeout waiting for message")
                    msg = sock.recv(msg_len)
                    try:
                        sample = json.loads(msg.decode())
                        try:
                            on_update(sample)
                        except KeyboardInterrupt:
                            return
                        except:
                            log_error(*sys.exc_info())
                    except:
                        pass
        except KeyboardInterrupt:
            return
        except:
            log_error(*sys.exc_info())
        log_info("Lost connection to weather station!")


def test_program():
    def update(d):
        log_info("UPDATE:", d)

    run(
        "192.168.0.31",
        2149,
        update
    )


if __name__ == "__main__":
    test_program()

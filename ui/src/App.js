import { useEffect } from "react"
import Anemometer from "./components/Anemometer";

const address = "localhost";
const port = 2148;

function create_endpoint() {
    let subscribers = [];
    let value;
    let initialized = false;
    let endpoint = {
        subscribe(subscriber) {
            subscribers.push(subscriber);
            if (initialized) {
                subscriber(value);
            }
            return () => {
                subscribers.splice(subscribers.indexOf(subscriber), 1);
            };
        },
        publish(newValue) {
            for (let subscriber of subscribers) {
                subscriber(newValue);
            }
        }
    };
    return endpoint
}

const stats = create_endpoint();

function App() {
    useEffect(() => {
        // TODO: keep trying to reconnect on connection failure, managing stale sockets along the way.
        const ws = new WebSocket(`ws://${address}:${port}`);
        ws.onopen = () => {
            console.log("Connected to backend.");
            ws.onmessage = msg => {
                let data = msg.data;
                stats.publish(JSON.parse(data));
            };
        };
        ws.onclose = () => {
            console.log("disconnected.");
        };
        return () => {
            ws.close();
        }
    }, []);

    return (
        <div>
            <Anemometer stats={stats} />
        </div>
    );
}

export default App;

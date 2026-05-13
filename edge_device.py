import socket
import paho.mqtt.client as mqtt

# Configuration
SOCKET_HOST = '127.0.0.1'
SOCKET_PORT = 5005
MQTT_BROKER = "broker.emqx.io"
MQTT_TOPIC = "savonia/iot/fozlearafat" # CHANGE 'yourname' to something unique

def start_edge():
    # Setup MQTT
    client = mqtt.Client()
    client.connect(MQTT_BROKER, 1883, 60)
    
    # Setup Socket Listener
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((SOCKET_HOST, SOCKET_PORT))
        s.listen()
        print(f"Edge Device listening on port {SOCKET_PORT}...")
        
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                # Forward to MQTT
                payload = data.decode()
                client.publish(MQTT_TOPIC, payload)
                print(f"Received via Socket and Published to MQTT: {payload}")

if __name__ == "__main__":
    start_edge()
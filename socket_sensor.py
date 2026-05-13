import socket
import time
import random

# Configuration
HOST = '127.0.0.1'  # Localhost (this computer)
PORT = 5005         # The "door" number for the connection

def start_sensor():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Connecting to Edge Device at {HOST}:{PORT}...")
        s.connect((HOST, PORT))
        
        try:
            while True:
                # Generate a random temperature
                temp = round(random.uniform(20.0, 30.0), 2)
                message = str(temp)
                
                # Send data
                s.sendall(message.encode())
                print(f"Sent to Edge: {temp}")
                
                time.sleep(2) # Wait 2 seconds
        except KeyboardInterrupt:
            print("Sensor stopped.")

if __name__ == "__main__":
    start_sensor()
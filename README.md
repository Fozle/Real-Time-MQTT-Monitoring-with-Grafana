# IoT Edge Computing & Visualization Lab

## Project Overview
This project demonstrates a complete IoT data pipeline, moving from a simulated sensor to a real-time cloud-based monitoring dashboard. It showcases the integration of **Socket Programming**, **MQTT (Message Queuing Telemetry Transport)**, and **Grafana** for data visualization.

The architecture follows an **Edge Computing** model, where data is processed locally before being published to a public broker for remote monitoring.

---

## System Architecture

The data flows through three distinct stages:

1.  **Data Generation (Sensor Layer):** `socket_sensor.py` simulates a hardware sensor, generating random data and sending it to a local port via TCP Sockets.
2.  **Edge Processing (Gateway Layer):** `edge_device.py` acts as the Edge Gateway. It listens for socket data, processes it, and publishes it to the EMQX public MQTT broker.
3.  **Visualization (Application Layer):** Grafana subscribes to the specific MQTT topic and displays the live data on a graphical dashboard.

---

## Setup Instructions

### 1. Prerequisites
* Python 3.x installed.
* Grafana installed (Windows Service or Standalone).
* MQTT Plugin installed in Grafana.
* Required Python libraries: `paho-mqtt`.

### 2. Running the System
To see the data live, run the scripts in this specific order:

1.  **Start the Edge Device:**
    ```bash
    python edge_device.py
    ```
2.  **Start the Sensor:**
    ```bash
    python socket_sensor.py
    ```
3.  **Launch Grafana:**
    Open `http://localhost:3000` and ensure your MQTT Data Source is connected to `tcp://broker.emqx.io:1883`.

---

## Configuration Details
* **MQTT Broker:** `broker.emqx.io`
* **MQTT Topic:** `savonia/iot/fozleafat`
* **Port:** 1883 (MQTT) / 3000 (Grafana)

---

## Lab Reflections

### What is the role of Grafana in this system?
Grafana serves as the **Presentation Layer**. It transforms raw numerical data into human-readable formats (graphs, gauges, and stats), allowing operators to monitor the health and status of IoT devices in real-time without looking at code.

### Why is MQTT used for IoT monitoring?
MQTT is used because it is a lightweight "Publish/Subscribe" protocol. It has low overhead, meaning it uses very little battery and bandwidth, making it the industry standard for IoT devices that need to send frequent updates over unreliable networks.

### Is the data currently Live or Historical?
The current setup is **Live**. Data is displayed as it arrives but is not saved to a database. To view **Historical** data (e.g., temperatures from yesterday), a time-series database like InfluxDB or Prometheus would need to be integrated to store the messages.

---

## Author
**Fozle Arafat**
Bachelor's Student, Savonia University of Applied Sciences

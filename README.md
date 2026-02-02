# 🛰️ Space Network Simulation

A Python-based simulation of a satellite communication network. This project demonstrates Object-Oriented Programming (OOP) principles, robust error handling, routing algorithms, and encryption techniques.

## 🚀 Key Features

* **OOP Architecture:** Built using inheritance and polymorphism (Base classes `SpaceEntity`, `Packet` and subclasses `Satellite`, `RelayPacket`, `EncryptedPacket`).
* **Smart Routing:** Implements an algorithm (similar to Onion Routing) to automatically calculate paths between distant satellites.
* **Security:** Custom **XOR Encryption** implementation with unique keys per satellite to prevent unauthorized interception.
* **Realistic Space Conditions:** Simulates real-world challenges like packet loss, data corruption, temporary interference, and range limitations.
* **Robust Error Handling:** Automatic retry mechanisms and custom exception management.

## 🛠️ How to Run

1. Clone the repository.
2. Run the simulation:
   ```bash
   python space_network.py
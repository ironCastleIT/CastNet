# CastNet
**CastNet** is an AI-assisted hypersonic and visual acquisition and targeting system prototype built with Raspberry Pi 5, the Hailo-8 AI Accelerator, and sensor fusion. Inspired by the battlefield data fusion capabilities of Anduril’s Lattice OS, this system simulates a compact edge-based vision network designed for real-time detection and classification of intrusions, vehicles, people, drones, and birds of prey.

## Key Capabilities

- Real-time object detection using TensorFlow Lite or Hailo-8 NPU
- Visual classification via Raspberry Pi Camera Module 3
- Motion and range sensing using PIR and ultrasonic sensors
- Web dashboard with object detection feed + event logging
- Modular Python code for easy expansion into tactical use cases

---

## Hardware Stack

| Component | Role |
|----------|------|
| Raspberry Pi 5 (8GB) | Edge compute node |
| Hailo-8 AI Kit + M.2 HAT+ | Neural inference accelerator |
| Arducam Camera Module 3 | Vision system |
| PIR + Ultrasonic Sensors | Motion + range detection |
| GPIO Header Extender | Allows sensors and AI hat to coexist |
| (Optional) Xeon Servers | Backend for offloading, logging, training |

---

## Project Structure
```
castnet/
├── .gitignore
├── README.md
├── setup/
│   ├── install_os.md
│   ├── enable_hailo.md
│   └── wiring_guide.md
├── sensors/
│   ├── motion_pir.py
│   └── distance_ultrasonic.py
├── inference/
│   ├── tflite_vehicle_person.py
│   ├── labels.txt
│   └── yolov8_hailo_stub.py
├── dashboard/
│   └── app.py
├── tests/
│   └── dry_run_simulated_input.py
└── logs/
    └── events.csv
```

---

## Status

This project is in development and serves as a portfolio demonstration of applied computer vision, edge AI, and real-time sensor integration. Contributions or ideas welcome.

---

## License

MIT License. See `LICENSE` file for details.

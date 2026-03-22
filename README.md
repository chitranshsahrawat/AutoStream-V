# 🛡️ AutoStream-V | Autonomous Perception & Safety Framework

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/AI-YOLOv8-red.svg)](https://github.com/ultralytics/ultralytics)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B.svg)](https://streamlit.io/)

## 🚀 Project Overview
**AutoStream-V** is a modular ADAS (Advanced Driver Assistance System) validation framework designed for **Software-Defined Vehicles (SDVs)**. It simulates the core perception and decision-making pipeline of an autonomous vehicle using computer vision and geometric spatial awareness.

### 🌟 Key Engineering Highlights
- **Monocular Depth Estimation:** Implemented distance calculation using the Pinhole Camera Model, enabling 3D spatial awareness from a standard 2D dashcam feed.
- **Safety-Critical Decision Engine:** Real-time proximity monitoring with automated alert triggers (Red/Green state management).
- **Edge Performance Optimization:** Achieved **<15ms inference latency**, suitable for high-speed vehicular environments.
- **Telemetry Dashboard:** Full-stack monitoring tool for system health, latency tracking, and object analytics.

---

## 🛠️ System Architecture
The system follows a decoupled architecture, separating the **Perception Engine** from the **Visual Telemetry Layer**.



1. **Perception Layer:** YOLOv8 for multi-object tracking.
2. **Logic Layer:** Geometric estimation of proximity based on object pixel width.
3. **UI Layer:** Responsive Streamlit dashboard with custom CSS for operator situational awareness.

---

## 📐 The Mathematics of Proximity
The distance estimation is calculated using the following geometric constraint:

$$Distance (m) = \frac{RealWidth (m) \times FocalLength (px)}{PixelWidth (px)}$$

*Where:*
- **RealWidth:** Fixed at 1.8m (Average passenger vehicle).
- **FocalLength:** Calibrated for standard 1080p dashcam FOV.

---

## 👥 Contributors & Collaboration
This project is a collaborative engineering effort:

* **Chitransh Sahrawat** ([@chitranshsahrawat](https://github.com/chitranshsahrawat))  
    *Role:* Lead Developer, Perception Engine & Mathematical Modeling.
* **Aditya** ((https://github.com/adityatiwari8630))  
    *Role:* System Validation, UI/UX Design & Data Processing.

---

## 🧪 Future Scope
- Integration with **Rust-based** high-frequency telemetry logging.
- Multi-camera fusion logic for 360-degree situational awareness.
- CI/CD automation via GitHub Actions for safety-code validation.

---

## 🐳 Deployment (Dockerized)
Run this project on any OS using Docker:

```bash
# Build the image
docker build -t autostream-v .

# Run the container
docker run -p 8501:8501 autostream-v

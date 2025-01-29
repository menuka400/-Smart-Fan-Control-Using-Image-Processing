# 🌀 Smart Fan Control System

## 📌 Overview
The **Smart Fan Control System** is an AI-powered fan automation solution that detects **hand gestures** using a camera and adjusts the fan speed accordingly. It enhances convenience, energy efficiency, and a **touch-free experience**.

![Product Image](images/product.jpg)  
*Smart Fan in Action*

## 🎯 Features
✅ AI-powered gesture recognition (YOLO Model)  
✅ ESP32-based fan control over WiFi  
✅ Adjustable fan speed using **hand gestures**  
✅ Real-time image processing via ESP32-CAM  
✅ Automatic **buzzer and RGB LED** activation  

## 📸 Hand Gesture Commands
| Gesture | Action |
|---------|--------|
| ✋ Paper | Set fan speed to **75%** |
| ✊ Rock | **Turn off** the fan |
| ✌ Scissors | Reduce speed to **50%** |
| 👍 Thumbs Up | **Turn On** the fan |
| ☝ Up | Set fan speed to **100%** |

## 🛠️ Installation & Setup

### 1️⃣ **Clone Repository**
```sh
git clone https://github.com/your-repo/smart-fan.git
cd smart-fan
```

### 2️⃣ **Install Dependencies**
```sh
pip install -r requirements.txt
```

### 3️⃣ **Run the Application**
```sh
python main.py
```

## 🔧 Hardware & Components
- **ESP32 Devkit (30-pin)**
- **ESP32-CAM**
- **120mm 4-Pin PC Fan**
- **TB6612FNG Motor Driver**
- **Relay Module**
- **Bridgelux Genesis Epistar Chip 3W High Power LED**
- **Buzzer & RGB LED**

## 📷 Demo Images
![Hand Gesture Demo](images/gesture-demo.jpg)  
*Gesture-based Fan Control*

![Product Poster](images/poster.jpg)  
*Promotional Poster*

## 📜 License
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---
### ⭐ *Star this repository if you like our project!* ⭐

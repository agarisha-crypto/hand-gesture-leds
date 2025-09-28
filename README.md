# hand-gesture-leds
“Prototype: Hand gesture recognition controlling LEDs using Python + Arduino”
# Hand Gesture Controlled LEDs

This is a **prototype project** connecting computer vision with Arduino hardware to control LEDs using hand gestures.  

The system detects the number of fingers shown to a webcam and lights up the corresponding number of LEDs in real time.  

---

## 🔍 Key Features
- Real-time finger counting using **MediaPipe + OpenCV**  
- Serial communication between Python and Arduino  
- Scalable logic for future extensions (motors, relays, robotics, etc.)  

---

## 🛠️ Tools & Components
- **Software:** Python, OpenCV, MediaPipe, PySerial, Arduino IDE  
- **Hardware:** Arduino UNO, LEDs, resistors, breadboard, jumper wires  

---

## ⚙️ System Workflow
1. Webcam captures live video.  
2. MediaPipe detects hand landmarks and counts extended fingers.  
3. Python sends the count to Arduino via serial communication.  
4. Arduino lights up the corresponding number of LEDs.  

---

## 🎥 Demo
[▶️ Watch the Demo Video](<https://github.com/agarisha-crypto/hand-gesture-leds/blob/main/demo-video.mp4>)

---

## 📚 Learning in Progress
This project is a **work-in-progress prototype**.  
- Learning how AI-based gesture recognition works  
- Integrating Python with Arduino hardware  
- Debugging real-world issues like lighting and serial communication delays  

---

## 🌱 Future Improvements
- Custom gesture recognition (e.g., thumbs up, OK sign)  
- Extending outputs from LEDs to robotic applications  
- Optimizing performance and reliability  

---



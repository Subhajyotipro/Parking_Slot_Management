Smart Parking Lot Management System (Python)
A menu-driven Python application that simulates a real-time parking lot management system similar to malls and airports.
The system handles automatic slot allocation, time-based billing, VIP priority parking, and daily revenue reporting.
📌 Project Overview
This project is designed using pure Python and demonstrates how real-world parking systems manage:
Vehicle entry and exit
Parking slot allocation
Time tracking using datetime
Duration-based billing
VIP reserved slots with priority entry
Daily revenue summary
It is ideal for college mini-projects, lab exams, and viva presentations.
✨ Features
✅ Core Features
Automatic parking slot allocation
Real-time entry & exit timestamp tracking
Duration-based billing system
Vehicle exit processing
Slot availability update
Daily revenue report
Menu-driven CLI interface
Input validation & error handling
⭐ Premium Add-Ons Implemented
Variable Pricing Model
First 2 hours → fixed charge
Additional hours → per-hour billing
VIP Reserved Slots
Dedicated VIP parking slots
VIP vehicles get priority entry
Normal vehicles cannot occupy VIP slots
Vehicle Type-Based Pricing
Bike, Car, EV, Heavy, VIP
🏗️ System Architecture
Slot Manager
     ↓
Vehicle Entry
     ↓
Time Logger (datetime)
     ↓
Billing Engine
     ↓
Vehicle Exit
     ↓
Revenue Recorder
🛠️ Technologies Used
Language: Python 3
Modules:
datetime – time tracking
math – billing calculation
Data Structures:
Dictionary (slot management)
⚙️ Slot & Pricing Configuration
Parking Slots
Total slots: 5
VIP slots: Slot 1 & Slot 2
Pricing (per hour after 2 hours)
Vehicle Type	Rate (₹/hour)
Bike	20
Car	50
EV	40
Heavy	80
VIP	60
📋 Menu Options
Vehicle Entry
Vehicle Exit
Show Parking Status
Daily Revenue Report
Exit System

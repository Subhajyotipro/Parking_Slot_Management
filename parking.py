import datetime
import math

# -------------------------------
# STEP 1: INITIAL SETUP
# -------------------------------

TOTAL_SLOTS = 10
VIP_SLOTS = [1, 2]   # Premium Add-on: VIP reserved slots

parking_slots = {i: None for i in range(1, TOTAL_SLOTS + 1)}

total_revenue = 0
total_vehicles = 0

PRICE_PER_HOUR = {
    "bike": 20,
    "car": 50,
    "ev": 40,
    "heavy": 80,
    "vip": 60
}

# -------------------------------
# STEP 2: VEHICLE ENTRY
# -------------------------------

def vehicle_entry():
    global total_vehicles

    vehicle_no = input("Enter Vehicle Number: ")
    vehicle_type = input("Enter Vehicle Type (bike/car/ev/heavy/vip): ").lower()

    if vehicle_type not in PRICE_PER_HOUR:
        print("Invalid vehicle type!")
        return

    entry_time = datetime.datetime.now()

    # Premium Add-on: VIP Priority Entry
    if vehicle_type == "vip":
        for slot in VIP_SLOTS:
            if parking_slots[slot] is None:
                parking_slots[slot] = {
                    "vehicle_no": vehicle_no,
                    "vehicle_type": vehicle_type,
                    "entry_time": entry_time
                }
                total_vehicles += 1
                print(f"VIP Vehicle parked at VIP Slot {slot}")
                print("Entry Time:", entry_time)
                return

    # Normal slot allocation (skip VIP slots)
    for slot in parking_slots:
        if slot in VIP_SLOTS:
            continue

        if parking_slots[slot] is None:
            parking_slots[slot] = {
                "vehicle_no": vehicle_no,
                "vehicle_type": vehicle_type,
                "entry_time": entry_time
            }
            total_vehicles += 1
            print(f"Vehicle parked at Slot {slot}")
            print("Entry Time:", entry_time)
            return

    print("Parking Full! No slots available.")

# -------------------------------
# STEP 3: VARIABLE PRICING BILLING
# -------------------------------

def calculate_bill(entry_time, vehicle_type):
    exit_time = datetime.datetime.now()
    hours = math.ceil((exit_time - entry_time).total_seconds() / 3600)

    # Premium Add-on: Variable pricing model
    if hours <= 2:
        bill = 100
    else:
        bill = 100 + (hours - 2) * PRICE_PER_HOUR[vehicle_type]

    return bill, exit_time, hours

# -------------------------------
# STEP 4: VEHICLE EXIT
# -------------------------------

def vehicle_exit():
    global total_revenue

    slot = int(input("Enter Slot Number: "))

    if slot not in parking_slots:
        print("Invalid slot number!")
        return

    if parking_slots[slot] is None:
        print("Slot already empty!")
        return

    vehicle = parking_slots[slot]

    bill, exit_time, hours = calculate_bill(
        vehicle["entry_time"],
        vehicle["vehicle_type"]
    )

    print("\n--- BILL DETAILS ---")
    print("Vehicle Number:", vehicle["vehicle_no"])
    print("Vehicle Type:", vehicle["vehicle_type"])
    print("Total Hours:", hours)
    print("Amount to Pay: ₹", bill)
    print("Exit Time:", exit_time)

    total_revenue += bill
    parking_slots[slot] = None
    print("Vehicle exited successfully.\n")

# -------------------------------
# STEP 5: PARKING STATUS
# -------------------------------

def show_status():
    print("\n--- PARKING STATUS ---")
    for slot, details in parking_slots.items():
        if details is None:
            print(f"Slot {slot}: Empty")
        else:
            print(f"Slot {slot}: Occupied by {details['vehicle_no']}")

# -------------------------------
# STEP 6: DAILY REPORT
# -------------------------------

def daily_report():
    occupied = sum(1 for v in parking_slots.values() if v is not None)
    free = TOTAL_SLOTS - occupied

    print("\n--- DAILY REPORT ---")
    print("Total Vehicles Parked:", total_vehicles)
    print("Total Revenue Collected: ₹", total_revenue)
    print("Occupied Slots:", occupied)
    print("Free Slots:", free)

# -------------------------------
# STEP 7: MENU SYSTEM
# -------------------------------

def main():
    while True:
        print("\nSMART PARKING LOT MANAGEMENT SYSTEM")
        print("1. Vehicle Entry")
        print("2. Vehicle Exit")
        print("3. Show Parking Status")
        print("4. Daily Revenue Report")
        print("5. Exit System")

        choice = input("Enter your choice: ")

        if choice == "1":
            vehicle_entry()
        elif choice == "2":
            vehicle_exit()
        elif choice == "3":
            show_status()
        elif choice == "4":
            daily_report()
        elif choice == "5":
            print("System Closed. Thank You!")
            break
        else:
            print("Invalid choice!")

main()

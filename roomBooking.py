slots = list(map(int, input("Enter the booked slots: ").split()))
time_slot=input("Enter the Requested time slot:")
print("Slot is available" if time_slot not in slots else "Slot is not available")
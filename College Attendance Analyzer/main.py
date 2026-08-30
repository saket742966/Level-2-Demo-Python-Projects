total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))
medical = input("Do you have a valid medical certificate? (yes/no): ").lower()

attendance = (attended_classes / total_classes) * 100

print(f"Attendance: {attendance:.2f}%")

if attendance >= 75:
    print("Eligible for examination")

elif 65 <= attendance < 75 and medical == "yes":
    print("Eligible for examination (Medical Certificate)")

elif attendance >= 60:
    print("Warning")

else:
    print("Not eligible")
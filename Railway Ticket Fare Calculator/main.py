def calculate_fare(distance, age):
    if distance <= 0:
        raise ValueError("Distance must be greater than 0 km.")
    if age < 0:
        raise ValueError("Age cannot be negative.")

    if distance <= 100:
        rate = 2.0
    elif distance <= 300:
        rate = 1.5
    elif distance <= 500:
        rate = 1.2
    else:
        rate = 1.0

    fare = distance * rate

    if age < 12:
        fare *= 0.5
    elif age >= 60:
        fare *= 0.6

    return round(fare, 2)


try:
    distance = float(input("Enter distance in km: "))
    age = int(input("Enter age: "))

    if age <= 0:
        raise ValueError("Age must be positive.")

    final_fare = calculate_fare(distance, age)
    print(f"Final ticket fare: ₹{final_fare:.2f}")

except ValueError as e:
    print(f"Invalid input: {e}")
except Exception:
    print("Invalid input. Please enter a valid number for distance and age.")

regular_ticket = 150
permium_ticket = 250
vip_ticket = 400

print("\n" + " " * 6 + "Choose Ticket Type")
print("1. Regular Ticket - ₹150")
print("2. Premium Ticket - ₹250")
print("3. VIP Ticket - ₹400")
ticket_choice = int(input("Enter Choice 1-3 : "))

total_tickets = int(input("Quantity of tickets: "))

age = int(input("Please enter your age: "))

if ticket_choice == 1:
    ticket_price = 150

if ticket_choice == 2:
    ticket_price = 250

if ticket_choice == 3:
    ticket_price = 400
    
grand_total = ticket_price * total_tickets
    
if age < 5 :
    grand_total *= 0

if age < 12 :
    grand_total *= 0.5
    
if age > 12 :
    grand_total *= 1
    

if total_tickets > 5 :
    grand_total *= 0.90

print(f"Your order total for {total_tickets} tickets is {grand_total:.2f}")

# Input: number of calls made
calls = int(input("Enter the number of calls made: "))

# Base charges
bill = 200  # Minimum Rs. 200 for upto 100 calls

# Calculate additional charges based on the number of calls
if calls > 100:
    # Next 50 calls (100-150)
    extra_calls_1 = min(50, calls - 100)
    bill += extra_calls_1 * 0.60

if calls > 150:
    # Next 50 calls (150-200)
    extra_calls_2 = min(50, calls - 150)
    bill += extra_calls_2 * 0.50

if calls > 200:
    # Calls beyond 200
    extra_calls_3 = calls - 200
    bill += extra_calls_3 * 0.40

# Output the final bill
print(f"Total telephone bill for {calls} calls is: Rs. {bill:.2f}")
# Samples of Operators
# Arithmetic Operators
print("Addition: ", 7 + 2)              # 9
print("Subtraction: ", 7 - 2)           # 5
print("Multiplication: ", 7 * 2)        # 14
print("Division: ", 7 / 2)              # 3.5
print("Modulus: ", 7 % 2)               # 1
print("Exponentiation: ", 7 ** 2)       # 49
print("Floor Division: ", 7 // 2)       # 3

# Comparison (Relational) Operators
print("Equal: ", 7 == 2)                # False
print("Not Equal: ", 7 != 2)            # True
print("Greater Than: ", 7 > 2)          # True
print("Less Than: ", 7 < 2)             # False
print("Greater Than or Equal To: ", 7 >= 2)  # True
print("Less Than or Equal To: ", 7 <= 2)     # False

# Assignment Operators
x = 20
x += 6
print("Add Assignment: ", x)             # 26
x -= 4
print("Subtract Assignment: ", x)        # 22
x *= 3
print("Multiply Assignment: ", x)        # 66
x /= 6
print("Divide Assignment: ", x)          # 11.0
x //= 2
print("Floor Divide Assignment: ", x)    # 5.0
x %= 3
print("Modulus Assignment: ", x)         # 2.0
x **= 4
print("Exponent Assignment: ", x)        # 16.0

# Logical Operators
print("Logical AND: ", True and True)    # True
print("Logical OR: ", False or False)    # False
print("Logical NOT: ", not False)        # True

# Bitwise Operators (12 = 1100, 10 = 1010)
print("Bitwise AND: ", 12 & 10)          # 8
print("Bitwise OR: ", 12 | 10)           # 14
print("Bitwise XOR: ", 12 ^ 10)          # 6
print("Bitwise NOT: ", ~12)              # -13

# Left shift — multiply by powers of 2
print("Left Shift 1: ", 3 << 1)          # 6  (3 × 2)
print("Left Shift 2: ", 3 << 3)          # 24 (3 × 8)

# Right shift — divide by powers of 2
print("Right Shift 1: ", 48 >> 1)        # 24 (48 ÷ 2)
print("Right Shift 2: ", 48 >> 3)        # 6  (48 ÷ 8)

# Membership Operators
print("Membership: ", 15 in [5, 10, 15, 20, 25])         # True
print("Not Membership: ", 12 not in [5, 10, 15, 20, 25]) # True

# Identity Operators
a = [4, 5, 6]
b = a
c = [4, 5, 6]
print("Identity: ", a is b)              # True
print("Non-Identity: ", a is not c)      # True

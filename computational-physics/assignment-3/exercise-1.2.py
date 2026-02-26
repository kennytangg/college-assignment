def decimal_to_binary(num, precision=17):
    if num == 0:
        return "0"
    
    # Handle negative numbers
    sign = "-" if num < 0 else ""
    num = abs(num)
    
    # Integer part
    integer_part = int(num)
    binary_int = "0"
    if integer_part > 0:
        binary_int = ""
        temp = integer_part
        while temp > 0:
            binary_int = str(temp % 2) + binary_int
            temp //= 2
    
    # Fractional part  
    fractional_part = num - integer_part
    binary_frac = ""
    if fractional_part > 0:
        for _ in range(precision):
            if fractional_part == 0:
                break
            fractional_part *= 2
            bit = int(fractional_part)
            binary_frac += str(bit)
            fractional_part -= bit
    
    # Combine
    if binary_frac:
        return f"{sign}{binary_int}.{binary_frac}"
    return f"{sign}{binary_int}"

# Interactive converter
print("Decimal to Binary Converter")
print("=" * 30)

while True:
    user_input = input("\nEnter decimal number (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        break
    
    try:
        num = float(user_input)
        result = decimal_to_binary(num)
        print(f"Binary: {result}")
    except ValueError:
        print("Enter valid number or 'q'")
    except KeyboardInterrupt:
        break

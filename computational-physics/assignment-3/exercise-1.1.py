def decimal_to_binary(num, precision=17):
    # Get integer and fractional parts
    integer_part = int(num)
    fractional_part = num - integer_part
    
    # Convert integer part to binary
    if integer_part == 0:
        integer_binary = "0"
    else:
        integer_binary = ""
        temp = integer_part
        while temp > 0:
            integer_binary = str(temp % 2) + integer_binary
            temp = temp // 2
    
    # Convert fractional part to binary
    fractional_binary = ""
    for _ in range(precision):
        if fractional_part == 0:
            break
        fractional_part *= 2
        bit = int(fractional_part)
        fractional_binary += str(bit)
        fractional_part -= bit
    
    # Combine parts
    if fractional_binary:
        return integer_binary + "." + fractional_binary
    return integer_binary

# Results
print("1. 20.25 =", decimal_to_binary(20.25))
print("\n2. 0.3   =", decimal_to_binary(0.3))
print("\n3. Each 0.1 =", decimal_to_binary(0.1))
print("   Sum =", decimal_to_binary(0.1+0.1+0.1))

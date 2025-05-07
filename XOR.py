input_string = "HelloWorld"

for char in input_string:
    ascii_val = ord(char)
    and_result = ascii_val & 127
    xor_result = ascii_val ^ 127
    
    print(f"Character: {char}")
    print(f"ASCII value: {ascii_val}")
    print(f"Result of AND with 127: {and_result}")
    print(f"Result of XOR with 127: {xor_result}")
    print("-" * 40)

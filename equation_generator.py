"""
equation_generator.py

This module generates random math equations for the Nerdle game.
It creates valid equations in the format: number operator number = result
For example: 12+34=46 or 8*7=56
"""

########################################
# TODO: Import the appropriate modules #
########################################

###########################################
# TODO: Implement the following functions #
###########################################

def generate_numbers_for_addition():
    while True:
        A = random.randint(10, 89) # pyright: ignore[reportUndefinedVariable]
        b_max = 99 - A
        if b_max < 10:
            continue
        B = random.randint(10, b_max) # pyright: ignore[reportUndefinedVariable]
        C = A + B
        if 10 <= C <= 99:
            return (A, B, C)

def generate_numbers_for_subtraction():
     while True:
        C = random.randint(10, 89) # pyright: ignore[reportUndefinedVariable]
        b_max =99 - C
        if b_max < 10:
            continue
        B = random.randint(10, b_max) # pyright: ignore[reportUndefinedVariable]
        A = B + C
        if 10 <= A <= 99:
            return (A, B, C)

def generate_numbers_for_multiplication():
    while True:
        A = random.randint(2,9) # pyright: ignore[reportUndefinedVariable]
        b_min = (100 + A - 1) // A
        if b_min < 10:
            b_min = 10
        if b_min > 99:
            continue
        B = random.randint(b_min, 99) # pyright: ignore[reportUndefinedVariable]
        C = A * B
        if 100 <= C <= 999:
            return (A, B, C)

def generate_numbers_for_division():
    while True:
        Q = random.randint(2, 9)   # pyright: ignore[reportUndefinedVariable]
        d_min = (100 + Q - 1) // Q  
        if d_min < 10:
            d_min = 10
        if d_min > 99:
            continue
        D = random.randint(d_min, 99)   # pyright: ignore[reportUndefinedVariable]
        N = D * Q  
        if 100 <= N <= 999:
            return (N, D, Q)
    
################################################################################
#  DO NOT EDIT BELOW THIS LINE, THESE FUNCTIONS ARE ALREADY COMPLETED FOR YOU  #
################################################################################

def generate_equation():
    """
    Generate a random math equation for the Nerdle game.
    
    Returns:
        str: A string representing a math equation (exactly 8 characters)
        
    Example return values:
        "12+34=46"
        "56-23=33" 
        "9*12=108" (Wait, this is 8 chars! 9*12=108)
        "84/4=21 " (This is 7 chars, need to pad or adjust)
    
    The equation will always be exactly 8 characters long and mathematically correct.
    """
    # Choose a random operation
    operations = ['+', '-', '*', '/']
    operation = random.choice(operations) # pyright: ignore[reportUndefinedVariable]
    
    # Generate numbers based on the operation
    if operation == '+':
        num1, num2, result = generate_numbers_for_addition()
        equation = f"{num1}+{num2}={result}"
    elif operation == '-':
        num1, num2, result = generate_numbers_for_subtraction()
        equation = f"{num1}-{num2}={result}"
    elif operation == '*':
        num1, num2, result = generate_numbers_for_multiplication()
        equation = f"{num1}*{num2}={result}"
    else:  # operation == '/'
        num1, num2, result = generate_numbers_for_division()
        equation = f"{num1}/{num2}={result}"
    
    # Ensure the equation is exactly 8 characters
    # If it's 7 characters, we might need to try again or adjust
    if len(equation) != 8:
        # For now, let's try again with a different operation
        return generate_equation()
    
    return equation

def validate_equation(equation):
    """
    Check if a given equation string is mathematically correct.
    
    Args:
        equation (str): The equation to validate (e.g., "12+34=46")
        
    Returns:
        bool: True if the equation is mathematically correct, False otherwise
        
    Example:
        validate_equation("12+34=46") returns True
        validate_equation("12+34=50") returns False
    """
    # Check if input is a string
    if not isinstance(equation, str):
        return False
        
    # Check if equation has the right format and length
    if len(equation) != 8:
        return False
    
    # Check if equation contains an equals sign
    if '=' not in equation:
        return False
    
    try:
        # Split the equation at the equals sign
        left_side, right_side = equation.split('=')
        
        # The right side should be the result
        expected_result = int(right_side)
        
        # Evaluate the left side of the equation
        # We need to be careful about the operation
        if '+' in left_side:
            parts = left_side.split('+')
            if len(parts) == 2:
                actual_result = int(parts[0]) + int(parts[1])
            else:
                return False
        elif '-' in left_side:
            parts = left_side.split('-')
            if len(parts) == 2:
                actual_result = int(parts[0]) - int(parts[1])
            else:
                return False
        elif '*' in left_side:
            parts = left_side.split('*')
            if len(parts) == 2:
                actual_result = int(parts[0]) * int(parts[1])
            else:
                return False
        elif '/' in left_side:
            parts = left_side.split('/')
            if len(parts) == 2:
                # Check for division by zero
                if int(parts[1]) == 0:
                    return False
                # Check if division is exact (no remainder)
                if int(parts[0]) % int(parts[1]) != 0:
                    return False
                actual_result = int(parts[0]) // int(parts[1])
            else:
                return False
        else:
            return False
        
        # Check if the calculated result matches the given result
        return actual_result == expected_result
        
    except ValueError:
        # If we can't convert strings to integers, the equation is invalid
        return False
    except ZeroDivisionError:
        # Division by zero is invalid
        return False
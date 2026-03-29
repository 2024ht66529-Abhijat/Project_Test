def calculate_calories(weight: int, program: str) -> int:
    """
    Core business logic for calorie calculation.
    This file MUST contain no Flask code.
    """

    program_factors = {
        "FL": 22,   # Fat Loss
        "MG": 35,   # Muscle Gain
        "BG": 26    # Beginner
    }

    program = program.upper()

    if weight <= 0:
        raise ValueError("Weight must be a positive number")

    if program not in program_factors:
        raise ValueError("Invalid program code")

    return weight * program_factors[program]
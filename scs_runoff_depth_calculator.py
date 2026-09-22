def calculate_runoff(cn, rainfall, amc):
    """
    Calculate runoff depth using the SCS Curve Number method.
    
    Args:
        cn (int): Curve Number (30-100)
        rainfall (float): Total rainfall depth in inches
        amc (str): Antecedent Moisture Condition ('AMC II (Average)', 'AMC I (Dry)', 'AMC III (Wet)')
    
    Returns:
        dict: Dictionary containing calculated values
    """
    # Validate inputs
    if not (30 <= cn <= 100):
        raise ValueError("Curve Number must be between 30 and 100")
    if rainfall < 0:
        raise ValueError("Rainfall depth cannot be negative")
    if amc not in ['AMC II (Average)', 'AMC I (Dry)', 'AMC III (Wet)']:
        raise ValueError("Invalid AMC value")

    # Adjust CN based on AMC if not AMC II
    if amc == 'AMC I (Dry)':
        adjusted_cn = cn / (2.281 - 0.01281 * cn)
    elif amc == 'AMC III (Wet)':
        adjusted_cn = cn / (0.427 + 0.00573 * cn)
    else:  # AMC II (Average)
        adjusted_cn = cn
    
    # Round to nearest integer
    adjusted_cn = round(adjusted_cn)
    
    # Ensure adjusted CN is within valid range
    adjusted_cn = max(30, min(100, adjusted_cn))
    
    # Calculate potential maximum retention S (inches)
    s_in = (1000 / adjusted_cn) - 10
    
    # Calculate initial abstraction Ia (inches)
    ia_in = 0.2 * s_in
    
    # Calculate direct runoff Q (inches)
    if rainfall <= ia_in:
        q_in = 0.0
    else:
        q_in = ((rainfall - ia_in) ** 2) / (rainfall + 0.8 * s_in)
    
    # Convert runoff to mm (1 inch = 25.4 mm)
    q_mm = q_in * 25.4
    
    # Calculate runoff ratio as percentage
    if rainfall > 0:
        runoff_ratio_percent = (q_in / rainfall) * 100
    else:
        runoff_ratio_percent = 0.0
    
    return {
        'adjusted_cn': adjusted_cn,
        's_in': s_in,
        'ia_in': ia_in,
        'q_in': q_in,
        'q_mm': q_mm,
        'runoff_ratio_percent': runoff_ratio_percent
    }

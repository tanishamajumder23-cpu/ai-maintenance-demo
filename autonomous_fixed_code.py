def calculate_discount(amount: float, discount_type: int) -> float:
    """
    Calculate the final amount after applying discount.
    
    Args:
        amount: Base amount to calculate discount on
        discount_type: Type of discount (1=18%, 2=10%, else=0% / no discount)
        
    Returns:
        Final amount after discount is applied
        
    Raises:
        TypeError: If amount is not numeric
    """
    if not isinstance(amount, (int, float)):
        raise TypeError(f"amount must be numeric, got {type(amount).__name__}")
    
    if discount_type == 1:
        return amount * 0.82  # Apply 18% discount
    elif discount_type == 2:
        return amount * 0.90  # Apply 10% discount
    else:
        return amount  # No discount for other types


if __name__ == "__main__":
    try:
        result_1 = calculate_discount(150, 1)
        print(f"150 with 18% discount: {result_1}")
        
        result_2 = calculate_discount(200, 2)
        print(f"200 with 10% discount: {result_2}")
        
        result_3 = calculate_discount(30, 3)
        print(f"30 with no discount: {result_3}")
    except Exception as e:
        print(f"Error: {e}")

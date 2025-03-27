def calculate_discount(price, discount_percent):
    """
    A function that calculates the final price after applying a discount.
    If discount is 20% or higher, the function applies the discount; otherwise it returns original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    return price

def main():
    try:
        # Get input from user
        price = float(input("Enter the original price of the item: "))
        discount_percent = float(input("Enter the discount percentage: "))
        
        # Calculate final price
        final_price = calculate_discount(price, discount_percent)
        
        # Print results
        if discount_percent >= 20:
            print(f"\nDiscount of {discount_percent}% applied!")
            print(f"Final price after discount: ${final_price:.2f}")
        else:
            print(f"\nNo discount applied")
            print(f"Final price: ${final_price:.2f}")
    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")
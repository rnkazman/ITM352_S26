def isLeapYear(year):
    """
    Determine if a year is a leap year using if-statements.
    
    Returns:
        "Leap year" - if the year is a leap year
        "Not a leap year" - if the year is not a leap year
    
    Logic using if-statements:
    1. If divisible by 400 → Leap year
    2. Else if divisible by 100 → Not a leap year
    3. Else if divisible by 4 → Leap year
    4. Else → Not a leap year
    """
    if year % 400 == 0:
        return "Leap year"
    elif year % 100 == 0:
        return "Not a leap year"
    elif year % 4 == 0:
        return "Leap year"
    else:
        return "Not a leap year"


def is_leap_year(year):
    """
    Determine if a year is a leap year using the conditional expression:
    (Condition A AND Condition B) OR Condition C
    
    Logic:
    - Condition A: year % 4 == 0 (divisible by 4)
    - Condition B: year % 100 != 0 (NOT divisible by 100)
    - Condition C: year % 400 == 0 (divisible by 400)
    
    Expression: (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    
    Parenthetical grouping is CRITICAL:
    - The outer parentheses around (year % 4 == 0 and year % 100 != 0) 
      ensure we evaluate the AND operation first as a single unit
    - Then the OR operator combines this result with the divisibility-by-400 check
    - Without explicit parentheses, AND has higher precedence than OR in Python,
      so the parentheses make the intent crystal clear and prevent evaluation errors
    """
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def test_leap_years():
    """
    Test the leap year function with various test cases.
    
    Test with:
    1. Your birth year
    2. The closest leap year to your birth year
    3. If your birth year is a leap year, use your birth year + 1 as the non-leap year
    
    Some common leap years: 1996, 2000, 2004, 2020, 2024
    Some common non-leap years: 1900, 1997, 1998, 2001, 2025
    """
    
    # Example test years - replace these with your own birth year
    birth_year = 2000  # Change this to your actual birth year
    
    # Test cases covering different scenarios
    test_cases = [
        # Regular leap years (divisible by 4, not by 100)
        (1996, True, "Regular leap year (divisible by 4, not 100)"),
        (2004, True, "Regular leap year (divisible by 4, not 100)"),
        (2024, True, "Regular leap year (divisible by 4, not 100)"),
        
        # Century years - only leap if divisible by 400
        (1900, False, "Century year not divisible by 400"),
        (2000, True, "Century year divisible by 400"),
        (2100, False, "Century year not divisible by 400"),
        
        # Non-leap years
        (1997, False, "Not divisible by 4"),
        (2001, False, "Not divisible by 4"),
        (2025, False, "Not divisible by 4"),
    ]
    
    print("=" * 70)
    print("LEAP YEAR CONDITIONAL LOGIC TEST")
    print("=" * 70)
    print(f"\nConditional Expression: (year % 4 == 0 and year % 100 != 0) or year % 400 == 0")
    print("\nTest Results:")
    print("-" * 70)
    
    all_passed = True
    for year, expected, description in test_cases:
        result = is_leap_year(year)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result != expected:
            all_passed = False
        print(f"{status} | Year {year}: {result:5} | {description}")
    
    print("-" * 70)
    
    # Test with birth year examples
    print("\nBIRTH YEAR EXAMPLE TESTS:")
    print("-" * 70)
    
    # Example: If you were born in 2000
    test_birth = 2000
    is_birth_leap = is_leap_year(test_birth)
    
    if is_birth_leap:
        test_non_leap = test_birth + 1
        print(f"Birth year {test_birth}: LEAP YEAR ✓")
        print(f"Non-leap year test: {test_non_leap}: {is_leap_year(test_non_leap)}")
    else:
        # Find closest leap year before birth year
        test_non_leap = test_birth
        test_leap = test_birth - (test_birth % 4)  # Find previous leap year
        print(f"Birth year {test_birth}: NOT a leap year")
        print(f"Closest leap year (before): {test_leap}: {is_leap_year(test_leap)}")
    
    print("-" * 70)
    
    if all_passed:
        print("\n✓ All tests passed! The conditional logic is working correctly.")
    else:
        print("\n✗ Some tests failed. Review the logic.")
    
    return all_passed


def test_isLeapYear():
    """
    Test the isLeapYear() function that uses if-statements.
    """
    test_cases = [
        # Regular leap years (divisible by 4, not by 100)
        (1996, "Leap year", "Regular leap year (divisible by 4, not 100)"),
        (2004, "Leap year", "Regular leap year (divisible by 4, not 100)"),
        (2024, "Leap year", "Regular leap year (divisible by 4, not 100)"),
        
        # Century years - only leap if divisible by 400
        (1900, "Not a leap year", "Century year not divisible by 400"),
        (2000, "Leap year", "Century year divisible by 400"),
        (2100, "Not a leap year", "Century year not divisible by 400"),
        
        # Non-leap years
        (1997, "Not a leap year", "Not divisible by 4"),
        (2001, "Not a leap year", "Not divisible by 4"),
        (2025, "Not a leap year", "Not divisible by 4"),
    ]
    
    print("\n" + "=" * 70)
    print("ISLEAPYEAR() - IF-STATEMENT VERSION TEST")
    print("=" * 70)
    print("\nTest Results:")
    print("-" * 70)
    
    all_passed = True
    for year, expected, description in test_cases:
        result = isLeapYear(year)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        if result != expected:
            all_passed = False
        print(f"{status} | Year {year}: {result:20} | {description}")
    
    print("-" * 70)
    
    if all_passed:
        print("\n✓ All tests passed! The if-statement version works correctly.")
    else:
        print("\n✗ Some tests failed. Review the logic.")
    
    return all_passed


# Run the tests
if __name__ == "__main__":
    test_leap_years()
    test_isLeapYear()

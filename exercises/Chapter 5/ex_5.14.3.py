

def is_triangle(a: int, b: int, c: int) -> bool:
    """
    function to check if 3 given sides form a triangle.
    
    Parameter
    ---------
    a:
        first side of the possible triangle
        
    b:
        second side of the possible triangle
        
    c:
        3rd side of the possible triangle
        
    Returns
    -------
    float:
        return True if the triangle is possible, else False
        
    Author
    ------
        chiv

    Date
    ----
        30-10-2024
    """

    return not a + b < c and not a + c < b and not b + c < a

def main():
    print(is_triangle(3, 4, 5))
    print(is_triangle(1, 1, 4))

    assert is_triangle(3, 4, 5) is True
    assert is_triangle(1, 1, 4) is False
    assert is_triangle(1, 2, 3) is True

if __name__ == "__main__":
    main()
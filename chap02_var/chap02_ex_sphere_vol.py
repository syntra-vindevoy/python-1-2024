import math


def sphere_val(*, r: float) -> float:
    """
    Calculate the volume of a sphere given its radius.

    Parameters
    ----------
    r : float
        The radius of the sphere. Must be a positive number.

    Returns
    -------
    float
        The volume of the sphere.

    Raises
    ------
    ValueError
        If the radius is not a positive number.

    Examples
    --------
    >>> sphere_val(r=5)
    523.5987755982989
    >>> sphere_val(r=2.5)
    65.44984694978736
    """
    if r <= 0:
        raise ValueError("The radius must be a positive number.")

    vol = (4 / 3) * math.pi * (r ** 3)
    return vol


# Example usage
try:
    print(f"The volume of the sphere is: {sphere_val(r=5)}")
except ValueError as e:
    print(e)
class TemperatureConverter:
    def __init__(self, temperature, unit='C'):
        """
        Initialize the TemperatureConverter object with an initial temperature and unit.
        Default unit is Celsius ('C').
        """
        self.temperature = temperature
        self.unit = unit

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        if unit.upper() in {'C', 'F'}:
            self.__unit = unit
        else:
            raise ValueError("Should be 'C' or 'F'")

    def convert(self):
        """
        Convert the temperature to the other unit and return it.
        """
        new_unit = 'F' if self.unit == 'C' else 'C'  # Determine the opposite unit
        return self._convert_to_unit(new_unit)

    def __call__(self):
        """
        Return the current temperature in the current unit.
        """
        return self.temperature

    def change_unit(self, new_unit):
        """
        Change the unit of the temperature to the specified new unit.
        """
        new_unit = new_unit.upper()  # Ensure the new unit is uppercase
        if new_unit not in ['C', 'F']:
            raise ValueError("Invalid unit. Choose 'C' for Celsius or 'F' for Fahrenheit.")

        if new_unit != self.unit:  # Only convert if the new unit is different
            self.temperature = self._convert_to_unit(new_unit)
            self.unit = new_unit

    def _convert_to_unit(self, target_unit):
        """
        Convert the temperature to the specified unit and return it.
        """
        if target_unit == 'C':
            return (self.temperature - 32) * 5 / 9  # Convert Fahrenheit to Celsius
        elif target_unit == 'F':
            return (self.temperature * 9 / 5) + 32  # Convert Celsius to Fahrenheit


# Example usage:
converter = TemperatureConverter(25, 'C')
print("Current temperature:", converter())
print("Temperature in Fahrenheit:", converter.convert())
converter.change_unit('F')
print("Current temperature:", converter())

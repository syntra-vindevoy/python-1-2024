class RunningAverage:
    def __init__(self):
        """
        Initialize the RunningAverage object with an empty list to store numbers.
        """
        self.numbers = []

    def add_number(self, number):
        """
        Add a number to the list of numbers.
        """
        self.numbers.append(number)

    def __call__(self):
        """
        Calculate and return the current running average of all numbers added so far.
        """
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

    def reset(self):
        """
        Clear the list of numbers and reset the running average to 0.
        """
        self.numbers = []


average = RunningAverage()
print("Current running average after initialization:", average())
for x in [3, 5, 12, 9, 1]:
    average.add_number(x)
    print("Current running average:", average())
average.reset()
print("average is reset: ", average())
for x in [3.1, 19.8, 3]:
    average.add_number(x)
    print("Current running average:", average())

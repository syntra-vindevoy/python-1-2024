from src.OO.employee import Employee


class Developer(Employee):
    raise_amt = 10.04

    # Correcting the constructor name from __int__ to __init__
    def __init__(self, first, last, pay):
        super().__init__(first, last, pay)  # Correct usage of super() to initialize parent class
        self.prog_langs = []  # Initialize the prog_langs attribute as an empty list

    def add_prog_lang(self, prog_lang):
        self.prog_langs.append(prog_lang)

    def remove_prog_lang(self, prog_lang):
        # Adding a check before removing to prevent errors if the programming language does not exist
        if prog_lang in self.prog_langs:
            self.prog_langs.remove(prog_lang)
        else:
            print(f"{prog_lang} not found in programming languages.")

    def display_prog_lang(self):
        print("Programming Languages:")
        for prog in self.prog_langs:
            print(f" - {prog}")

    def __str__(self):
        return f"{super().__str__()}\nProgramming Languages: {', '.join(self.prog_langs)}"

    def __repr__(self):
        return f"Developer('{self.id} {self.first}', '{self.last}', {self.pay}, {self.prog_langs})"


if __name__ == "__main__":
    # Corrected initialization of the Developer instance
    dev_1 = Developer("Benoit", "Goethals", 23)

    dev_1.add_prog_lang("Python")
    dev_1.add_prog_lang("Java")
    dev_1.display_prog_lang()

    print(dev_1.pay)
    dev_1.apply_raise()
    print(dev_1.pay)

    print(dev_1)


def griddrawer_cross():
    print("+ " + 4 * "- " + "+ " + 4 * "- " + "+ ")

def griddrawer_lines():
    print("| " + 8 * " " + "| " + 8 * " " + "|")
    print("| " + 8 * " " + "| " + 8 * " " + "|")
    print("| " + 8 * " " + "| " + 8 * " " + "|")
    print("| " + 8 * " " + "| " + 8 * " " + "|")

def griddrawer():
    griddrawer_cross()
    griddrawer_lines()
    griddrawer_cross()
    griddrawer_lines()
    griddrawer_cross()

if __name__ == "__main__":
    griddrawer()
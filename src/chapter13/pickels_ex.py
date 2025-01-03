import pickle
import time


class PickelsFile:

    PICKLES_FILENAME :str= "PickelsFileSerial.txt"

    def __init__(self, filename="", students: dict[str, dict]=None, status=False, name="", age=0):
        self.__filename = filename
        self.__status=status
        self.__name=name
        self.__age=age
        self.__students=students
        self.__content = ""



    def read_file(self):
        with open(self.__filename, 'r',encoding='utf-8') as file:
            self.__content= file.read()




    def serialization(self):

        try:
            with open(self.PICKLES_FILENAME , 'wb') as file:
                pickle.dump(self, file)
        except (OSError, ValueError) as e:
            print(f"Error during file operation: {e}")
        except pickle.PickleError as e:
            print(f"Error during pickling: {e}")


    def deserialization(self):
        try:
            with open(self.PICKLES_FILENAME , 'rb') as file:
                loaded_object = pickle.load(file)
                self.__dict__.update(loaded_object.__dict__)
        except FileNotFoundError:
            print("File not found.")
        except EOFError:
            print("File is empty or corrupted.")
        except pickle.UnpicklingError:
            print("Error while loading the pickled data.")


    def copy(self):
        return PickelsFile(self.__filename,self.__students,self.__status,self.__name,self.__age)

    def __repr__(self):
        return f"File: {self.__filename}\nStatus: {self.__status}\nName: {self.__name}\nAge: {self.__age}\nStudents: {self.__students}"

    def __str__(self):
        return f"File: {self.__filename}\nStatus: {self.__status}\nName: {self.__name}\nAge: {self.__age}\nStudents: {self.__students}"

    def __eq__(self, other):
        if not isinstance(other, PickelsFile):
            return False
        return (
                self.__filename == other.__filename
                and self.__students == other.__students
                and self.__status == other.__status
                and self.__name == other.__name
                and self.__age == other.__age
                and self.__content == other.__content
        )

    def __hash__(self):
        return hash((self.__filename, frozenset(self.__students.items()), self.__status, self.__name, self.__age, self.__content))


if __name__ == "__main__":

    students_data = {

        'Student 1': {
            'Name': "Alice", 'Age': 10, 'Grade': 4,
        },
        'Student 2': {
            'Name': 'Bob', 'Age': 11, 'Grade': 5
        },
        'Student 3': {
            'Name': 'Elena', 'Age': 14, 'Grade': 8
        }
    }

    start = time.time()
    march = PickelsFile("AI.txt",students=students_data,status=True,name="Benoit",age=23)
    march.read_file()
    march.serialization()
    end = time.time()
    print(end - start)

    start = time.time()
    march2 = PickelsFile()
    march2.deserialization()
    end = time.time()
    print(end - start)


    assert march == march2
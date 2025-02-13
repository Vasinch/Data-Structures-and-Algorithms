import json
class Student:
    def __init__(self,std_id,name,gpa):
        self.__std_id = std_id
        self.__name = name
        self.__gpa = gpa
    def getid(self):
        return self.__std_id
    def getname(self):
        return self.__name
    def getgpa(self):
        return self.__gpa
    def print_details(self):
        print(f"ID: {self.__std_id}")
        print(f"Name: {self.__name}")
        print(f"GPA: {self.__gpa:.2f}")

def binary_search(data, name):
    low = 0
    high = len(data) - 1
    comparisons = 0

    while low <= high:
        mid = low + (high - low) // 2
        comparisons += 1

        mid_name = data[mid].getname()

        if mid_name == name:
            print(f"Found {name} at index {mid}")
            data[mid].print_details()
            print(f"Comparisons times: {comparisons}")
            return mid

        elif mid_name < name:
            low = mid + 1

        else:
            high = mid - 1

    print(f"{name} does not exists.")
    print(f"Comparisons times: {comparisons}")


if __name__ == "__main__":
    data_input = input()
    name_input = input()

    data = json.loads(data_input)
    data_list = [Student(item["id"], item["name"], item["gpa"]) for item in data]

    binary_search(data_list, name_input)
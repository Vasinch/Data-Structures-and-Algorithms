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

class ProbHash:
    def __init__(self,size):
        self.hash_table = [None] * size
        self.size = size

    def hash(self,key):
        return key%self.size

    def rehash(self,key):
        return (key + 1) % self.size

    def insert_data(self, std):
        key = self.hash(std.getid())
        start_key = key
        while self.hash_table[key] is not None:
            key = self.rehash(key)
            if key == start_key:
                print(f"The list is full. {std.getid()} could not be inserted.")
                return
        self.hash_table[key] = std
        print(f"Insert {std.getid()} at index {key}")
    
    def search_data(self, std_id):
        key = self.hash(std_id)
        start_key = key
        while self.hash_table[key] is not None:
            if self.hash_table[key].getid() == std_id:
                print(f"Found {std_id} at index {key}")
                return self.hash_table[key]
            key = self.rehash(key)
            if key == start_key:
                break
        print(f"{std_id} does not exist.")
        return None

def main():
    import json
    size = int(input())
    hashtable = ProbHash(size)
    while True:
        finish = input()
        if finish == "Done":
            break
        condition, data = finish.split(" = ")
        if condition == "I":
            std_in = json.loads(data)
            std = Student(std_in["ID"], std_in["Name"], std_in["GPA"])
            hashtable.insert_data(std)
        elif condition == "S":
            print("------")
            student = hashtable.search_data(int(data))
            if student is not None:
                student.print_details()
            print("------")
        else:
            print("Invalid Condition!")
main()
# self zorunlu değil ama class altında bir argüman almak zorunda
class Human:
    name = "name" #default
    #built-in
    #initialize
    def __init__(self, name):
        self.name = name
        print("Bir human instance üretildi")

    def __str__(self) -> str:
        return f"str fonksiyonundan dönen değer: {self.name}"

    def talk(self, sentence): 
        print(f"{self.name}: {sentence}")

    def walk(self):
        print(f"{self.name} is walking..")
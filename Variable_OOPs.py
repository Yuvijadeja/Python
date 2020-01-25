class Computer:
    # class variable
    # it can be changed by class it self e.g. Computer.hard_drive
    hard_drive = "1 TB"

    def __init__(self, cpu, ram):
        # instance variable
        # it can be changed by object it self e.g. com1.cpu
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config: ", self.cpu, self.ram, self.hard_drive)


com1 = Computer("A9", "6GB")
com1.config()

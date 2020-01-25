class Laptop:
    def code(self, ide):
        ide.execute()


class PyCharm:
    def execute(self):
        print("Compile")
        print("Run")


class VSCode:
    def execute(self):
        print("Spell Check")
        print("Compile")
        print("Run")


ide = VSCode()
lap1 = Laptop()
lap1.code(ide)

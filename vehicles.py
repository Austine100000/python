class vehicles:
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model

    def drive(self):
        raise NotImplementedError("child classes must implement ")


class Toyota(vehicles):
    def drive(self):
        return


class Nissan(vehicles):
    def drive(self):
        return


class mistubishi(vehicles):
    def drive(self):
        return


mistubishi = mistubishi("Mistubishi", "Fusso")

print(mistubishi.Brand)
print(mistubishi.Model)

Nissan = Nissan("Nissan", "X-Trail")
print(Nissan.Brand)
print(Nissan.Model)

Toyota = Toyota("Toyota", "corrola")
print(Toyota.Brand)
print(Toyota.Model)

from abc import ABC, abstractmethod

# 1. Interfaces de productos
class Chair(ABC):
    @abstractmethod
    def assemble(self):
        pass

class Sofa(ABC):
    @abstractmethod
    def recline(self):
        pass

class CoffeeTable(ABC):
    @abstractmethod
    def place_items(self):
        pass

# 2. Clases concretas

class ModernChair(Chair):
    def assemble(self):
        print("Assembling modern chair")

class VictorianChair(Chair):
    def assemble(self):
        print("Assembling victorian chair")

class RusticChair(Chair):
    def assemble(self):
        print("Assembling rustic chair")

class ModernSofa(Sofa):
    def recline(self):
        print("Reclining modern sofa")

class VictorianSofa(Sofa):
    def recline(self):
        print("Reclining victorian sofa")

class RusticSofa(Sofa):
    def recline(self):
        print("Reclining rustic sofa")

class ModernCoffeeTable(CoffeeTable):
    def place_items(self):
        print("Placing items on modern coffee table")

class VictorianCoffeeTable(CoffeeTable):
    def place_items(self):
        print("Placing items on victorian coffee table")

class RusticCoffeeTable(CoffeeTable):
    def place_items(self):
        print("Placing items on rustic coffee table")

# 3. Interfaz Abstract Factory

class FurnitureFactory(ABC):
    @abstractmethod
    def create_chair(self) -> Chair:
        pass

    @abstractmethod
    def create_sofa(self) -> Sofa:
        pass

    @abstractmethod
    def create_coffee_table(self) -> CoffeeTable:
        pass

# 4. Fábricas concretas

class ModernFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return ModernChair()
    
    def create_sofa(self) -> Sofa:
        return ModernSofa()
    
    def create_coffee_table(self) -> CoffeeTable:
        return ModernCoffeeTable()

class VictorianFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return VictorianChair()
    
    def create_sofa(self) -> Sofa:
        return VictorianSofa()
    
    def create_coffee_table(self) -> CoffeeTable:
        return VictorianCoffeeTable()

class RusticFurnitureFactory(FurnitureFactory):
    def create_chair(self) -> Chair:
        return RusticChair()
    
    def create_sofa(self) -> Sofa:
        return RusticSofa()
    
    def create_coffee_table(self) -> CoffeeTable:
        return RusticCoffeeTable()

# 5. Código cliente

def main(factory: FurnitureFactory):
    chair = factory.create_chair()
    sofa = factory.create_sofa()
    coffee_table = factory.create_coffee_table()

    chair.assemble()
    sofa.recline()
    coffee_table.place_items()

# Pruebas

print("Creating modern furniture:")
main(ModernFurnitureFactory())

print("\nCreating victorian furniture:")
main(VictorianFurnitureFactory())

print("\nCreating rustic furniture:")
main(RusticFurnitureFactory())

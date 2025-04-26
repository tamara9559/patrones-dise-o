public class RusticFurnitureFactory implements FurnitureFactory {
    @Override
    public Chair createChair() {
        return new RusticChair();
    }

    @Override
    public Sofa createSofa() {
        return new RusticSofa();
    }

    @Override
    public CoffeeTable createCoffeeTable() {
        return new RusticCoffeeTable();
    }
}


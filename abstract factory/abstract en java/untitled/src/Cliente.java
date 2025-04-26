public class Cliente {
    private Chair chair;
    private Sofa sofa;
    private CoffeeTable coffeeTable;

    public Cliente(FurnitureFactory factory) {
        this.chair = factory.createChair();
        this.sofa = factory.createSofa();
        this.coffeeTable = factory.createCoffeeTable();
    }

    public void someOperation() {
        this.chair.assemble();
        this.sofa.recline();
        this.coffeeTable.arrange();
    }
}


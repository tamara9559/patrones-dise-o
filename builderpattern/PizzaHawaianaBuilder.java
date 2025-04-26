package PizzeriaEjemplo;
// 3. ConcreteBuilder (implementa los pasos de construcción de la pizza hawaiana)
public class PizzaHawaianaBuilder implements PizzaBuilder {
    private Pizza pizza;

    public PizzaHawaianaBuilder() {
        pizza = new Pizza();  // Inicializamos el objeto Pizza
    }

    @Override
    public void buildMasa() {
        pizza.setMasa("Fina");
    }

    @Override
    public void buildTamaño() {
        pizza.setTamaño("Mediana");
    }

    @Override
    public void buildIngredientes() {
        pizza.setIngredientes("Jamon, Piña");
    }

    @Override
    public Pizza getPizza() {
        return pizza;
    }
}

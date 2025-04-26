package PizzeriaEjemplo;

public class PizzaPersonalizada implements PizzaBuilder {
    private Pizza pizza;
    private String masa;
    private String tamaño;
    private String ingredientes;

    public PizzaPersonalizada(String masa, String tamaño, String ingredientes) {
        this.masa = masa;
        this.tamaño = tamaño;
        this.ingredientes = ingredientes;
        this.pizza = new Pizza();
    }

    @Override
    public void buildMasa() {
        pizza.setMasa(masa);
    }

    @Override
    public void buildTamaño() {
        pizza.setTamaño(tamaño);
    }

    @Override
    public void buildIngredientes() {
        pizza.setIngredientes(ingredientes);
    }

    @Override
    public Pizza getPizza() {
        return pizza;
    }
}

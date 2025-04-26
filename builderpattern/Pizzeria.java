package PizzeriaEjemplo;
// 4. Director (opcional, organiza el proceso de construcción)
public class Pizzeria {
    private PizzaBuilder builder;

    public Pizzeria(PizzaBuilder builder) {
        this.builder = builder;
    }

    public Pizza hacerPizza() {
        builder.buildMasa();
        builder.buildTamaño();
        builder.buildIngredientes();
        return builder.getPizza();
    }
}

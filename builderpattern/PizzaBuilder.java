    package PizzeriaEjemplo;
    // 2. Interfaz Builder (los pasos para construir la Pizza)
    public interface PizzaBuilder {
        void buildMasa();
        void buildTamaño();
        void buildIngredientes();
        Pizza getPizza();  // Devuelve el objeto final
    }

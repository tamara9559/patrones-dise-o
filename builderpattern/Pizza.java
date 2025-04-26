package PizzeriaEjemplo;
//Product, el objeto final a construir
public class Pizza {
    private String masa;
    private String tamaño;
    private String ingredientes;

    // Setters
    public void setMasa(String masa) {
        this.masa = masa;
    }

    public void setTamaño(String tamaño) {
        this.tamaño = tamaño;
    }

    public void setIngredientes(String ingredientes) {
        this.ingredientes = ingredientes;
    }

    // Método para mostrar la pizza final
    public void mostrarPizza() {
        System.out.println("Pizza [Masa: " + masa + ", Tamaño: " + tamaño + ", Ingredientes: " + ingredientes + "]");
    }
}

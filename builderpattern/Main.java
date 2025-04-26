package PizzeriaEjemplo;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("=== Crear tu Pizza Personalizada ===");

        System.out.print("Elige el tipo de masa (Fina / Gruesa / Integral): ");
        String masa = scanner.nextLine();

        System.out.print("Elige el tamaño (Pequeña / Mediana / Grande): ");
        String tamaño = scanner.nextLine();

        System.out.print("Escribe los ingredientes separados por comas (ej: Queso, Tomate, Jamón): ");
        String ingredientes = scanner.nextLine();

        // Crear el builder personalizado con los datos ingresados
        PizzaBuilder builder = new PizzaPersonalizada(masa, tamaño, ingredientes);
        Pizzeria pizzeria = new Pizzeria(builder);
        Pizza miPizza = pizzeria.hacerPizza();

        System.out.println("\n🍕 Tu pizza personalizada:");
        miPizza.mostrarPizza();

        scanner.close();
    }
}

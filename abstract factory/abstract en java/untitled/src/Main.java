public class Main {
    public static void main(String[] args) {
        // Creando muebles modernos
        System.out.println("Creating modern furniture:");
        Cliente cliente1 = new Cliente(new ModernFurnitureFactory());
        cliente1.someOperation();

        // Creando muebles victorianos
        System.out.println("\nCreating victorian furniture:");
        Cliente cliente2 = new Cliente(new VictorianFurnitureFactory());
        cliente2.someOperation();

        // Creando muebles rústicos
        System.out.println("\nCreating rustic furniture:");
        Cliente cliente3 = new Cliente(new RusticFurnitureFactory());
        cliente3.someOperation();
    }
}

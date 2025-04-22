import java.util.Hashtable;
import java.util.Scanner;

/**
 * caso numero 2:
 Los empleados de una cierta compañía se representan en la base de datos de la compañía
 por su nombre, número de empleado y número de la seguridad social. Construir una
 estructura de tablas hash que permita acceder al registro de un empleado por cualquiera de
 estos tres datos.
 */
class Empleado {
    String nombre;
    int numeroEmpleado;
    String numeroSeguridadSocial;

    public Empleado(String nombre, int numeroEmpleado, String numeroSeguridadSocial) {
        this.nombre = nombre;
        this.numeroEmpleado = numeroEmpleado;
        this.numeroSeguridadSocial = numeroSeguridadSocial;
    }

    @Override
    public String toString() {
        return "Nombre: " + nombre + ", Número de Empleado: " + numeroEmpleado +
                ", NSS: " + numeroSeguridadSocial;
    }
}

/**
 * Clase principal que maneja la base de empleados con una sola tabla hash.
 */
public class BaseEmpleados {
    // Solo una tabla hash para todos los accesos
    static Hashtable<String, Empleado> tablaEmpleados = new Hashtable<>();

    /**
     * Agrega un nuevo empleado a la tabla hash con tres claves distintas.
     */
    public static void agregarEmpleado(Scanner sc) {
        System.out.println("\n--- Agregar nuevo empleado ---");

        System.out.print("Nombre: ");
        String nombre = sc.nextLine();

        System.out.print("Número de empleado: ");
        int numeroEmpleado = Integer.parseInt(sc.nextLine());

        System.out.print("Número de Seguridad Social: ");
        String nss = sc.nextLine();

        // Verifica si ya existe uno de los identificadores
        if (tablaEmpleados.containsKey("nombre:" + nombre) ||
                tablaEmpleados.containsKey("id:" + numeroEmpleado) ||
                tablaEmpleados.containsKey("nss:" + nss)) {
            System.out.println("Error: Ya existe un empleado con ese nombre, número o NSS.");
            return;
        }

        // Crear empleado y guardarlo bajo tres claves
        Empleado emp = new Empleado(nombre, numeroEmpleado, nss);

        tablaEmpleados.put("nombre:" + nombre, emp);
        tablaEmpleados.put("id:" + numeroEmpleado, emp);
        tablaEmpleados.put("nss:" + nss, emp);

        System.out.println("Empleado agregado correctamente.");
    }

    /**
     * Buscar empleado por nombre.
     */
    public static void buscarPorNombre(Scanner sc) {
        System.out.print("Nombre del empleado: ");
        String nombre = sc.nextLine();
        Empleado emp = tablaEmpleados.get("nombre:" + nombre);
        System.out.println(emp != null ? emp : "Empleado no encontrado.");
    }

    /**
     * Buscar empleado por número de empleado.
     */
    public static void buscarPorID(Scanner sc) {
        System.out.print("Número de empleado: ");
        int id = Integer.parseInt(sc.nextLine());
        Empleado emp = tablaEmpleados.get("id:" + id);
        System.out.println(emp != null ? emp : "Empleado no encontrado.");
    }

    /**
     * Buscar empleado por NSS.
     */
    public static void buscarPorNSS(Scanner sc) {
        System.out.print("Número de Seguridad Social: ");
        String nss = sc.nextLine();
        Empleado emp = tablaEmpleados.get("nss:" + nss);
        System.out.println(emp != null ? emp : "Empleado no encontrado.");
    }

    /**
     * Menú principal.
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int opcion;

        do {
            System.out.println("\n--- Menú de Empleados ---");
            System.out.println("1. Agregar empleado");
            System.out.println("2. Buscar por nombre");
            System.out.println("3. Buscar por número de empleado");
            System.out.println("4. Buscar por NSS");
            System.out.println("0. Salir");
            System.out.print("Opción: ");

            try {
                opcion = Integer.parseInt(sc.nextLine());
            } catch (NumberFormatException e) {
                opcion = -1;
            }

            switch (opcion) {
                case 1 -> agregarEmpleado(sc);
                case 2 -> buscarPorNombre(sc);
                case 3 -> buscarPorID(sc);
                case 4 -> buscarPorNSS(sc);
                case 0 -> System.out.println("Saliendo...");
                default -> System.out.println("Opción inválida.");
            }

        } while (opcion != 0);

        sc.close();
    }
}

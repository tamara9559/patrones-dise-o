public class DemoEnviosFactory {
    public static void main(String[] args) {
        System.out.println("Procesando envío terrestre:");
        FabricaEnvios terrestre = new FabricaEnvioTerrestre();
        terrestre.procesarEntrega();

        System.out.println("\nProcesando envío marítimo:");
        FabricaEnvios maritimo = new FabricaEnvioMaritimo();
        maritimo.procesarEntrega();

        System.out.println("\nProcesando envío aéreo:");
        FabricaEnvios aereo = new FabricaEnvioAereo();
        aereo.procesarEntrega();
    }
}
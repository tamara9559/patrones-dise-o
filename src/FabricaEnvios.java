public abstract class FabricaEnvios {
    public abstract Envio crearEnvio();

    public void procesarEntrega() {
        Envio envio = crearEnvio();
        System.out.println("Resultado del envío: " + envio.realizarEntrega());
    }
}
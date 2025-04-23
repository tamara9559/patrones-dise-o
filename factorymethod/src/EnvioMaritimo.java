public class EnvioMaritimo implements Envio {
    @Override
    public String realizarEntrega() {
        return "Entrega realizada por barco (envío marítimo).";
    }
}
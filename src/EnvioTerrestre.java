public class EnvioTerrestre implements Envio {
    @Override
    public String realizarEntrega() {
        return "Entrega realizada por camión (envío terrestre).";
    }
}
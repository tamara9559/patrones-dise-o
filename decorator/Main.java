// Clase principal para patrón Decorator
public class Main {

    interface Notificador {
        void enviar(String mensaje);
    }

    static class NotificadorBase implements Notificador {
        @Override
        public void enviar(String mensaje) {
            System.out.println("Notificación estándar: " + mensaje);
        }
    }

    static abstract class DecoradorNotificador implements Notificador {
        protected Notificador notificador;

        public DecoradorNotificador(Notificador notificador) {
            this.notificador = notificador;
        }

        @Override
        public void enviar(String mensaje) {
            notificador.enviar(mensaje);
        }
    }

    static class NotificadorEmail extends DecoradorNotificador {
        public NotificadorEmail(Notificador notificador) {
            super(notificador);
        }

        @Override
        public void enviar(String mensaje) {
            super.enviar(mensaje);
            System.out.println("Enviando notificación por correo: " + mensaje);
        }
    }

    static class NotificadorSMS extends DecoradorNotificador {
        public NotificadorSMS(Notificador notificador) {
            super(notificador);
        }

        @Override
        public void enviar(String mensaje) {
            super.enviar(mensaje);
            System.out.println("Enviando notificación por SMS: " + mensaje);
        }
    }

    static class NotificadorFacebook extends DecoradorNotificador {
        public NotificadorFacebook(Notificador notificador) {
            super(notificador);
        }

        @Override
        public void enviar(String mensaje) {
            super.enviar(mensaje);
            System.out.println("Enviando notificación por Facebook: " + mensaje);
        }
    }

    static class NotificadorSlack extends DecoradorNotificador {
        public NotificadorSlack(Notificador notificador) {
            super(notificador);
        }

        @Override
        public void enviar(String mensaje) {
            super.enviar(mensaje);
            System.out.println("Enviando notificación por Slack: " + mensaje);
        }
    }

    static class NotificadorWhatsApp extends DecoradorNotificador {
        public NotificadorWhatsApp(Notificador notificador) {
            super(notificador);
        }

        @Override
        public void enviar(String mensaje) {
            super.enviar(mensaje);
            System.out.println("Enviando notificación por WhatsApp: " + mensaje);
        }
    }

    public static void main(String[] args) {
        Notificador notificador = new NotificadorBase();
        notificador = new NotificadorEmail(notificador);
        notificador = new NotificadorSMS(notificador);
        notificador = new NotificadorFacebook(notificador);
        notificador = new NotificadorSlack(notificador);
        notificador = new NotificadorWhatsApp(notificador); // nuevo canal

        notificador.enviar("¡Alerta de seguridad!");
    }
}
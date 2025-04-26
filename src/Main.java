// Interfaz que el sistema espera (Target)
interface HDMI {
    void conectarConHDMI();
}

// Clase existente con una interfaz incompatible (Adaptee - VGA)
class VGA {
    public void conectarConVGA() {
        System.out.println("Conectado usando interfaz VGA.");
    }
}

// Clase nueva que también es incompatible (Adaptee - DisplayPort)
class DisplayPort {
    public void conectarConDisplayPort() {
        System.out.println("Conectado usando interfaz DisplayPort.");
    }
}

// Adaptador que permite usar un VGA como si fuera HDMI
class AdaptadorVGAaHDMI implements HDMI {
    private VGA vga;

    public AdaptadorVGAaHDMI(VGA vga) {
        this.vga = vga;
    }

    @Override
    public void conectarConHDMI() {
        System.out.println("Adaptando señal de VGA a HDMI...");
        vga.conectarConVGA();
    }
}

// Adaptador nuevo que permite usar DisplayPort como si fuera HDMI
class AdaptadorDisplayPortaHDMI implements HDMI {
    private DisplayPort displayPort;

    public AdaptadorDisplayPortaHDMI(DisplayPort displayPort) {
        this.displayPort = displayPort;
    }

    @Override
    public void conectarConHDMI() {
        System.out.println("Adaptando señal de DisplayPort a HDMI...");
        displayPort.conectarConDisplayPort();
    }
}

// Cliente que solo trabaja con HDMI
public class Main {
    public static void main(String[] args) {
        // Dispositivo con salida VGA
        VGA miMonitorVGA = new VGA();
        HDMI adaptadorVGA = new AdaptadorVGAaHDMI(miMonitorVGA);
        adaptadorVGA.conectarConHDMI();

        System.out.println();

        // Dispositivo con salida DisplayPort
        DisplayPort miMonitorDisplayPort = new DisplayPort();
        HDMI adaptadorDisplayPort = new AdaptadorDisplayPortaHDMI(miMonitorDisplayPort);
        adaptadorDisplayPort.conectarConHDMI();
    }
}

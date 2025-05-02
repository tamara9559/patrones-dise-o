from typing import List, Optional

# Subsistema: Reproductor de Audio
class AudioPlayer:
    def load_audio(self, file: str) -> None:
        print(f"Cargando archivo de audio: {file}")
    
    def play(self) -> None:
        print("Reproduciendo audio...")
    
    def stop(self) -> None:
        print("Deteniendo reproducción de audio")
    
    def set_volume(self, volume: int) -> None:
        print(f"Estableciendo volumen del audio a {volume}%")


# Subsistema: Reproductor de Video
class VideoPlayer:
    def load_video(self, file: str) -> None:
        print(f"Cargando archivo de video: {file}")
    
    def play(self) -> None:
        print("Reproduciendo video...")
    
    def stop(self) -> None:
        print("Deteniendo reproducción de video")
    
    def set_resolution(self, resolution: str) -> None:
        print(f"Ajustando resolución a {resolution}")


# Subsistema: Subtítulos
class SubtitleManager:
    def load_subtitles(self, file: str) -> None:
        print(f"Cargando archivo de subtítulos: {file}")
    
    def display(self) -> None:
        print("Mostrando subtítulos")
    
    def hide(self) -> None:
        print("Ocultando subtítulos")
    
    def set_language(self, language: str) -> None:
        print(f"Estableciendo idioma de subtítulos a: {language}")


# Subsistema: Gestor de Listas de Reproducción
class PlaylistManager:
    def __init__(self):
        self.playlist: List[str] = []
        self.current_index: int = 0
    
    def create_playlist(self) -> None:
        self.playlist.clear()
        self.current_index = 0
        print("Lista de reproducción creada")
    
    def add_to_playlist(self, file: str) -> None:
        self.playlist.append(file)
        print(f"Añadido a la lista de reproducción: {file}")
    
    def get_next_item(self) -> Optional[str]:
        if not self.playlist:
            return None
        
        item = self.playlist[self.current_index]
        self.current_index = (self.current_index + 1) % len(self.playlist)
        print(f"Siguiente elemento de la lista: {item}")
        return item
    
    def display_playlist(self) -> None:
        print("=== Lista de reproducción actual ===")
        for i, item in enumerate(self.playlist):
            prefix = "→ " if (i == self.current_index - 1 or 
                            (self.current_index == 0 and i == len(self.playlist) - 1)) else "  "
            print(f"{prefix}{i + 1}. {item}")
        print("===================================")


# Nuevo Subsistema: Ecualizador
class Equalizer:
    def __init__(self):
        self.preset_modes = {
            "rock": {"bass": 8, "mid": 5, "treble": 7},
            "pop": {"bass": 5, "mid": 7, "treble": 6},
            "jazz": {"bass": 6, "mid": 4, "treble": 3},
            "classical": {"bass": 4, "mid": 4, "treble": 5},
            "flat": {"bass": 5, "mid": 5, "treble": 5}
        }
        self.current_mode = "flat"
    
    def set_mode(self, mode: str) -> None:
        mode = mode.lower()
        if mode in self.preset_modes:
            self.current_mode = mode
            settings = self.preset_modes[mode]
            print(f"Modo de ecualización configurado a: {mode.upper()}")
            print(f"Configuración: Graves={settings['bass']}, Medios={settings['mid']}, Agudos={settings['treble']}")
        else:
            available_modes = ", ".join(self.preset_modes.keys())
            print(f"Modo no reconocido. Modos disponibles: {available_modes}")
    
    def get_current_mode(self) -> str:
        return self.current_mode
    
    def custom_equalization(self, bass: int, mid: int, treble: int) -> None:
        if not all(0 <= x <= 10 for x in [bass, mid, treble]):
            print("Los valores deben estar entre 0 y 10")
            return
            
        print(f"Configurando ecualización personalizada: Graves={bass}, Medios={mid}, Agudos={treble}")
        self.current_mode = "custom"


# FACHADA (FACADE)
class MediaPlayerFacade:
    def __init__(self):
        self.audio_player = AudioPlayer()
        self.video_player = VideoPlayer()
        self.subtitle_manager = SubtitleManager()
        self.playlist_manager = PlaylistManager()
        self.equalizer = Equalizer()  # Agregamos la instancia del ecualizador
        
        # Almacena el tipo de archivo actual
        self.current_media_type = None
    
    # Determina el tipo de archivo por su extensión
    def _get_file_type(self, file: str) -> str:
        if file.endswith((".mp3", ".wav", ".ogg")):
            return "audio"
        elif file.endswith((".mp4", ".avi", ".mkv")):
            return "video"
        else:
            return "unknown"
    
    # Método principal para reproducir un archivo multimedia
    def play_media(self, file: str) -> None:
        print("\n=== INICIANDO REPRODUCCIÓN DE MEDIA ===")
        file_type = self._get_file_type(file)
        self.current_media_type = file_type
        
        if file_type == "audio":
            self.audio_player.load_audio(file)
            self.audio_player.set_volume(80)
            self.audio_player.play()
        elif file_type == "video":
            self.video_player.load_video(file)
            self.video_player.set_resolution("1080p")
            
            # Intentar cargar subtítulos automáticamente
            subtitle_file = file[:file.rfind('.')] + ".srt"
            self.subtitle_manager.load_subtitles(subtitle_file)
            self.subtitle_manager.set_language("Español")
            self.subtitle_manager.display()
            
            self.video_player.play()
        else:
            print(f"Formato de archivo no soportado: {file}")
    
    # Detener la reproducción actual
    def stop_media(self) -> None:
        print("\n=== DETENIENDO REPRODUCCIÓN ===")
        
        if self.current_media_type is None:
            print("No hay reproducción activa")
            return
        
        if self.current_media_type == "audio":
            self.audio_player.stop()
        elif self.current_media_type == "video":
            self.video_player.stop()
            self.subtitle_manager.hide()
        
        self.current_media_type = None
    
    # Administrar listas de reproducción
    def create_playlist(self) -> None:
        self.playlist_manager.create_playlist()
    
    def add_to_playlist(self, file: str) -> None:
        self.playlist_manager.add_to_playlist(file)
    
    def play_next(self) -> None:
        next_item = self.playlist_manager.get_next_item()
        if next_item is not None:
            self.play_media(next_item)
        else:
            print("La lista de reproducción está vacía")
    
    def show_playlist(self) -> None:
        self.playlist_manager.display_playlist()
    
    # Métodos adicionales de conveniencia
    def toggle_subtitles(self) -> None:
        if self.current_media_type is not None and self.current_media_type == "video":
            print("Alternando visibilidad de subtítulos")
            # En una implementación real, consultaríamos el estado actual
            self.subtitle_manager.display()  # O hide() dependiendo del estado
        else:
            print("Los subtítulos solo están disponibles durante la reproducción de video")
    
    def set_volume(self, volume: int) -> None:
        if volume < 0 or volume > 100:
            print("El volumen debe estar entre 0 y 100")
            return
        
        print(f"Estableciendo volumen a {volume}%")
        self.audio_player.set_volume(volume)
    
    # Nuevo método para establecer el modo del ecualizador
    def set_sound_mode(self, mode: str) -> None:
        print("\n=== CONFIGURANDO ECUALIZADOR ===")
        if self.current_media_type is None:
            print("Configurando ecualizador para la próxima reproducción")
        elif self.current_media_type == "video":
            print("Configurando ecualizador para la reproducción de video actual")
        elif self.current_media_type == "audio":
            print("Configurando ecualizador para la reproducción de audio actual")
        
        self.equalizer.set_mode(mode)
    
    # Método adicional para ecualizador personalizado
    def set_custom_equalization(self, bass: int, mid: int, treble: int) -> None:
        print("\n=== CONFIGURANDO ECUALIZADOR PERSONALIZADO ===")
        self.equalizer.custom_equalization(bass, mid, treble)


# Cliente 
def main():
    # El cliente utiliza únicamente la interfaz simplificada de la fachada
    media_player = MediaPlayerFacade()
    
    # Crear y configurar una lista de reproducción
    media_player.create_playlist()
    media_player.add_to_playlist("cancion1.mp3")
    media_player.add_to_playlist("pelicula.mp4")
    media_player.add_to_playlist("cancion2.mp3")
    media_player.show_playlist()
    
    # Configurar el modo de sonido del ecualizador
    media_player.set_sound_mode("Rock")
    
    # Reproducir un archivo específico
    media_player.play_media("documental.mp4")
    
    # Ajustar volumen
    media_player.set_volume(70)
    
    # Alternar subtítulos
    media_player.toggle_subtitles()
    
    # Cambiar el modo de ecualizador durante la reproducción
    media_player.set_sound_mode("Jazz")
    
    # Configuración personalizada del ecualizador
    media_player.set_custom_equalization(8, 6, 7)
    
    # Detener la reproducción actual
    media_player.stop_media()
    
    # Reproducir el siguiente elemento de la lista
    media_player.play_next()


if __name__ == "__main__":
    main()
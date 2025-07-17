import socket
import threading
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
from plyer import vibrator

class VirusApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.label = Label(text='[✓] T-SOCIETY çalışıyor...\nIP ve Port bekleniyor', font_size='20sp')
        self.layout.add_widget(self.label)
        Clock.schedule_once(self.start_server, 1)
        return self.layout

    def start_server(self, dt):
        def server():
            s = socket.socket()
            s.bind(('', 0))  # rastgele port
            port = s.getsockname()[1]
            ip = socket.gethostbyname(socket.gethostname())
            Clock.schedule_once(lambda dt: self.label_update(ip, port))
            s.listen(1)
            conn, addr = s.accept()
            while True:
                try:
                    data = conn.recv(1024).decode().strip()
                    if not data:
                        break
                    Clock.schedule_once(lambda dt: self.execute_command(data))
                except:
                    break
            conn.close()
            s.close()

        threading.Thread(target=server, daemon=True).start()

    def label_update(self, ip, port):
        self.label.text = f"[✓] T-SOCIETY Dinleniyor\nIP: {ip}\nPort: {port}"

    def execute_command(self, cmd):
        if cmd == "karart":
            Window.clearcolor = (0, 0, 0, 1)
        elif cmd == "titre":
            try:
                vibrator.vibrate(3)
            except:
                self.label.text = "Titreşim desteklenmiyor"
        elif cmd == "verisil":
            self.label.text = "[❗] Veriler siliniyor...\nT-SOCIETY başlattı"
        elif cmd == "glitch":
            self.label.text = "[⚠️] Sistem hatası - Glitch!!!"
            Window.clearcolor = (1, 0, 1, 1)
        elif cmd == "hata":
            self.label.text = "[💥] Android ÇÖKTÜ!"
            Window.clearcolor = (1, 0, 0, 1)
        elif cmd == "kapat":
            App.get_running_app().stop()

VirusApp().run()

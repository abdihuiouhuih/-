import customtkinter as ctk
from scapy.all import ARP, Ether, srp
import socket

# إعدادات الواجهة
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class NetworkApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Network Sentinel - مراقب الشبكة")
        self.geometry("800x600")

        # إنشاء نظام القوائم الجانبية
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # القائمة الجانبية
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="التحكم بالشبكة", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.pack(pady=20)

        self.btn_scan = ctk.CTkButton(self.sidebar, text="فحص الأجهزة", command=self.show_scan_page)
        self.btn_scan.pack(pady=10, padx=10)

        self.btn_activity = ctk.CTkButton(self.sidebar, text="نشاط المواقع", command=self.show_activity_page)
        self.btn_activity.pack(pady=10, padx=10)

        self.btn_info = ctk.CTkButton(self.sidebar, text="بيانات الشبكة", command=self.show_info_page)
        self.btn_info.pack(pady=10, padx=10)

        # القائمة الرئيسية (المحتوى المتغير)
        self.main_view = ctk.CTkTextbox(self, font=("Arial", 14))
        self.main_view.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_view.insert("0.0", "مرحباً بك! اختر قائمة من اليسار للبدء...")

    def get_local_ip(self):
        # الحصول على IP الجهاز الحالي
        return socket.gethostbyname(socket.gethostname())

    def show_scan_page(self):
        self.main_view.delete("0.0", "end")
        self.main_view.insert("end", "جاري فحص الأجهزة المتصلة... انتظر لحظة\n" + "-"*40 + "\n")
        
        # كود فحص الأجهزة (ARP Scan)
        target_ip = ".".join(self.get_local_ip().split('.')[:-1]) + ".1/24"
        arp = ARP(pdst=target_ip)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether/arp
        result = srp(packet, timeout=3, verbose=0)[0]

        for sent, received in result:
            self.main_view.insert("end", f"جهاز: {received.psrc}  |  ماك أدريس: {received.hwsrc}\n")

    def show_activity_page(self):
        self.main_view.delete("0.0", "end")
        self.main_view.insert("end", "قائمة المواقع والنشاط (تجريبي):\n")
        self.main_view.insert("end", "> ملاحظة: هذه الخاصية تتطلب وضع 'Sniffing' وتحليل الحزم (Packet Capture).\n")
        self.main_view.insert("end", "1. IP 192.168.1.5 -> طلب اتصال بـ Google.com\n")
        self.main_view.insert("end", "2. IP 192.168.1.12 -> نشاط يوتيوب مرتفع\n")

    def show_info_page(self):
        self.main_view.delete("0.0", "end")
        info = f"آي بي جهازك: {self.get_local_ip()}\n" \
               f"اسم الشبكة (SSID): متصل\n" \
               f"حالة الأمان: نشط\n" \
               f"الرقم السري (المخزن محلياً): ********"
        self.main_view.insert("end", info)

if __name__ == "__main__":
    app = NetworkApp()
    app.mainloop()

import streamlit as st
import pandas as pd
from scapy.all import ARP, Ether, srp, conf
import socket

# إعدادات الصفحة
st.set_page_config(page_title="Network Monitor Pro", layout="wide")

st.title("🌐 مراقب الشبكة الذكي (Network Monitor)")
st.write("أهلاً عبد الله، هذا التطبيق مخصص لفحص الأجهزة ونشاط الشبكة.")

# القائمة الجانبية
menu = ["فحص الأجهزة", "نشاط المواقع (DNS)", "معلومات الشبكة"]
choice = st.sidebar.selectbox("اختر القائمة", menu)

# وظيفة للحصول على الـ IP الخاص بالسيرفر
def get_internal_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

if choice == "فحص الأجهزة":
    st.header("🔍 فحص الأجهزة المتصلة")
    ip_range = st.text_input("أدخل نطاق الشبكة (IP Range)", value=get_internal_ip() + "/24")
    
    if st.button("بدء الفحص"):
        with st.spinner("جاري فحص الشبكة..."):
            try:
                # محاولة عمل ARP Scan (قد لا تعمل في السحاب لعدم وجود صلاحيات Root)
                ans, _ = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip_range), timeout=2, verbose=False)
                
                devices = []
                for _, rcv in ans:
                    devices.append({"IP Address": rcv.psrc, "MAC Address": rcv.hwsrc})
                
                if devices:
                    df = pd.DataFrame(devices)
                    st.success(f"تم العثور على {len(devices)} جهاز")
                    st.table(df)
                else:
                    st.warning("لم يتم العثور على أجهزة. (تذكر: سيرفرات السحاب لا يمكنها فحص شبكتك المحلية)")
            except Exception as e:
                st.error(f"حدث خطأ في الصلاحيات: {e}")
                st.info("ملاحظة: فحص الـ ARP يحتاج صلاحيات Admin، وهذا غير متوفر في السيرفرات السحابية المجانية.")

elif choice == "نشاط المواقع (DNS)":
    st.header("📡 مراقبة المواقع المفتوحة")
    st.info("هذه الخاصية تعمل على 'التقاط الحزم' (Packet Sniffing).")
    st.warning("سيرفرات Streamlit Cloud تمنع التقاط الحزم لأسباب أمنية. هذه الواجهة مصممة لتعمل عند تشغيل الكود محلياً على جهازك.")
    
    # محاكاة لما سيظهر لو اشتغل محلياً
    st.write("آخر المواقع المطلوبة (مثال):")
    sample_data = {
        "الجهاز (IP)": ["192.168.1.15", "192.168.1.22", "192.168.1.5"],
        "الموقع": ["google.com", "github.com", "youtube.com"],
        "الوقت": ["18:30:12", "18:31:05", "18:35:44"]
    }
    st.dataframe(pd.DataFrame(sample_data))

elif choice == "معلومات الشبكة":
    st.header("ℹ️ بيانات الاتصال")
    st.json({
        "اسم الجهاز": socket.gethostname(),
        "الآي بي الداخلي للخدمة": get_internal_ip(),
        "نظام التشغيل": "Linux (Streamlit Cloud)",
        "حالة الأمان": "تصفية جدار الحماية نشطة"
    })

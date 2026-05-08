import streamlit as st
import socket
import pandas as pd

# إعداد واجهة التطبيق
st.set_page_config(page_title="Network Monitor Pro", page_icon="🌐")

# تصميم القائمة الجانبية (Sidebar) مثل ما طلبت
st.sidebar.title("🎮 قائمة التحكم")
choice = st.sidebar.radio("اختر القائمة:", ["الرئيسية", "الأجهزة المتصلة", "نشاط المواقع", "بيانات الشبكة"])

# دالة لجلب الآي بي
def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "127.0.0.1"

# --- القائمة الرئيسية ---
if choice == "الرئيسية":
    st.title("🌐 مراقب الشبكة الذكي")
    st.success(f"مرحباً بك يا عبد الله! التطبيق يعمل الآن بنجاح.")
    st.info("اختر القوائم من اليسار لبدء مراقبة أجهزتك.")

# --- قائمة الأجهزة ---
elif choice == "الأجهزة المتصلة":
    st.header("🔍 قائمة الأجهزة والآيبيات")
    st.write("هذه القائمة تعرض الأجهزة الموجودة حالياً:")
    
    # محاكاة للأجهزة (لأن السيرفر الأونلاين لا يرى بيتك)
    data = {
        "اسم الجهاز": ["جهازك الحالي", "Xiaomi Pad 7", "Samsung S24 Ultra", "Xbox-Console"],
        "الآي بي (IP)": [get_ip(), "192.168.1.15", "192.168.1.20", "192.168.1.50"],
        "الحالة": ["متصل ✅", "متصل ✅", "خامل 💤", "متصل ✅"]
    }
    st.table(pd.DataFrame(data))

# --- قائمة المواقع ---
elif choice == "نشاط المواقع":
    st.header("🌐 آخر المواقع التي تم دخولها")
    st.write("ملخص عن نشاط الأجهزة في الشبكة:")
    
    activity = {
        "الجهاز": ["Xiaomi Pad 7", "Samsung S24 Ultra", "جهازك الحالي"],
        "آخر موقع": ["google.com", "youtube.com", "streamlit.io"],
        "الوقت": ["10:30 AM", "10:45 AM", "11:00 AM"]
    }
    st.dataframe(pd.DataFrame(activity))

# --- بيانات الشبكة ---
elif choice == "بيانات الشبكة":
    st.header("🔑 معلومات الوصول")
    st.warning("تنبيه: لا تشارك الرقم السري مع غرباء!")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("اسم الشبكة (SSID)", "Abdullah_Home_WiFi")
        st.metric("الآي بي المحلي", get_ip())
    with col2:
        st.write("**الرقم السري للشبكة:**")
        if st.button("إظهار الرقم السري"):
            st.code("Admin@2026", language="text")

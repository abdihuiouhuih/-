import streamlit as st
import pandas as pd

# إعداد الصفحة وتغيير الثيم ليكون مريح للعين
st.set_page_config(page_title="Network Pro", page_icon="📡", layout="centered")

# إضافة لمسات جمالية بالـ CSS
st.markdown("""
    <style>
    /* تصميم الأزرار الكبيرة */
    .stButton > button {
        width: 100%;
        border-radius: 15px;
        height: 80px;
        font-size: 22px !important;
        font-weight: bold;
        background-color: #f0f2f6;
        border: 2px solid #007BFF;
        color: #007BFF;
        transition: 0.3s;
    }
    .stButton > button:hover {
        background-color: #007BFF;
        color: white;
    }
    /* تصميم الحقوق */
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        text-align: center;
        padding: 15px;
        background-color: white;
        border-top: 1px solid #eee;
        color: #555;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة الصفحات داخل التطبيق
if 'page' not in st.session_state:
    st.session_state.page = 'home'

def change_page(name):
    st.session_state.page = name

# --- الواجهة الرئيسية ---
if st.session_state.page == 'home':
    st.markdown("<h1 style='text-align: center;'>📡 النظام الشامل لمعرفة أجهزة الشبكة</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #666;'>مرحباً بك في لوحة التحكم.. اختر أحد الخيارات أدناه</h4>", unsafe_allow_html=True)
    st.write("---")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("📱 الأجهزة والآيبيات"):
            change_page('devices')
    with col2:
        if st.button("🌐 مراقبة المواقع"):
            change_page('sites')
            
    col3, col4 = st.columns(2)
    with col3:
        if st.button("🔑 بيانات الشبكة"):
            change_page('wifi_info')
    with col4:
        if st.button("📊 إحصائيات الاستخدام"):
            change_page('usage')

# --- واجهة الأجهزة والآيبيات ---
elif st.session_state.page == 'devices':
    st.title("📱 قائمة الأجهزة المتصلة")
    st.info("هنا تظهر جميع الأجهزة والآيبيات المرتبطة بشبكتك حالياً:")
    
    devices = pd.DataFrame({
        "الجهاز": ["Xiaomi Pad 7", "Samsung S24 Ultra", "PC - Abdullah", "Xbox Console"],
        "الآي بي (IP)": ["192.168.1.15", "192.168.1.20", "192.168.1.10", "192.168.1.45"],
        "نوع الاتصال": ["Wi-Fi", "Wi-Fi", "Ethernet", "Wi-Fi"]
    })
    st.table(devices)
    if st.button("🔙 العودة للقائمة"): change_page('home')

# --- واجهة مراقبة المواقع ---
elif st.session_state.page == 'sites':
    st.title("🌐 المواقع النشطة الآن")
    st.write("عرض مباشر للمواقع التي يتم تصفحها من قبل الأجهزة:")
    
    activity = pd.DataFrame({
        "الجهاز": ["PC - Abdullah", "Samsung S24 Ultra", "Xiaomi Pad 7"],
        "الموقع المفتوح حالياً": ["github.com", "youtube.com/live", "google.com.sa"],
        "حجم البيانات": ["15 MB", "450 MB", "2 MB"]
    })
    st.dataframe(activity, use_container_width=True)
    if st.button("🔙 العودة للقائمة"): change_page('home')

# --- واجهة بيانات الشبكة ---
elif st.session_state.page == 'wifi_info':
    st.title("🔑 بيانات الوصول للشبكة")
    st.markdown("""
    <div style="background-color: #f9f9f9; padding: 20px; border-radius: 15px; border: 1px solid #ddd;">
        <h3 style="color: #333;">تفاصيل الاتصال:</h3>
        <p><b>اسم الشبكة (SSID):</b> Abdullah_5G_Fiber</p>
        <p><b>نوع التشفير:</b> WPA3-Personal (آمن)</p>
        <hr>
        <p><b>رمز الشبكة الحالي:</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("إظهار الرمز السري"):
        st.success("الرمز هو: **Abdullah@Vip2026**")
    
    if st.button("🔙 العودة للقائمة"): change_page('home')

# --- واجهة إحصائيات الاستخدام ---
elif st.session_state.page == 'usage':
    st.title("📊 ملخص الاستخدام العام")
    st.write("تحليل كمية البيانات المستهلكة لكل جهاز:")
    st.bar_chart({"الاستهلاك (GB)": [5, 12, 8, 20]})
    st.write("الأكثر استهلاكاً: **Xbox Console**")
    if st.button("🔙 العودة للقائمة"): change_page('home')

# --- الحقوق الثابتة في كل الصفحات ---
st.markdown("""
    <div class="footer">
        هذا التطبيق مصمم بواسطة أخوك عبد الله ✍️
    </div>
    """, unsafe_allow_html=True)

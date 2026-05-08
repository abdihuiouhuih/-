import streamlit as st
import pandas as pd
import socket

# إعدادات الصفحة
st.set_page_config(page_title="Network Tool", page_icon="📶")

# تنسيق بسيط للواجهة (CSS)
st.markdown("""
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: transparent;
        color: #777;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    .main-title {
        text-align: center;
        color: #007BFF;
        font-family: 'Arial';
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("<h1 class='main-title'>📶 النظام الشامل لمعرفة أجهزة الشبكة</h1>", unsafe_allow_html=True)
st.write("<center>أهلاً بك في نظامك الخاص لمراقبة وتحليل نشاط الشبكة بسهولة تامة.</center>", unsafe_allow_html=True)
st.markdown("---")

# القوائم البسيطة (Tabs) بدلاً من القائمة الجانبية المعقدة
tab1, tab2, tab3 = st.tabs(["🔍 فحص الأجهزة", "🌐 نشاط المواقع", "🔑 بيانات الوصول"])

with tab1:
    st.subheader("الأجهزة المتصلة حالياً")
    # بيانات تجريبية بسيطة
    devices = pd.DataFrame({
        "اسم الجهاز": ["هاتف ذكي", "جهاز لوحي", "كمبيوتر", "إكس بوكس"],
        "الآي بي (IP)": ["192.168.1.15", "192.168.1.20", "192.168.1.10", "192.168.1.50"],
        "الحالة": ["نشط", "نشط", "خامل", "نشط"]
    })
    st.table(devices)
    if st.button("تحديث الفحص"):
        st.toast("جاري تحديث القائمة...")

with tab2:
    st.subheader("سجل المواقع الأخير")
    st.write("ملخص للمواقع التي تم زيارتها عبر الشبكة:")
    logs = pd.DataFrame({
        "الجهاز": ["192.168.1.15", "192.168.1.10", "192.168.1.50"],
        "الموقع": ["google.com", "github.com", "youtube.com"],
        "التوقيت": ["منذ دقيقتين", "منذ 5 دقائق", "منذ ساعة"]
    })
    st.dataframe(logs, use_container_width=True)

with tab3:
    st.subheader("معلومات الشبكة الحالية")
    st.info("بيانات الاتصال المحمية")
    st.text(f"IP الجهاز الحالي: {socket.gethostbyname(socket.gethostname())}")
    st.text("نوع التشفير: WPA2-Personal")
    if st.button("إظهار رمز الدخول"):
        st.code("Pass: Abdullah_2026", language="text")

# وضع الحقوق في أسفل الصفحة
st.markdown("""
    <div class="footer">
        <hr>
        هذا التطبيق مصمم بواسطة أخوك <b>عبد الله</b> | جميع الحقوق محفوظة 2026 ©
    </div>
    """, unsafe_allow_html=True)

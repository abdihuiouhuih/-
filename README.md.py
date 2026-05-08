import streamlit as st
import pandas as pd

# إعدادات الصفحة
st.set_page_config(page_title="Network Monitor", page_icon="🌐", layout="wide")

# تصميم CSS احترافي (ألوان مريحة وأزرار ضخمة)
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; }
    
    /* تصميم الأزرار العملاقة */
    div.stButton > button {
        width: 100%;
        height: 220px;
        border-radius: 25px;
        font-size: 32px !important;
        font-weight: bold;
        background: linear-gradient(145deg, #1e293b, #0f172a);
        color: #38bdf8;
        border: 3px solid #38bdf8;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        transition: 0.3s;
    }
    
    div.stButton > button:hover {
        background: #38bdf8;
        color: #0f172a;
        transform: scale(1.02);
    }

    .main-title { text-align: center; color: white; font-size: 45px; font-weight: bold; margin-top: -30px; }
    .sub-title { text-align: center; color: #94a3b8; font-size: 22px; margin-bottom: 50px; }

    /* الحقوق */
    .footer {
        position: fixed;
        left: 0; bottom: 0; width: 100%;
        background-color: #0f172a; color: #38bdf8;
        text-align: center; padding: 15px;
        font-weight: bold; border-top: 1px solid #38bdf8;
    }
    </style>
    """, unsafe_allow_html=True)

# إدارة الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'main'

def go_to(page_name):
    st.session_state.page = page_name
    st.rerun()

# --- الواجهة الرئيسية ---
if st.session_state.page == 'main':
    st.markdown("<h1 class='main-title'>اهلا بك في النظام الشامل لمعرفة الاجهزة على الشبكة</h1>", unsafe_allow_html=True)
    st.markdown("<p class='sub-title'>اختر أحد الأقسام التالية لمتابعة نشاط شبكتك</p>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📱 أسماء الأجهزة المتصلة"):
            go_to('devices')
    with col2:
        if st.button("📊 مراقبة استخدام الشبكة"):
            go_to('usage')

# --- واجهة أسماء الأجهزة ---
elif st.session_state.page == 'devices':
    st.markdown("<h1 style='text-align: center; color: white;'>📱 قائمة الأجهزة الحالية</h1>", unsafe_allow_html=True)
    
    devices_data = pd.DataFrame({
        "اسم الجهاز (المعروف)": ["كمبيوتر عبد الله الشخصي", "جهاز لوحي (Xiaomi)", "جوال سامسونج الترا", "جهاز بلايستيشن / إكس بوكس"],
        "رقم الجهاز (IP)": ["192.168.1.10", "192.168.1.15", "192.168.1.22", "192.168.1.50"],
        "حالة الاتصال": ["متصل الآن ✅", "متصل ✅", "غير نشط 💤", "متصل ✅"]
    })
    
    st.table(devices_data)
    if st.button("🔙 العودة للقائمة الرئيسية"):
        go_to('main')

# --- واجهة استخدام الشبكة ---
elif st.session_state.page == 'usage':
    st.markdown("<h1 style='text-align: center; color: white;'>📊 نشاط واستخدام الأجهزة</h1>", unsafe_allow_html=True)
    
    usage_data = pd.DataFrame({
        "اسم الجهاز": ["كمبيوتر عبد الله الشخصي", "جهاز لوحي (Xiaomi)", "جوال سامسونج الترا", "جهاز بلايستيشن / إكس بوكس"],
        "الموقع المفتوح الآن": ["تطوير البرامج (GitHub)", "بحث جوجل", "تطبيق اليوتيوب", "تحميل ألعاب"],
        "كمية الاستهلاك": ["متوسط", "خفيف", "عالي", "عالي جداً"],
        "النشاط": ["يعمل الآن", "يعمل الآن", "خامل", "يعمل الآن"]
    })
    
    st.table(usage_data)
    
    if st.button("🔙 العودة للقائمة الرئيسية"):
        go_to('main')

# --- الحقوق الثابتة ---
st.markdown("""
    <div class="footer">
        هذا التطبيق مصمم من أخوك عبد الله
    </div>
    """, unsafe_allow_html=True)

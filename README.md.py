import streamlit as st
import subprocess
import platform
import re
import pandas as pd
import socket

st.set_page_config(
    page_title="Network Scanner",
    page_icon="📡",
    layout="wide"
)

st.title("📡 مراقبة الأجهزة المتصلة بالشبكة")
st.caption("يفحص الأجهزة المتصلة بنفس الشبكة المحلية")


def get_devices():
    devices = []

    try:
        system = platform.system()

        if system == "Windows":
            output = subprocess.check_output(
                "arp -a",
                shell=True
            ).decode(errors="ignore")
        else:
            output = subprocess.check_output(
                ["arp", "-a"]
            ).decode(errors="ignore")

        pattern = r"([0-9]+(?:\.[0-9]+){3})"
        ips = re.findall(pattern, output)

        unique_ips = list(set(ips))

        for ip in unique_ips:
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except Exception:
                hostname = "غير معروف"

            devices.append({
                "اسم الجهاز": hostname,
                "IP": ip,
                "الحالة": "متصل"
            })

    except Exception as error:
        st.error(f"خطأ أثناء الفحص: {error}")

    return devices


if "known_ips" not in st.session_state:
    st.session_state.known_ips = []


if st.button("🔍 فحص الشبكة"):
    with st.spinner("جاري الفحص..."):

        devices = get_devices()

        current_ips = [d["IP"] for d in devices]

    "لا يمكن استخراج كلمات السر أو مراقبة المواقع أو التجسس على المستخدمين"

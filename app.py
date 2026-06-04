import streamlit as st

st.set_page_config(page_title="My Multi-page App", layout="wide")

st.title("🏠 หน้าหลัก")
st.write("### Boot Camp: Data Science and Machine Learning")
st.info("7 Day Intensive Hands-on Workshop")
st.markdown(''':green[📢CHANATHIP]''')
st.write("##### Day 1: การจัดการข้อมูลพื้นฐานและโครงสร้างข้อมูลด้วย Python")

if st.button("💰 ระบบคำนวณส่วนลดตามยอดซื้อ"):
    st.switch_page("pages/app1_discount_calc.py")
elif st.button("📢ทำความสะอาดข้อมูล"):
    st.switch_page("pages/clean_app.py")
elif st.button("📢ทำความสะอาดข้อมูล"):
    st.switch_page("pages/clean_pech.py")
elif st.button("📢การแปลงข้อมูล"):
    st.switch_page("pages/transform_app(2).py")
elif st.button("📢การวิเคราะห์ข้อมูลเชิงสำรวจ"):
    st.switch_page("pages/EDA_app.py")
elif st.button("📢พยากรณ์ยอดขาย"):
    st.switch_page("pages/sale_predict.py")
elif st.button("📢ช่วยพยากรณ์เวลาบริการรถบรรทุก"):
    st.switch_page("pages/truck_predict.py")

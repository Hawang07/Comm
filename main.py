import streamlit as st
import pandas as pd

# CSS ซ่อน sidebar + GitHub link (แก้ไขแล้ว)
st.markdown("""
    <style>
        /* ซ่อน sidebar ทั้งหมด */
        section[data-testid="stSidebar"] { 
            display: none !important; 
        }
        [data-testid="stSidebarNav"] { 
            display: none !important; 
        }
        div[data-testid="stSidebarNav"] > div { 
            display: none !important; 
        }
        
        /* ซ่อน GitHub source code link + Menu */
        #MainMenu { visibility: hidden !important; }
        #GithubIcon { visibility: hidden !important; }
        button[kind="header"] { display: none !important; }
        footer { visibility: hidden !important; }
        header .css-1jc7ptx, 
        .e1ewe7hr3, 
        .viewerBadge_container__1QSob, 
        .styles_viewerBadge__1yB5_ { 
            display: none !important; 
        }
    </style>
""", unsafe_allow_html=True)

# ตั้งค่า page config
st.set_page_config(
    page_title="Commission",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Users dictionary (แก้ไขชื่อซ้ำ)
USERS = {
    "admin": "123456*",
    "Somwang": "0944542994",
    "Tharinee": "0955405556",
    "Chutipa": "0963544236",
    "Jittima": "0968625565",
    "Thanapon": "0842465935",
    "Charinthip": "0829514536",
    "Namoun": "0886774449",
    "Areewan": "0967193456",
    "Maneewan": "0815914236",
    "Kitti": "0972456459",
    "Khanittha": "0990834923",
    "Darawan": "0929242899",
    "Panisara": "0946592445",
    "Kriangkrai": "0635199969",
    "Sumintra": "0949655693",
    "Surachet": "0949644423",
    "Jittra": "0963566592",
    "Siriya": "0875569928",
    "Namphueng": "0626965495",
    "Wanwisa": "0886966512",
    "Nathawat": "0619295978",
    "Khanittayada": "0971565697",
    "Narin": "0925495655",
    "Thawatchai": "0925495656",  # แก้ไม่ซ้ำ
    "Jiraporn": "0868293697",
    "Ponphan": "0822282526",
    "Chatphat": "0814536195",
    "Chalothon": "0993619241",
    "Preecha": "0993619242",     # แก้ไม่ซ้ำ
    "Waruth": "0952464692",
    "Natthawat": "0959199455",
    "Suriphon":"0966942642",
    "Preecha":"0816554223",
    "Suriphon":"0966942642",
    "Settawut":"0966695936", 
    "Lanlanin":"0802896166", 
    "Panitta":"0814223613", 
    "Tanpisit":"0633263632", 
    "Somsak":"0805456926", 
    "Wimada":"081555948",
    "Kitti7": "0972456459",
  "Janthira": "0642244695",
  "Sattawat": "0830445095",
  "Khanittha": "0990834923",
  "Boonyarit": "0917707536",
  "Areewan": "0967193456",
  "Phakin": "0955961645",
  "Cheerawat": "0824249456",
  "Teeraphong": "0839719596",
  "Maneewan": "0815914236",
  "Charinthip": "0829514536",
  "Chanida": "0816464562",
  "Kridsada": "0617824456",
  "Chanida pala": "0816464562",
  "Wijitt1": "0816196324",
  "khunrues": "0946269445",
  "Detchat": "0829934614",
  "Narimol": "0971246641",
  "Panchalee": "0838256642",
  "Nankamon": "0955956592",
  "thanapon": "0842465935",
  "Mathurot": "0809832031",
  "Chutipa": "0963544236",
  "Jittra": "0963566592",
  "Sumintra": "0949655693",
  "Panitta": "0814223613",
  "Pongnarad": "0829459356",
  "Panisara": "0946592445",
  "Tanika Yunila": "0955963695",
  "Ponphan": "0822282526",
  "Nittaya asas": "0832328744",
  "NarinS": "0925495655",
  "Rawipa": "0955545395",
  "MyNameOnair": "0633565566",
  "Jira": "0868293697",
  "Teerakorn": "0961595979",
  "Ampa": "0814025968",
  "Tanika": "0955963695",
  "Thawatchai": "0944466695",
  "pairin": "0889242823",
  "Chanwit": "0971599645",
  "Surasak": "0909646446",
  "Kingkanjana": "0955954462",
  "Surachet": "0949644423",
  "Namphueng": "0626965495",
  "Namoun": "0886774449",
  "Kittisak": "0658299789"
}

# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = None

# Login page
if not st.session_state.logged_in:
    st.title("🔒 เข้าสู่ระบบ")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        username = st.text_input("👤 Username", placeholder="ป้อนชื่อผู้ใช้")
        password = st.text_input("🔑 Password", type="password", placeholder="ป้อนรหัสผ่าน")
        
        if st.button("🚀 เข้าสู่ระบบ", type="primary", use_container_width=True):
            if username in USERS and USERS[username] == password:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.success(f"✅ สวัสดี {username}!")
                st.rerun()
            else:
                st.error("❌ Username หรือ Password ไม่ถูกต้อง")
                st.info("💡 กรุณาตรวจสอบอีกครั้ง")

else:
    st.title(f"💎 สวัสดี {st.session_state.username}")
    st.success("✅ เข้าสู่ระบบสำเร็จ!")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📊 Commission Dashboard", type="primary", use_container_width=True):
            st.switch_page("pages/commission.py")
    with col2:
        if st.button("🚪 ออกจากระบบ", type="secondary", use_container_width=True):
            # Clear all session state
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

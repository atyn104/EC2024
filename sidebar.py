import streamlit as st

st.set_page_config(page_title="Student Performance Metrics")

# ⚠️ Menonaktifkan navigasi sidebar default Streamlit
# Ini memerlukan file .streamlit/config.toml dengan [client] showSidebarNavigation = false

# --- Menu Navigasi di Badan Utama Aplikasi ---
selected_page_title = st.selectbox(
    "Pilih Halaman",
    list(PAGES.keys()),
    index=0 # Default ke Homepage
)

# Halaman yang tersedia (hanya untuk referensi)
PAGES = {
    "Homepage": "home.py",
    "Objective Number 1": "Performance Metrics.py",
    "Objective Number 2": "obj number 2.py",
    "Objective Number 3": "obj number 3.py",
}


# Ganti halaman
if selected_page_title:
    target_page = PAGES[selected_page_title]
    # PENTING: st.switch_page hanya berfungsi di aplikasi multi-halaman
    # dengan file di folder 'pages'. 
    # Jika Anda menggunakan struktur file yang rata, Anda harus mengimpor 
    # dan menjalankan konten halaman secara langsung.
    # Jika Anda menggunakan folder 'pages', gunakan:
    # st.switch_page(target_page) 

    # Karena Anda menggunakan st.Page di contoh, Anda mungkin 
    # menjalankan file ini dan file-file lain di direktori yang sama. 
    # Untuk meniru st.navigation(), Anda harus menggunakan st.switch_page() 
    # atau mengganti st.navigation() dengan logika tampilan yang kompleks.

    st.write(f"Anda memilih untuk pergi ke: {selected_page_title}") 
    # Tambahkan st.switch_page(target_page) di sini

# Sembunyikan sidebar (jika diperlukan)
# Ini adalah trik CSS, gunakan dengan hati-hati!
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        display: none
    }
    </style>
    """, unsafe_allow_html=True)

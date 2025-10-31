import streamlit as st

st.set_page_config(
    page_title="Student Performance Metrics "
)

# 1. Tentukan Semua Halaman
home = st.Page('home.py', title='Homepage', default=True, icon=":material/home:")
objective2 = st.Page('obj number 2.py', title='Objective 2', icon=":material/ads_click:")
objective3 = st.Page('obj number 3.py', title='Objective 3', icon=":material/ads_click:")

# Halaman-halaman yang ingin dijadikan sub-menu
visualise_graph = st.Page('Visualise_Graph.py', title='Graph', icon=":material/insights:")
visualise_metrics = st.Page('Performance Metrics.py', title='Performance Metrics', icon=":material/trending_up:")


# 2. Susun Halaman dalam Kamus untuk st.navigation
# 'Menu' akan menjadi tajuk utama (section header) dalam sidebar.
# 'Visualise' akan menjadi tajuk dropdown (group header) di bahagian atas.
pages_dictionary = {
    # Bahagian Sidebar Utama (tanpa dropdown, hanya senarai)
    "Menu": [home, objective2, objective3],
    
    # Bahagian Navigasi Atas (yang akan menjadi dropdown)
    "Visualise": [visualise_graph, visualise_metrics],
}


# 3. Tetapkan st.navigation dengan posisi "top"
# Ini akan memaparkan 'Menu' di sidebar, dan 'Visualise' sebagai dropdown di bahagian atas app.
pg = st.navigation(pages_dictionary, position="top")

pg.run()

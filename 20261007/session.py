def session_manager():

    if "user_list" not in st.session_state:
        st.session_state.user_list = []

    with st.form("input_form"):
        name = st.text_input("이름")
        if st.form_submit_button("등록") and name :
            st.session_state.user_list.append(name)
import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Use the Hasher module to generate Hashed passwords, delete this after generating 
hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
print(hashed_passwords)

# Streamlit authenticator config for login
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

name, authentication_status, username = authenticator.login()

# Streamlit app

if authentication_status:
    authenticator.logout('Logout', 'main')
    st.subheader('Lorem Ipsum')
    st.write(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

    Pharetra convallis posuere morbi leo urna molestie at elementum. Non blandit massa enim nec dui nunc mattis enim ut. Tempus iaculis urna id volutpat. Nunc non blandit massa enim nec. In pellentesque massa placerat duis ultricies lacus sed. At urna condimentum mattis pellentesque. Natoque penatibus et magnis dis parturient montes nascetur ridiculus mus. Adipiscing elit ut aliquam purus sit amet luctus. Aliquet bibendum enim facilisis gravida neque. Morbi quis commodo odio aenean sed adipiscing diam donec adipiscing. Aliquet nibh praesent tristique magna sit amet purus. Lobortis scelerisque fermentum dui faucibus in. Dictum at tempor commodo ullamcorper a lacus vestibulum. Cursus eget nunc scelerisque viverra mauris in aliquam sem fringilla. Cursus metus aliquam eleifend mi in. Convallis a cras semper auctor neque vitae tempus quam pellentesque. Magna ac placerat vestibulum lectus mauris ultrices eros. Arcu ac tortor dignissim convallis aenean et tortor at. Mollis nunc sed id semper risus in.
    """
    )
    
    def footer():
        st.markdown("""
        <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f5f5f5;
            color: black;
            text-align: center;
        }
        </style>
        <div class="footer">
        <p>Please note that this is just a learning project, hence it may not follow all best practices.</p>
        </div>
        """, unsafe_allow_html=True)

    footer()
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')

st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
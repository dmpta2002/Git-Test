import streamlit as st

def main():
    st.title("Streamlit Presents:")
    st.write("The Emergency Broadcast System")

    # Display the video
    video_url = "https://youtu.be/wdpLWML_tDU?si=rmM-_JE2-3EUnier"
    st.video(video_url)

if __name__ == "__main__":
    main()


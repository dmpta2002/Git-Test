import streamlit as st

def main():
    st.title("Hello, World with Video!")
    st.write("This is a Streamlit app that displays a 'Hello, World!' message along with a video.")

    # Display the video
    video_url = "https://youtu.be/hp4pYFASTrc"
    st.video(video_url)

if __name__ == "__main__":
    main()


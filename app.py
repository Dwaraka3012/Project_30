import streamlit as st
from emoji import emojize
import pywhatkit


def playvideo(video_title):
    try:
        pywhatkit.playonyt(video_title)
    except Exception as e:
        print("something went wrong Check with Developer")

def ask_questions():
    st.subheader("Additional Questions")
    
    # List of additional questions and their corresponding videos
    additional_questions = [
        {"question": "Do you want to know how i feel when i saw you for the first time?", "video": "https://youtube.com/shorts/sP7OCKYTg0U?si=Jqhklb_rr7PEaiee"},
        {"question": "Do you want to know how i feel when your not taking to me?", "video": "https://www.youtube.com/shorts/x0-y26W9aOw"}
    ]

    for i, q in enumerate(additional_questions):
        # Display the question and radio button
        st.write(f"Question {i + 1}: {q['question']}")
        user_choice = st.radio(
            f"Please select an option for Question {i + 1}:",
            ["Yes", "No"],
            key=f"video_choice_{i}"
        )

        # Handle user choice
        if user_choice == "Yes":
            playvideo(q["video"])
        elif user_choice == "No":
            st.write("Thanks for your confirmation! 😊")
        st.write("---")  # Add a separator between questions

def main():
    st.title("Romantic App")
    
    # List of questions and their correct answers
    questions = [
        {"question":"You want a iteam for every year (you wishing to buy that every year:)", "answer": "Diary"},
        {"question":"What gift I gave to you for first time ", "answer": "Earrings"},
        {"question": "Which i like in you most?", "answer": "Eyes"},
        {"question":"On the day1 you saw me right which color shirt i wear on that day?","answer":"Black"}
    ]
    # Initialize session state for score
    if 'score' not in st.session_state:
        st.session_state.score = 0
    
    # Create two columns
    col1, col2 = st.columns(2)

    with col1:
        # Iterate through each question
        for index, q in enumerate(questions):
            st.subheader(f"Question {index + 1}")
            st.write(q["question"])
        
            # Input for the user's answer
            user_answer = st.text_input(f"Your Answer for Question {index + 1}", key=f"answer_{index}")

            # Submit button for each question
            if st.button(f"Submit Answer for Question {index + 1}", key=f"submit_{index}"):
                if user_answer.strip().lower() == q["answer"].strip().lower():
                    st.balloons()
                    st.success("Congratulations! Your answer is correct.")
                    st.write("Congratulation you won the points",emojize(":star-struck:"),emojize(":trophy::confetti_ball:"))
                    if f"answered_{index}" not in st.session_state:
                            st.session_state.score += 1
                            st.session_state[f"answered_{index}"] = True
                else:
                    st.error("Sorry, your answer is incorrect.")
                    st.write("Sorry you given answer is absolute Wrong ",emojize(":pensive_face:"))
    with col2:
         st.image("F:\website.png")

# Display the final score
    st.write("---")
    st.caption("You won points are:",st.session_state.score)

    st.write("----")
    ask_questions()
if __name__ == "__main__":
    main()


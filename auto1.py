import streamlit as st

# Sample list of suggestions
suggestions = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def main():
    st.title("Text Input with Autocomplete Dropdown")

    # Text input for custom input
    custom_input = st.text_input("Enter a fruit:", "")

    # Filter suggestions based on user input
    filtered_suggestions = [sugg for sugg in suggestions if custom_input.lower() in sugg.lower()]

    # Display suggestions as a dropdown
    if filtered_suggestions:
        selected_suggestion = st.selectbox("Select a suggestion:", filtered_suggestions)
        st.write("Selected Suggestion:", selected_suggestion)

if __name__ == "__main__":
    main()

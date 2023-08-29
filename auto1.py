import streamlit as st

# Sample list of preset options
preset_options = ['Option 1', 'Option 2', 'Option 3', 'Option 4']

def main():
    st.title("Text Input with Autocomplete and Preset Options")

    # Text input for custom input with autocomplete
    custom_input = st.text_input("Enter your own option:", "", key="custom_input")

    # Filter preset options based on user input
    filtered_options = [option for option in preset_options if custom_input.lower() in option.lower()]

    # Dropdown for preset options
    selected_option = st.selectbox("Select a preset option:", filtered_options)

    st.write("Custom Input:", custom_input)
    st.write("Selected Preset Option:", selected_option)

if __name__ == "__main__":
    main()

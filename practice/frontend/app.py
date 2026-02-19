# 'import' tells Python to bring in a library (a toolkit).
# 'streamlit' is the toolkit that builds the website.
# 'as st' means we can just type 'st' instead of the long word 'streamlit'.
import streamlit as st

# 'st.set_page_config' sets the text that appears on the browser tab.
st.set_page_config(page_title="Task 2: Calculator")

# 'st.title' puts a big, bold heading at the very top of the page.
st.title("🔢 Calculator with History")

# 'if' checks a condition.
# 'st.session_state' is the app's long-term memory.
# 'not in' checks if the word 'history' is missing from that memory.
if 'history' not in st.session_state:
    # 'st.session_state.history = []' creates an empty list (the square brackets).
    # This is where we will store the text of our calculations.
    st.session_state.history = []

# 'st.subheader' creates a smaller heading.
st.subheader("Inputs")

# 'st.number_input' creates a box for typing numbers.
# 'value=0.0' sets the starting number in the box to zero.
num1 = st.number_input("Enter first number:", value=0.0)
num2 = st.number_input("Enter second number:", value=0.0)

# 'st.selectbox' creates a dropdown menu.
# The items in ['square brackets'] are the options the user can click.
operation = st.selectbox("Choose operation:", ["Add (+)", "Subtract (-)", "Multiply (*)", "Divide (/)"])

# 'if st.button' only runs the code inside it when the user clicks 'Calculate'.
if st.button("Calculate"):
    # 'result = None' creates a variable to hold our answer, but starts it as empty.
    result = None
    # 'error_found = False' acts like a switch. We assume there is no error at the start.
    error_found = False
    
    # 'if "Add" in operation' checks if the user chose the Addition option.
    if "Add" in operation:
        # '+' is the math symbol for addition.
        result = num1 + num2
    # 'elif' is short for 'else if' (it checks the next option).
    elif "Subtract" in operation:
        # '-' is the math symbol for subtraction.
        result = num1 - num2
    elif "Multiply" in operation:
        # '*' is the math symbol for multiplication.
        result = num1 * num2
    elif "Divide" in operation:
        # This nested 'if' checks if the second number is zero before dividing.
        if num2 == 0:
            # 'st.error' shows a red message box to the user.
            st.error("Error: Cannot divide by zero!")
            # We flip our 'switch' to True so the app knows an error happened.
            error_found = True
        else:
            # '/' is the math symbol for division.
            result = num1 / num2

    # 'if not error_found' means: "Only do this if no error happened."
    if not error_found:
        # 'st.success' shows a green message box with the final answer.
        # 'f' before the string lets us put variables like {result} inside the text.
        st.success(f"The result is: {result}")
        
        # 'calc_string' creates a sentence like "5.0 + 5.0 = 10.0".
        calc_string = f"{num1} {operation} {num2} = {result}"
        
        # '.insert(0, ...)' adds our new calculation to the START (index 0) of the list.
        st.session_state.history.insert(0, calc_string)
        
        # '[:5]' is a "slice." It cuts the list so it only keeps the first 5 items.
        # This satisfies the "Last 5" requirement in your task.
        st.session_state.history = st.session_state.history[:5]

# 'st.write("---")' draws a horizontal line across the screen to separate sections.
st.write("---")
st.subheader("History (Last 5)")

# 'for item in ...' is a loop. It goes through every item in our history list one by one.
for item in st.session_state.history:
    # 'st.write(item)' prints each calculation onto the screen.
    st.write(item)
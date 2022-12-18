import re

# Define a dictionary of data
data = {
    "name": "John Smith",
    "age": 30,
    "location": "New York",
    "hobbies": ["reading", "running", "cooking"]
}

# Define a function to parse the answers
def parse_answer(question, data):
    # Extract the key from the question
    key = re.search(r"what is (\w+)", question).group(1)
    # Return the value for the key from the data dictionary
    return data[key]

# Start the chatbot loop
while True:
    # Get the user's input
    user_input = input("Enter a question or data: ")
    # Check if the user is asking a question
    if re.match(r"what is \w+", user_input):
        # Parse the answer from the data
        answer = parse_answer(user_input, data)
        print("The answer is:", answer)
    # Check if the user is entering data
    elif re.match(r"\w+ is \w+", user_input):
        # Split the user input into key and value
        key, value = user_input.split(" is ")
        # Update the data dictionary with the new value
        data[key] = value
    else:
        print("I'm sorry, I didn't understand your input.")

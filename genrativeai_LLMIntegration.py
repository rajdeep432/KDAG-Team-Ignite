# -*- coding: utf-8 -*-
"""GenrativeAI.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XMWa4jfRmxwftdhfUFrVRXGLcjWgiIhK

# A trivial prompt generation with GPT 3(Not implemented)
"""

def add_numbers(a, b):
    return a + b

# SELECT * FROM users;  # This is an SQL statement, not valid Python code

# document.body.style.backgroundColor = "blue";  # This is JavaScript code, not valid Python code

def simulate_llm_integration(prompt):
    """
    Simulates the integration with an LLM for code generation.
    This function is a stub to represent how you might call an LLM API
    and receive generated code based on a prompt.

    Parameters:
    - prompt (str): The natural language description or prompt for code generation.

    Returns:
    - str: The generated code snippet as a string.
    """

    # Example responses for demonstration purposes. In a real scenario,
    # this function would make an API call to an LLM like GPT-3 or GPT-4.
    example_responses = {
        "create a Python function to add two numbers": '''def add_numbers(a, b):\n    return a + b''',
        "generate a SQL query to select all from a table called users": '''SELECT * FROM users;''',
        "write JavaScript code to change the background color of a page to blue": '''document.body.style.backgroundColor = "blue";'''
    }

    # Return an example response based on the prompt, if available.
    return example_responses.get(prompt, "# No example available for this prompt.")

# Sample prompts for demonstration
prompts = [
    "create a Python function to add two numbers",
    "generate a SQL query to select all from a table called users",
    "write JavaScript code to change the background color of a page to blue"
]

# Simulating LLM integration with sample prompts
generated_code_examples = {prompt: simulate_llm_integration(prompt) for prompt in prompts}

# Displaying the generated code for each prompt
for prompt, code in generated_code_examples.items():
    print(f"Prompt: {prompt}\nGenerated Code:\n{code}\n")

"""# Open AI , Engine: code-davince-002
**This code was formulated correctly, but couldn't implement because of security restrictions , which can be avoided with authorised key**
"""

!pip install --upgrade openai
import openai

# Replacing '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' .
openai.api_key = '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'

def generate_code_with_gpt(prompt, engine="code-davinci-002", max_tokens=100):
    """
    Generates code based on a given prompt using the updated OpenAI GPT API.

    Parameters:
    - prompt (str): The prompt describing the code to generate.
    - engine (str): The ID of the OpenAI GPT engine to use.
    - max_tokens (int): The maximum number of tokens to generate.

    Returns:
    - str: The generated code.
    """
    try:
        response = openai.Completion.create(
            model=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=0.5,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        generated_code = response['choices'][0]['text'].strip()
        return generated_code
    except Exception as e:
        return f"Error generating code: {str(e)}"

# Example usage
prompt = "Write a Python function to check if a number is even."
generated_code = generate_code_with_gpt(prompt)
print("Generated Code:\n", generated_code)

"""# LLM: EleutherAI GPT-Neo-2.7B
**Since this code is executed in colab so the RAM is limited which exceeded the capacity . To execute this LLM model , Colab PRO is required which has more RAM**
"""

!pip install transformers

from transformers import pipeline

# Load the GPT-J model pipeline for text generation
generator = pipeline('text-generation', model='EleutherAI/gpt-j-6B', device=0)  # Use device=0 for GPU

# Define a prompt for code generation
prompt = "Write a Python function to check if a number is even:"

# Generate code using the model
generated_texts = generator(prompt, max_length=100, num_return_sequences=1)

# Print the generated code
for generated in generated_texts:
    print("Generated Code:\n", generated['generated_text'])

from transformers import pipeline

# Function to generate code using a specified LLM model
def generate_code(prompt, model_name='EleutherAI/gpt-neo-2.7B'):
    """
    Generates code from a natural language description using the specified LLM model.

    Parameters:
    - prompt (str): Natural language description of the code to generate.
    - model_name (str): Model identifier for the Hugging Face Transformers library.

    Returns:
    - str: Generated code snippet.
    """
    try:
        # Load the model and tokenizer and setup the generation pipeline
        generator = pipeline('text-generation', model=model_name)

        # Generate code based on the prompt
        results = generator(prompt, max_length=100, num_return_sequences=1)

        # Extract and return the generated code
        generated_code = results[0]['generated_text']
        return generated_code
    except Exception as e:
        return f"Error generating code: {e}"

# Example usage
prompt = "Write a Python function to calculate the factorial of a number:"
generated_code = generate_code(prompt)
print("Generated Code:\n", generated_code)

"""# LLM: DistilGPT-2
**This LLM was implemented completely in this current environment with 60 prompts**
"""

from transformers import pipeline
# Initialize a pipeline for text generation using DistilGPT-2
generator = pipeline('text-generation', model='distilgpt2')

# Define a prompt for code generation
prompt = "Write a Python function to check if a number is even:"

# Generate code with the specified prompt
generated_texts = generator(prompt, max_length=50, num_return_sequences=1)

# Print the generated code
for generated in generated_texts:
    print("Generated Code:\n", generated['generated_text'])

!pip install transformers torch

"""# Prompt Engineering
**(Generating prompts related to data manipulation, analysis and user interface elements)**
Total Prompts:60
Divided into 3 categories i.e. data manipulation, analysis and user interface elements.
In the current code a sample from each batch is shown.
To see the complete batch refer to these text files (generate them from the executing the last code) which contains prompts for the three categories.


1.   Data Manipulation
2.   Data Analysis
3.   User Interface elements


"""

from transformers import pipeline
import torch

# Function to initialize and return a text-generation pipeline
def get_text_generation_pipeline(model_name='distilgpt2'):
    """
    Initializes a text-generation pipeline with the specified model.

    Parameters:
    - model_name (str): Identifier for the model to use.

    Returns:
    - A text generation pipeline object.
    """
    # Check if GPU is available and specify the device accordingly
    device = 0 if torch.cuda.is_available() else -1
    return pipeline('text-generation', model=model_name, device=device)

# Function to generate code using the specified pipeline and prompt
def generate_code(pipeline, prompt, max_length=50):
    """
    Generates code based on a given prompt using the specified text-generation pipeline.

    Parameters:
    - pipeline: The text generation pipeline.
    - prompt (str): The prompt describing the code to generate.
    - max_length (int): The maximum length of the generated text.

    Returns:
    - str: The generated code snippet.
    """
    try:
        # Generate text with the provided prompt
        results = pipeline(prompt, max_length=max_length, num_return_sequences=1)
        return results[0]['generated_text']
    except Exception as e:
        return f"Error generating code: {str(e)}"

# Example usage
text_gen_pipeline = get_text_generation_pipeline()
prompt = "Write a Python function to check if a number is even:"
generated_code = generate_code(text_gen_pipeline, prompt)
print("Generated Code:\n", generated_code)

from transformers import pipeline
import torch

# Initialize the text-generation pipeline with GPU support if available
device = 0 if torch.cuda.is_available() else -1
text_gen_pipeline = pipeline('text-generation', model='distilgpt2', device=device)

# Define the new prompt for code generation
prompt = "Create a JavaScript function that fetches user data from a placeholder API and displays the users' names and emails in a list on a webpage."

# Generate code using the pipeline and the prompt
try:
    results = text_gen_pipeline(prompt, max_length=150, num_return_sequences=1)
    generated_code = results[0]['generated_text']
except Exception as e:
    generated_code = f"Error generating code: {str(e)}"

print("Generated Code:\n", generated_code)

# Assuming the previous setup and functions are already defined and executed

# New prompt for generating JavaScript code
new_prompt = """
Write JavaScript code to fetch user data from the URL 'https://api.example.com/users',
then update the HTML element with id 'user-list' to display a list of user names.
"""

# Generate code using the new prompt
generated_code = generate_code(text_gen_pipeline, new_prompt, max_length=150)  # Increased max_length for more complex output

print("Generated Code:\n", generated_code)

def simulate_code_generation(prompt):
    """
    Simulates code generation for data manipulation prompts.

    Parameters:
    - prompt (str): Description of the coding task.

    Returns:
    - str: Simulated code snippet for the task.
    """
    # Mapping prompts to their simulated code snippets
    prompt_to_code = {
        "Write a Python function to merge two dictionaries": "def merge_dicts(d1, d2):\n    return {**d1, **d2}",
        "Generate SQL to update the 'email' of a 'users' table where 'user_id' is 10": "UPDATE users SET email = 'newemail@example.com' WHERE user_id = 10;",
        "Create a JavaScript function that removes duplicates from an array": "function removeDuplicates(array) {\n  return [...new Set(array)];\n}",
        "Write a Python script to convert a CSV file into a JSON file": "import csv\nimport json\n\ndef csv_to_json(csv_filepath, json_filepath):\n    with open(csv_filepath, mode='r') as infile, open(json_filepath, mode='w') as outfile:\n        reader = csv.DictReader(infile)\n        json.dump(list(reader), outfile, indent=4)",
        "Develop a SQL query to select users with more than one order from the 'orders' table": "SELECT user_id FROM orders GROUP BY user_id HAVING COUNT(order_id) > 1;",
        "Craft a JavaScript snippet to sort an array of objects by a 'date' attribute": "array.sort((a, b) => new Date(a.date) - new Date(b.date));",
        "Formulate a Python function to find the intersection of two lists": "def intersect(lst1, lst2):\n    return list(set(lst1) & set(lst2))",
        "Construct a SQL command to delete records from 'log' table older than 1 year": "DELETE FROM log WHERE log_date < NOW() - INTERVAL 1 YEAR;",
        "Design a JavaScript function to capitalize the first letter of each word in a string": "function capitalizeWords(str) {\n  return str.replace(/\\b\\w/g, char => char.toUpperCase());\n}",
        "Create a Python snippet to send an email with SMTP": "import smtplib\nfrom email.mime.text import MIMEText\n\ndef send_email(subject, message, from_addr, to_addr, smtp_server):\n    msg = MIMEText(message)\n    msg['Subject'] = subject\n    msg['From'] = from_addr\n    msg['To'] = to_addr\n\n    server = smtplib.SMTP(smtp_server)\n    server.send_message(msg)\n    server.quit()",
        # Additional prompts and their corresponding code snippets would continue here
    }

    # Return the code snippet for the provided prompt
    return prompt_to_code.get(prompt, "No code snippet available for this prompt.")

# Example usage of the function
prompts = [
    "Write a Python function to merge two dictionaries",
    "Generate SQL to update the 'email' of a 'users' table where 'user_id' is 10",
    # Add more prompts as needed
]

# Iterating over prompts to simulate code generation
for prompt in prompts:
    print(f"Prompt: {prompt}\nGenerated Code:\n{simulate_code_generation(prompt)}\n")

def simulate_ui_code_generation(prompt):
    """
    Simulates code generation for user interface elements prompts.

    Parameters:
    - prompt (str): Description of the UI task.

    Returns:
    - str: Simulated code snippet for the task.
    """
    # Mapping prompts to their simulated code snippets
    prompt_to_code = {
        "Write HTML and CSS to create a responsive navigation menu":
        '''HTML:
<nav class="responsive-nav">
    <ul>
        <li><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Services</a></li>
        <li><a href="#">Contact</a></li>
    </ul>
</nav>

CSS:
.responsive-nav ul {
    list-style-type: none;
    padding: 0;
}
.responsive-nav li {
    display: inline-block;
    margin-right: 20px;
}
@media (max-width: 600px) {
    .responsive-nav li {
        display: block;
        margin-bottom: 10px;
    }
}''',

        "Generate JavaScript to dynamically update a progress bar based on user input":
        '''<progress id="file-progress" value="0" max="100"></progress>
<input type="file" id="file-input" />

<script>
document.getElementById('file-input').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onprogress = function(event) {
        if (event.lengthComputable) {
            const percentLoaded = Math.round((event.loaded / event.total) * 100);
            document.getElementById('file-progress').value = percentLoaded;
        }
    };
    reader.readAsDataURL(file);
});
</script>''',

        "Create a React component for a user profile card":
        '''import React from 'react';

function UserProfileCard({ user }) {
    return (
        <div className="user-profile-card">
            <img src={user.avatar} alt={`${user.name}'s avatar`} />
            <h2>{user.name}</h2>
            <p>{user.bio}</p>
        </div>
    );
}

export default UserProfileCard;''',

        # Other prompts follow similar structure...
    }

    # Return the code snippet for the provided prompt
    return prompt_to_code.get(prompt, "No code snippet available for this prompt.")

# Example usage of the function
prompts = [
    "Write HTML and CSS to create a responsive navigation menu",
    "Generate JavaScript to dynamically update a progress bar based on user input",
    # Add more prompts as needed
]

# Iterating over prompts to simulate UI code generation
for prompt in prompts:
    print(f"Prompt: {prompt}\nGenerated Code:\n{simulate_ui_code_generation(prompt)}\n")

def simulate_data_analysis_code_generation(prompt):
    """
    Simulates code generation for data analysis prompts.

    Parameters:
    - prompt (str): Description of the data analysis task.

    Returns:
    - str: Simulated code snippet for the task.
    """
    # Mapping prompts to their simulated code snippets
    prompt_to_code = {
        "Write a Python function to calculate the mean, median, and mode of a dataset":
        '''import numpy as np
from scipy import stats

def calculate_statistics(data):
    mean = np.mean(data)
    median = np.median(data)
    mode = stats.mode(data)[0][0]
    return mean, median, mode''',

        "Generate a Python script using pandas to read a CSV and filter rows by a column value":
        '''import pandas as pd

df = pd.read_csv('data.csv')
filtered_df = df[df['column_name'] > some_value]
print(filtered_df)''',

        "Create a Matplotlib plot to visualize the sales data over the past year":
        '''import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_data.csv')
plt.plot(df['Month'], df['Sales'])
plt.title('Sales Over the Past Year')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()''',

        "Develop a SQL query to calculate the average purchase amount per customer":
        '''SELECT customer_id, AVG(purchase_amount) AS average_purchase
FROM purchases
GROUP BY customer_id;''',

        "Formulate a Python code snippet using NumPy to solve a system of linear equations":
        '''import numpy as np

# Example system: a + 2b = 5, 3a + 4b = 6
A = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])
solution = np.linalg.solve(A, b)
print(solution)''',

        # Additional prompts and code snippets can be added here...
    }

    # Return the code snippet for the provided prompt
    return prompt_to_code.get(prompt, "No code snippet available for this prompt.")

# Example usage of the function
prompts = [
    "Write a Python function to calculate the mean, median, and mode of a dataset",
    "Generate a Python script using pandas to read a CSV and filter rows by a column value",
    # Continue with other prompts as needed...
]

# Iterating over prompts to simulate data analysis code generation
for prompt in prompts:
    print(f"Prompt: {prompt}\nGenerated Code:\n{simulate_data_analysis_code_generation(prompt)}\n")

"""# Error handling"""

# Feedback Collection Mechanism

from flask import Flask, request, jsonify
app = Flask(__name__)

# Placeholder for storing feedback
feedback_db = []

@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    feedback_data = request.json
    feedback_db.append(feedback_data)
    # Here, you would have logic to process and categorize the feedback,
    # such as saving it to a database and flagging it for review.
    return jsonify({"status": "success", "message": "Feedback received"}), 200

# Example of feedback data structure
# {
#   "prompt": "Generate a Python function to add two numbers",
#   "generated_code": "def add(a, b): return a + b",
#   "feedback": "The code works as expected, but lacks error checking for non-numeric inputs.",
#   "error_reported": "",
#   "user_rating": 4
# }

if __name__ == '__main__':
    app.run(debug=True)

# Simulated code generation based on a prompt
def generate_code(prompt):
    # Simulating code generation for a specific prompt
    if prompt == "sum two numbers in Python":
        return "def sum_numbers(a, b):\n    return a + b"
    return "# No code for this prompt"

# Simulated error checking function
def check_code_for_errors(code):
    if "def" not in code:
        return True, "Error: Code does not define a function."
    return False, "No errors found."

# Function to simulate collecting feedback
def collect_feedback():
    prompt = "sum two numbers in Python"  # Example prompt
    generated_code = generate_code(prompt)

    # Check for errors in the generated code
    has_errors, error_message = check_code_for_errors(generated_code)
    print(f"Generated Code:\n{generated_code}\n")

    if has_errors:
        print(f"Error Detected: {error_message}")
        # Here, you could log the error or send it to a database for analysis

    # Simulate asking for user feedback
    feedback = input("Please provide your feedback on the generated code: ")
    print("Thank you for your feedback!")

    # Here, you would normally store the feedback for further analysis or model improvement
    return feedback

# Execute the feedback collection function
feedback = collect_feedback()
print(f"Collected Feedback: {feedback}")

# Simulated Model Training and A/B Testing

# Function to simulate training a model with data
def train_model(data):
    print(f"Training model with data size: {len(data)}")
    # Simulate model training and return a mock model performance metric
    performance = len(data) * 0.1  # Simplified performance metric
    return performance

# Function to simulate A/B testing between two models
def ab_test(model_a_perf, model_b_perf):
    print(f"Model A Performance: {model_a_perf}, Model B Performance: {model_b_perf}")
    if model_a_perf > model_b_perf:
        print("Model A wins!")
    else:
        print("Model B wins!")

# Simulated User Feedback Collection

def collect_feedback():
    feedback = input("Please provide your feedback on the model's performance: ")
    print("Feedback collected: ", feedback)
    # For simplicity, feedback will just adjust the size of the training data
    return len(feedback)

# Main workflow

# Step 1: Simulate initial model training
initial_data = [1, 2, 3]  # Placeholder for initial training data
model_a_perf = train_model(initial_data)

# Step 2: Collect new data based on user feedback
feedback_data_size = collect_feedback()
new_data = list(range(feedback_data_size))

# Step 3: Train a new model with the feedback-informed data
model_b_perf = train_model(new_data)

# Step 4: Perform A/B testing to decide which model to deploy
ab_test(model_a_perf, model_b_perf)

"""**This is was code which can be executed in the current environment. for full scale production of three LLMs implementation , we have to use more RAM and would require heavy computational time**

**Additional Code (Converting all the prompts into text files)**
**Execute this code to make the .txt files**
"""

# Let's create three text files with sample prompts for each of the specified categories.

data_manipulation_prompts = [
    "Write a Python function to merge two dictionaries."
"Generate SQL to update the 'email' of a 'users' table where 'user_id' is 10."
"Create a JavaScript function that removes duplicates from an array."
"Write a Python script to convert a CSV file into a JSON file."
"Develop a SQL query to select users with more than one order from the 'orders' table."
"Craft a JavaScript snippet to sort an array of objects by a 'date' attribute."
"Formulate a Python function to find the intersection of two lists."
"Construct a SQL command to delete records from 'log' table older than 1 year."
"Design a JavaScript function to capitalize the first letter of each word in a string."
"Create a Python snippet to send an email with SMTP."
"Generate a SQL query to find the top 3 most expensive products in 'products' table."
"Write a JavaScript code to dynamically add a table row with data to an existing HTML table."
"Develop a Python function to compress a file using gzip."
"Compose a SQL statement to alter a table 'employees', adding a column 'birthdate'."
"Script a JavaScript function to fetch data from an API and log it to the console."
"Write a Python code snippet to read a specific sheet from an Excel file and print its content."
"Create a SQL query to count the number of transactions per user in 'transactions' table."
"Design a JavaScript code snippet to replace all instances of a string in a text area."
"Formulate a Python function to calculate the age given a birthdate."
"Generate a SQL query to find all users who have not logged in in the last month."
]

data_analysis_prompts = [
    "Write a Python function to calculate the mean, median, and mode of a dataset."
"Generate a Python script using pandas to read a CSV and filter rows by a column value."
"Create a Matplotlib plot to visualize the sales data over the past year."
"Develop a SQL query to calculate the average purchase amount per customer."
"Formulate a Python code snippet using NumPy to solve a system of linear equations."
"Write a JavaScript function to calculate the standard deviation of an array of numbers."
"Generate a Python Jupyter notebook cell that displays a correlation matrix heatmap using Seaborn."
"Create an R script to perform a linear regression analysis on a dataset."
"Develop a Python script to scrape weather data from a webpage and parse it into a CSV file."
"Write a SQL query to find the month-over-month growth rate in sales."
"Formulate a Python function using scikit-learn to cluster a dataset using K-means."
"Generate a plot in Python with Plotly to show the distribution of a dataset."
"Create a JavaScript code snippet to dynamically display data on a webpage using D3.js."
"Develop a Python script to automate the download of stock prices and calculate their moving average."
"Write an SQL query to segment users into cohorts based on their signup date."
"Generate a Python notebook cell that uses TensorFlow to predict house prices based on a dataset."
"Design a dashboard in Power BI to analyze sales data from multiple sources."
"Create a Python script to detect outliers in a dataset using the Z-score method."
"Develop a SQL query to rank products based on the number of times they were purchased."
"Write a Python function to automate the generation of a PDF report summarizing key metrics from a dataset."
]

user_interface_elements_prompts = [
"Write HTML and CSS to create a responsive navigation menu."
"Generate JavaScript to dynamically update a progress bar based on user input."
"Create a React component for a user profile card."
"Design a CSS stylesheet for a form that uses Flexbox for layout."
"Develop a JavaScript snippet to validate an email field in a form."
"Write a Python Flask route to render a template with a list of items."
"Create an animated loading spinner with CSS animations."
"Generate a Vue.js component for a dropdown menu that fetches its items from an API."
"Design a mobile-responsive layout using Bootstrap for a dashboard page."
"Write JavaScript code to implement a modal popup when a button is clicked."
"Create a CSS theme switcher to toggle between light and dark modes."
"Develop a dynamic search filter in JavaScript that filters items on a webpage as you type."
"Formulate a React hook for fetching and storing data from an API."
"Generate HTML and CSS for a footer section with social media links."
"Write a Vue.js directive that auto-focuses on an input field when a form is loaded."
"Design an interactive slider with JavaScript and CSS."
"Create an Angular service for handling HTTP GET requests to an API."
"Develop a CSS grid layout for a photo gallery."
"Script a JavaScript countdown timer for a quiz application."
"Write HTML and CSS to style a table with alternating row colors and hover effects."
]

# Define a function to save prompts to text files
def save_prompts_to_file(file_name, prompts_list):
    with open(f"/content/{file_name}.txt", "w") as file:
        for prompt in prompts_list:
            file.write(prompt + "\n")

# Save each batch of prompts to its respective file
save_prompts_to_file("data_manipulation_prompts", data_manipulation_prompts)
save_prompts_to_file("data_analysis_prompts", data_analysis_prompts)
save_prompts_to_file("user_interface_elements_prompts", user_interface_elements_prompts)

# Return the file paths for downloading
"/content/data_manipulation_prompts.txt", "/content/data_analysis_prompts.txt", "/content/user_interface_elements_prompts.txt"

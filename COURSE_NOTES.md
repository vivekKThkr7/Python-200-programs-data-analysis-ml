# Python 200 Programs — Course Notes

These notes collect the main ideas from the later sections of the Python 200-program course. The repository contains 200 numbered programs and 200 matching challenges, progressing from Python fundamentals to data analysis and introductory machine learning.

## Course roadmap

| Program range | Main topic |
|---|---|
| 1–20 | Python fundamentals |
| 21–40 | Decision making |
| 41–60 | Loops and algorithms |
| 61–70 | Strings |
| 71–90 | Lists and structured data |
| 91–100 | Functions and reusable code |
| 101–110 | Dictionaries |
| 111–120 | Tuples, sets, and choosing data structures |
| 121–130 | Exception handling |
| 131–140 | Object-oriented programming (OOP) fundamentals |
| 141–150 | Encapsulation, inheritance, and polymorphism |
| 151–160 | Cleaner, more practical Python |
| 161–170 | Building a small real-world project |
| 171–180 | Reliable file paths and error handling |
| 181–190 | APIs and HTTP requests |
| 191–200 | NumPy, Pandas, visualization, and machine learning |

## Programs 91–100: Functions — turning code into reusable tools

A **function** is a named block of code that performs a specific task. Functions let us write a piece of logic once and reuse it whenever we need it.

The main ideas in this section are defining a function, calling it, passing information through parameters, and returning a result.

## Programs 101–110: Dictionaries — storing data with meaning

A **dictionary** stores data as key-value pairs. Each key identifies the value associated with it.

```python
student = {
    "name": "Vivek",
    "age": 27,
    "country": "Nepal",
}
```

Compare these three ways of storing information:

```python
age = 27

ages = [20, 24, 38, 30]

ages_by_person = {
    "Vivek": 27,
    "Ram": 25,
    "Sita": 30,
}
```

- A variable stores one value under one name.
- A list stores an ordered collection of values.
- A dictionary stores values under meaningful keys.

## Programs 111–120: Tuples, sets, and choosing the right data structure

Python provides several built-in collection types. Choose one based on how the data should behave.

| Structure | Example | Changeable? | Duplicates? | Main idea |
|---|---|---:|---:|---|
| List | `[1, 2, 3]` | Yes | Yes | Ordered collection |
| Tuple | `(1, 2, 3)` | No | Yes | Ordered, fixed collection |
| Set | `{1, 2, 3}` | Yes | No | Unique values |
| Dictionary | `{"a": 1}` | Yes | Keys are unique | Key-value mapping |

### Simple memory trick

- **List** — many values that may change.
- **Tuple** — values grouped together that should not change.
- **Set** — unique values.
- **Dictionary** — named values stored as key-value pairs.

## Programs 121–130: Exception handling

An **exception** is an event that interrupts the normal flow of a program while it is running. For example, converting non-numeric text to an integer raises a `ValueError`.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a whole number.")
```

`try` contains code that may raise an exception. `except` handles a specified exception so the program can respond appropriately.

Handle expected errors specifically. Avoid catching every possible exception unless there is a clear reason to do so.

## Programs 131–140: Object-oriented programming — classes and objects

**Object-oriented programming (OOP)** organizes a program around objects that combine data and behaviour.

Think about a bank account. Its data may include the account holder and balance. Its behaviour may include depositing money, withdrawing money, and checking the balance.

| Term | Simple meaning |
|---|---|
| Class | A blueprint used to create objects |
| Object | An individual instance created from a class |
| Attribute | Data belonging to an object |
| Method | A function defined in a class |
| `self` | The current object instance inside an instance method |
| `__init__()` | The initializer called when an object is created |
| Instance | Another word for an object created from a class |

### Four important OOP ideas

1. **Class:** defines the structure and behaviour that objects can have.
2. **Object:** an actual instance created from a class.
3. **Inheritance:** a child class can reuse or extend behaviour from a parent class.
4. **Polymorphism:** different object types can respond to the same method call in different ways.

For example:

```python
employees = [
    Developer("Ram"),
    Designer("Sita"),
]

for employee in employees:
    employee.work()
```

`employees` refers to the whole list. `employee` refers to one object at a time. Each object's `work()` method can behave differently.

### Four related terms

| Concept | Simple meaning |
|---|---|
| Encapsulation | Keeping related data and behaviour together and controlling access to data |
| Inheritance | A child class reuses or extends a parent class |
| Method overriding | A child class provides its own version of an inherited method |
| Polymorphism | The same method call can produce different behaviour for different object types |

## Programs 141–150: OOP in practice

This section develops the OOP ideas through a small sequence of examples:

| Program | Topic |
|---:|---|
| 141 | Encapsulation |
| 142 | Getter methods |
| 143 | Setter methods |
| 144 | Inheritance |
| 145 | Adding child-class attributes |
| 146 | Reusing parent methods and adding child methods |
| 147 | Method overriding |
| 148 | Using `super()` with method overriding |
| 149 | Polymorphism |
| 150 | Mini OOP system |

Encapsulation groups an object's data with the methods that control it. Getter methods read a value; setter methods update a value in a controlled way. Inheritance lets a child class reuse a parent class's attributes and methods. A child class can add its own attributes, add methods, or override inherited methods. `super()` lets a child class call behaviour from its parent class.

## Programs 151–160: Writing cleaner, more practical Python

| Program | Topic |
|---:|---|
| 151 | `import` |
| 152 | Useful built-in modules |
| 153 | Creating your own module |
| 154 | Variable scope |
| 155 | Global and local variables |
| 156 | List comprehensions |
| 157 | Comprehensions with conditions |
| 158 | Dictionary comprehensions |
| 159 | Lambda functions |
| 160 | Combining these ideas |

## Programs 161–170: From Python exercises to a real project

A practical program connects several pieces into a workflow:

```text
User
  ↓
Input
  ↓
Validation
  ↓
Data structure
  ↓
Functions
  ↓
File storage
  ↓
Reports
```

The important lesson is that a real program is more than a single calculation. It accepts input, checks it, organizes information, performs operations, stores data when needed, and presents useful results.

## Programs 171–180: Making a real project reliable

### What is `pathlib`?

`pathlib` is a Python standard-library module for working with file-system paths. Instead of treating a path only as a string, it provides a `Path` object with useful methods for working with files and folders.

```python
from pathlib import Path

file_path = Path("outputs/text/notes.txt")
```

Here, `file_path` is a `Path` object representing `outputs/text/notes.txt`.

### Why raise an exception instead of printing an error inside a function?

Raising an exception allows the code that called the function to decide how to handle the problem. This separates the function's core work from the application's response to an error.

## Programs 181–190: Working with APIs and HTTP requests

| Program | Topic |
|---:|---|
| 181 | What an API is and how to make a GET request |
| 182 | HTTP status codes and successful responses |
| 183 | Query parameters |
| 184 | Reading and processing API data |
| 185 | Handling API errors and timeouts |
| 186 | Sending data using POST |
| 187 | Working with nested JSON |
| 188 | Building reusable API functions |
| 189 | Saving API data into a JSON file |
| 190 | Mini project: User Directory API |

### What is `requests`?

`requests` is a third-party Python library that makes it easier to send HTTP requests to web servers. Unlike `pathlib`, `json`, and `datetime`, it is not part of Python's standard library and must be installed.

```bash
python -m pip install requests
```

### What is an API?

**API** means **Application Programming Interface**. An API provides a defined way for one application to request information or services from another application.

A typical request-and-response flow looks like this:

```text
Python program → API / web server → response → Python program
```

An API request commonly uses a URL called an **endpoint**. For example, the course exercises use the JSONPlaceholder endpoint:

`https://jsonplaceholder.typicode.com/posts/1`

### What is HTTP?

**HTTP** (Hypertext Transfer Protocol) is the protocol used for communication between HTTP clients and servers.

- `GET` requests retrieve information.
- `POST` requests send data to a server, commonly to create a resource.

### What is an HTTP status code?

An HTTP status code is a number returned with an HTTP response that describes the result of the request.

| Status code | Meaning |
|---:|---|
| 200 | Request succeeded |
| 201 | Resource created |
| 400 | Bad request |
| 401 | Authentication required or failed |
| 403 | Access forbidden |
| 404 | Resource not found |
| 500 | Internal server error |

### Handling request errors and timeouts

Networks can fail, URLs can be incorrect, records can be missing, and a server can become temporarily unavailable.

| Exception | Typical meaning |
|---|---|
| `HTTPError` | An unsuccessful HTTP status was raised after checking the response |
| `Timeout` | The request took too long |
| `ConnectionError` | A network connection problem occurred |
| `RequestException` | The base exception class for request-related errors in `requests` |

Use exception handling to make API programs respond clearly to expected failures. A timeout should be set when a request must not wait indefinitely.

## Programs 191–200: NumPy, Pandas, visualization, and machine learning

This section connects numerical computing, data analysis, visualization, and introductory machine learning.

| Program | Topic |
|---:|---|
| 191 | NumPy arrays |
| 192 | NumPy calculations and statistics |
| 193 | Pandas DataFrames |
| 194 | Reading and writing CSV data |
| 195 | Handling missing values and duplicate records |
| 196 | Grouping and analysing data |
| 197 | Visualizing data with Matplotlib |
| 198 | Understanding machine learning and splitting data |
| 199 | Training and evaluating a machine-learning model |
| 200 | Final capstone: data analysis and machine-learning pipeline |

### Program 196: Grouping and analysing data

Suppose a company wants to know how much revenue each product category generated. We could loop through every record and calculate the totals manually, but Pandas provides the convenient `groupby()` operation.

`groupby()` divides records into groups based on one or more columns so that a calculation can be performed for each group. This is often described as **split–apply–combine**:

1. Split the data into groups.
2. Apply a calculation to each group.
3. Combine the results.

### Program 197: Visualizing data with Matplotlib

Numbers and tables are useful, but a chart can make a pattern easier to recognize. **Matplotlib** is a Python visualization library used to create line charts, bar charts, scatter plots, and other graphics.

A typical chart workflow is to create a figure and axes, draw the data, add labels, and then display or save the chart.

### Program 198: Understanding machine learning and splitting data

**Machine learning** is a field of artificial intelligence in which a model learns patterns from data and uses those patterns to make predictions.

Consider a program that identifies a flower type from its measurements:

```text
Flower measurements
        ↓
     Features
        ↓
Machine-learning model
        ↓
 Predicted flower type
```

- **Features (`X`)** are the input measurements used by the model.
- **Target (`y`)** is the answer or label the model is trained to predict.

The exercise uses the Iris dataset provided by scikit-learn. It contains 150 flower samples, four numerical measurements per sample, and three flower classes.

### Why split the data?

A dataset is commonly divided into two parts:

- **Training data** is used to fit the model and learn patterns.
- **Testing data** is held back to evaluate predictions on examples the model did not use during training.

### Program 199: Training and evaluating a machine-learning model

Training means giving an algorithm examples so it can learn patterns from the data.

For the Iris exercise:

- Features (`X`) contain flower measurements.
- Labels (`y`) identify the flower species.
- The training subset is used to fit the model.
- The test subset is used to evaluate predictions against the correct labels.

The overall process is:

```text
Dataset
   ↓
Train/test split
   ↓
Train the model on the training data
   ↓
Predict labels for the test data
   ↓
Compare predictions with the correct labels
```

Programs 198 and 199 use the Iris dataset. Program 199 evaluates a Logistic Regression classifier; Challenge 199 compares Logistic Regression with K-Nearest Neighbors (KNN) using the same train/test split.

### Program 200: Final capstone — data analysis and machine-learning pipeline

A **data-analysis and machine-learning pipeline** is a sequence of connected steps that turns raw data into useful information and model predictions.

The final capstone uses the Wine dataset provided by scikit-learn and brings together Pandas, visualization, and machine learning.

The workflow is:

1. Load the dataset.
2. Explore it with Pandas.
3. Inspect missing values and duplicate records.
4. Summarize and visualize the data.
5. Separate features from the target labels.
6. Split the data into training and testing subsets.
7. Train a machine-learning model.
8. Evaluate its predictions and try a prediction on a test example.

The Wine dataset used by the capstone contains 178 samples, 13 numerical features, and three target classes. The model workflow uses a scikit-learn `Pipeline` to keep `StandardScaler` preprocessing together with `LogisticRegression` training. The program saves its scatter plot to `outputs/charts/wine_scatter.png`.

This capstone is more than one Python exercise because it connects several tools in one workflow:

- **Pandas:** inspect and summarize the dataset.
- **Matplotlib:** visualize relationships in the data.
- **scikit-learn:** prepare data, train a model, and make predictions.
- **Evaluation metrics:** assess model performance.

An important real-world lesson: missing values and duplicate records should be handled according to the meaning of the dataset. Do not remove them automatically just because they exist.

## Code quality checklist

Use this checklist when writing or reviewing programs in the repository:

1. **Readable names:** choose variable, function, and class names that explain their purpose. Use `snake_case` for variables and functions and `PascalCase` for classes.
2. **Consistent formatting:** use four spaces for indentation, keep related code together, and include a final newline in each source file.
3. **Focused functions:** keep each function responsible for one clear task. Avoid unnecessary repeated code.
4. **Useful comments:** explain intent or a non-obvious decision rather than translating every line into English.
5. **Safe input and errors:** validate user input and catch specific expected exceptions.
6. **Reliable paths:** use `pathlib.Path` for file and folder paths rather than relying on the current working directory.
7. **Data care:** inspect missing values and duplicates before deciding how to handle them.
8. **Reproducible model evaluation:** keep training and testing data separate. Fit preprocessing steps on training data only; using a scikit-learn `Pipeline` helps keep preprocessing and model training together.
9. **Project organization:** keep source code, input data, and generated outputs in their appropriate folders. Do not commit virtual environments, caches, or secrets.
10. **Verification:** compile Python files and run appropriate exercises or tests before committing changes. Do not run every script blindly when it expects interactive input, makes network requests, or changes files.

### Repository verification

From the repository root, run:

```bash
python scripts/check_course_quality.py
git diff --check
```

The checker verifies the numbered program/challenge structure and Python syntax. It does not execute every exercise, because some exercises require input, network access, or create files.

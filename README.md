
Python 200 Programs: From Beginner to Data Analysis & Machine Learning

A hands-on Python learning repository containing 200 programs and practice challenges, organized into progressive sets. The project begins with Python fundamentals and problem-solving, then progresses toward data analysis and introductory machine learning.

This repository documents my learning journey through practical coding exercises. The goal was not only to learn Python syntax, but also to understand how to break problems into steps, write code, inspect results, debug errors, and apply Python libraries to real data.

Learning Goals
1. Build a strong foundation in Python syntax, variables, data types, and input/output.
2. Practice decision-making, loops, and algorithmic problem-solving.
3. Work with strings and Python collections.
4. Use functions, modules, files, and exception handling.
5. Understand object-oriented programming and more advanced Python concepts.
6. Analyze numerical and tabular data with NumPy and pandas.
7. Visualize data and build introductory machine-learning workflows with scikit-learn.
8. Develop the habit of testing code, checking results, and correcting logical errors.


Curriculum Overview: Programs 1–200
| Program numbers | Topics | Main skills practiced |
|---|---|---|
| **1–20** | Python fundamentals and data types | `print()`, `input()`, variables, arithmetic, strings, integers, floats, booleans, type conversion, and comparisons. |
| **21–40** | Conditions and decision-making | `if`, `elif`, `else`, logical operators, nested conditions, range checks, eligibility rules, and menu-based decision programs. |
| **41–60** | Loops and number algorithms | `while`, `for`, `range()`, nested loops, counters, accumulators, `break`, digit processing, reversing numbers, palindromes, factorials, prime checks, and number analysis. |
| **61–80** | Strings and collections | String indexing, slicing, searching, counting, cleaning and transforming text, followed by working with Python collections such as lists and tuples. |
| **81–100** | Dictionaries, sets, and functions | Organizing related data, working with unique values, creating reusable functions, and solving problems with structured data. |
| **101–120** | Files, exceptions, and modules | Reading and writing files, handling errors with `try`/`except`, and organizing code using modules. |
| **121–140** | Object-oriented programming (OOP) | Classes, objects, attributes, methods, and core object-oriented design concepts. |
| **141–160** | Advanced Python | More advanced language features and techniques that build on the fundamentals and improve code quality. |
| **161–180** | Practical programming and problem-solving | Applying earlier concepts to more complete programs and multi-step problems. |
| **181–190** | Advanced problem-solving and preparation for data work | Further practice leading into numerical computing, data analysis, and AI-oriented programming. |
| **191–200** | NumPy, pandas, visualization, and machine learning | Numerical arrays, statistics, DataFrames, CSV workflows, data cleaning, grouping, visualization, data splitting, model training/evaluation, and a final capstone. |

Final 10 Programs: Data Analysis and AI Foundations

| Program | Topic | What it practices |
|---|---|---|
| **191** | NumPy numerical arrays | Creating arrays, performing element-wise calculations, and accessing array elements. |
| **192** | NumPy calculations and statistics | Calculating totals, means, medians, minimums, maximums, and standard deviation. |
| **193** | pandas DataFrames | Creating tabular data, adding calculated columns, and filtering records. |
| **194** | Reading and writing CSV files | Saving a DataFrame to CSV, loading it again, and analyzing the loaded data. |
| **195** | Data cleaning | Finding missing values and duplicate records, and practicing suitable cleaning operations. |
| **196** | Grouping and analysis | Summarizing data by categories and comparing group-level results. |
| **197** | Data visualization | Creating charts to communicate patterns in data. |
| **198** | Understanding machine learning and data splitting | Separating features and labels, and preparing training and test sets with `train_test_split()`. |
| **199** | Training and evaluating a model | Training classifiers, generating predictions, and evaluating accuracy and classification results. |
| **200** | Data Analysis and AI Pipeline capstone | Combining data inspection, cleaning checks, grouped analysis, visualization, model training, prediction, and evaluation in one workflow. |

Capstone Project

The final capstone uses the Wine dataset from scikit-learn. It demonstrates an end-to-end introductory workflow:

1. Load the dataset and create a pandas DataFrame.
2. Inspect rows, dimensions, descriptive statistics, missing values, and duplicate rows.
3. Compare selected measurements across classes.
4. Create and save a scatter plot.
5. Separate features from target labels and split the data into training and test sets.
6. Use a scikit-learn pipeline to scale features and train a Logistic Regression classifier.
7. Evaluate predictions with accuracy, a confusion matrix, and a classification report.
8. Predict the class of a held-out example and compare it with the actual label.

The test score is a result from one particular split of this dataset. It is a learning exercise, not a guarantee of performance on new data or a production-ready AI system.


Tools and Libraries

1. Python — programming language used for the exercises.
2. NumPy — numerical arrays and mathematical operations.
3. pandas — tabular data handling and analysis.
4. Matplotlib — charts and data visualization.
5. scikit-learn — sample datasets, data splitting, preprocessing, machine-learning models, and evaluation metrics.
6. Git, GitHub, and GitHub Codespaces — version control, repository hosting, and cloud-based development.

Most early exercises use Python's built-in features. The data-analysis and machine-learning exercises require the relevant external libraries.



Getting Started

1. Open the repository
Open this repository on GitHub. If you want to run the programs on your own computer, clone the repository first:

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
Replace YOUR-USERNAME and YOUR-REPOSITORY with your GitHub username and repository name.

Alternatively, open the repository in GitHub Codespaces and use its terminal.

2. Install the libraries
If the repository does not already have an environment with the required libraries, install them with:

python -m pip install numpy pandas matplotlib scikit-learn
3. Run a program
Navigate to the relevant Python file and run it from the terminal. For example:

python path/to/program.py
Replace path/to/program.py with the actual path and filename in this repository. Some programs create output files, such as CSV files or chart images, in the current working directory.


How the Project Was Practiced
1. Study a concept and a short example.
2. Write a related challenge independently.
3. Run the code and inspect the output.
4. Debug errors and improve the logic when necessary.
5. Commit each completed set to GitHub to keep a record of progress.



Future Learning
This repository provides a foundation for further study. Possible next topics include functions and code structure in larger projects, testing, data validation, exploratory data analysis, statistics, feature engineering, cross-validation, model selection, model persistence, APIs, and deeper machine-learning or AI application development.



Note
This is an educational learning project. The examples are intended for practice and demonstration; they should be reviewed and adapted before being used in real production systems.


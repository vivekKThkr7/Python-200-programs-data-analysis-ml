# Python 200 Programs: From Fundamentals to Data Analysis and Introductory Machine Learning

A hands-on Python learning repository containing **200 programs and 200 related practice challenges**, arranged into 20 progressive exercise sets. The project starts with Python fundamentals and problem-solving, then moves through functions, data structures, file handling, object-oriented programming, practical applications, API requests, data analysis, and introductory machine learning.

This repository documents my learning through practical coding. I used each set to study a concept, write a program, attempt a related challenge, run the code, inspect the result, and correct mistakes. The goal was to build problem-solving skills and become more comfortable applying Python to practical tasks.

## Learning roadmap

The table below follows the topics covered by the actual exercise folders in this repository.

| Programs | Main topics | Skills practised | Exercise set |
|---|---|---|---|
| **1–20** | Python fundamentals | `print()`, `input()`, variables, arithmetic, data types, type conversion, strings, comparisons, and Boolean logic. | [`Basic_first_10`](Basic_first_10/) · [`11-20`](11-20/) |
| **21–40** | Conditions and decision-making | `if`, `elif`, `else`, comparison and logical operators, nested decisions, and practical decision programs. | [`21-30`](21-30/) · [`31-40`](31-40/) |
| **41–60** | Loops and number algorithms | `for`, `while`, repetition, counters, accumulators, number patterns, digit processing, palindrome checks, factorials, prime checks, and number analysis. | [`41-50`](41-50/) · [`51-60`](51-60/) |
| **61–70** | String handling | String length, indexing, negative indexing, slicing, reversing, case conversion, whitespace handling, searching, and word counting. | [`61-70`](61-70/) |
| **71–90** | Lists and structured list processing | Creating and updating lists, indexing, iteration, totals and averages, searching, filtering, duplicate handling, nested lists, and list analysis. | [`71-80`](71-80/) · [`81-90`](81-90/) |
| **91–100** | Functions | Defining and calling functions, parameters, return values, conditions inside functions, combining functions, and a student analyser. | [`91-100`](91-100/) |
| **101–110** | Dictionaries | Key-value data, reading and updating values, adding and deleting keys, checking membership, iteration, and analysing student records. | [`101-110`](101-110/) |
| **111–120** | Tuples, sets, and data structures | Tuple access and immutability, set operations, membership, removing duplicates, and choosing between lists, tuples, and sets. | [`111-120`](111-120/) |
| **121–130** | File handling and exceptions | Creating, reading, writing, and appending files; using `with open()`; handling exceptions with `try` and `except`; and validating input. | [`121-130`](121-130/) |
| **131–140** | OOP fundamentals | Classes, objects, attributes, constructors, methods, object state, and a simple bank-account example. | [`131-140`](131-140/) |
| **141–150** | Core OOP concepts | Encapsulation, getters and setters, inheritance, overriding, `super()`, polymorphism, and a mini OOP system. | [`141-150`](141-150/) |
| **151–160** | Modules and useful Python features | Imports, built-in and custom modules, variable scope, local and global variables, list and dictionary comprehensions, lambda functions, and combining concepts. | [`151-160`](151-160/) |
| **161–170** | Practical project: expense tracker | Input validation, menus, dictionaries and lists for expense records, totals, category filtering, JSON storage, loading saved data, and a mini expense tracker. | [`161-170`](161-170/) |
| **171–180** | Writing more reliable Python programs | `pathlib`, dates and times, CSV files, dataclasses, type hints, custom exceptions, assertions, debugging, refactoring, and a mini inventory system. | [`171-180`](171-180/) |
| **181–190** | APIs and HTTP requests | Using the `requests` library, GET and POST requests, HTTP responses and status codes, query parameters, JSON data, error handling, timeouts, reusable functions, and a user-directory API project. | [`181-190`](181-190/) |
| **191–200** | Data analysis and introductory machine learning | NumPy arrays and calculations, pandas DataFrames, CSV workflows, data cleaning, grouping, Matplotlib charts, train/test splitting, model training, predictions, and evaluation. | [`191-200`](191-200/) |

## Programs 191–200: Data analysis and machine-learning foundations

The final ten programs introduce common tools used in Python data analysis and introductory machine learning.

| Program | Topic | What it practises |
|---|---|---|
| **191** | NumPy arrays | Creating numerical arrays, performing element-wise calculations, and accessing array elements. |
| **192** | NumPy calculations and statistics | Calculating a total, mean, median, maximum, and minimum. |
| **193** | pandas DataFrames | Creating tabular data, adding a calculated column, and filtering rows. |
| **194** | Reading and writing CSV data | Saving a DataFrame to a CSV file, reading it back, and calculating a total. |
| **195** | Data cleaning | Identifying missing values, filling missing prices, and removing exact duplicate rows in an example dataset. |
| **196** | Grouping and analysis | Grouping records by category and calculating summary statistics. |
| **197** | Data visualization | Creating and saving a bar chart with Matplotlib. |
| **198** | Preparing data for machine learning | Separating features and labels and creating stratified training and test sets with the Iris dataset. |
| **199** | Training and evaluating a model | Scaling features, training a Logistic Regression classifier, generating predictions, and reviewing evaluation metrics. |
| **200** | Data Analysis and AI Pipeline capstone | Bringing data inspection, cleaning checks, grouped analysis, visualization, model training, prediction, and evaluation into one workflow. |

## Final capstone

The final set contains a complete example and a related independent challenge:

- **Main Program 200** (`191-200/200.py`) uses the **Wine dataset**. It creates a pandas DataFrame from the dataset's chemical measurements, inspects and summarizes the data, checks for missing and duplicate rows, compares selected measurements by wine class, creates a scatter plot, trains a scaled Logistic Regression model, and evaluates its predictions. The plot is saved to `outputs/charts/wine_scatter.png`.
- **Challenge 200** (`191-200/challenges/challenge200.py`) also uses the **Wine dataset** and follows a similar analysis and machine-learning workflow. It saves its scatter plot to `outputs/charts/wine_scatter.png`, the same output location used by Main Program 200.

The evaluation score produced by either script depends on its dataset and train/test split. These are educational examples for learning the workflow; they are not production-ready machine-learning systems or guarantees of performance on new data.

## Tools and libraries

- **Python** — the programming language used throughout the exercises.
- **Requests** — sends HTTP requests in Programs 181–190.
- **NumPy** — numerical arrays and calculations.
- **pandas** — tabular data handling and analysis.
- **Matplotlib** — charts and data visualization.
- **scikit-learn** — sample datasets, data splitting, preprocessing, machine-learning models, and evaluation metrics.
- **Git, GitHub, and GitHub Codespaces** — version control, repository hosting, and the cloud development environment used during the project.

The early exercises mainly use Python's standard library. The API, data-analysis, and machine-learning exercises also require the external libraries listed in the setup instructions below.

## Getting started

### Requirements

- Python **3.10 or newer** is recommended.
- Git, if you are cloning the repository to your computer.
- An internet connection for the API exercises in Programs 181–190.

### Option 1: GitHub Codespaces

1. Open this repository on GitHub.
2. Select **Code** and open or create a Codespace.
3. In the Codespaces terminal, install the external libraries:

   ```bash
   python -m pip install requests numpy pandas matplotlib scikit-learn
   ```

4. Run a program from the repository root. For example:

   ```bash
   python "191-200/191.py"
   ```

### Option 2: Run on a local computer

Clone the repository and move into its folder:

```bash
git clone https://github.com/vivekKThkr7/Python-200-programs-data-analysis-ml.git
cd Python-200-programs-data-analysis-ml
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
source .venv/bin/activate
```

Install the libraries used by the API, data-analysis, and machine-learning exercises:

```bash
python -m pip install requests numpy pandas matplotlib scikit-learn
```

### Running a program or challenge

Run the command from the repository's root directory, replacing the example path with the program you want to practise:

```bash
python "191-200/191.py"
```

For a challenge, use the path to its file inside that set's challenge folder. For example:

```bash
python "191-200/challenges/challenge191.py"
```

**Important:** Run exercises from the repository root unless a program says otherwise. Some programs read or write files using relative paths, so running them from a different working directory may cause Python not to find the expected files. Some exercises also ask for keyboard input or create output files. Generated text, CSV, JSON, and chart files are organized under `outputs/text/`, `outputs/csv/`, `outputs/json/`, and `outputs/charts/`. The employee file used by Challenge 171 remains under `data/`.

## How I practised

1. Studied the concept and reviewed a short example.
2. Wrote the related program.
3. Attempted the matching challenge independently.
4. Ran the code and checked the output.
5. Debugged mistakes and improved the logic.
6. Committed completed sets to GitHub to keep a record of progress.

## Course notes

The repository also includes **[COURSE_NOTES.md](COURSE_NOTES.md)**, which contains additional definitions, explanations, examples, and notes from the learning process.

## Next learning goals

Possible next steps include automated testing, data validation, exploratory data analysis, statistics, feature engineering, cross-validation, model selection, model persistence, and building larger Python applications that use APIs and machine learning.

## Note

This is an educational learning project. The programs demonstrate concepts and introductory workflows. Review, test, and adapt the code before using it in real-world or production systems.

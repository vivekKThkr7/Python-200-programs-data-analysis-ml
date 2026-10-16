<!-- # somthing -->
<!-- Trying somthing new -->

<!-- Python is high-level programming language to build applications, automate tasks, analyze data, develop websites, and build AI/ML systems. -->

Programs 91 -100 : Functions -- Turing Code into Reusable Tools

** Functions let us write a piece of logic once and reuse it whenever we need it. 

Definition -> A function is a named block of code that performs a specific task.


100 / 200 -> 50 % Completed  💐  (Halfway Point)

1 - 20 Fundamentsls
21 - 40 Decision making
41 - 60 Loops & Algorithms
61 - 70 Strings
71 - 90 Lists & Structured Data
91 - 100 Functions


Program 101 - 110 Dictionaries -- Storing Data with meaning

marks = [75, 82, 85]  -> (List)


<!-- DDictionary -->
student = {
    "name": "Vivek",
    "age": 27,
    "country": "Nepal"
}

<!-- Important things to Notice -->

1. variable

age = 27


2. List

age = [20, 24, 38, 30]


3. Dictionary

ages = {
    "Vivek": 27,
    "Ram": 25,
    "Sita": 30
}


<!-- Programms 111 - 120: Tuples, sets, & choosing the right Data Structure -->

<!-- Tuple : is a collection of values that normally should not be changed -->

eg numbers = (10, 20, 30, 40, 50)
looks similar to lsit but 
numbers = [10, 20, 30, 40, 50]

<!-- list -> can be changed -->
<!-- Tuple cannot be changed -->




<!-- List
[10, 20, 20, 30]
→ ordered collection
→ duplicates allowed
→ changeable

Tuple
(10, 20, 20, 30)
→ ordered collection
→ duplicates allowed
→ not changeable

Set
{10, 20, 30}
→ unique values
→ duplicates removed -->



🧠 DATA STRUCTURE CHEAT SHEET

This is one of the most important tables in your course.

Structure	 Example   Changeable?	Duplicates?	   Main idea
List	     [1,2,3]	✅	        ✅	        Ordered collection
Tuple	     (1,2,3)	❌	        ✅	        Fixed collection
Set	         {1,2,3}	✅	        ❌	        Unique values
Dictionary	 {"a":1}	✅	      Keys unique	 Key → value


<!-- Simple memory trick
LIST       → MANY VALUES
TUPLE      → FIXED VALUES
SET        → UNIQUE VALUES
DICTIONARY → NAMED VALUES -->










<!-- 121 - 130 :  -->

# What is an exception?

# Exception : error that happens while the program is running.

age = int(input("Enter your age: "))

# any value except integer return an error 

# eg: if someone type abcd it gives ValueError



Program 131 - 140 : OOP - Class & Objects
130/200 -> 65%

<!-- What is OOP? -->

Its a way of organizing a program around objects data and behavior.

For example, think about a bank account.

It has data:

account holder
balance
account number

And it has behavior:

deposit
withdraw
check balance

Instead of keeping everything scattered around, OOP lets us package related things together.

Think:

BANK ACCOUNT OBJECT
────────────────────
Data:
  owner
  balance

Actions:
  deposit()
  withdraw()
  check_balance()

That's the core idea.



Term   -----> Simple Meaning
Class          Blueprint
Object        Actual thing created from class
Attribute     Data belonging to the onjebt
Method        Function benlonging to object.
self          current object
_init_( )     Setup when object is created
instance      Another word for an object










🧠 OOP FUNDAMENTAL CHECKPOINT

I especially want you to understand these four levels.

Level 1 — Class
class Student:

Blueprint.

Level 2 — Object
student = Student(...)

Actual thing.

Level 3 — Inheritance
class Student(Person):

Student gets reusable behavior from Person.

Level 4 — Polymorphism
for employee in employees:
    employee.work()

Different objects can perform the same method differently.

🔥 Your biggest fundamental concept — one more time

Look at:

employees = [
    Developer("Ram"),
    Designer("Sita")
]

Here:

employees
   ↓
WHOLE LIST

Inside:

for employee in employees:
employees → whole collection
employee  → one object

Then:

employee.work()

means:

Call work() on this particular object.

This is the same fundamental pattern you've been learning since lists:

marks → whole list
mark  → one item

and now:

employees → whole list
employee  → one object

🔥 Same thinking. Different data.

🧠 Four OOP Terms — Simple Definitions
Concept	Simple meaning
Encapsulation	Control access to object data
Inheritance	Child reuses parent
Overriding	Child changes inherited behavior
Polymorphism	Same method call, different behavior



<!-- Program 151 to 160 : Writing Cleaner, more Practical Python -->
151 → import
152 → useful built-in modules
153 → create your own module
154 → variable scope
155 → global vs local
156 → list comprehension
157 → comprehension with condition
158 → dictionary comprehension
159 → lambda
160 → combining these ideas





<!-- Programs 161–170: From Python Exercises to a Real Project -->
<!-- 
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
 -->


 <!-- Programs 171–180: Making a Real Project Reliable -->
<!-- IN this level we are going to learn how real Python programs are organized and used in practical work. -->

<!-- Q. What is pathlib? -->

Pathlib is a built-in python module used to work with; Files, Folders, File paths.
Instead of treating a path as jsut a string, oython gives us a path object.

Example:

from pathlib import path

file_path = path("notes.txt)

here:
file_path -> path object -> notes.txt




from Program 176.py
Q. Why not simply print an error inside the function?
A. Because raising an exception allows the calling code to decide how to handle the problem. This helps separate the business logic from the application's response to errors.





<!-- Python Set 19  -->
<!-- Our learning plan -->
<!-- 

Program	     Topic
181	        What an API is and how to make a GET request
182	        HTTP status codes and successful responses
183	        Query parameters
184	        Reading and processing API data
185	        Handling API errors and timeouts
186	        Sending data using POST
187	        Working with nested JSON
188	        Building reusable API functions
189	        Saving API data into a JSON file
190	        Mini project: User Directory API

 -->


# what is requests?
#  It is Python library that makes it easier to communicate with web serrvers. unlike Pathlib, JSON and datatime,  it is not part of Python's standard library, so need to be installed form the terminal. 

# python -m pip install requests

# What is API?

# API -> APPLICATION PROGRAMMING INTERFACE.
# API as a way for one application to request information or services from another application.

python program (request a post) <==> API/Web server(Receives the request and returns data) <==> Python Program (Read thye response and uses the data)


API request often involves aa URL called an endpoint. 
<!--  https://jsonplaceholder.typicode.com/posts/1 -->


<!-- What is HTTP -->
<!-- HTTP is a protocal that allows clients and servers to communicate over a network. -->

<!--   GET   ==> Retrieve Information  -->
<!--   POST ==>  Send data to a server -->


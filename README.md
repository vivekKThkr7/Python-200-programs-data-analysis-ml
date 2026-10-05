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
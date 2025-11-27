[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21857029)
# Advanced Python Practice — Data Structures, Scope & `match`

This assignment is meant for students who to explore more Python features:

* lists
* tuples
* sets
* dictionaries
* global vs local variables
* `match` expressions

You **do not need loops** for these tasks. Everything here can be done with simple operations and function calls.

---

## 1. Lists

### What is a list?

A **list** in Python is an ordered collection of items.

* It is *ordered*: items have a position (index) starting from 0.
* It is *mutable*: you can change, add or remove elements.
* It can contain different types (integers, strings, etc.), but usually we keep the same type for clarity.

**Example structure (conceptual, not code):**

* A list of colors: `["red", "green", "blue"]`
* Index positions:

  * index 0 → `"red"`
  * index 1 → `"green"`
  * index 2 → `"blue"`

### What can you do with a list?

* Access an element by its **index**
* Access a **slice** (a sub-part) of the list: e.g. elements from position 1 to 3
* Modify an element
* Add or remove elements

More details:
👉 [https://www.w3schools.com/python/python_lists.asp](https://www.w3schools.com/python/python_lists.asp)

---

### Exercise 1 — Lists: Create and Print Specific List Items

You are given this list:

```python
colors = ["red", "green", "blue", "yellow", "purple"]
```

You must write a function `color_info(items)` that:

* prints the first color
* prints the last color
* prints the second and third colors using slicing

Then call the function with `colors`.

**Relevant documentation:**

* Lists: [https://www.w3schools.com/python/python_lists.asp](https://www.w3schools.com/python/python_lists.asp)
* List indexing & slicing: https://www.w3schools.com/python/python_lists_access.asp

#### How to solve it (step by step, no full code):

1. Think of the function as a small “tool” that receives a list of colors.
2. Inside the function, you need to **access elements by position**:

   * The first element is at index 0.
   * The last element can be accessed using a negative index (last position) or by using the list length minus one.
3. To get the second and third colors together, use a **slice**:

   * A slice selects a range of indices, starting at a position and ending *before* another position.
4. For each required part (first, last, slice), **display the values** with `print`.
5. Outside the function, call it and pass in the `colors` list so that it runs using that data.

You’re basically practicing:

* how to access specific positions in a list
* how slicing works
* how to pass a list into a function

---

## 2. Tuples

### What is a tuple?

A **tuple** is like a list, but **immutable** (cannot be changed after creation).

* Ordered
* Can contain multiple values
* Often used for fixed groups of data, like coordinates, or `(name, age)` pairs.

Structure example:

* `("Alice", 21)` → a tuple with two items: name and age.

You can still **access items by index** and **unpack** a tuple into separate variables.

More details:
👉 [https://www.w3schools.com/python/python_tuples.asp](https://www.w3schools.com/python/python_tuples.asp)
https://www.w3schools.com/python/python_tuples_unpack.asp

---

### Exercise 2 — Tuples: Unpacking a Tuple

You are given:

```python
person = ("Alice", 21)
```

Write a function `print_person(info)` that:

* unpacks the tuple into `name` and `age`
* prints a sentence like: `"Alice is 21 years old."`

Then call the function with `person`.

**Relevant documentation:**

* Tuples: [https://www.w3schools.com/python/python_tuples.asp](https://www.w3schools.com/python/python_tuples.asp)

#### How to solve it (step by step):

1. The function will receive one parameter: the tuple `info`.
2. Inside the function, **unpack** the tuple into two variables:

   * One for the name
   * One for the age
3. Build a string that includes both the name and the age in a sentence.

   * You can use string concatenation or a formatting method such as f-strings or `.format()`.
4. Print the final sentence.
5. Outside the function, call it and pass `person` as the argument.

You’re practicing:

* working with tuples
* unpacking values into separate variables
* using them in a formatted message

---

## 3. Sets

### What is a set?

A **set** is an unordered collection of unique items.

* It **does not keep order** (no index like lists).
* It **does not allow duplicates**.
* Useful when you want to store distinct elements only (e.g. unique words).

Structure example:

* `{"apple", "banana", "orange"}` → a set of fruit names.

You can:

* add items
* remove items
* check if a value is in the set

More details:
👉 Sets: [https://www.w3schools.com/python/python_sets.asp](https://www.w3schools.com/python/python_sets.asp)
👉 Add items to a set: [https://www.w3schools.com/python/python_sets_add.asp](https://www.w3schools.com/python/python_sets_add.asp)

---

### Exercise 3 — Sets: Add an Item to a Set

You have:

```python
fruits = {"apple", "banana", "orange"}
```

Write a function `add_fruit(fruit_set, new_fruit)` that:

* adds `new_fruit` to the set
* returns the updated set

Then, in the main program, call the function with `"kiwi"` and display the result.

**Relevant documentation:**

* Sets: [https://www.w3schools.com/python/python_sets.asp](https://www.w3schools.com/python/python_sets.asp)
* Adding items: [https://www.w3schools.com/python/python_sets_add.asp](https://www.w3schools.com/python/python_sets_add.asp)

#### How to solve it (step by step):

1. The function should accept two parameters:

   * one for the existing set
   * one for the new fruit name
2. Inside the function, use the appropriate **method to add an element** to a set.
3. After modifying the set, make the function **return** this set.
4. In the main part of the program:

   * use the given `fruits` set
   * call the function, passing `fruits` and `"kiwi"`
   * store the returned set in a variable
   * display it to confirm that the new fruit was added.

You’re practicing:

* how to pass a set into a function
* how to modify it
* how sets store unique values

---

## 4. Dictionaries

### What is a dictionary?

A **dictionary** stores data as **key–value pairs**.

* Example: a dictionary that maps countries to capitals:

  * `"France"` → `"Paris"`
  * `"Germany"` → `"Berlin"`
* You access values by their **key**, not by position.

Structure example:

```python
{
  "France": "Paris",
  "Germany": "Berlin"
}
```

You can:

* read a value using its key
* add a new key–value pair
* update an existing value
* remove pairs

More details:
👉 [https://www.w3schools.com/python/python_dictionaries.asp](https://www.w3schools.com/python/python_dictionaries.asp)

---

### Exercise 4 — Dictionaries: Simple Dictionary Lookup

You are given:

```python
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid"
}
```

Write a function `get_capital(country, capitals_dict)` that:

* returns the capital of the given country
* returns `"Unknown"` if the country is not in the dictionary

Ask the user for a country name and print the function’s result.

**Relevant documentation:**

* Dictionaries: [https://www.w3schools.com/python/python_dictionaries.asp](https://www.w3schools.com/python/python_dictionaries.asp)

#### How to solve it (step by step):

1. The function must accept:

   * the country name (string)
   * the dictionary of capitals
2. Inside the function, check whether the given country is one of the **keys** in the dictionary.
3. If it exists, return the corresponding value (the capital).
4. If it does not exist, return the string `"Unknown"`.
5. In the main program:

   * ask the user to type a country name
   * call the function with the user’s input and the `capitals` dictionary
   * print the returned result.

You’re practicing:

* reading values from a dictionary
* handling missing keys gracefully
* combining user input and dictionaries

---

## 5. Local vs Global Scope

### What is scope?

**Scope** describes *where* a variable is visible and can be used.

* **Global variable**:

  * defined outside any function
  * visible in the entire file (module), unless shadowed
* **Local variable**:

  * defined inside a function
  * only available within that function

Python also allows you to modify a global variable inside a function using the `global` keyword, but this should be used carefully.

More details:
👉 [https://www.w3schools.com/python/python_variables_global.asp](https://www.w3schools.com/python/python_variables_global.asp)

---

### Exercise 5 — Local vs Global Scope: Modifying a Global Variable

Create a global variable:

```python
counter = 0
```

Write a function `increase_counter()` that:

* uses the `global` keyword
* increases `counter` by 2 each time it is called
* prints the updated value

Then, in the main program, call this function three times and watch how the global `counter` changes.

**Relevant documentation:**

* Global variables: [https://www.w3schools.com/python/python_variables_global.asp](https://www.w3schools.com/python/python_variables_global.asp)
https://www.w3schools.com/python/python_scope.asp

#### How to solve it (step by step):

1. Define a variable with some initial numeric value **outside** any function.
2. Inside the function:

   * declare that you want to use the global variable (using the proper keyword)
   * increase its value by the required amount
   * display the new value
3. In the main program:

   * call the function once → observe printed value
   * call it again and again → observe how the value continues from the last value rather than restarting
4. Understand that the global variable is shared between calls.

You’re practicing:

* the difference between local and global variables
* how to modify a global variable from a function
* how values persist between function calls

---

## 6. `match` Expressions

### What is a `match` expression?

A `match` expression (introduced in Python 3.10) is similar to a “switch” in other languages, but more powerful.

Basic idea:

* You compare a given value against several **cases**.
* For each case, if it matches, the corresponding block of code runs.
* You can also define a **default** case for “anything else”.

Structure example (conceptual):

```text
match some_value:
    case "something":
        do one thing
    case "other":
        do something else
    case _:
        default action
```

More details:
👉 [https://www.w3schools.com/python/python_match.asp](https://www.w3schools.com/python/python_match.asp)

---

### Exercise 6 (Optional) — match Expression: Simple Command Menu

Write a function `handle_command(cmd)` that uses a `match` expression to:

* print `"Starting..."` if `cmd` is `"start"`
* print `"Stopping..."` if `cmd` is `"stop"`
* print `"Saving..."` if `cmd` is `"save"`
* print `"Unknown command"` for anything else

Ask the user for a command, then call the function once.

**Relevant documentation:**

* Match/case: [https://www.w3schools.com/python/python_match.asp](https://www.w3schools.com/python/python_match.asp)

#### How to solve it (step by step):

1. The function takes a single parameter: the command string.
2. Inside the function, write a `match` expression that compares the command to several fixed strings.
3. For each case:

   * decide what message to print
4. Add a final “catch-all” case that matches any other value and prints a default message.
5. In the main program:

   * ask the user to type a command (for example: `"start"`, `"stop"`, or `"save"`)
   * call `handle_command` with the user input.

You’re practicing:

* basic pattern matching syntax with `match`
* simple branching based on user input
* default handling for unknown commands

---

## How to Work Through This Assignment

1. Read the concept explanations for each section.
2. Open the W3Schools links and skim the examples.
3. For each exercise:

   * restate it in your own words
   * follow the step-by-step guide above
   * implement the function
   * test it with different input values if possible
4. Don’t worry if you don’t finish everything in one sitting — these are bonus/advanced topics meant to help you grow beyond the core curriculum.

If you get stuck on a particular idea, go back to the relevant section and link, and try to understand *one small piece at a time* before returning to the code.

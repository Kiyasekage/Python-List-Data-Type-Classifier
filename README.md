# Python List Data Type Classifier

A simple Python program that classifies elements in a list based on their data types. It uses the `dict.fromkeys()` method to create a dictionary from the input list and `isinstance()` to determine whether each element is an integer or a string.

## Features

- Accepts a list containing integers and strings.
- Creates a dictionary using `dict.fromkeys()`.
- Identifies integer values using `isinstance()`.
- Categorizes each element as either `Integer` or `String`.
- Displays the resulting dictionary with the original elements as keys and their data types as values.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the code in a file named `list_data_type_classifier.py`.
3. Open a terminal or command prompt.
4. Run the program:

   ```bash
   python list_data_type_classifier.py
   ```

## Example

**Input:**

```python
custom_list = [10, "one", "two", "ten", 20, 30, "five", 40, "nine", 50]
```

**Output:**

```python
{
    10: 'Integer',
    'one': 'String',
    'two': 'String',
    'ten': 'String',
    20: 'Integer',
    30: 'Integer',
    'five': 'String',
    40: 'Integer',
    'nine': 'String',
    50: 'Integer'
}
```

## Concepts Practiced

- **Dictionaries:** Creating and updating dictionaries using `dict.fromkeys()`.
- **Lists:** Processing a collection of different data types.
- **Loops:** Iterating through dictionary keys using a `for` loop.
- **Conditional Statements:** Classifying elements based on their data types.
- **Type Checking:** Using `isinstance()` to identify integer values.
- **Functions:** Creating a reusable `group_types()` function.

## Language

Python 3

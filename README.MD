# ChefsGeneralLib

ChefsGeneralLib is a Python library containing some general utility functions.

## Functions

| Function | Description |
|-|-|  
| print_obj | Prints the attributes of an object passed to it |
| Colored | Prints colored text using ANSI escape codes |
| generate_int_list | Generates a list of random integers |
| generate_float_list | Generates a list of random floats |
| isPalindrome | Checks if a string is a palindrome (reads the same forwards and backwards) |
| removeDuplicates | Removes duplicate elements from a list |
| readJSONfile | Reads data from a JSON file |
| factorial | Calculates the factorial of a number |
| isWebsiteUp | Checks if a website is up/down |
| getWebsiteStatusCode | Gets status code of a website |
| HTTP_STATUS_CODES | Dictionary of HTTP status codes |
| validateEmail | Validates an email address |
| validateUrl | Validates a URL |
| generatePassword | Generates a random password |
| checkStrength | Checks strength of a password |
| timeFunction | Times execution of a function |
| runFileToTXT | Runs a Python file and saves output to text file |

### `print_obj(class_obj, showBoundMethods, printDocs, printReturns)`

Prints the attributes of an object passed to it.

Useful for quick debugging.

**Parameters:**

- `class_obj`: Class object.
- `showBoundMethods (bool, optional)`: Whether or not to show bound Methods.

    Defaults to True.
- `printDocs (bool, optional)`: Whether or not to print documentations.

    Defaults to True.
- `printReturns (bool, optional)`: Whether or not to print what type the function is returning.

    Defaults to True.

**Returns:**
None

**Example:**

```python
from ChefsGeneralLib import print_obj

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("John", 30)  
print_obj(person)

# Output:
# Class Name: Person
# Values:
#     name: John        
#     age: 30
# Functions:
#     __init__():       
#         Returns: Any  
#         Documentation:
#         +--------------------+
#         |  No documentation  |
#         +--------------------+
```

### `Colored(text)`

Prints colored text using ANSI escape codes.

**Parameters:**

- `text`: The text to be colored.

**Returns:**
None

**Example:**

```python
from ChefsGeneralLib import Colored

c = Colored("Hello World")
c.color_red()
print()
# Prints red text
```

### `generate_int_list(length, minimum_random_number,maximum_random_number, order_min_max)`

Generates a list of random integers.

**Parameters:**

- `length (int, optional)`: Length of the list.

    Defaults to 0.
- `minimum_random_number (int, optional)`: Minimum random number.

    Defaults to 0.

- `maximum_random_number (int, optional)`: Maximum random number.

    Defaults to 100.

- `order_min_max (bool, optional)`: Whether or not to sort minimum and maximum in 'minimum_random_number' and 'maximum_random_number' and prevent an error.

    Defaults to False.

**Returns:**
List of random integers

**Example:**

```python
from ChefsGeneralLib import generate_int_list

nums = generate_int_list(5, 1, 100)
print(nums)

# Output: [34, 67, 2, 84, 23]
```

### `generate_float_list(length, minimum_random_number,maximum_random_number, order_min_max)`

Generates a list of random floats.

**Parameters:**

- `length (int, optional)`: Length of the list.

    Defaults to 0.
- `minimum_random_number (float, optional)`: Minimum random number.

    Defaults to 0.

- `maximum_random_number (float, optional)`: Maximum random number.

    Defaults to 100.

- `order_min_max (bool, optional)`: Whether or not to sort minimum and maximum in 'minimum_random_number' and 'maximum_random_number' and prevent an error.

    Defaults to False.

**Returns:**
List of random floats

**Example:**

```python
from ChefsGeneralLib import generate_float_list

nums = generate_float_list(3, 0, 1) 
print(nums)

# Output: [0.24, 0.54, 0.82]
```

### `isPalindrome(s, case_sensitive)`

Checks if a string is a palindrome (reads the same forwards and backwards).

**Parameters:**

- `s (str)`: string to check if it is a palindrome.
- `case_sensitive (bool, optional)`: Whether or not the check is case sensitive.

    Defaults to True.

**Returns:**
True if palindrome otherwise False

**Example:**

```python
from ChefsGeneralLib import isPalindrome

print(isPalindrome("raCecar", False))    #True
print(isPalindrome("hello"))             #False
```

### `removeDuplicates(a)`

Removes duplicate elements from a list.

**Parameters:**

- `a (list)`: list.

**Returns:**
List without duplicates

**Example:**

```python
from ChefsGeneralLib import removeDuplicates

nums = [1, 2, 3, 2, 5]
unique = removeDuplicates(nums)
print(unique)  # [1, 2, 3, 5]
```

### `readJSONfile(path)`

Reads data from a JSON file.

**Parameters:**

- `path (str)`: path to the JSON file.

**Returns:**
The JSON file as a dictionary

**Example:**

```python
# Usage example:
from ChefsGeneralLib import readJSONfile
data = readJSONfile("example.json")
print(data)
```

### `factorial(n)`

Calculates factorial of a number.

**Parameters:**

- `n (int)`: number.

**Returns:**
Factorial of the number

**Example:**

```python
# Usage example:
from ChefsGeneralLib import factorial
n = factorial(5)
print(n) #120
```

### `isWebsiteUp(url)`

Checks if a website is up.

**Parameters:**

- `url (str)`: URL of the website.

**Returns:**
Whether or not the website is up

**Example:**

```python
# Usage example:
from ChefsGeneralLib import isWebsiteUp
g = isWebsiteUp("google.com")
print(g) #True
```

### `getWebsiteStatusCode(link)`

Gets the status of a website request.

**Parameters:**

- `link (str)`: URL of the website.

**Returns:**
Status of the website request

**Example:**

```python
# Usage example:
from ChefsGeneralLib import getWebsiteStatusCode
sc = getWebsiteStatusCode("google.com")
print(sc) #200: OK
```

### `HTTP_STATUS_CODES`

Dictionary of HTTP status codes.

**Returns:**
Dictionary of HTTP status codes

**Example:**

```python
# Usage example:
from ChefsGeneralLib import HTTP_STATUS_CODES
sc = HTTP_STATUS_CODES[200]
print(sc) #OK
```

### `validateEmail(email)`

Calculates factorial of a number.

**Parameters:**

- `email (str)`: email to validate.

**Returns:**
Whether or not the email is valid

**Example:**

```python
# Usage example:
from ChefsGeneralLib import validateEmail
n = validateEmail("HelloWorld@gmail.com")
print(n) #True
```

### `validateUrl(url)`

Validate URL.

**Parameters:**

- `url (str)`: URL to validate.

**Returns:**
Whether or not the URL is valid.

**Example:**

```python
# Usage example:
from ChefsGeneralLib import validateUrl
n = validateUrl("google.com")
print(n) #True
```

### `generatePassword(length)`

Generate a random password.

**Parameters:**

- `length (int, optional)`: length of the password.

    Defaults to 10.

**Returns:**
Random password

**Example:**

```python
# Usage example:
from ChefsGeneralLib import generatePassword
n = generatePassword(5)
print(n) #`#AMi9`
```

### `checkStrength(password)`

Calculates factorial of a number.

**Parameters:**

- `password (str)`: password to check.

**Returns:**
Whether or not the password is strong

**Example:**

```python
# Usage example:
from ChefsGeneralLib import checkStrength
n = checkStrength("#AMi9")
print(n) #Password is too short. It should be at least 8 characters.
```

### `timeFunction(function, *args, **kwargs)`

Time a function.

**Parameters:**

- `function` (Callable): function to time.
- `*args`: args to pass to the function.
- `**kwargs`: kwargs to pass to the function.

**Returns:**
Time taken to run the function

**Example:**

```python
# Usage example:
from ChefsGeneralLib import timeFunction
n = timeFunction(factorial, 50000)
print(n) #0.4770522117614746
```

### `runFileToTXT(file, output)`

Run a file and output the result to a txt file.

**Parameters:**

- `file (str)`: file to run.
- `output (str)`: output file.

**Returns:**
None

**Example:**

```python
# Usage example:
from ChefsGeneralLib import runFileToTXT
runFileToTXT("Test.py", "test.txt")
```

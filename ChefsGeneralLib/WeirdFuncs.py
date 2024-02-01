import json
import requests
import string
import random
import re
import time
import subprocess


HTTP_STATUS_CODES = {
    # 1xx Informational
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",

    # 2xx Success
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    226: "IM Used",

    # 3xx Redirection
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    306: "(Unused)",
    307: "Temporary Redirect",
    308: "Permanent Redirect",

    # 4xx Client Error
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",

    # 5xx Server Error
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Required",
}


def isPalindrome(s: str, case_sensitive: bool = True) -> bool:
    """Checks if a string is a palindrome.

    Args:
        s (str): string to check if it is a palindrome.
        case_sensitive (bool, optional): Whether or not the check is case sensitive. Defaults to True.

    Returns:
        bool: whether or not the string is a palindrome.
    """
    if not case_sensitive:
        s = s.lower()
    return s == s[::-1]


def removeDuplicates(a: list) -> list:
    """Removes duplicates from list.

    Args:
        a (list): list.

    Returns:
        list: list without duplicates.
    """
    s = set()
    l = []
    for i in a:
        if i not in s:
            s.add(i)
            l.append(i)
    return l


def readJSONfile(path: str) -> dict:
    """Reads a JSON file.

    Args:
        path (str): path to the JSON file.

    Returns:
        dict: the JSON file as a dictionary.
    """
    with open(path, 'r') as f:
        return json.load(f)


def factorial(n: int) -> int:
    """Calculates factorial of a number.

    Args:
        n (int): number.

    Returns:
        int: factorial of the number.
    """
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


def isWebsiteUp(url: str) -> bool:
    """Checks if a website is up.

    Args:
        url (str): URL of the website.

    Returns:
        bool: whether or not the website is up.
    """
    try:
        requests.get(url)
        return True
    except:
        return False


def getWebsiteStatusCode(link: str) -> str:
    """Gets the status of a website request.

    Args:
        link (str): URL of the website.

    Returns:
        str: status of the website request.
    """
    try:
        r = requests.get(link)
        return f'{r.status_code}: {HTTP_STATUS_CODES[r.status_code]}'
    except:
        return f"Failed to request from `{link}`"


def validateEmail(email: str) -> bool:
    """Validate email.

    Args:
        email (str): email to validate.

    Returns:
        bool: whether or not the email is valid.
    """
    import re
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None


def validateUrl(url: str) -> bool:
    """Validate URL.

    Args:
        url (str): URL to validate.

    Returns:
        bool: whether or not the URL is valid.
    """
    import re
    return re.match(r"https?://.*", url) is not None


def generatePassword(length: int = 10) -> str:
    """Generate a random password.

    Args:
        length (int, optional): length of the password. Defaults to 10.

    Returns:
        str: random password.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits*2 + '@#$&*_!'*3, k=length))


def checkStrength(password: str) -> str:
    """Check the strength of a password.

    Args:
        password (str): password to check.

    Returns:
        str: Whether or not the password is strong.
    """
    # Define criteria
    min_length = 8
    has_uppercase = re.search(r'[A-Z]', password) is not None
    has_lowercase = re.search(r'[a-z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special_char = re.search(
        r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    # Check criteria
    if len(password) < min_length:
        return "Password is too short. It should be at least {} characters.".format(min_length)
    elif not has_uppercase:
        return "Password should contain at least one uppercase letter."
    elif not has_lowercase:
        return "Password should contain at least one lowercase letter."
    elif not has_digit:
        return "Password should contain at least one digit."
    elif not has_special_char:
        return "Password should contain at least one special character."
    else:
        return "Password is strong."


def timeFunction(function, *args, **kwargs) -> float:
    """Time a function.

    Args:
        function (Callable): function to time.
        *args: args to pass to the function.
        **kwargs: kwargs to pass to the function.

    Returns:
        float: time taken to run the function.
    """
    start = time.time()
    function(*args, **kwargs)
    end = time.time()
    return end - start


def runFileToTXT(file: str, output: str) -> None:
    """Run a file and output the result to a txt file.

    Args:
        file (str): file to run.
        output (str): output file.
    """
    try:
        # Run the script and redirect the output to the file
        subprocess.run(["python", file], stdout=open(output, "w"), check=True)
        print(f"Script output saved to {output}")
    except FileNotFoundError:
        print(f"File {file} not found.")
    except subprocess.CalledProcessError as e:
        with open(output, "+a") as f:
            g = f.read()
            f.write(g + str(e))
        print(f"Script output saved to {output}")

# Lab 5: Static Code Analysis — Issue Documentation

## Objective

To identify and fix code quality, programming, and security issues in the Course Enrollment System using Pylint, Bandit, and Flake8.

## Issue Table

| Issue | Type | Line(s) in Original Code | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe `eval()` usage | Security — High | 45–48 | The `eval()` function executes a supplied string as Python code, which could allow arbitrary code execution if the expression is untrusted. | Replaced expression evaluation with a numeric discount percentage and validated the input range from 0 to 100. |
| Hard-coded registrar token | Security — High | 74–84 | A sensitive authentication token was stored directly in the source code and printed to the terminal, potentially exposing credentials. | Removed the hard-coded token and its print statement. |
| Weak MD5 hashing | Security — Medium | 51–52 | MD5 has known cryptographic weaknesses and is unsuitable for security-sensitive hashing. | Replaced MD5 with SHA-256 for generating the student identifier hash. |
| Insecure OTP generation | Security — Medium | 55–56 | `random.randint()` is not designed for security-sensitive random number generation. | Replaced it with `secrets.randbelow()` to generate a four-digit OTP. |
| Mutable default argument | Bug | 15 | The default argument `audit_trail=[]` could reuse the same list across function calls, causing unintended shared state. | Changed the default to `None` and initialized a new list inside the function when required. |
| Bare exception handler | Code quality / Bug | 27–32 | A bare `except` catches all exceptions and silently ignores errors, making debugging difficult. | Removed the broad exception handler and explicitly checked whether the course exists. |
| Unused import and variables | Code quality | 4, 36, 46 | The original program contained an unused `math` import and unused variables such as `lab_fee` and an unnecessary `base_fee` assignment. | Removed unnecessary imports and variables. |
| Unsafe shell command and file handling | Security / Code quality | 59–63 | The original code used `os.system()` with a filename and opened a file without a context manager. | Used `with open(...)` with an encoding and ordinary Python output instead of executing a shell command. |
| Missing enrollment validation | Logic bug | 17–23 | The original enrollment function did not adequately validate seat availability, student names, or registered credits. | Added checks for course existence, availability, a non-empty student name, and positive credits. |
| Incorrect `None` comparison | Style | 37 | The original code used `== None` instead of the recommended identity comparison. | Replaced the comparison with `is None`. |
| Inconsistent naming conventions | Code quality / Style | Multiple lines | Function names such as `enrollStudent` and `dropCourse` did not follow the recommended Python `snake_case` naming convention. | Renamed functions and updated their corresponding calls to use `snake_case`. |
| Global variable usage | Code quality | 12, 16 | The original function used `global total_tuition`, making the program's state harder to maintain. | Adjusted tuition tracking to avoid reassigning the global variable. |

## Verification

The corrected program was analyzed using Pylint, Bandit, and Flake8.

- **Pylint:** Improved from 4.00/10 initially to 9.71/10 in a later run.
- **Bandit:** Reported no issues in the final scan shown.
- **Flake8:** Reported no violations after the indentation correction shown.

## Conclusion

Static code analysis helped identify potential security vulnerabilities, programming errors, and style violations. The code was improved by replacing unsafe operations, validating inputs, improving file handling, and following Python naming conventions. The final analysis reports were used to verify the changes.
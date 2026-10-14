# Lab 5: Static Code Analysis — Issue Documentation

| Issue | Type | Line(s) in Original Code | Description | Fix Approach |
|---|---|---|---|---|
| Unsafe `eval()` usage | Security — High | 47 | Executes a supplied string as Python code, potentially allowing arbitrary code execution. | Replaced expression evaluation with a validated numeric discount percentage. |
| Hard-coded registrar token | Security — High | 75, 84 | A secret is stored directly in the source code and printed, risking credential exposure. | Removed the hard-coded token and its print statement. |
| Weak MD5 hashing | Security — Medium | 52 | MD5 is not suitable for security-sensitive hashing because of known weaknesses. | Replaced MD5 with SHA-256. Note that plain SHA-256 is not password storage. |
| Insecure OTP generation | Security — Medium | 56 | `random.randint()` is not designed for security-sensitive random values. | Replaced it with `secrets.randbelow()` to generate a four-digit OTP. |
| Mutable default argument | Bug | 15 | `audit_trail=[]` can reuse the same list across function calls, causing unintended shared state. | Changed the default to `None` and initialized a list inside the function. |
| Bare exception handler | Code quality / Bug | 28–32 | A bare `except` catches all exceptions and silently ignores errors. | Removed the broad exception handler and explicitly checked whether the course exists. |
| Unused import and variables | Code quality | 4, 36, 46 | `math`, `lab_fee`, and the original `base_fee` assignment were unused in the original code. | Removed unnecessary imports and variables, retaining only variables required by the corrected logic. |
| Unsafe shell command and file handling | Security / Code quality | 59–63 | `os.system()` uses a shell command containing a filename, and the file is not managed with a context manager. | Used `with open(...)` and ordinary Python output instead of executing a shell command. |
| Missing enrollment validation | Logic bug | 17–23 | The original function could reduce seats below zero and did not validate the student's name or credit count. | Added checks for course availability, a non-empty name, and positive credits. |
| Incorrect `None` comparison | Style | 37 | The original code used `== None` instead of the recommended identity comparison. | Replaced the comparison with `is None`. |

Lab 5: Static Code Analysis — Issues Report



Repository: L5\_33\_movie\_reviews

Python File: movie\_reviews.py



1\. Identified Issues and Fixes

|Issues|type|Original Line(s)|Description|Fix approach|
|-|-|-|-|-|
|Missing docstrings (C0114, C0116)|Code Quality|1, 11, 16, 26, 34, 39, 45, 48, 54, 58|Module and functions lacked documentation.|Added module and function docstrings.|
|Invalid naming conventions (C0103)<br /><br />|Code Quality|8, 11, 16, 26, 34, 39, 45, 48, 54|Function and argument names did not follow snake\_case conventions.|<br /><br />Renamed functions and arguments using snake\_case and removed the unused featured variable.|
|unnescessary else after return(R1705)|code quality|28|an else block unnecessary after a return statement|Removed the else block|
|Global ststement(W0603)|code quality|40|The function used a global variable unnecessarily.|Returned the selected movie directly.|
|<br /><br />Range and len usage (C0200)|Code Quality|50|Iteration used range(len()) instead of a simpler approach.|Replaced with enumerate().|
|Hardcoded bind address (B104)|Security — Medium|4|The server address used 0.0.0.0, which can expose a service on all network interfaces.|Changed the address to 127.0.0.1.|
|<br /><br />Hardcoded password (B105)<br />|Security — Low|6|A password was stored directly in source code.|Used an environment variable to retrieve the password.|
|<br />Insecure random generator (B311)<br />|Security — Low|41|The standard random module was flagged as unsuitable for security-sensitive randomness.|Replaced random.choice() with secrets.choice().|
|<br /><br />Weak MD5 hash (B324)|Security — High|46|MD5 is a weak cryptographic hash function.|Replaced MD5 with SHA-256|
|Missing whitespace (E225)|Formatting|35|Missing spaces around an assignment operator|Added spaces around the equals sign.|
|<br /><br />Missing blank line (E302)|Formatting|48|Insufficient blank lines between function definitions.|Corrected spacing between functions.|
|Incorrect inline comment spacing (E261)|Formatting|70|Only one space appeared before an inline comment.|Added two spaces before the comment.|
|Missing space after comma (E231)|Formatting|72|Missing whitespaces after comma|Added a space after a comma.|
|Excessive blank lines (E303)|Formatting|after initial fixes|Too many blank lines between top-level statements.|Removed the extra blank line.|



2\. Static Analysis Results



|Tool|Before|After|
|-|-|-|
|pylint|5.47/10|10.00/10|
|Bandit|4 issues(1 High, 1 Medium,2 low)|0 issues|
|Flake8|4 formatting issues|0 issues|







3\. Reflection Questions



Q1. What is static code analysis?



Static code analysis is the process of examining source code without executing it. It helps identify bugs, security vulnerabilities, coding standard violations, and maintainability issues.



Q2. What is the purpose of Pylint, Bandit, and Flake8?



Pylint checks Python code quality and coding practices. Bandit detects common Python security vulnerabilities. Flake8 identifies formatting and style violations.



Q3. Which issues were most important to fix?



The MD5 hashing issue was particularly important because Bandit classified it as High severity. The exposed network interface was also important because it could increase network exposure.



Q4. How did static analysis improve the program?



Static analysis helped improve code readability, consistency, security, and maintainability. It also helped remove unnecessary code and identify potentially unsafe programming practices.



Q5. What did you learn from this lab?



I learned how to install and use Pylint, Bandit, and Flake8, interpret their reports, correct the identified issues, and verify the fixes. I also learned how to use Git commits to track changes separately.



4\. Conclusion



The Python movie reviews program was analyzed and improved using three static analysis tools. The Pylint score increased from 5.47/10 to 10.00/10, all four Bandit security findings were resolved, and Flake8 reported no remaining formatting issues. The fixes were tracked using three separate Git commits.


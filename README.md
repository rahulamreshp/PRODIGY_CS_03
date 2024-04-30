# PRODIGY_CS_03
# Password Complexity Checker

The Password Complexity Checker is a command-line utility designed to assess the strength of passwords based on various criteria such as length, character diversity, and commonality. It aims to provide users with insights into the robustness of their chosen passwords and offer suggestions for improvement if necessary.

#usage
pip install -r Requirements.txt

python3 main.py

#modules

Complexity Assessment

1. The program evaluates the complexity of passwords by analyzing their length and the presence of uppercase and lowercase letters, digits, and special characters.

2. It also checks if the password is common by comparing it against a predefined wordlist.

3. Based on these criteria, the program assigns a complexity score to the password.


Strength Evaluation

1. Using the complexity score, the program determines the strength of the password.

2. If the password is deemed strong, it indicates that the password meets or exceeds recommended security standards.

3. For passwords with medium strength, the program offers suggestions for strengthening by generating an improved password.

4. Weak passwords prompt the program to recommend generating a strong password for better security.
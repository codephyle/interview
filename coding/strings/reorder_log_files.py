# Reorder log files

# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

# There are two types of logs:

# - **Letter-logs**: All words (except the identifier) consist of lowercase English letters.
# - **Digit-logs**: All words (except the identifier) consist of digits.

# Reorder these logs so that:

# - The **letter-logs** come before all **digit-logs**.
# - The **letter-logs** are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# - The **digit-logs** maintain their relative ordering.

# Return _the final order of the logs._

# ```
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".


# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
def reorder_logs(logs):
    letter_logs = []
    digit_logs = []

    # Split logs into letter-logs and digit-logs
    for log in logs:
        if log.split()[1].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append(log)

    # Sort letter-logs lexicographically by their contents and identifiers
    letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    # Combine letter-logs and digit-logs
    return letter_logs + digit_logs


logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
reordered_logs = reorder_logs(logs)
print(reordered_logs)

# ```

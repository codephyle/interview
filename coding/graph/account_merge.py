# 721. Accounts Merge

# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

# Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
# Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]

from collections import defaultdict


def accountsMerge(accounts):
    # Step 1: Build the graph
    graph = defaultdict(list)
    email_to_name = {}
    for account in accounts:
        name = account[0]
        emails = account[1:]
        for email in emails:
            # Connect all emails to the first email in the account
            graph[email].append(emails[0])
            email_to_name[email] = name

    # Step 2: Perform DFS traversal to merge accounts
    visited = set()
    merged_accounts = []

    def dfs(email):
        visited.add(email)
        merged_account.append(email)
        for neighbor in graph[email]:
            if neighbor not in visited:
                dfs(neighbor, graph, visited, merged_account)

    for email in graph:
        if email not in visited:
            merged_account = []
            dfs(email, graph, visited, merged_account)
            merged_accounts.append(merged_account)

    # Step 3: Sort the emails in each merged account
    for account in merged_accounts:
        account[1:] = sorted(account[1:])

    return merged_accounts


def accountsMerge(accounts):
    # Step 1: Create a dictionary to store the email to account mapping
    email_to_account = {}

    # Step 2: Create a dictionary to store the parent of each email
    parent = {}

    # Step 3: Create a dictionary to store the name of each email
    name = {}

    # Step 4: Initialize the parent and name dictionaries
    for account in accounts:
        for i in range(1, len(account)):
            email = account[i]
            parent[email] = email
            name[email] = account[0]

    # Step 5: Perform union-find operations
    def find(email):
        if parent[email] != email:
            parent[email] = find(parent[email])
        return parent[email]

    def union(email1, email2):
        parent[find(email1)] = find(email2)

    for account in accounts:
        root_email = find(account[1])
        for i in range(2, len(account)):
            union(root_email, account[i])

    # Step 6: Group the emails by their root email
    merged_accounts = defaultdict(list)
    for email in parent:
        root_email = find(email)
        merged_accounts[root_email].append(email)

    # Step 7: Format the merged accounts
    result = []
    for root_email, emails in merged_accounts.items():
        result.append([name[root_email]] + sorted(emails))

    return result


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]
result = accountsMerge(accounts)
print(result)

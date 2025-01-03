# Robinhood is famous for its referral program. It’s exciting to see our users spreading the word across their friends and family. One thing that is interesting about the program is the network effect it creates. We would like to build a dashboard to track the status of the program. Specifically, we would like to learn about how people refer others through the chain of referral.

# For the purpose of this question, we consider that a person refers all other people down the referral chain. For example, A refers B, C, and D in a referral chain of A -> B -> C -> D. Please build a leaderboard for the top 3 users who have the most referred users along with the referral count.

# Referral rules:
    # A user can only be referred once.
    # Once the user is on the RH platform, he/she cannot be referred by other users. For example: if A refers B, no other user can refer A or B since both of them are on the RH platform.
    # Referrals in the input will appear in the order they were made.

# Leaderboard rules:
    # The user must have at least 1 referral count to be on the leaderboard.
    # The leaderboard contains at most 3 users.
    # The list should be sorted by the referral count in descending order.
    # If there are users with the same referral count, break the ties by the alphabetical order of the user name.

# Input
    # rh_users = ["A", "B", "C"]
    # new_users = ["B", "C", "D"]
# Output
    # ["A 3", "B 2", "C 1"]
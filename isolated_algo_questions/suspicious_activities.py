suspicious_activities = [
       ("Albert", "San Francisco", "deposit"),
       ("Brad", "San Francisco", "withdraw"),
       ("Claire", "New York", "withdraw")
]

new_activities = [
       ("Joe", "Miami", "withdraw"),
       ("John", "San Francisco", "deposit"),
       ("Diana", "London", "withdraw"),
       ("Diana", "San Francisco", "withdraw"),
       ("Albert", "London", "withdraw"),
       ("Joe", "New York", "update_address"),
       ("Claire", "Miami", "deposit"),
       ("Diana", "New York", "deposit"),
       ("Albert", "Chicago", "withdraw"),
       ("Brad", "Paris", "deposit"),
       ("Claire", "Paris", "deposit"),
       ("Diana", "Vancouver", "file_dispute"),
       ("John", "Mumbai", "withdraw")
]

k = 2


def findsuspiciousactivities(suspicious_activities, new_activities, k):
    new_suspicious = []

    for suspicious_activity in suspicious_activities:
        for idx, new_activity in enumerate(new_activities):
            
            count = 0
            if suspicious_activity[0] == new_activity[0]:
                count += 1
            if suspicious_activity[1] == new_activity[1]:
                count += 1
            if suspicious_activity[2] == new_activity[2]:
                count += 1
            if count >= k and new_activity not in suspicious_activities:
                del new_activities[idx]
                suspicious_activities.append(new_activity)
                new_suspicious.append(new_activity)
    return new_suspicious

print(findsuspiciousactivities(suspicious_activities, new_activities, k))

from fetch_contributors import get_contributors, get_commenters
from fetch_stargazers import get_stargazers

def set_valid_user_list() -> None:
    # This proves who logged in
    commenters = get_commenters()
    # These two prove who is contributor and/or stargazers
    contributors = get_contributors()
    stargazers = set(get_stargazers())

    valid_users = set(map(str, commenters.union(contributors).union(stargazers)))

    with open('valid_commenters.txt', 'w') as f:
        output = ','.join(commenters)
        f.write(output)

    with open('valid_contributors.txt', 'w') as f:
        output = ','.join(contributors)
        f.write(output)

    with open('valid_stargazers.txt', 'w') as f:
        output = ','.join(stargazers)
        f.write(output)

    with open('valid_users.txt', 'w') as f:
        output = ','.join(valid_users)
        f.write(output)


def get_valid_user_list() -> list:
    with open('valid_users.txt', 'r') as f:
        data = f.read()

    valid_user_list = data.split(',')
    return valid_user_list


def get_access_level(user: str) -> int:
    # return access level of a user
    with open('valid_commenters.txt', 'w') as f:
        commenters = f.read()

    with open('valid_contributors.txt', 'w') as f:
        contributors = f.read()

    with open('valid_stargazers.txt', 'w') as f:
        stargazers = f.read()

    if user not in commenters:
        return -1

    if (user in stargazers) and (user not in contributors):
        return 0

    if (user in stargazers) and (user in contributors):
        return 1

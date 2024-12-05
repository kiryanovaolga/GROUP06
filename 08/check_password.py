import re

rx_number = re.compile(r'\d')
rx_lower = re.compile(r'[a-z]')
rx_upper = re.compile(r'[A-Z]')
rx_spec = re.compile(r'[-._]')


def check_password(password: str) -> bool:
    match_number = rx_number.search(password)
    match_lower = rx_lower.search(password)
    match_upper = rx_upper.search(password)
    match_spec = rx_spec.search(password)

    return all((
        match_number,
        match_lower,
        match_upper,
        match_spec,
    ))

print(check_password('hello'))
print(check_password('hello1ZZZ-'))


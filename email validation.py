--Email Slicer--

email = input('enter your email :').strip()

username = email[:email.index('@')]
domain = email[email.index('@')+1:]

print(f"your username {username} & domain is {domain}")
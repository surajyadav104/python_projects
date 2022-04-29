email = str(input("Enter your email address\n"))
username=email[:email.index("@")]
domain=email[email.index("@")+1:]
print(username)
print(domain)
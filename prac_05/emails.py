def main():
    """stores users emails (unique keys) and names (values) in a dictionary."""

    email_name_dict = {}
    user_email = input("Email:")
    while user_email != '':
      user_name = get_name_from_email(user_email)
      confirm = input("Is your name {}? (Y/n) ".format(user_name))
      if confirm.upper() != "Y" and confirm != "":
        user_name = input("Name: ")
      email_name_dict[user_email] = user_name
      user_email = input("Email: ")

    for user_email, user_name in email_name_dict.items():
        print("{} ({})".format(user_name, user_email))


def get_name_from_email(user_email):
    """Get the name from email."""
    part_1 = user_email.split('@')[0]
    part_2 = part_1.split('.')
    user_name = " ".join(part_2).title()
    return user_name


main()

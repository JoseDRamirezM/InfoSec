def get_passwords(pass_list):
    with open("./passwords.txt") as passwords:
        for line in passwords:
            pass_list.append(f'"{line.rstrip()}"')
        return pass_list

all_pass_string = ",".join(get_passwords([]))
print(all_pass_string)
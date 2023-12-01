import shutil
import re

def clean_and_extract_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return [re.sub(r' - .*', '', line).strip().lower() for line in file]

def mangle_names(names):
    mangled_names = []
    for name in names:
        parts = name.split()
        if len(parts) >= 2:
            first, last = parts[0], parts[-1]
            mangled_names.append(f"{first[0]}{last}".lower())
        else:
            continue
    return mangled_names

def save_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(f"{item}\n" for item in data)

def filter_names(names):
    return [name for name in names if '.' not in name]

def create_potential_emails(file_path, output_file, domain):
    with open(file_path, 'r', encoding='utf-8') as file:
        names = file.readlines()
    emails = [name.strip() + f"@{domain}\n" for name in names]
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(emails)

def clean_email_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        emails = file.readlines()
    cleaned_emails = set()
    for email in emails:
        email = email.strip()
        if ' ' not in email and "'" not in email:
            cleaned_emails.add(email)
    with open(file_path, 'w', encoding='utf-8') as file:
        for email in sorted(cleaned_emails):
            file.write(f"{email}\n")

def mangler_main(input_file, output_file, domain):
    shutil.copyfile(input_file, 'key/user-title.txt')
    clean_names = clean_and_extract_names('key/user-title.txt')
    mangled_names = mangle_names(clean_names)
    filtered_names = filter_names(mangled_names)
    save_to_file('key/filtered.txt', filtered_names)
    create_potential_emails('key/filtered.txt', output_file, domain)
    clean_email_file(output_file)

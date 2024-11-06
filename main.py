import zipfile

# Function to try passwords from a wordlist on a zip file
def crack_zip_with_wordlist(zip_filename, wordlist_file):
    # Open the zip file in read mode
    zip_file = zipfile.ZipFile(zip_filename, 'r')

    # Read the wordlist
    with open(wordlist_file, 'r') as file:
        for line in file:
            password = line.strip()  # Strip newlines and any extra spaces
            try:
                # Try extracting the zip file with the current password
                zip_file.extractall(pwd=password.encode())
                print(f'Password found: {password}')
                return password
            except RuntimeError:
                # If the password is incorrect, skip to the next one
                continue

    print('Password not found in the wordlist.')
    return None

# Main execution - get file paths from the user
zip_filename = input('Enter the path to the ZIP file: ')  # Get ZIP file path from the user
wordlist_file = input('Enter the path to the wordlist file: ')  # Get wordlist file path from the user

crack_zip_with_wordlist(zip_filename, wordlist_file)

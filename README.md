
# ZIP Wordlist Cracker

This is a simple Python script for cracking ZIP file passwords using a wordlist.

## Requirements

- Python 3.x
- `zipfile` module (comes with Python by default)

## Usage

1. Make sure you have the `Flag.zip` file (or any other ZIP file you want to crack) and a wordlist file (e.g., `my-rockyou.txt`).
2. Place the ZIP file and the wordlist file in the same directory as the script, or provide their full paths.
3. Run the script using the following command:

   ```bash
   python main.py
   ```

4. The script will prompt you to enter the path of the ZIP file and the wordlist file.

   Example:
   ```
   Enter the path to the ZIP file: G:\Codes\CS\ZIP Wordlist Cracker\Flag.zip
   Enter the path to the wordlist file: G:\Codes\CS\ZIP Wordlist Cracker\my-rockyou.txt
   ```

5. The script will try each password from the wordlist and attempt to extract the contents of the ZIP file. If it finds the correct password, it will print the password and stop.

## Notes

- Ensure the ZIP file is not encrypted with additional protection layers (e.g., AES).
- The script works by attempting to extract the contents of the ZIP file using passwords from the provided wordlist.
- The script will print the found password if it successfully extracts the file.

## License

This project is licensed under the MIT License.

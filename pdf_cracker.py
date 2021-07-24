import pikepdf
from tqdm import tqdm
import requests



url = 'https://raw.githubusercontent.com/x4nth055/pythoncode-tutorials/master/ethical-hacking/pdf-cracker/wordlist.txt'
page = requests.get(url)



# load password list
passwords = page.text.strip().split("\n")


# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    
    try:
        # open PDF file
        with pikepdf.open("foo.pdf", password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            print("[+] Password found:", password)
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue
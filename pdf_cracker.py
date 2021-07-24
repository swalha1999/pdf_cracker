import pikepdf
from tqdm import tqdm
import requests



url = 'https://raw.githubusercontent.com/swalha1999/pdf_cracker/main/wordlist.txt'
page = requests.get(url)



# load password list
passwords = page.text.strip().split("\n")


final_password = ""

# iterate over passwords
for password in tqdm(passwords, "Decrypting PDF"):
    
    try:
        # open PDF file
        with pikepdf.open("foo.pdf", password=password) as pdf:
            # Password decrypted successfully, break out of the loop
            #print("[+] Password found:", password)
            final_password = password
            break
    except pikepdf._qpdf.PasswordError as e:
        # wrong password, just continue in the loop
        continue

if final_password != "":
    print('\033[92m' ,"[+] Password found:", password ,'\033[0m')

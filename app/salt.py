# Hashing
from cryptography.fernet import Fernet 
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC 
import base64

# json files
import json

# system information
import os

from fastapi import FastAPI, Query
# uvicorn salt:app --host 0.0.0.0 --port 8000
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://localhost.tiangolo.com",
    "http://127.0.0.1:5500",
    "https://hashing-service-waelke553.cloud.okteto.net",
    "https://hashing-service-waelke553.cloud.okteto.net:8080",
    "https://hashing-service-waelke553.cloud.okteto.net:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





file_name = "salt_file.json"
# https://stackoverflow.com/questions/22082004/python-check-if-data-file-exists-relative-to-source-code-file
absolute_path_to_this_python = os.path.dirname(os.path.realpath(__file__))
path_to_file = absolute_path_to_this_python + "/" + file_name



def make_salt(password_for_hash_and_unhashing):
    key = password_for_hash_and_unhashing.encode()
    salt = b'SALT'
    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
            )
    safe_key = base64.urlsafe_b64encode(kdf.derive(key))

    return safe_key
    

# f = Fernet(make_salt("test"))


if (os.path.isfile(path_to_file) and os.stat(path_to_file).st_size != 0):
    # File bestaat
    with open(path_to_file, "r") as file:
        existing_data = json.load(file)

    # list = existing_data
else:
    # File bestaat nog niet
    # file = open(path_to_file, "w")
    existing_data = {}


def encrypt(password_to_hash, salt_password):
    f = Fernet(make_salt(salt_password)) 
    encpassword = f.encrypt(password_to_hash.encode())

    # This will return a encrypted password.
    return encpassword.decode()



def decrypt(user_name, user_website, salt_password):

    try:
        hashed_password = existing_data[user_name][user_website]
        f = Fernet(make_salt(salt_password))

        decpassword = f.decrypt(hashed_password.encode())

        return {
            "user_name": user_name,
            "website": user_website,
            "password": decpassword.decode(),
            "key": salt_password
        }
        # "password of " + user_name + "/" + user_website + " has being decrepted: " + decpassword.decode()

    except KeyError:
        return {
            "error": "Can't find your Name or Website!"
        }
        
        
    except:
        return {
            "error": "Sorry! The key you gave is wrong"
        }







# Get all user sites if the user exists.
@app.get("/users/1/{user_name}")
async def get_user_websites(user_name: str):
    # ask for websites of the user.
    for user in existing_data:
        if user_name == user:
            websites = []
            for website in existing_data[user]:
                websites.append(website)
            return {
                "user_name": user_name,
                "websites": websites
            }
            # "The websites of the user " + user_name.upper() + " are " + websites[:-2]
        else:
            return {
                "error": 'Did not find your user in the system.'
            }

# Get Decrypted passwords of user his website. 
@app.get("/users/2/{user_name}/{user_website}/{key_password}")
async def unhash_password_of_website(user_name: str, user_website:str, key_password: str):
    # Decrypt passwords
    if existing_data == {}:
        # File is empty and you can't decrypt anything.
        return {
            "error": "You haven't put any user in the system yet"
        }
    else:
        return decrypt(user_name, user_website, key_password)  


# Add/change a user and website password.
@app.post("/users/3/{user_name}/{user_website}/{user_password}/{key_password}")
async def add_and_change_user_and_website(user_name: str, user_website:str, user_password: str | None = Query(default=None, min_length=6), key_password: str | None = Query(default=None, min_length=6)):
    
    if user_password == None or key_password == None:
        return "Your password or key password is empty and this is not allowed."
    else:
        # Encrypt passwords
        file = open(path_to_file, "w")

        if user_name not in existing_data.keys():
            # Nieuw user wants to encrypt something.
            existing_data[user_name] = {
                user_website: encrypt(user_password, key_password)
            }

            file.write(json.dumps(existing_data,indent = 4))
            file.close()

            return {
                "user_name": user_name,
                "website": user_website
            } 
            #"Nieuw user: " + user_name + " with the password of website: " + user_website + " has being encrypted."
        else:
            # Old User wants to encrypt something.
            if user_website not in existing_data[user_name]:
                # User exists but NEW website being added.
                existing_data[user_name][user_website] = encrypt(user_password, key_password)
            else:
                # User exists and website also exists.
                # password has being changed
                existing_data[user_name][user_website] = encrypt(user_password, key_password)

        file.write(json.dumps(existing_data,indent = 4))
        file.close()

        return {
                "user_name": user_name,
                "website": user_website
            } 
        #"Old user: " + user_name + " with the password of website: " + user_website + " has being encrypted."

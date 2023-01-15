import pyrebase
from db.config import config_keys as keys
# store your own firebase config there


from flet.security import encrypt, decrypt
 


secret_key = "sample"

class PyrebaseWrapper:
    """
    Wraps Pyrebase with flet authentication flow. 
    """

    def __init__(self, page):
        self.page = page
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.idToken = None
        self.check_token()

    def save_token(self, token, page):
        encrypted_token = encrypt(token, secret_key)
        page.client_storage.set("firebase_token", encrypted_token)
    
    def erase_token(self):
        self.page.client_storage.remove("firebase_token")

    def sign_in(self, email, password):
        user = self.auth.sign_in_with_email_and_password(email, password)
        if user:
            token = user["idToken"]
            self.save_token(token, self.page)

    def sign_out(self):
        self.erase_token()

    def check_token(self):
        encrypted_token = self.page.client_storage.get("firebase_token")
        if encrypted_token:
            decrypted_token = decrypt(encrypted_token, secret_key)
            self.idToken = decrypted_token
            return True
        else:
            return None

    def get_data(self):
        return self.db.child("data").get(token=self.idToken).val()
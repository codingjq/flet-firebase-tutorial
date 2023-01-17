import pyrebase
from db.config import config_keys as keys

from flet.security import encrypt, decrypt
 


secret_key = "sample"

class PyrebaseWrapper:
    """
    Wraps Pyrebase with flet authentication flow and abstracts crud for my app. 
    """

    def __init__(self, page):
        ### Database initialization for the entire app
        self.page = page
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        ### Where we store the temporary token and permanent user ID while app is running
        self.idToken = None
        self.uuid = None
        ### If app was recently runnnig we can grab the token from user's machine.
        self.check_token()

        self.streams = []

    def save_tokens(self, token, uuid, page):
        ### encrypt the token before storing to prevent other applications from stealing it.
        encrypted_token = encrypt(token, secret_key)
        page.client_storage.set("firebase_token", encrypted_token)
        page.client_storage.set("firebase_id", uuid)
        self.idToken = token
        self.uuid=uuid
    
    def erase_token(self):
        self.page.client_storage.remove("firebase_token")
        self.page.client_storage.remove("firebase_id")

    def register_user(self, name, username, email, password):
        self.auth.create_user_with_email_and_password(email, password)
        self.sign_in(email, password)
        self.db.child("users").child(self.uuid).update(data={"name": name, "username": username}, token=self.idToken)

    def sign_in(self, email, password):
        user = self.auth.sign_in_with_email_and_password(email, password)
        if user:
            token = user["idToken"]
            uuid = user["localId"]
            self.save_tokens(token, uuid, self.page)

    def sign_out(self):
        self.erase_token()

    def check_token(self):
        ### Prevents the user from having to sign in all the time
        encrypted_token = self.page.client_storage.get("firebase_token")
        uuid = self.page.client_storage.get("firebase_id")
        if encrypted_token:
            decrypted_token = decrypt(encrypted_token, secret_key)
            self.idToken = decrypted_token
            self.uuid = uuid
            try:
                self.auth.get_account_info(self.idToken)
                return "Success"
            except:
                return None
        return None

    def get_username(self):
        return self.db.child("users").child(self.uuid).child("username").get(token=self.idToken).val()

    ### CRUD ###
    def add_note(self, data):
        if self.uuid == None:
            self.uuid = self.auth.get_account_info(self.idToken)["users"][0]["localId"]
        self.db.child("users").child(self.uuid).child("notes").push(data, self.idToken)

    def get_notes(self):
        return self.db.child("users").child(self.uuid).get(token=self.idToken).val()

    def stream_data(self, stream_handler):
        stream = self.db.child("users").child(self.uuid).child("notes").stream(stream_handler=stream_handler, token=self.idToken)
        self.streams.append(stream)

    def edit_note(self, note_uuid, data):
        self.db.child("users").child(self.uuid).child("notes").child(note_uuid).update(data, token=self.idToken)

    def delete_note(self, note_uuid):
        self.db.child("users").child(self.uuid).child("notes").child(note_uuid).remove(token=self.idToken)

    ### not killing the streams causes read multiplication
    def kill_all_streams(self):
        for stream in self.streams:
            try:
                stream.close()
            except:
                print("no streams")
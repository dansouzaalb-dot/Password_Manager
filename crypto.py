from cryptography.fernet import Fernet
KEY_FILE = "key.key"

#--- Key Generator ---
def generate_key():
	key = Fernet.generate_key()
	with open(KEY_FILE, "wb") as f:
		f.write(key)

#--- Loads Key ---
def load_key():
	return open(KEY_FILE, "rb").read()

#--- Encrypts ---
def encrypt(text):
	key = load_key()
	f = Fernet(key)
	return f.encrypt(text.encode()).decode()

#--- Decrypts ---
def decrypt(token):
	key = load_key()
	f = Fernet(key)
	return f.decrypt(token.encode()).decode()


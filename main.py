from crypto import generate_key, encrypt, decrypt
from storage import load_data, save_data
from color import red, green
from getpass import getpass

#--- Adds passwords ---
def add_password(data):
	site = input("Site: ")
	username = input("Username: ")
	password = getpass("Password: ")

	encrypted = encrypt(password)

	data.append({
		"site": site,
		"username": username,
		"password": encrypted
	})

	save_data(data)
	print(green("Saved securely."))

#--- View Passwords ---
def view_passwords(data):
	if not data:
		print(red("No data"))
		return
	
	for item in data:
		print("\nSite:", item["site"])
		print("User:", item["username"])
		print("Pass:", decrypt(item["password"]))

#--- Search by Site ---
def search_site(data):
	if not data:
		print(red("\nNo Sites!"))
		return

	keyword = input("Search site: ").lower()
	found = False

	for item in data:
		if keyword in item["site"].lower():
			print(green(item["site"]))
			print("User:", item["username"])
			print("Pass:", decrypt(item["password"]))
			found = True

	if not found:
		print(red("Site not found"))

#--- Delete Datas ---
def delete(data):
	if not data:
		print(red("No data to delete."))
		return

	for i, item in enumerate(data, 1):
		print(f"{i} - {item['site']}")

	try:
		index = int(input("Choose a index to delete: "))	
		removed = data.pop(index -1)
		save_data(data)
		print(green(f"Removed: {removed['site']}"))
	except (ValueError, IndexError):
		print(red("Invalid selection"))
		return

#--- Menu ---
def menu():
	print("\n---PASSWORD MANAGER ---")
	print("1 Add password")
	print("2 View passwords")
	print("3 Search by site")
	print("4 Delete datas")
	print("5 Quit")

#--- Main ---
def main():

	try:
		open("key.key")
	except:
		generate_key()

	data = load_data()

	while True:
		menu()
		choice = input("Choose: ")

		if choice == "1":
			add_password(data)
		elif choice == "2":
			view_passwords(data)
		elif choice == "3":
			search_site(data)
		elif choice == "4":
			delete(data)
		elif choice == "5":
			break
		else:
			print(red("INVALID"))

if __name__ == "__main__":
	main()


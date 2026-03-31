except:
	generate_key()

data = load_data()

While True:
	menu()
	choice = input("Choose: ")

	if choice == "1":
		add_passsword(data)
	elif choice == "2":
		view_passwords(data)
	elif choice == "3":
		break
	else:
		print(red("INVALID"))

if __name__ == "__main__":
	main()


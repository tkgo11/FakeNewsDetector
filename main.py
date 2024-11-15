import os
choice = input("(1) Run main (2) Run accuracy checker : ")
if choice == "1":
    os.system("python app.py")
elif choice == "2":
    data = ["data/사실.txt", "data/대체로 사실.txt", "data/절반의 사실.txt", "data/대체로 사실 아님.txt", "data/전혀 사실 아님.txt"]

    non_existent_files = []
    empty_files = []
    for file in data:
        if not os.path.exists(file):
            non_existent_files.append(file)
        elif os.path.getsize(file) == 0:
            empty_files.append(file)
    if non_existent_files:
        for file in non_existent_files:
            print(f"{file} does not exist.")
    if empty_files:
        for file in empty_files:
            print(f"{file} is empty.")
    if non_existent_files or empty_files:
        choice = input("Data files are not ready. Get them? (y/n) : ")
        if choice == "y":
            os.system("python crawling.py")
        else:
            print("Exiting...")
            exit(1)
    else:
        os.system("python accuracy_checker.py")
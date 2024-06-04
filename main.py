
def addVoters():
    print()
    print('ADD VOTER')
    vid = input("Enter Voter's ID: ")
    vname = input("Enter Voter's Name: ")
    with open("voters.txt", "a") as file:
        file.write(f"{vid.upper()},{vname.upper()}\n")
    print("Voter Account created successfully!")
    print()

def viewVoters():
    print()
    print('VIEW VOTERS')
    print("Voter's ID | Voter's Name")
    with open("voters.txt", "r") as file:
        for line in file:
            info = line.strip().split(",")
            print(f"{info[0]} | {info[1]}")
    print()


def addCandidates():
    print()
    print('ADD CANDIDATE')
    cname = input("Enter Candidate's Name: ")
    cp = input("Enter Candidate's Party: ")
    votes = 0
    with open("candidates.txt", "a") as file:
        file.write(f"{cname.upper()},{cp.upper()},{votes}\n")
    print("Candidates Account created successfully!")
    print()


def viewCandidates():
    print()
    print('VIEW CANDIDATES')
    with open("candidates.txt", "r") as file:
        print("Candidate's Name | Candidate's Party")
        for line in file:
            info = line.strip().split(",")
            print(f"{info[0]} | {info[1]}")
    print()

def voteNow():
    print()
    print('VOTE NOW')
    vid = input("Enter Your Voter's ID: ")
    with open("voters.txt", "r+") as file:
        data = file.readlines()
        file.seek(0)
        for line in data:
            info = line.strip().split(",")
            if info[0] == vid:
                with open("candidates.txt", "r") as file:
                    print("Candidate's Name | Candidate's Party")
                    for line in file:
                        info = line.strip().split(",")
                        print(f"{info[0]} | {info[1]}")
                cp = input("Enter Party To Vote For: ")
                with open("candidates.txt", "r+") as file:
                    data = file.readlines()
                    file.seek(0)
                    for line in data:
                        info = line.strip().split(",")
                        if info[1] == cp:
                            info[2] = str(int(info[2]) + 1)
                            file.write(",".join(info) + "\n")
                        else:
                            file.write(line)
                    file.truncate()

    print("Vote CASTED successfully!")
    print()


def viewResults():
    print()
    print('VIEW RESULT')
    with open("candidates.txt", "r") as file:
        print("Candidate's Name | Candidate's Party | Result")
        for line in file:
            info = line.strip().split(",")
            print(f"{info[0]} | {info[1]}| {info[2]}")
    print()


if __name__ == "__main__":
    while True:
        print("1. Create Voter's Account")
        print("2. View Voters")
        print("3. Create Candidate's Account")
        print("4. View Candidates")
        print("5. Vote Now")
        print("6. View Result")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addVoters()
        elif choice == "2":
            viewVoters()
        elif choice == "3":
            addCandidates()
        elif choice == "4":
            viewCandidates()
        elif choice == "5":
            voteNow()
        elif choice == "6":
            viewResults()
        elif choice == "7":
            break
        else:
            print("Invalid choice!")

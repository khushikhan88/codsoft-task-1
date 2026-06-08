# Student Mood Chatbot
# Created by Khushi Khan

print("=" * 50)
print("      WELCOME TO STUDENT MOOD CHATBOT")
print("=" * 50)

name = input("Enter your name: ")

print(f"\nHello {name}! I am here to help you.")

while True:
    print("\nChoose your mood:")
    print("1. Happy")
    print("2. Stressed")
    print("3. Tired")
    print("4. Bored")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("\n😊 That's great!")
        print("Keep working towards your goals and stay positive.")

    elif choice == "2":
        print("\n😟 You seem stressed.")
        print("Try the 25-5 study technique:")
        print("Study for 25 minutes and rest for 5 minutes.")

    elif choice == "3":
        print("\n😴 You seem tired.")
        print("Take a short break, drink water, and get some rest.")

    elif choice == "4":
        print("\n😐 Feeling bored?")
        print("Try learning a new Python concept or solving a coding problem.")

    elif choice == "5":
        print(f"\nGoodbye {name}! Have a wonderful day.")
        break

    else:
        print("\nInvalid choice. Please try again.")
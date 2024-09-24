from src.main import lib, tms, calc, oms

if __name__ == "__main__":
    try:
        print("Select Tasks:\n")

        print("""
        > Task 1: Library Management (src/lib.py)
        > Task 2: Task Management System (src/tms.py)
        > Task 3: Calculator using design patterns (src/calc.py)
        > Task 4: Order Management System (src/oms.py)
        Usage example in `src/main.py`
        """)

        user_input = input("")

        match user_input:
            case "1":
                lib()

            case "2":
                tms()

            case "3":
                calc()

            case "4":
                oms()

            case _:
                print("Enter number!")

    except KeyboardInterrupt:
        print("\nExiting...")

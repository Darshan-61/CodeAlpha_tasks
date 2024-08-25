def calculate_average(grades):
    return sum(grades) / len(grades) if grades else 0

def main():
    std_name = input("Enter student name: ")
    n = int(input("Enter the number of subjects: "))

    grades = [float(input(f"Enter grade for subject {i+1}: ")) for i in range(n)]

    average = calculate_average(grades)

    print("\n--- GRADE TRACKER  ---")
    print(f"Student: {std_name}")
    for i, grade in enumerate(grades, 1):
        print(f"Subject {i}: {grade}")
    print(f"Average Grade: {average}")

if __name__ == "__main__":
    main()
    
    
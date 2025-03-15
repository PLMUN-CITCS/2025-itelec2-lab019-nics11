def get_student_score() -> int:
    """
    Function to get the score input from the user. Ensures valid numeric input.
    
    Returns:
        int: The student's numerical score.
    """
    while True:
        try:
            score = int(input("Enter your score: "))
            if 0 <= score <= 100:  # Ensuring the score is within a valid range
                return score
            else:
                print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid numerical score.")

def calculate_grade(score: int) -> str:
    """
    Function to calculate the grade based on the score.
    
    Args:
        score (int): The numerical score of the student.
        
    Returns:
        str: The grade corresponding to the score.
    """
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def main():
    """
    Main function to drive the grade calculation process.
    """
    score = get_student_score()  # Get the score from the user
    grade = calculate_grade(score)  # Calculate the grade based on the score
    print(f"Your Grade is: {grade}")

# Calling the main function to execute the program
if __name__ == "__main__":
    main()

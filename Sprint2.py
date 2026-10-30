# Breaking Bad Trivia Quiz - Sprint 2
# Author: Evan Scalo
"""Run a twenty-question Breaking Bad quiz with timing, scoring, and replay."""

__author__ = "Evan Scalo"

# Used GeeksForGeeks to learn how to import and use time in Sprint 1.
import time

def show_instructions(question_count):
    """Accept the number of questions and print instructions; return None."""

    # String * repeats text to create a divider.
    divider = "=" * 79

    # String + joins text.
    print("\n" + divider + "\n")

    print("Welcome to Breaking Bad Trivia!!!")
    print("SPOILER WARNING")
    print("Questions cover events from the entire series.")

    print("\nINSTRUCTIONS")
    print("There are", question_count, "questions in each round.")
    print("Enter A, B, C, or D. Lowercase letters also work.")
    print("Each correct answer earns 10 base points.")
    print("An incorrect or invalid answer earns zero points.")
    print("Every five consecutive correct answers earn 100 bonus points.")
    print("An incorrect or invalid answer resets your streak.")
    print("The timer measures how long you take to finish the round.")

    print("\n" + divider + "\n")

def ask_question(question_number):
    """Accept a question number from 1 to 20; return 1 if correct, else 0."""

    print("\nQUESTION", question_number)

    # These variables store the correct answer for the selected question.
    correct_answer = ""
    correct_text = ""

    # An if-elif structure selects which question to display.
    # == checks whether two values are equal.
    if question_number == 1:
        print("What subject does Walter White teach?")
        print("A. Physics")
        print("B. Biology")
        print("C. Chemistry")
        print("D. Mathematics")
        correct_answer = "C"
        correct_text = "Chemistry"

    elif question_number == 2:
        print("What is Walter White's criminal alias?")
        print("A. Heisenberg")
        print("B. Cap'n Cook")
        print("C. The Governor")
        print("D. Eladio")
        correct_answer = "A"
        correct_text = "Heisenberg"

    elif question_number == 3:
        print("What is the name of Walter's former student and partner?")
        print("A. Todd Alquist")
        print("B. Gale Boetticher")
        print("C. Badger Mayhew")
        print("D. Jesse Pinkman")
        correct_answer = "D"
        correct_text = "Jesse Pinkman"

    elif question_number == 4:
        print("Which fast-food chain does Gus Fring operate?")
        print("A. Taco Bell")
        print("B. Los Pollos Hermanos")
        print("C. Cluckin' Bell")
        print("D. El Pollo Loco")
        correct_answer = "B"
        correct_text = "Los Pollos Hermanos"

    elif question_number == 5:
        print("What is the name of Walter's wife?")
        print("A. Marie")
        print("B. Lydia")
        print("C. Skyler")
        print("D. Jane")
        correct_answer = "C"
        correct_text = "Skyler"

    elif question_number == 6:
        print("Which agency does Hank Schrader work for?")
        print("A. DEA")
        print("B. FBI")
        print("C. CIA")
        print("D. IRS")
        correct_answer = "A"
        correct_text = "DEA"

    elif question_number == 7:
        print("What color is Walter's signature methamphetamine?")
        print("A. Green")
        print("B. Red")
        print("C. Purple")
        print("D. Blue")
        correct_answer = "D"
        correct_text = "Blue"

    elif question_number == 8:
        print("What is the name of Walter and Jesse's lawyer?")
        print("A. Howard Hamlin")
        print("B. Saul Goodman")
        print("C. Chuck McGill")
        print("D. Rich Schweikart")
        correct_answer = "B"
        correct_text = "Saul Goodman"

    elif question_number == 9:
        print("In which city is Breaking Bad primarily set?")
        print("A. Phoenix")
        print("B. El Paso")
        print("C. Albuquerque")
        print("D. Denver")
        correct_answer = "C"
        correct_text = "Albuquerque"

    elif question_number == 10:
        print("What business do Walter and Skyler buy to launder money?")
        print("A. A car wash")
        print("B. A bowling alley")
        print("C. A restaurant")
        print("D. A laundromat")
        correct_answer = "A"
        correct_text = "A car wash"

    elif question_number == 11:
        print("What name does Walter Jr. choose to go by?")
        print("A. Junior")
        print("B. Henry")
        print("C. Jake")
        print("D. Flynn")
        correct_answer = "D"
        correct_text = "Flynn"

    elif question_number == 12:
        print("What type of cancer is Walter diagnosed with?")
        print("A. Brain cancer")
        print("B. Lung cancer")
        print("C. Skin cancer")
        print("D. Colon cancer")
        correct_answer = "B"
        correct_text = "Lung cancer"

    elif question_number == 13:
        print("What does Hector Salamanca use to communicate?")
        print("A. A bell")
        print("B. A phone keyboard")
        print("C. A whistle")
        print("D. Sign language")
        correct_answer = "A"
        correct_text = "A bell"

    elif question_number == 14:
        print("What vehicle do Walter and Jesse first use as a mobile lab?")
        print("A. A cargo van")
        print("B. A school bus")
        print("C. An RV")
        print("D. A pickup truck")
        correct_answer = "C"
        correct_text = "An RV"

    elif question_number == 15:
        print("What business hides Gus Fring's underground superlab?")
        print("A. A restaurant")
        print("B. A car wash")
        print("C. An auto repair shop")
        print("D. An industrial laundry")
        correct_answer = "D"
        correct_text = "An industrial laundry"

    elif question_number == 16:
        print("What is Mike's last name?")
        print("A. Salamanca")
        print("B. Ehrmantraut")
        print("C. Boetticher")
        print("D. Welker")
        correct_answer = "B"
        correct_text = "Ehrmantraut"

    elif question_number == 17:
        print("What food does Walter throw onto the roof of his house?")
        print("A. A sandwich")
        print("B. A cake")
        print("C. A pizza")
        print("D. A burrito")
        correct_answer = "C"
        correct_text = "A pizza"

    elif question_number == 18:
        print("What does Hank collect and insist are not simply rocks?")
        print("A. Minerals")
        print("B. Stamps")
        print("C. Coins")
        print("D. Baseball cards")
        correct_answer = "A"
        correct_text = "Minerals"

    elif question_number == 19:
        print("What alias does Jesse use before partnering with Walter?")
        print("A. Heisenberg")
        print("B. Tuco")
        print("C. Krazy-8")
        print("D. Cap'n Cook")
        correct_answer = "D"
        correct_text = "Cap'n Cook"

    elif question_number == 20:
        print("What is the name of Skyler's sister?")
        print("A. Lydia")
        print("B. Marie")
        print("C. Jane")
        print("D. Andrea")
        correct_answer = "B"
        correct_text = "Marie"

    # strip() removes leading and trailing spaces.
    # upper() allows lowercase answers by converting them to uppercase.
    answer = input("Your answer: ").strip().upper()

    # not in checks whether the answer is outside the valid choices.
    # Invalid answers receive zero points without another attempt.
    if answer not in ("A", "B", "C", "D"):
        print("Invalid answer. No points awarded.")
        print("Correct answer:", correct_answer + ". " + correct_text)
        return 0

    # An if-else structure checks whether a valid answer is correct.
    # The returned value is used to update the score in main().
    if answer == correct_answer:
        print("Correct! You earned 10 base points.")
        return 1
    else:
        print("Incorrect. No points awarded.")
        print("Correct answer:", correct_answer + ". " + correct_text)
        return 0

def show_results(player_name, correct, question_count, bonus, elapsed_time):
    """Accept round statistics, calculate and display results; return None."""

    # Subtraction calculates the number of incorrect answers.
    incorrect = question_count - correct

    # Each correct answer earns 10 base points.
    base_score = correct * 10

    # Addition combines base points and streak bonuses.
    final_score = base_score + bonus

    # // calculates the maximum number of five-answer streak bonuses.
    # ** squares 10 to calculate each 100-point bonus.
    maximum_score = question_count * 10 + (question_count // 5) * (10 ** 2)

    # / and * calculate the percentage of questions answered correctly.
    percentage = (correct / question_count) * 100

    # Convert elapsed time to whole seconds.
    total_seconds = int(elapsed_time)

    # // gives whole minutes; % gives the remaining seconds.
    minutes = total_seconds // 60
    seconds = total_seconds % 60

    print("\n" + "=" * 79)
    print("QUIZ RESULTS")

    # sep controls the separator between printed items.
    print("Player", player_name, sep=": ")
    print("Correct:", correct, "Incorrect:", incorrect)
    print("Base points:", base_score, "Bonus points:", bonus)

    # end keeps the following print output on the same line.
    print("Final score: ", end="")
    print(final_score, maximum_score, sep="/")

    # round() limits the displayed accuracy to one decimal place.
    print("Answer accuracy: ", round(percentage, 1), "%", sep="")
    print("Time taken:", minutes, "minutes and", seconds, "seconds")

    # An if-elif-else structure selects a performance message.
    # >= checks whether a value meets or exceeds a threshold.
    if correct == question_count:
        print("Perfect round! You are a Breaking Bad expert!")
    elif percentage >= 70:
        print("Great job! You know the show well.")
    elif percentage >= 40:
        print("Nice effort! Try another round to improve.")
    else:
        print("Time for a rewatch!")

    print("=" * 79)

def main():
    """Run the quiz and replay loop; take no parameters and return None."""

    question_count = 20

    # Pass the question count as an argument to the instructions function.
    show_instructions(question_count)

    player_name = input("Enter your name: ").strip()

    # A standalone if uses Boolean not to check for an empty name.
    if not player_name:
        player_name = "Player"

    # Start with Y so the player can complete the first round.
    play_again = "Y"

    # != means not equal.
    # This while loop ends when the player enters N.
    while play_again != "N":
        print("\nGood luck, " + player_name + "!")

        # Reset all round statistics before starting each round.
        correct = 0
        streak = 0
        bonus = 0

        # Start timing immediately before the questions.
        start_time = time.perf_counter()

        # for, in, and range() repeat the questions from 1 through 20.
        # The ending value of range() is excluded.
        for question_number in range(1, question_count + 1):

            # Pass the question number into ask_question().
            # Store the returned 1 or 0 in result.
            result = ask_question(question_number)

            # += is a shortcut operator that adds to the current value.
            correct += result

            # Correct answers increase the streak.
            # Incorrect or invalid answers reset the streak.
            if result == 1:
                streak += 1
            else:
                streak = 0

            # Boolean and requires both conditions to be true.
            # >= prevents a bonus at streak zero.
            # % checks whether the streak is a multiple of five.
            if streak >= 5 and streak % 5 == 0:
                bonus += 10 ** 2
                print("Five more consecutive correct answers! +100 bonus points!")

        # Stop timing after the final question.
        elapsed_time = time.perf_counter() - start_time

        # Pass the round statistics into the results function.
        show_results(player_name, correct, question_count, bonus, elapsed_time)

        play_again = input("\nPlay again? Enter Y or N: ").strip().upper()

        # Boolean or accepts either Y or N.
        # Boolean not keeps this loop running while the choice is invalid.
        # Asking for new input allows the loop to terminate.
        while not (play_again == "Y" or play_again == "N"):
            print("Invalid choice. Please enter Y or N.")
            play_again = input("Play again? Enter Y or N: ").strip().upper()

    print("\nThanks for playing, " + player_name + "!")

# Start the quiz only when this file is run directly.
if __name__ == "__main__":
    main()

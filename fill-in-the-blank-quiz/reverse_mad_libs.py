import six
import time

user_difficulty_selection = raw_input("Select difficulty: Easy, Medium, Hard --> ")

# verify_answer receives the text according to the difficulty selected, the user selected blank space, the user answer to be verified...
# the correct answer to check against, and the list of blank spaces so that the program can find the blank spaces to be replaced by...
# the correct answer.
def verify_answer(text, selected_space, user_answer, correct_answer, list_of_spaces):
	if correct_answer in user_answer.lower(): #used 'in' instead of '==' in case a user puts an accidental character or space before or after the answer
		print "Correct!"
		time.sleep(1)
		print text is None
		text = text.replace(list_of_spaces[eval(selected_space) - 1], user_answer)
		print text
		return text
	elif user_answer.lower() != correct_answer:
		print "Incorrect. Please try again."

# Function that runs a reverse mad libs that describes HTML.
def answer_reverse_mad_libs(blank_spaces, text, text_answers): # HTML.

	# Prints text with blank spaces so the user can select the blank space they want to fill.
	print text

	# When any of the blank spaces are in the text, this loop should keep running.
	while blank_spaces[0] or blank_spaces[1] or blank_spaces [2] or blank_spaces[3] or blank_spaces[4] in text:
		# It took me a while to figure this out, but without the "is not None" I would get an error.
		if text is not None and "_" not in text: # Prints complete when all blank spaces are filled in with correct answers.
			print "Complete!"
			return # Returning so that the function and program can end.

		# Variable that holds the user selection for the blank space they would like to answer.
		num_selection_var = raw_input("Choose number to answer --> ")

		# This while loop checks the user input and notifies the user if they are selecting a blank space that does not exist.
		# A loop is necessary so that it checks the input again after they put a new input. It should not end until the user...
		# puts in an input within bounds.
		while eval(num_selection_var) < 1 or eval(num_selection_var) > 5:
			print "Invalid number selection. Please enter a valid number."
			num_selection_var = raw_input("Choose number to answer --> ")
		answer = str(raw_input("What is the answer to " + num_selection_var + "? "))

		num_selection_list = [1, 2, 3, 4, 5]

		# For each answer the program verifies if the answer is correct with the verify_answer function.
		while "-" in answer:
			print "Please do not use hyphens."
			answer = str(raw_input("What is the answer to " + num_selection_var + "? "))
		if eval(num_selection_var) in num_selection_list:
			text = verify_answer(text, num_selection_var, answer, text_answers[eval(num_selection_var) - 1], blank_spaces)

# Function that runs the easy, medium, or hard functions based off of the user selected input.
def reverse_mad_libs(user_difficulty_selection):
	# Variable that holds a list of blank spaces so that I can check if these values are in each section of text.
	blank_spaces = ["_____1_____", "_____2_____", "_____3_____", "_____4_____", "_____5_____"]

	easy_text = "\n\nHTML stands for _____1_____. HTML is the standard language used for creating web pages. " \
	+ "HTML begins with a(n) _____2_____ tag and ends with a _____3_____ tag. HTML _____4_____ form the building " \
	+ "blocks of all websites. These _____4_____ are _____5_____ in shape.\n"

	medium_text = "\n\nBash is an acronym for _____1_____. Bash is a Unix shell and command language written by " \
	+ "_____2_____. Released in 1989, it has been distributed widely as the shell for the GNU operating " \
	+ "system on _____3_____ and OS X.  _____4_____ are command interpreters. They are applications that provide " \
	+ "users with the ability to give commands to their operating system interactively, or to execute batches of " \
	+ "commands quickly. _____5_____ are basically lists of commands stored in a file.\n"

	hard_text = "\n\nPython is a widely used general-purpose, _____1_____-level programming language. Its " \
	+ "design philosophy emphasizes code _____2_____, and its _____3_____ allows programmers to express " \
	+ "concepts in fewer lines of code than would be possible in languages such as C++ or Java. The language " \
	+ "provides constructs intended to enable clear programs on both a small and large scale. Python supports " \
	+ "multiple _____4_____, including _____5_____-oriented, imperative and functional programming or " \
	+ "procedural styles.\n"

	easy_text_answers = ["hypertext markup language", "<html>", "</html>", "elements", "rectangular"]

	medium_text_answers = ["bourne again shell", "brian fox", "linux", "shells", "scripts"]

	hard_text_answers = ["high", "readability", "syntax", "programming paradigms", "object"]

	# .lower is used so that there are no issues with capitalization or lack there of.
	if user_difficulty_selection.lower() == "easy":
		answer_reverse_mad_libs(blank_spaces, easy_text, easy_text_answers)
	elif user_difficulty_selection.lower() == "medium":
		answer_reverse_mad_libs(blank_spaces, medium_text, medium_text_answers)
	elif user_difficulty_selection.lower() == "hard":
		answer_reverse_mad_libs(blank_spaces, hard_text, hard_text_answers)
	else:
		user_difficulty_selection = raw_input("Please type: Easy, Medium, or Hard --> ")
		reverse_mad_libs(user_difficulty_selection)

reverse_mad_libs(user_difficulty_selection)

#Sources of information:
#https://en.wikipedia.org/wiki/Python_(programming_language)
#https://en.wikipedia.org/wiki/Bash_(Unix_shell)
#http://mywiki.wooledge.org/BashGuide
#https://www.gnu.org/software/bash/


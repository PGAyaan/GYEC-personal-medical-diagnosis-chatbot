import re

def main():
    print("Welcome to the Health Diagnosis Chatbot!")
    print("Please describe your symptoms.")

    while True:
        user_input = input("> ")

        if user_input.lower() == "exit":
            print("Thank you for using the Health Diagnosis Chatbot. Goodbye!")
            break

        diagnosis = diagnose_symptoms(user_input)
        if diagnosis:
            print("Possible health problems you might have:")
            print(diagnosis)
            print("Gambia Red Cross has been notified about your issue. Please stand by.")
        else:
            print("Sorry, I couldn't determine any possible health problems. Please try again or consult a medical professional.")

def diagnose_symptoms(symptoms):
    symptoms = symptoms.lower()

    possible_problems = []

    if re.search(r'\bheadache\b', symptoms):
        possible_problems.append("Migraine")
        possible_problems.append("Tension headache")
        possible_problems.append("Cluster headache")

    if re.search(r'\bfever\b', symptoms):
        possible_problems.append("Influenza")
        possible_problems.append("Common cold")
        possible_problems.append("Urinary tract infection")

    if re.search(r'\bcough\b', symptoms):
        possible_problems.append("Bronchitis")
        possible_problems.append("Pneumonia")
        possible_problems.append("Asthma")



    if re.search(r'\bstomachache\b', symptoms):
        possible_problems.append("Gastritis")
        possible_problems.append("Food poisoning")
        possible_problems.append("Appendicitis")

    if re.search(r'\bsore throat\b', symptoms):
        possible_problems.append("Strep throat")
        possible_problems.append("Pharyngitis")
        possible_problems.append("Tonsillitis")

    return possible_problems

if __name__ == "__main__":
    main()

class DigiNurseBot:
    def __init__(self):
        self.rules = {
            "what is hypertension": "Hypertension (high blood pressure) is when the force of your blood against your artery walls is consistently too high.",
            "normal blood pressure": "Normal blood pressure is around 120/80 mmHg. Above 140/90 mmHg may indicate hypertension.",
            "causes of hypertension": "Common causes include stress, poor diet, lack of exercise, and genetics.",
            "symptoms": "Often called the 'silent killer', hypertension may have no obvious symptoms. Headaches, vision problems, and fatigue can occur in severe cases.",
            "prevention": "Exercise regularly, reduce salt intake, eat healthy, avoid smoking, and manage stress.",
            "medication": "Always follow your doctor’s advice. Common medications include ACE inhibitors, beta blockers, and diuretics.",
            "diet": "Eat foods rich in potassium (like bananas), reduce salt, and avoid processed foods.",
            "bye": "Take care of your health. Keep monitoring your BP. Goodbye!",
            "help": "Ask me about hypertension symptoms, prevention, medication, or what it means."
        }

    def respond(self, message):
        message = message.lower().strip()
        for pattern in self.rules:
            if pattern in message:
                return self.rules[pattern]
        return "Sorry, I didn’t understand that. Try asking something like 'what is hypertension' or 'diet'."

# Start interaction
if __name__ == "__main__":
    bot = DigiNurseBot()
    print("Welcome to DigiNurse! Ask me anything about hypertension (type 'bye' to exit).")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye", "exit", "quit"]:
            print("Bot:", bot.rules["bye"])
            break
        print("Bot:", bot.respond(user_input))

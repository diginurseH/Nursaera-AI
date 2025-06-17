from flask import Flask, request, render_template_string, jsonify

class DigiNurseBot:
    def __init__(self):
        self.rules = {
            "what is hypertension": "Hypertension, or high blood pressure, is when the force of blood pushing against the walls of your blood vessels stays too high for a long time. It's called the 'silent killer' because it often doesn't cause symptoms—but it can damage your heart, brain, and kidneys over time.",
            "normal blood pressure": "Normal blood pressure is below 120/80 mmHg. Elevated: 120–129/less than 80. Grade 1: 140–159/90–99. Grade 2: 160–179/100–109. Grade 3: 180+/110+.",
            "my bp is": "Please provide the full reading, like '150/95', so I can classify it.",
            "i forgot my meds": "It's important to stay consistent with your medication. Would you like help setting reminders?",
            "i feel dizzy": "Dizziness could be a symptom of abnormal BP. Please check your pressure or seek help if it continues.",
            "diet": "Focus on fruits, vegetables, whole grains. Cut back on salt and avoid processed foods.",
            "symptoms": "Hypertension often has no symptoms, but in some cases, you may feel headaches, fatigue, or vision problems.",
            "help": "You can ask about your blood pressure reading, missed meds, symptoms, diet, or what hypertension means.",
            "bye": "Goodbye! Remember to take care of your blood pressure."
        }

    def respond(self, message):
        message = message.lower().strip()
        for pattern in self.rules:
            if pattern in message:
                return self.rules[pattern]
        if "/" in message:
            try:
                systolic, diastolic = map(int, message.split("/")[:2])
                if systolic < 80 or diastolic < 50:
                    return "Your pressure is very low. Please seek immediate medical attention. 🚨"
                elif systolic < 120 and diastolic < 80:
                    return "Your BP is in the safe range. ✅"
                elif 120 <= systolic < 130 and diastolic < 80:
                    return "Keep an eye on this. It's slightly high. ⚠️"
                elif 140 <= systolic < 160 or 90 <= diastolic < 100:
                    return "This is mild hypertension. Let's monitor closely. 🟠"
                elif 160 <= systolic < 180 or 100 <= diastolic < 110:
                    return "Moderate hypertension. Action needed. 🔴"
                elif systolic >= 180 or diastolic >= 110:
                    return "This is dangerously high. If you feel confused, dizzy, or have chest pain, go to the nearest hospital now. 🚨"
                else:
                    return "BP reading noted. Stay observant and take care."
            except:
                return "I couldn't understand the BP format. Please enter like '150/95'."
        return "I'm not sure how to respond to that. Try asking 'what is hypertension'."

app = Flask(__name__)
bot = DigiNurseBot()

HTML = """
<!doctype html>
<title>DigiNurse Chatbot</title>
<h2>DigiNurse: Hypertension Assistant</h2>
<form id=\"chat-form\">
  <input name=\"message\" placeholder=\"Ask a question...\" autofocus>
  <button>Send</button>
</form>
<pre id=\"output\"></pre>
<script>
const form = document.getElementById('chat-form');
const output = document.getElementById('output');
form.onsubmit = async e => {
  e.preventDefault();
  const msg = form.message.value;
  output.textContent += \"You: \" + msg + \"\\n\";
  const res = await fetch('/ask', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message: msg})
  });
  const data = await res.json();
  output.textContent += \"Bot: \" + data.reply + \"\\n\\n\";
  form.message.value = "";
};
</script>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.json.get('message', '')
    reply = bot.respond(user_input)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)

 
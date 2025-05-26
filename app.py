from flask import Flask, request, render_template_string, jsonify

class DigiNurseBot:
    def __init__(self):
        self.rules = {
            "what is hypertension": "Hypertension is when the pressure in your blood vessels is too high.",
            "normal blood pressure": "A healthy BP is around 120/80 mmHg.",
            "causes": "Causes include stress, obesity, high salt intake, and genetics.",
            "symptoms": "Often there are no symptoms, but severe cases can cause headaches and fatigue.",
            "diet": "Eat fruits, veggies, whole grains. Reduce salt and avoid processed foods.",
            "bye": "Goodbye! Take care of your heart.",
            "help": "You can ask me about hypertension, causes, symptoms, or treatment."
        }

    def respond(self, message):
        message = message.lower().strip()
        for pattern in self.rules:
            if pattern in message:
                return self.rules[pattern]
        return "I'm not sure how to respond to that. Try asking 'what is hypertension'."

app = Flask(__name__)
bot = DigiNurseBot()

HTML = """
<!doctype html>
<title>DigiNurse Chatbot</title>
<h2>DigiNurse: Hypertension Assistant</h2>
<form id="chat-form">
  <input name="message" placeholder="Ask a question..." autofocus>
  <button>Send</button>
</form>
<pre id="output"></pre>
<script>
const form = document.getElementById('chat-form');
const output = document.getElementById('output');
form.onsubmit = async e => {
  e.preventDefault();
  const msg = form.message.value;
  output.textContent += "You: " + msg + "\\n";
  const res = await fetch('/ask', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message: msg})
  });
  const data = await res.json();
  output.textContent += "Bot: " + data.reply + "\\n\\n";
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

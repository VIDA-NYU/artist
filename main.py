from flask import Flask, request, jsonify
import openai

API_KEY = ""

app = Flask(__name__)

# Initialize the OpenAI API with your API key
openai.api_key = API_KEY

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    input_text = data.get('text')
    objects_list = data.get('objects')

    if not input_text or not objects_list:
        return jsonify({'error': 'Invalid input'}), 400

    # Combine input text and objects into a prompt for GPT-3
    prompt = f"Input text: {input_text}\nObjects: {', '.join(objects_list)}\n"

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150
        )

        # Extract the text from the response
        gpt3_output = response.choices[0].text.strip()

        return jsonify({'response': gpt3_output})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

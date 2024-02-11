from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    code = request.form.get('code')
    target_language = request.form.get('target_language')

    prompt = f"Translate the following code from {target_language} to Python:\n\n{code}\n\nTranslated code:"

    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=prompt,
            max_tokens=150
        )

        result = response.choices[0].text.strip()
        return jsonify({'result': result})

    except Exception as e:
        print("OpenAI API error:", e)
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)

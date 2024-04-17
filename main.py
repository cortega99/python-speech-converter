from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/convert-to-text', methods=['POST'])
def convert_audio_to_text():
    # Log the request details
    print('Incoming request headers:', request.headers)
    print('Incoming request form data:', request.form)
    print('Incoming request files:', request.files)
    # Check if a file was uploaded
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        # Save the file temporarily (consider using a secure method for production)
        filepath = "./temp_audio.wav"
        file.save(filepath)

        # Use Whisper to convert audio to o
        import whisper

        model = whisper.load_model("base")  # Consider specifying the model size you need
        result = model.transcribe(filepath, language="es")
        text = result["text"]

        # Cleanup the temporary file
        import os
        os.remove(filepath)

        return jsonify({"text": text})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Use a different port than your Next.js app
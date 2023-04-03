from flask import Flask, request, render_template
import qrcode
import io
import base64

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # Get the data from the form
    data = request.form['data']

    # Generate the QR code
    img = qrcode.make(data)

    # Convert the image to a base64-encoded string
    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.getvalue()).decode()

    # Pass the data to the template
    return render_template('qr.html', data=data, img_base64=img_base64)

if __name__ == '__main__':
    app.run(debug=True)

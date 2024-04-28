from flask import Blueprint, request, jsonify

routes = Blueprint("routes", __name__)

@routes.route('/upload', methods=['POST'])
def run_model():

    print("file sent", len(request.files))

    if 'file' not in request.files:
        print('no file')
        return 'no file', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    file.save('uploaded_image.jpg')

    print(request.files['file'])

    return jsonify({'result': "result"})

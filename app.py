from flask import Flask, render_template, request, jsonify, url_for
from utils import image_processing
from models.models import db, ResizeImagesCount

app = Flask(__name__)
db.init_app(app)

app.config.from_object('config.Config')

with app.app_context():
    db.create_all()


@app.route('/')
def dashboard():
    try:
        count = ResizeImagesCount.query.count()
    except Exception as e:
        count = 0
    return render_template('dashboard.html', count=count)


@app.route('/resize-image', methods=['POST'])
def resize_image():
    url = image_processing(request.form, request)
    resize_images_count = ResizeImagesCount()
    if url not in ['', None]:
        resize_images_count.count = 1
        resize_images_count.url = url
        db.session.add(resize_images_count)
        db.session.commit()
        url = url_for('static', filename=url)
    count = ResizeImagesCount.query.count()
    return jsonify(url=url, count=count)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

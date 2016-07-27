from flask import Flask, render_template, redirect, url_for, request
import os
import cv2
import base64
import tempfile
from modules.faceswap import swap_faces,NoFaces, TooManyFaces

# create the application object
app = Flask(__name__)
app.config.from_object('config')


def _img_as_b64(path):
    return base64.encodestring(open(path, 'rb').read())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file1, file2 = request.files['file1'], request.files['file2']

        # temp files
        tmpdir = tempfile.mkdtemp()
        path1 = os.path.join(tmpdir, file1.filename)
        path2 = os.path.join(tmpdir, file2.filename)
        sol1_path = os.path.join(tmpdir, 'sol1.jpg')
        sol2_path = os.path.join(tmpdir, 'sol2.jpg')

        file1.save(path1)
        file2.save(path2)

        # generate sol
        im1, im2 = map(cv2.imread, [path1, path2])
        try:
            solution12 = swap_faces(im1, im2)
            solution21 = swap_faces(im2, im1)
        except (NoFaces, TooManyFaces) as ex:
            return "%s in passed images" % str(type(ex).__name__)

        # store solutions
        cv2.imwrite(sol1_path, solution12)
        cv2.imwrite(sol2_path, solution21)

        # load as b64
        im1, im2, sol1, sol2 = map(_img_as_b64, [path1, path2, sol1_path, sol2_path])
        return render_template('solution.html', img1=im1, img2=im2,
                               sol12=sol1, sol21=sol2)
    else:
        return render_template('index.html')

# Main
if __name__ == '__main__':
    app.run()


# FaceSwap

Simple flask web app to automatically replace facial features on an image of a face, with the facial features from a second image of a face using `Python`, `dlib` and `OpenCV`.
Can be run as a simple script from command line or as web app.

## Instructions
#### CLI demo
    ./cli_faceswap.py <head_image> <face_image> [<output_path>]
    ./cli_faceswap.py --help
#### FLASK
    ./app.py
#####
See `config.py` for host and port settings.
______
### Steps
The process breaks down into four steps:
* Detecting facial landmarks.
* Rotating, scaling, and translating the second image to fit over the first.
* Adjusting the colour balance in the second image to match that of the first.
* Blending features from the second image on top of the first.

Facial landmarks obtained using trained model [from sourceforge](http://sourceforge.net/projects/dclib/files/dlib/v18.10/shape_predictor_68_face_landmarks.dat.bz2).


_________
## Original README.md
_________
This is the code behind the [Switching Eds blog post](http://matthewearl.github.io/2015/07/28/switching-eds-with-python/).

See the link for an explanation of the code.

To run the script you'll need to install dlib (http://dlib.net) including its
Python bindings, and OpenCV. You'll also need to obtain the trained model [from sourceforge](http://sourceforge.net/projects/dclib/files/dlib/v18.10/shape_predictor_68_face_landmarks.dat.bz2).

Unzip with `bunzip2` and change `PREDICTOR_PATH` to refer to this file. The
script is run like so:

    ./faceswap.py <head image> <face image>

If successful, a file `output.jpg` will be produced with the facial features
from `<head image>` replaced with the facial features from `<face image>`.



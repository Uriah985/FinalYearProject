import flask
import os
from objectdetection_finalversion import run_detector_withDefinedModel
dp1 = "result.html"
img_path = "/home/ugo/Downloads/20240107_143216.jpg" ##input image directory u want to detect 

app = flask.Flask(__name__)
@app.route('/')
@app.route('/show_result')
def show_result():
    try:
        # Run object detection and get the image path and results
        image_path, results = run_detector_withDefinedModel(img_path)
        web_image_path = f"/static/detections/{os.path.basename(image_path)}"
        print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
        print("Debug: Image path -", image_path)
        print("Debug: Web image path -", web_image_path)
        print("Debug: Results -", results)
        return flask.render_template('result.html', image_path=web_image_path, results=results)
    except Exception as e:
        # Handle exceptions and render an error template if needed
        return flask.render_template('error.html', error=str(e))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

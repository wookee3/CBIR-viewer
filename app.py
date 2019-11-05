import os, json
from flask import Flask, render_template, send_from_directory, url_for
from config import Config

app = Flask(__name__, static_folder="/")
app.config.from_object(Config)


# load scene graph and annotation information
with open("/data2/graph/visual_genome/vg_coco_flickr_gen_caption.json", "r") as f:
    captions = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/caption/<image_id>')
def caption(image_id):
    path = os.path.join(app.config['VG_PATH'], "VG_100K", "{}.jpg".format(image_id))
    # path = os.path.join(app.config['VG_PATH'], "VG_100K")
    return render_template("image.html", src_image=path, image_id=image_id)


@app.route('/image/<image_id>')
def input_image(image_id):
    # path = "file:///data2/graph/visual_genome/VG_100K/{}.jpg".format(image_id)
    # path = os.path.join(app.config['VG_PATH'], "VG_100K", "{}.jpg".format(image_id))
    # print(image_id)
    path = os.path.join(app.config['VG_PATH'], "VG_100K")
    return send_from_directory(path, filename="{}.jpg".format(image_id), conditional=True)
    # return render_template("image.html", src_image=path, image_id=image_id)


@app.route('/graph/<image_id>')
def graph_image(image_id):
    # path = "file:///data2/graph/visual_genome/VG_100K/{}.jpg".format(image_id)
    path = os.path.join(app.config['VG_PATH'], "graphs")
    return send_from_directory(path, filename="{}.png".format(image_id))


@app.route('/resnet/<image_id>')
def resnet_image(image_id, k=100):
    # path = "file:///data2/graph/visual_genome/VG_100K/{}.jpg".format(image_id)
    path = os.path.join(app.config['RESULT_PATH'], "resnet", "images")
    return send_from_directory(path, filename="resnet_{}_top{}.png".format(image_id, k))


@app.route('/resnet/coco/<image_id>')
def resnet_coco_image(image_id, k=100):
    # path = "file:///data2/graph/visual_genome/VG_100K/{}.jpg".format(image_id)
    path = os.path.join("/data3", "graph", "results", "coco", "resnet", "images")
    print(path)
    return send_from_directory(path, filename="resnet_coco_{}_top{}.png".format(image_id, k))


@app.route('/bert/coco/<image_id>')
def bert_coco_image(image_id, k=100):
    # path = "file:///data2/graph/visual_genome/VG_100K/{}.jpg".format(image_id)
    path = "/data4/graph/bert/coco/images"
    return send_from_directory(path, filename="bert_coco_{}_top{}.png".format(image_id, k))


@app.route('/gwd/<image_id>')
def gwd_image(image_id, k=100):
    # path = "file:///data2/graph/visual_genome/VG_100K/{}.jpg".format(image_id)
    path = os.path.join(app.config['RESULT_PATH'], "gwd", "images")
    return send_from_directory(path, filename="gwd_{}_top{}.png".format(image_id, k))


@app.route('/image/caption/<image_id>')
def caption_image(image_id):
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9998)

# posenetaccuracy
testing posenet accuracy using COCO dataset

browser_data: data collected from using Posenet on the browser (Intel NUC)

browser_scripts: scripts to run posenet.js on browser - need to fix so that it uses local image files and not URLs
- data_posenet.py starts a basic python HTTPServer
- load.py creates the template index.html + runs posenet.js which runs posenet in browser (https://github.com/tensorflow/tfjs-models/tree/master/posenet)

calculation_scripts: calculate accuracy and time

download_images_coco: list of image urls (parsed by coco_gt.py to only include those with single pose and showing at least some of head/shoulders), script to download each image from these urls

coco_gt.py: script to parse coco dataset for relevant images and to save ground truth keypoints and url of these images

data_gt.json: ground truth keypoints of relevant images

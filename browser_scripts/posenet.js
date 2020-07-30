var imageElement = document.getElementById('image');
var url = imageElement.src;

posenet.load({
    architecture: 'MobileNetV1',
    outputStride: 8,
    inputResolution: 449,
    multiplier: 0.50
}).then(function (net) {
    const t0 = performance.now();
    const pose = net.estimateSinglePose(imageElement, {
        flipHorizontal: false
    });
    const t1 = performance.now();
    time = t1-t0;
    return (pose);
}).then(function (pose) {

    var data = {
        url: url,
        score: pose.scores,
        nose_x: pose.keypoints[0].position.x,
        nose_y: pose.keypoints[0].position.y,
        nose_score: pose.keypoints[0].score,
        l_eye_x: pose.keypoints[1].position.x,
        l_eye_y: pose.keypoints[1].position.y,
        l_eye_score: pose.keypoints[1].score,
        r_eye_x: pose.keypoints[2].position.x,
        r_eye_y: pose.keypoints[2].position.y,
        r_eye_score: pose.keypoints[2].score,
        l_ear_x: pose.keypoints[3].position.x,
        l_ear_y: pose.keypoints[3].position.y,
        l_ear_score: pose.keypoints[3].score,
        r_ear_x: pose.keypoints[4].position.x,
        r_ear_y: pose.keypoints[4].position.y,
        r_ear_score: pose.keypoints[4].score,
        l_shoulder_x: pose.keypoints[5].position.x,
        l_shoulder_y: pose.keypoints[5].position.y,
        l_shoulder_score: pose.keypoints[5].score,
        r_shoulder_x: pose.keypoints[6].position.x,
        r_shoulder_y: pose.keypoints[6].position.y,
        r_shoulder_score: pose.keypoints[6].score,
        time: time
    };

    fetch("/", {
      method: "POST", 
      body: JSON.stringify(data)
    }).then(res => {
      console.log("Request complete! response:", res);
    });

})
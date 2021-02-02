const tf = require('@tensorflow/tfjs-node-gpu');
const posenet = require('@tensorflow-models/posenet');


// TENSORFLOW PARAMTER
const imageScaleFactor = 0.5;
const outputStride = 16;
const flipHorizontal = false;


class PoseNet {
    constructor() {
        this.init_network();
    }

    async init_network() {
        this.network = await posenet.load();
        console.log('Posenet Initialize Successfully');
    }
    
    async predict(canvas) {
        try {
            const input = tf.browser.fromPixels(canvas);
            const pose = await this.network.estimateSinglePose(input, imageScaleFactor, flipHorizontal, outputStride);
            input.dispose();
            return pose;
        } catch (e) {
            console.log(e);
        }
    }
    
}


module.exports = PoseNet
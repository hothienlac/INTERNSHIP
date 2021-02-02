const { createCanvas, Image } = require('canvas');
const grpc = require('grpc');
const protoLoader = require('@grpc/proto-loader');

const path = require('path');
const PROTO_PATH = path.join(__dirname, './picture.proto');
const SERVER_ADDRESS = 'localhost:5001';

process.env.TF_CPP_MIN_LOG_LEVEL = 2


const proto = grpc.loadPackageDefinition(
    protoLoader.loadSync(PROTO_PATH, {
        keepCase: true,
        longs: String,
        enums: String,
        defaults: true,
        oneofs: true
    })
);


const PoseNet = require('./posenet');
const posenet = new PoseNet();

const loadImage = (image) => {
    const img = new Image();
    img.src = image;
    const canvas = createCanvas(img.width, img.height);
    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);

    return canvas;
}

const getPose = (call, callback) => {
    const picture = call.request.picture;
    const canvas = loadImage(picture);
    posenet.predict(canvas)
            .then((pose) => callback(null, {pose: JSON.stringify(pose)}))
            .catch((err) => console.log(err));
}



const server = new grpc.Server();

server.addService(proto.picture.GetPose.service, { getPose });
server.bind(SERVER_ADDRESS, grpc.ServerCredentials.createInsecure());
server.start();

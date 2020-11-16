const grpc = require("grpc");
const PROTO_PATH = "../cztrie.proto";
const CztrieService = grpc.load(PROTO_PATH).CztrieService;
let provider = "0.0.0.0:50051";
const client = new CztrieService(provider, grpc.credentials.createInsecure());

module.exports = client;

const registry = require("./registryOnChain/registryOnChain");

const connect = require("connect");
const query = require("qs-middleware");
const fs = require("fs");
const { makeExecutableSchema } = require("graphql-tools");
const express = require("express");
const { ApolloServer, gql } = require("apollo-server-express");

const graphql = require("express-graphql");
const sofa = require("sofa-api").default;

const typeDefs = fs.readFileSync("./schema.gql", "utf8");
const resolvers = require("./resolver");

const schema = makeExecutableSchema({ typeDefs, resolvers });

const server = new ApolloServer({ typeDefs, resolvers });

const app = express();
const path = "/graphql";

server.applyMiddleware({ app, path });
app.use("/graphiql", graphql({ schema, graphiql: true }));
app.use("/api", sofa({ schema }));

app.get("/api/getContractAddress", (req, res) => {
    registry.getContractAddress().then((val) => {
        res.json({ address: val });
    });
});

app.get("/api/getServices", (req, res) => {
    registry.getServices().then((val) => {
        res.json({ services: val });
    });
});

app.get("/api/getService/:serviceId", function (req, res) {
    const serviceId = parseInt(req.params["serviceId"]);
    registry
        .getService(serviceId)
        .then((val) => {
            res.json({ serviceId: serviceId, service: val });
        })
        .catch((error) => {
            console.log(error);
        });
});

app.get("/api/getBootstraps/:serviceId", function (req, res) {
    const serviceId = parseInt(req.params["serviceId"]);
    registry
        .getBootstraps(serviceId)
        .then((val) => {
            res.json({ serviceId: serviceId, service: val });
        })
        .catch((error) => {
            console.log(error);
        });
});

app.listen({ port: 4000 }, () => {
    console.log(`🚀 Apollo GraphQL Server ready at http://localhost:4000${server.graphqlPath}`);
    console.log(`🚀 REST API Server ready at http://localhost:4000/api/ 
                    (e.g. http://localhost:4000/api/dapps/
                          http://localhost:4000/api/getContractAddress/)`);
    console.log(`🚀 GraphiQL Server ready at http://localhost:4000/graphiql/ `);
});

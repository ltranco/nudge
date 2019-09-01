const crossFetch = require('cross-fetch/polyfill');
const ab = require('apollo-boost');
const ac = require('apollo-client');
const ApolloClient = ac.default;
const exec = require('child_process').exec;
const dotenv = require('dotenv');
dotenv.config();


class TopicFetcher {
    constructor(url) {
        this._urlString = url;
        this.url = new ab.HttpLink({
            uri: url
        });
    }

    fetchToken() {
        const client = new ApolloClient({
            link: this.url,
            cache: new ab.InMemoryCache()
        });
        return client.mutate({
            mutation: ab.gql`
                mutation {
                    tokenAuth(username: "${process.env.USERNAME}", password: "${process.env.PASSWORD}") {
                        token
                    }
                }
            `
        });
    }

    fetchTopics() {
        this.fetchToken().then((result) => {
            this.token = result['data']['tokenAuth']['token'];
        }).then(_ => {
            const client = new ApolloClient({
                link: this.getAuthedLink(this.token),
                cache: new ab.InMemoryCache()
            });
            client.query({
                query: ab.gql`
                    query {
                        topics {
                            id
                            name
                            url
                        }
                    }
                `
            }).then(v => {
                const topic = this.randomlyPickTopic(v['data']['topics']);
                if(topic) {
                    this.sendiMessage(this.constructPayload(topic));
                }
            });
        });
    }

    constructPayload(topic) {
        return `"Today's learning:\n${topic['name']}\n\n${topic['url']}"`;
    }

    randomlyPickTopic(topics) {
        if(!topics && !topics.isPrototypeOf(Array)) {
            return null;
        }
        return topics[Math.floor(Math.random() * topics.length)];
    }

    sendiMessage(payload) {
        const handler = (error, stdOut, stdErr) => {
        };
        exec(`osascript ./run.applescript ${process.env.DESTINATION_NUMBER} ${payload}`, handler);
    }

    getAuthedLink(token) {
        return new ab.HttpLink({
            uri: this._urlString,
            headers: {
                authorization: `JWT ${token}`
            }
        });
    }
}

const fetcher = new TopicFetcher(`${process.env.URL}`);
fetcher.fetchTopics();


This is a test project to try out docker an kubenetes

There will be producer's that are wrapped in a docker container that generates random messages.

There will be a queue that the producer deploys messages to.

There will be consumer's that are wrapped in a docker container that consume the messages, and write to an elastic search
database.
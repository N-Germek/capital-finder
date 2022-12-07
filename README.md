# Serverless

## Problem Domain

Use requests library to interact with REST Countries API.

Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:

1. The serverless function should handle a GET http request with a given country name that responds with a string with the form "The capital of X is Y".
E.g./capital-finder?country=Chile should generate an http response of The capital of Chile is Santiago.

2. The serverless function should handle a GET http request with a given capital that responds with a string with the form "The capital of X is Y".
E.g./capital-finder?capital=Santiago should generate an http response of Santiago is the capital of Chile.

Stretch Goals:

1. Extend lab to take in country and capital at same time, then generate response informing user if the values supplied were a correct county/capital match.

2. Handle the few countries with multiple capitals.

3. Add currency, national languages, etc.

## API

[Capital Finder App](https://capital-finder-natalija-germek-clarke-9wg1mv8ib-n-germek.vercel.app)
[Date Example Working Site](https://serverless-4c6c4tycw-n-germek.vercel.app/api/date)
[Hello World Working Site](https://serverless-4c6c4tycw-n-germek.vercel.app/api/hello_world)
[Countries and Capitals](/api/countries.py)

### Approach and efficiency
Version 1.0 - Nov 24, 2022 Created Serverless project and established connection with Vercel. Installed dependencies and
tested with Hello World and date.py. Started countries.py to identify country and capital.

Version 2.0 - December 7, 2022 renamed project to capital-finder, refactored countries.py, updated README.md file and
link to vercel. 



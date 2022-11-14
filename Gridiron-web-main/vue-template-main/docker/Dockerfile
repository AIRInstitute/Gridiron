ARG NODE_VERSION=14-alpine3.10
FROM node:${NODE_VERSION}

RUN npm install -g http-server

RUN mkdir /app

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 2727

CMD [ "http-server", "dist" ]

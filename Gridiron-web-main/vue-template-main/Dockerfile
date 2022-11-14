
# https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html

# build stage
ARG NODE_VERSION=14-alpine3.10
FROM node:${NODE_VERSION} as build-stage

RUN mkdir /app

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# production stage
FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
EXPOSE 2727
CMD ["nginx", "-g", "daemon off;"]
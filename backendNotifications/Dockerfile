ARG NODE_VERSION=14-alpine3.10
FROM node:${NODE_VERSION}

ARG PORT

COPY . /app

WORKDIR /app

# Install PM2
RUN npm install pm2 -g

# Install dependencies
RUN npm install

# Show the content of the workdir
# RUN ls -la -R


CMD ["pm2-runtime", "src/index.js"]

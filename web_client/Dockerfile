FROM node:latest

EXPOSE 5173

WORKDIR /app

COPY ./package.json ./
COPY ./package-lock.json ./

RUN npm install

COPY . ./

RUN npm run build

CMD ["npm", "run", "dev"]
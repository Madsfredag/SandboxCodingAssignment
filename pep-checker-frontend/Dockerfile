# pep-checker-frontend/Dockerfile
FROM node:20-alpine

WORKDIR /app

COPY . .

RUN npm install && npm run build

EXPOSE 3000

CMD ["npx", "serve", "-s", "build"]

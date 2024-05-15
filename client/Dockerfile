#Build phase
FROM node:16-alpine AS builer

WORKDIR /usr/app

COPY package.json .
RUN npm install

COPY . .
RUN npm run build

#Run phase
FROM nginx

EXPOSE 3000

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
COPY --from=builer /usr/app/build /usr/share/nginx/html
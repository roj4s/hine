FROM node:16-alpine as dev

WORKDIR /frontend

COPY ./ ./

RUN npm install

EXPOSE 3000

CMD ["npm", "start"]

FROM node:16-alpine as builder

WORKDIR /frontend

COPY --from=dev /frontend ./

RUN npm run build

FROM nginx:1.19.0 as prod

WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=builder /frontend/build/ ./

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]

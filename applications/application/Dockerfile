FROM node:20-alpine3.19 As builder
WORKDIR /app
COPY . .
RUN corepack yarn install --immutable
RUN corepack yarn build

#FROM node:20-slim
FROM node:20-alpine3.19
ENV NODE_ENV production
ENV BEE_FRAMEWORK_LOG_PRETTY true
ENV BEE_FRAMEWORK_LOG_LEVEL info
ENV BEE_FRAMEWORK_LOG_SINGLE_LINE false
ENV WATSONX_MODEL meta-llama/llama-3-1-70b-instruct
ENV WATSONX_BASE_URL https://eu-de.ml.cloud.ibm.com
USER node
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/prompts ./prompts
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/package.json package.json
COPY --from=builder /app/public ./public
EXPOSE 8080
CMD [ "node", "dist/index.js" ]
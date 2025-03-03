import "@opentelemetry/instrumentation/hook.mjs";
import { NodeSDK } from "@opentelemetry/sdk-node";
import { OTLPTraceExporter } from "@opentelemetry/exporter-trace-otlp-http";
import { Resource } from "@opentelemetry/resources";
import { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } from "@opentelemetry/semantic-conventions";
import { Version } from "bee-agent-framework/version";
import { SimpleSpanProcessor } from "@opentelemetry/sdk-trace-base";

const exporter = new OTLPTraceExporter({
  url: "http://localhost:4318/v1/traces",
});
const spanProcessor = new SimpleSpanProcessor(exporter)

const sdk = new NodeSDK({
  resource: new Resource({
    [ATTR_SERVICE_NAME]: "Bee-Agent-Framework",
    [ATTR_SERVICE_VERSION]: Version,
  }),
  spanProcessor,
});

sdk.start();

process.on("beforeExit", async () => {
  await sdk.shutdown();
});
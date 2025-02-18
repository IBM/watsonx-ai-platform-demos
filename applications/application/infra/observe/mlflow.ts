import { createObserveConnector } from 'bee-observe-connector';
import { RunContext } from 'bee-agent-framework/context';
import { BeeCallbacks, BeeRunInput, BeeRunOptions } from 'bee-agent-framework/agents/bee/types';

export function createTraceConnector() {
  return createObserveConnector({
    api: { 
      baseUrl: process.env.MLFLOW_TRACKING_URL || 'http://127.0.0.1:4002', 
      apiAuthKey: process.env.MLFLOW_API_KEY || 'testing-api-key' 
    },
    cb: async (err, data) => {
      if (err) console.error('MLflow tracking error:', err);
      else console.log('MLflow trace logged:', data);
    }
  }) as (context: RunContext<BeeCallbacks, [BeeRunInput, BeeRunOptions?]>) => void;;
}
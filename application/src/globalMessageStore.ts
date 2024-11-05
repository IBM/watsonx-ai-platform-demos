export interface Message {
  author: string;
  text: string;
  subMessages?: Message[];
}

export const messageStore: Message[] = [];

let messageQueue = Promise.resolve();

function appendMessage(author: string, text: string) {
  messageQueue = messageQueue.then(() => {
      return new Promise<void>((resolve) => {
          messageStore.push({ author, text });
          resolve();
      });
  }).catch((error) => {
      console.error(`Failed to append message from ${author}: ${error}`);
  });
}

const overrideConsoleMethod = (methodName: keyof Console) => {
  const originalMethod = (console[methodName] as (...args: any[]) => void).bind(console);
  
  (console as any)[methodName] = function (...args: any[]) {
      const messageText = args.join(' ');
      const author = `console.${methodName}`;
      
      appendMessage(author, messageText);
      
      originalMethod(...args);
  };
};

['log', 'info', 'warn', 'error', 'debug'].forEach(method => {
  overrideConsoleMethod(method as keyof Console);
});

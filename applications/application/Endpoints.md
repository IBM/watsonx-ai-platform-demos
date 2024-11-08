# Endpoints

* [Summary](#summary)
* [Router](#router)
* [Mail](#mail)
* [All](#all)

For Code Engine replace the domain:

```
From: 
http://localhost:8080/
To:
https://niklas-watson-xxx.eu-de.codeengine.appdomain.cloud/
```

API documentation: https://niklas-watson-xxx.eu-de.codeengine.appdomain.cloud/docs/

The custom transcript model can be run locally via Ollama: [Local Custom Model](#ollama-summary)

## Summary

```
curl -X 'POST' \
  'http://localhost:8080/summary' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "transcript": "John (Teltop Customer Care Agent): Hello, this is John from Teltop customer care. How can I assist you today?\n\nMary (Disappointed Subscriber): Hi John, it'\''s Mary again. I'\''ve been having a nightmare with your service. My home Wi-Fi is acting up, and the TV service over fiber is terrible.\n\nJohn: I'\''m sorry to hear about the troubles you'\''re facing at home, Mary. Let'\''s address these issues. Can you please provide me with your account number or the phone number associated with your account?\n\nMary: Sure, it'\''s 123-555-1234.\n\nJohn: Thank you. Can you provide me with more details about the Wi-Fi problems and the TV service quality?\n\nMary: The Wi-Fi keeps dropping, and the TV service over fiber is pixelated and glitchy. It'\''s making it impossible to enjoy any show or movie.\n\nJohn: I understand how frustrating that can be, Mary. Let me check our system to see if there are any reported issues in your area.\n\nJohn checks the system and finds no reported issues in Mary'\''s area.\n\nJohn: Mary, it seems there are no reported issues in your area. It could be a specific problem with your equipment or connection. Can you check if all cables are properly connected and if there are any obstructions to the router?\n\nMary: I'\''ve checked, and everything seems fine. This is so frustrating!\n\nJohn: I'\''m sorry to hear that, Mary. It might be best to perform a remote diagnostic check on your router. I can guide you through the process.\n\nJohn guides Mary through the diagnostic check, and it reveals some issues with the router.\n\nJohn: Mary, it appears there are some issues with your router. We need to update the router software. Additionally, I'\''ll address the TV service quality. There might be a signal issue or equipment malfunction.\n\nMary: Finally some answers! When will the router be updated, and how soon can you fix the TV service?\n\nJohn: We'\''ll start the router update immediately. As for the TV service, our team will work on it directly, and you should see improvements within the next 24 hours.\n\nMary: Well, it'\''s about time! I hope this gets sorted out.\n\nJohn: I appreciate your patience, Mary. To make up for the inconvenience, I'\''d like to offer you three months of free TV service once everything is resolved. Does that sound fair?\n\nMary: That'\''s more like it, John. I appreciate the offer. Let'\''s hope the technician and your team can fix these issues once and for all.\n\nJohn: Thank you for understanding, Mary. We'\''re committed to providing you with a seamless experience. If you have any other concerns or questions, feel free to reach out.\n\nMary: Thanks, John. I'\''ll take the offer for the free TV service, and let'\''s hope things get better soon.\n\nJohn: Absolutely, Mary. We appreciate your loyalty, and we'\''re here to make things right. If there'\''s anything else, don'\''t hesitate to contact us. Have a great day!"
}'
```

Output:

```
{
  "summary": "..."
}
```

## Router

Note the encoding issue:

```
From:
**Subscriber's Phone Number:** 123-555-1234
To:
**Subscriber Phone Number:** 123-555-1234
```

```
curl -X 'POST' \
  'http://localhost:8080/router' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "summary": "\n\n**Summary:**\n\n* **Agent:** John (Teltop Customer Care Agent)\n* **Subscriber:** Mary (123-555-1234)\n* **Specific Issues:** Home Wi-Fi keeps dropping, and TV service over fiber is pixelated and glitchy.\n* **Corrective Actions:** Remote diagnostic check on the router, router software update, and addressing the TV service quality by the technical team.\n* **Issue Resolved:** Not yet, but expected to be resolved within 24 hours.\n* **Follow-up Actions and Timelines:** The technical team will work on the TV service quality, and the router update will be completed immediately. The subscriber will be offered three months of free TV service once everything is resolved.\n**Subscriber Phone Number:** 123-555-1234"
}'
```

Output:

```
{
  "text": "..."
}
```

## Mail

```
curl -X 'POST' \
  'http://localhost:8080/mail' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "The router update was successful.",
  "summary": "\n\n**Summary:**\n\n* **Agent:** John (Teltop Customer Care Agent)\n* **Subscriber:** Mary (123-555-1234)\n* **Specific Issues:** Home Wi-Fi keeps dropping, and TV service over fiber is pixelated and glitchy.\n* **Corrective Actions:** Remote diagnostic check on the router, router software update, and addressing the TV service quality by the technical team.\n* **Issue Resolved:** Not yet, but expected to be resolved within 24 hours.\n* **Follow-up Actions and Timelines:** The technical team will work on the TV service quality, and the router update will be completed immediately. The subscriber will be offered three months of free TV service once everything is resolved.\n**Subscriber Phone Number:** 123-555-1234"
}'
```

Output:

```
{
  "text": "..."
}
```

## All

```
curl -X 'POST' \
  'http://localhost:8080/all' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "transcript": "John (Teltop Customer Care Agent): Hello, this is John from Teltop customer care. How can I assist you today?\n\nMary (Disappointed Subscriber): Hi John, it'\''s Mary again. I'\''ve been having a nightmare with your service. My home Wi-Fi is acting up, and the TV service over fiber is terrible.\n\nJohn: I'\''m sorry to hear about the troubles you'\''re facing at home, Mary. Let'\''s address these issues. Can you please provide me with your account number or the phone number associated with your account?\n\nMary: Sure, it'\''s 123-555-1234.\n\nJohn: Thank you. Can you provide me with more details about the Wi-Fi problems and the TV service quality?\n\nMary: The Wi-Fi keeps dropping, and the TV service over fiber is pixelated and glitchy. It'\''s making it impossible to enjoy any show or movie.\n\nJohn: I understand how frustrating that can be, Mary. Let me check our system to see if there are any reported issues in your area.\n\nJohn checks the system and finds no reported issues in Mary'\''s area.\n\nJohn: Mary, it seems there are no reported issues in your area. It could be a specific problem with your equipment or connection. Can you check if all cables are properly connected and if there are any obstructions to the router?\n\nMary: I'\''ve checked, and everything seems fine. This is so frustrating!\n\nJohn: I'\''m sorry to hear that, Mary. It might be best to perform a remote diagnostic check on your router. I can guide you through the process.\n\nJohn guides Mary through the diagnostic check, and it reveals some issues with the router.\n\nJohn: Mary, it appears there are some issues with your router. We need to update the router software. Additionally, I'\''ll address the TV service quality. There might be a signal issue or equipment malfunction.\n\nMary: Finally some answers! When will the router be updated, and how soon can you fix the TV service?\n\nJohn: We'\''ll start the router update immediately. As for the TV service, our team will work on it directly, and you should see improvements within the next 24 hours.\n\nMary: Well, it'\''s about time! I hope this gets sorted out.\n\nJohn: I appreciate your patience, Mary. To make up for the inconvenience, I'\''d like to offer you three months of free TV service once everything is resolved. Does that sound fair?\n\nMary: That'\''s more like it, John. I appreciate the offer. Let'\''s hope the technician and your team can fix these issues once and for all.\n\nJohn: Thank you for understanding, Mary. We'\''re committed to providing you with a seamless experience. If you have any other concerns or questions, feel free to reach out.\n\nMary: Thanks, John. I'\''ll take the offer for the free TV service, and let'\''s hope things get better soon.\n\nJohn: Absolutely, Mary. We appreciate your loyalty, and we'\''re here to make things right. If there'\''s anything else, don'\''t hesitate to contact us. Have a great day!"
}'
```

Output:

```
{
  "text": "..."
}
```

## Ollama Summary

```
curl -X 'POST' \
  'http://localhost:11434/v1/completions' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "model": "transcript-summary:latest",
  "max_tokens": 400,
  "temperature": 0,
  "prompt": "<|system|>\nI am, Red Hat\u00ae Instruct Model based on Granite 7B, an AI language model developed by Red Hat and IBM Research, based on the Granite-7b-base language model. My primary function is to be a chat assistant.\n<|user|>\nSummarize the transcript of the call. Identify the agent and the subscriber. Add any specific issues mentioned by the subscriber. Add any corrective actions taken as directed by the agent. Please mention if the issue is resolved. Mention any follow-up actions and timelines. If the a diagnostic check had to be done, the router has to be updated. List the phone number of the subscriber at the end.\n\nTranscript:\n\nJohn (Teltop Customer Care Agent): Hello, this is John from Teltop customer care. How can I assist you today?\n\nMary (Disappointed Subscriber): Hi John, it is Mary again. I have been having a nightmare with your service. My home Wi-Fi is acting up, and the TV service over fiber is terrible.\n\nJohn: I am sorry to hear about the troubles you are facing at home, Mary. Let us address these issues. Can you please provide me with your account number or the phone number associated with your account?\n\nMary: Sure, it is 123-555-1234.\n\nJohn: Thank you. Can you provide me with more details about the Wi-Fi problems and the TV service quality?\n\nMary: The Wi-Fi keeps dropping, and the TV service over fiber is pixelated and glitchy. It is making it impossible to enjoy any show or movie.\n\nJohn: I understand how frustrating that can be, Mary. Let me check our system to see if there are any reported issues in your area.\n\nJohn checks the system and finds no reported issues in Mary area.\n\nJohn: Mary, it seems there are no reported issues in your area. It could be a specific problem with your equipment or connection. Can you check if all cables are properly connected and if there are any obstructions to the router?\n\nMary: I have checked, and everything seems fine. This is so frustrating!\n\nJohn: I am sorry to hear that, Mary. It might be best to perform a remote diagnostic check on your router. I can guide you through the process.\n\nJohn guides Mary through the diagnostic check, and it reveals some issues with the router.\n\nJohn: Mary, it appears there are some issues with your router. We need to update the router software. Additionally, I will address the TV service quality. There might be a signal issue or equipment malfunction.\n\nMary: Finally some answers! When will the router be updated, and how soon can you fix the TV service?\n\nJohn: We will start the router update immediately. As for the TV service, our team will work on it directly, and you should see improvements within the next 24 hours.\n\nMary: Well, it is about time! I hope this gets sorted out.\n\nJohn: I appreciate your patience, Mary. To make up for the inconvenience, I would like to offer you three months of free TV service once everything is resolved. Does that sound fair?\n\nMary: That is more like it, John. I appreciate the offer. Let us hope the technician and your team can fix these issues once and for all.\n\nJohn: Thank you for understanding, Mary. We are committed to providing you with a seamless experience. If you have any other concerns or questions, feel free to reach out.\n\nMary: Thanks, John. I will take the offer for the free TV service, and let us hope things get better soon.\n\nJohn: Absolutely, Mary. We appreciate your loyalty, and we are here to make things right. If there is anything else, do not hesitate to contact us. Have a great day!\n\nInstruction: Please create the summary now as defined above. Do not forget to include the phone number.",
  "stop": [
    "###"
  ]
}'
```
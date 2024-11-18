/**
 * Copyright 2024 IBM Corp.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import express from 'express';
import EndpointRAGController from './endpointRAG.js';

const router = express.Router();

router.get('/', async (_req, res) => {
    return res.send("Server is up and running!\nUse [URL]/docs to access the swagger UI.");
});

router.post('/db2_agent_help', async (_req, res) => {
    const controller = new EndpointRAGController();
    console.log(_req.body)
    console.log(_req.headers)
    
    const response = await controller.postResponse(_req.body);
    return res.send(response);
  
});

export default router;

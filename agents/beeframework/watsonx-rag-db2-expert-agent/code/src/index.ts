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

import express, { Application } from 'express';
import router from './routes.js';
import swaggerUi from 'swagger-ui-express';

const PORT = 8080;
const app: Application = express();

// Response in JSON 
app.use(express.json());

app.use(express.static('public'));

app.use(
    "/docs",
    swaggerUi.serve,
    swaggerUi.setup(undefined, {
      swaggerOptions: {
        url: "/swagger.json",
      },
    })
  );


// Routen einbinden
app.use(router);

// Server starten
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT} and API documentation: http://localhost:${PORT}/docs`);
});
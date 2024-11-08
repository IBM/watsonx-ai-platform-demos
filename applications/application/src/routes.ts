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

import express from "express";
import EndpointAllController from "./endpointAll.js";
import EndpointSummaryController from "./endpointSummary.js";
import EndpointRouterController from "./endpointRouter.js";
import EndpointMailController from "./endpointWrite.js";

const router = express.Router();

router.post("/all", async (_req, res) => {
  const controller = new EndpointAllController();
  const response = await controller.run(_req.body);
  return res.send(response);
});

router.post("/summary", async (_req, res) => {
  const controller = new EndpointSummaryController();
  const response = await controller.run(_req.body);
  return res.send(response);
});

router.post("/router", async (_req, res) => {
  const controller = new EndpointRouterController();
  const response = await controller.run(_req.body);
  return res.send(response);
});

router.post("/mail", async (_req, res) => {
  const controller = new EndpointMailController();
  const response = await controller.run(_req.body);
  return res.send(response);
});

export default router;
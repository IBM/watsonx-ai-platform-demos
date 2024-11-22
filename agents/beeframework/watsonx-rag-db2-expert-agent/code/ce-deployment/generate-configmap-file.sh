# Copyright 2024 IBM Corp.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

#!/bin/bash
cat <<EOF
WATSONX_BASE_URL=${WATSONX_BASE_URL:-''}
WATSONX_PROJECT_ID=${WATSONX_PROJECT_ID:-''}
WATSONX_API_KEY=${WATSONX_API_KEY:-''}
WATSONX_REGION=${WATSONX_REGION:-''}
WATSONX_MODEL=${WATSONX_MODEL:-''}
WATSONX_DEPLOYMENT_ID=${WATSONX_DEPLOYMENT_ID:-''}
CODE_INTERPRETER_URL=${CODE_INTERPRETER_URL:-''}
BEE_FRAMEWORK_LOG_PRETTY=${BEE_FRAMEWORK_LOG_PRETTY:-''}
BEE_FRAMEWORK_LOG_LEVEL=${BEE_FRAMEWORK_LOG_LEVEL:-''}
BEE_FRAMEWORK_LOG_SINGLE_LINE=${BEE_FRAMEWORK_LOG_LEVEL:-''}
EOF
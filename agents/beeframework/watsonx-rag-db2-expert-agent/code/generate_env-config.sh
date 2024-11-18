#
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
########################################
# Create a file based on the environment variables
# given by the dockerc run -e parameter
########################################
cat <<EOF
## WatsonX
export WATSONX_BASE_URL=${WATSONX_BASE_URL}
export WATSONX_PROJECT_ID=${WATSONX_PROJECT_ID}
# Max cloud account
export WATSONX_API_KEY=${WATSONX_API_KEY}
export WATSONX_API_KEY_MAX=${WATSONX_API_KEY_MAX}
export WATSONX_MODEL=${WATSONX_MODEL}
export WATSONX_DEPLOYMENT_ID=${WATSONX_DEPLOYMENT_ID}
# Tools
export CODE_INTERPRETER_URL=${CODE_INTERPRETER_URL}
# Framework related
export BEE_FRAMEWORK_LOG_PRETTY=${BEE_FRAMEWORK_LOG_PRETTY}
export BEE_FRAMEWORK_LOG_LEVEL=${BEE_FRAMEWORK_LOG_LEVEL}
export BEE_FRAMEWORK_LOG_SINGLE_LINE=${BEE_FRAMEWORK_LOG_LEVEL}
EOF
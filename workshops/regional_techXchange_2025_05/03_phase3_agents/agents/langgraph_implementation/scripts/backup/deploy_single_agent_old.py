import json
import logging
from pathlib import Path
import json

import ibm_watsonx_ai

###########################################
# Select the agent type you want to deploy
# 1. Single agent
from ai_service_single_agent import deployable_ai_service
from scripts.build_package_single_agent import build_zip_sc, get_package_name_and_version
from utils import load_config

logging.basicConfig()
logger = logging.getLogger(__name__)

# 1. Get the deployment space information
print("***Log: 1. Get the deployment space information")
config = load_config()

dep_config = config["deployment"]

client = ibm_watsonx_ai.APIClient(
    credentials=ibm_watsonx_ai.Credentials(url=dep_config["watsonx_url"], api_key=dep_config["watsonx_apikey"]),
    space_id=dep_config["space_id"])

root_dir = Path(__file__).parents[1]
pyproject_path = root_dir / "pyproject.toml"
pkg_name, pkg_version = get_package_name_and_version(str(pyproject_path))

# 2. Create package extension
print("***Log: 2. Create package extension")
pkg_ext_metadata = {
    client.package_extensions.ConfigurationMetaNames.NAME: pkg_name,
    client.package_extensions.ConfigurationMetaNames.TYPE: "pip_zip"
}

pkg_ext_sc = root_dir / "dist" / f"{pkg_name.replace('-', '_')}-{pkg_version}.zip"
print(f"***Log: - Save the source code in the `dist` directory and build a package ({pkg_ext_sc})")

if not pkg_ext_sc.exists():
    build_zip_sc(pkg_ext_sc)
    print(f"***Log: - Delete package {pkg_ext_sc} and build it new.")
else:
    logger.warning(
        f"package extension was not built as path: '{pkg_ext_sc}' is not empty. Using the already existing path for deployment. "
        "In case of any problems you might want to delete it and rerun the `deploy.py` script")

pkg_ext_asset_details = client.package_extensions.store(
    meta_props=pkg_ext_metadata,
    file_path=str(pkg_ext_sc)
)
pkg_ext_asset_id = client.package_extensions.get_id(pkg_ext_asset_details)

# 3. Load base software specification configuration to extend
dep_custom_config = config["deployment"]["custom"]
sw_runtime_spec=dep_custom_config["sw_runtime_spec"]
print(f"***Log: 3. Select base software specification to extend ({sw_runtime_spec})")
base_sw_spec_id = client.software_specifications.get_id_by_name(sw_runtime_spec)

# 4. Define new software specification based on base one and custom library
template_sw_spec_name = f"{pkg_name}-sw-spec"
print(f"***Log: 4. Define new software specification based on base one and custom library ({template_sw_spec_name})")

sw_spec_metadata = {
    client.software_specifications.ConfigurationMetaNames.NAME:
        template_sw_spec_name,
    client.software_specifications.ConfigurationMetaNames.BASE_SOFTWARE_SPECIFICATION:
        {"guid": base_sw_spec_id},
    client.software_specifications.ConfigurationMetaNames.PACKAGE_EXTENSIONS:
        [{"guid": pkg_ext_asset_id}]
}

# 5. Delete if sw_spec already exists
print("***Log: 5. Delete if sw_spec already exists")
try:
    sw_spec_id = client.software_specifications.get_id_by_name(template_sw_spec_name)
    logger.warning(f"Deleting previously created sw_spec: {template_sw_spec_name}")
    client.software_specifications.delete(sw_spec_id)
except ibm_watsonx_ai.wml_client_error.ResourceIdByNameNotFound:
    pass

# 6. Store the software spec
sw_spec_asset_details = client.software_specifications.store(meta_props=sw_spec_metadata)
print(f"***Log: 6. Store the software spec")

# 7. Get the id of the new asset
asset_id = client.software_specifications.get_id(sw_spec_asset_details)
print(f"***Log: 7. Get the id of the new asset ({asset_id})")

sw_spec_asset_details = client.software_specifications.get_details(asset_id)

print(f"***Log: 8. Define the schema for the REST API")
with (root_dir / "schema" / "request.json").open("r", encoding="utf-8") as file:
    request_schema = json.load(file)

with (root_dir / "schema" / "response.json").open("r", encoding="utf-8") as file:
    response_schema = json.load(file)

meta_props = {
    client.repository.AIServiceMetaNames.SOFTWARE_SPEC_ID: asset_id,
    client.repository.AIServiceMetaNames.NAME: "online ai_service 'older version' 0.1.4",
    client.repository.AIServiceMetaNames.REQUEST_DOCUMENTATION: request_schema,
    client.repository.AIServiceMetaNames.RESPONSE_DOCUMENTATION: response_schema
}

stored_ai_service_details = client.repository.store_ai_service(deployable_ai_service, meta_props)
ai_service_id = stored_ai_service_details["metadata"].get("id")

# Note: Easier to understand what is the content of the meta data.
#CUSTOM_META = {
#        "space_id": client.default_space_id,
#        "url": client.credentials.url,       
#        "model_id": dep_custom_config['model_id'],
#        "thread_id": dep_custom_config['thread_id']
#        "sw_runtime_spec": dep_custom_config['sw_runtime_spec']
#}

CUSTOM_META = {
        "space_id": client.default_space_id,
        "url": client.credentials.url,       
        **dep_config['custom']
}

meta_props = {
    client.deployments.ConfigurationMetaNames.NAME:
        f"online ai_service 'older version' 0.1.4 zurich",
    client.deployments.ConfigurationMetaNames.ONLINE: {},
    client.deployments.ConfigurationMetaNames.CUSTOM: CUSTOM_META,
}

deployment_details = client.deployments.create(ai_service_id, meta_props)

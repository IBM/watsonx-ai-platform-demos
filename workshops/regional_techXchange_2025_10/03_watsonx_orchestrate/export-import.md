# Export/import agents

* Export agents

```sh
#export NAME=GalaxiumTravelerAgent
#export NAME=UseImportedModel
#export NAME=RESTAPI_GalaxiumTravelerAgent
export NAME=WORKFLOW_GalaxiumTravelerAgent

export KIND="native"
export OUTPUT="./${NAME}_export.yaml"
orchestrate agents export --name ${NAME} --kind ${KIND} --output ${OUTPUT} --agent-only
```

* Import agents

```sh
#export NAME=GalaxiumTravelerAgent
#export NAME=Use_Imported_Model_Granite
#export NAME=RESTAPI_GalaxiumTravelerAgent
export NAME=WORKFLOW_GalaxiumTravelerAgent

export FILE="./${NAME}_export.yaml"
orchestrate agents import --file ${FILE} --app-id ${APP_ID}
```
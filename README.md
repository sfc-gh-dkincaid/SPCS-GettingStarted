# Snowpark Container Services - Hosted Application Connecting to Snowflake

Pre-reqs

* Docker Desktop
* Python environment with SnowCLI installed (`conda env create -f conda_env.yml`) and SnowCLI connection created (`snow connection add`)
* Run setup.sql until "STOP HERE" section

## Steps

1. Fill in Env variables in docker-compose.yaml
2. Build image - `docker compose build --no-cache`
3. Test locally - `docker compose up`
4. Tag image - `docker tag spcs-gettingstarted-streamlit_spcs [account].registry.snowflakecomputing.com/spcs_playground/public/images/streamlit_spcs`
5. Login to image repository - `snow spcs image-registry token --format=JSON -c spcs-azure | docker login [account].registry.snowflakecomputing.com/spcs_playground/public/images -u 0sessiontoken --password-stdin`
6. Push image to Snowflake image repository - `docker image push [account].registry.snowflakecomputing.com/spcs_playground/public/images/streamlit_spcs`
7. Upload spec file to Internal Stage @SPCS_PLAYGROUND.PUBLIC.SPECS
8. Create service in Snowflake

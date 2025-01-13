import logging

logging.basicConfig(level=logging.DEBUG)
from envisolation import EnvIsolatedModel

model = EnvIsolatedModel(
    model_id="test-model",
    model_path="test_model",
    pip_requirements_path="test_model/requirements.txt",
    model_arguments={"test": 3},
    env_install_dir="/tmp/env-isolation",
)
logging.info(model.execute({"input": "test"}))
model.unload()

model = EnvIsolatedModel(
    model_id="test-model",
    model_path="test_model",
    pip_requirements_path="test_model/requirements.txt",
    model_arguments={"test": 2},
    env_install_dir="/tmp/env-isolation",
)
logging.info(model.execute({"input": "test"}))
model.unload(unload_env=True)

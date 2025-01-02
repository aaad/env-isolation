import logging
logging.basicConfig(level=logging.INFO)
from envisolation import EnvIsolatedModel

model = EnvIsolatedModel(model_id="test-model", model_path="test_model", pip_requirements_path="test_model/requirements.txt")
logging.info(model.execute({"input": "test"}))
model.unload()

model = EnvIsolatedModel(model_id="test-model", model_path="test_model", pip_requirements_path="test_model/requirements.txt")
logging.info(model.execute({"input": "test"}))
model.unload(unload_env=True)
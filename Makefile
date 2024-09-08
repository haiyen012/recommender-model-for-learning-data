SHELL = /bin/bash
PYTHON := python3
VENV_NAME = venv
DATA_FOLDER = data_manager
MODEL_FOLDER = model_manager

# Environment
#venv:
#	conda create --name ${VENV_NAME} python=3.10 && \
#	conda init bash && \
#	source $$(conda info --base)/etc/profile.d/conda.sh && \
#	conda activate ${VENV_NAME} && \
#	${PYTHON} -m pip install pip setuptools wheel && \
#	${PYTHON} -m pip install -e .[dev] && \
#	pre-commit install


# Style
style:
	black ./${DATA_FOLDER}/ ./${MODEL_FOLDER}/
	flake8 ./${DATA_FOLDER}/ ./${MODEL_FOLDER}/
	${PYTHON} -m isort -rc ./${DATA_FOLDER}/ ./${MODEL_FOLDER}/


# Test
# test:
# 	${PYTHON} -m flake8 ./${DATA_FOLDER}/ ./${MODEL_FOLDER}/
# 	${PYTHON} -m mypy ./${DATA_FOLDER}/ ./${MODEL_FOLDER}/
# 	# pytest -s --durations=0 --disable-warnings ./${MODEL_FOLDER}/
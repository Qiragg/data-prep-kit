import os
import sys
from pathlib import Path

from data_processing.ray import TransformLauncher
from data_processing.utils import ParamsUtils
from transforms.code.antivirus.src.antivirus_transform import AntivirusTransformConfiguration


# create launcher
launcher = TransformLauncher(transform_runtime_config=AntivirusTransformConfiguration())
# create parameters
s3_cred = {
    "access_key": "YOUR KEY",
    "secret_key": "YOUR SECRET KEY",
    "cos_url": "https://s3.us-east.cloud-object-storage.appdomain.cloud",
}

# Configure lakehouse unit test tables
lakehouse_config = {
    "lh_environment": "STAGING",
    "input_table": "code.ieee",
    "input_dataset": "",
    "input_version": "main",
    "output_table": "code.adap_antivirus_test",
    "output_path": "lh-test/tables/code/adap_antivirus_test",
    "token": "YOUR LAKEHOUSE TOKEN",
}

worker_options = {"num_cpus": 0.8}
code_location = {"github": "github", "commit_hash": "12345", "path": "path"}
params = {
    "run_locally": True,
    "max_files": -1,
    "s3_cred": ParamsUtils.convert_to_ast(s3_cred),
    "lh_config": ParamsUtils.convert_to_ast(lakehouse_config),
    "worker_options": ParamsUtils.convert_to_ast(worker_options),
    "num_workers": 5,
    "checkpointing": False,
    "pipeline_id": "pipeline_id",
    "job_id": "job_id",
    "creation_delay": 0,
    "code_location": ParamsUtils.convert_to_ast(code_location),
    "input_column": "content",
    "output_column": "virus_detection"
}
sys.argv = ParamsUtils.dict_to_req(d=params)

# launch
launcher.launch()

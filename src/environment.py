import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Environment:
    """ Class describes .env variables. """
    aws_access_key: str = os.getenv('AWS_ACCESS_KEY')
    aws_secret_key: str = os.getenv('AWS_SECRET_KEY')
    aws_region: str = os.getenv('AWS_REGION')

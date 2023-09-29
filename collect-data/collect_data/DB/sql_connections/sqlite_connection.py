from sqlalchemy.engine import URL
from tools.yaml_reader import YAMLReader
from tools.constants import RelativePath, DB


def sqlite_url_connection():
    dyg = YAMLReader(yaml_file=RelativePath.ENV_SETTINGS)
    params = dyg.get_values(section=DB.SQLITE)
    url = URL.create(
        drivername=params["drivername"],
        database=params["database"]
        )

    return url

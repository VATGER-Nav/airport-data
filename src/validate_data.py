import sys

from settings import OUTPUT_DIRECTORY, ROOT_DIRECTORY
from tasks.toml_data import TomlData

if __name__ == "__main__":
    tomldata = TomlData(data_dir=ROOT_DIRECTORY, output_dir=OUTPUT_DIRECTORY, export=False)

    if len(tomldata.errors) != 0:
        sys.exit(1)

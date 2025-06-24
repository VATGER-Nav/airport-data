from settings import OUTPUT_DIRECTORY, ROOT_DIRECTORY
from tasks.export_stands import export_hp_csv
from tasks.read_grp_data import GrpDataReader
from tasks.toml_data import TomlData


def main():
    TomlData(data_dir=ROOT_DIRECTORY, output_dir=OUTPUT_DIRECTORY)
    airports = GrpDataReader().process_stand_files(ROOT_DIRECTORY)
    export_hp_csv(airports, OUTPUT_DIRECTORY)


if __name__ == "__main__":
    main()

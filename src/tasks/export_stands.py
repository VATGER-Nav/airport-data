import csv
from pathlib import Path
from statistics import mean


def parse_stand_name(stand_name: str):
    """The library the homepage uses does not accept spaces in the name"""
    return stand_name.replace(" ", "-")


def export_hp_csv(airports: dict, output_path: str):
    """Exports the airports dict in the format as required by the homepage"""
    output_path = Path(output_path)
    Path.mkdir(output_path, exist_ok=True, parents=True)

    for airport, stands in airports.items():
        csv_filename = output_path / f"{airport}.csv"

        with Path.open(csv_filename, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["stand", "latcoord", "longcoord"])

            for stand in stands:
                lat = mean(stand.lat) if isinstance(stand.lat, list) else stand.lat
                lon = mean(stand.lon) if isinstance(stand.lon, list) else stand.lon
                writer.writerow([parse_stand_name(stand.name), lat, lon])

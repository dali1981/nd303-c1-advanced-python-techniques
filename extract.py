"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.
    def load_to_generator():
        with open(neo_csv_path, 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                if row['neo'] == 'Y':
                    yield NearEarthObject(row['pdes'],
                                          row['name'] if row['name'] != '' else None,
                                          None if row['diameter'] == '' else float(row['diameter']),
                                          row['pha'] == 'Y'
                                          )
    return list(load_to_generator())


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    def load_to_generator():
        with open(cad_json_path, 'r') as infile:
            data = json.load(infile)['data']
            for line in data:
                yield CloseApproach(designation=line[0],
                                    time=line[3],
                                    distance=line[4],
                                    velocity=line[-4],
                                    neo=NearEarthObject(''))
    return list(load_to_generator())


if __name__ == '__main__':
    # neos = load_neos('./data/neos.csv')
    # for neo in neos:
    #     print(next(neos))
    cas = load_approaches('./data/cad.json')
    for ca in cas:
        print(ca)

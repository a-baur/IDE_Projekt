import json
from typing import Dict, List, Union
import requests
import os


def search_author_ids(author_name: str, institution_id: str = None) -> Dict[str, Union[str, List]]:
    # adding mail address allows faster access (see https://docs.openalex.org/api#the-polite-pool)
    params = {'mailto': 'janik.hasche@studium.uni-hamburg.de'}
    if institution_id:
        url = 'https://api.openalex.org/authors?filter=last_known_institution.id:{0},display_name.search:{1}&per-page=200'.format(
            institution_id, author_name)
    else:
        url = 'https://api.openalex.org/authors?filter=display_name.search:{0}&per-page=200'.format(author_name)
    print('query: ' + url)
    query = requests.get(
        url, params=params
    ).json()

    meta = query['meta']
    query_results = query['results']
    count = meta['count']

    result = {'search_name': author_name, 'institution_id': institution_id, 'results': []}
    if count == 0:
        return result

    if count >= 200:
        print('More than 200 results for: ' + author_name + '. Only get first 200')
        count = 200

    results = []
    for i in range(count):
        author_id = query_results[i]['ids']['openalex']
        display_name = query_results[i]['display_name']
        result['results'].append(
            {
                'id': author_id,
                'display_name': display_name
            }
        )

    return result


def process_employee_input_file(input_path: str):
    input_file_name = os.path.basename(input_path)
    input_file = open(input_path, 'r', encoding='utf-8')
    input_json = json.load(input_file)
    institution_name = input_json['institution_name']
    institution_id = input_json['open_alex_id']
    names = input_json['names']

    all_author_ids = []
    n_found = 0
    not_found = []
    for author_name in names:
        author_name = author_name.rstrip()
        author_ids = search_author_ids(author_name, institution_id)
        if len(author_ids['results']) > 0:
            n_found += 1
        else:
            not_found.append(author_name)
        all_author_ids.append(author_ids)

    # write output json file
    output_file_path = os.path.join('1_get_author_ids_output', input_file_name)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(all_author_ids, file, ensure_ascii=False, indent=4)

    # write report txt file
    report = 'Found ' + str(n_found) + 'out of ' + str(len(names)) + ' author ids. \n'
    report += 'No ids found for: ' + str(not_found)
    report_file_name = input_file_name.split('.')[0] + '_report.txt'
    report_file_path = os.path.join('1_get_author_ids_output', report_file_name)
    with open(report_file_path, 'w', encoding='utf-8') as file:
        file.write(report)



def main():
    # go through all json files in 'employee_input'-directory
    employee_input_file_paths = []
    for file in os.listdir('employee_input'):
        if file.endswith(".json"):
            path = os.path.join('employee_input', file)
            process_employee_input_file(path)


main()

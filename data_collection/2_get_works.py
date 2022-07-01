import json
from typing import Dict, List, Union
import requests
import os


def get_works_with_author_id(author_id: str) -> List[Dict[str, any]]:
    next_cursor = '*'
    all_results = []
    while next_cursor is not None:
        # adding mail address allows faster access (see https://docs.openalex.org/api#the-polite-pool)
        params = {'mailto': 'janik.hasche@studium.uni-hamburg.de'}
        url = 'https://api.openalex.org/works?filter=author.id:{0}&per-page=200&cursor={1}'.format(author_id, next_cursor)
        print('query: ' + url)
        try:
            query = requests.get(
                url, params=params
            ).json()
        except Exception as e:
            print(e)
            continue

        meta = query['meta']
        next_cursor = meta['next_cursor']
        results = query['results']
        all_results.extend(results)

    return all_results


def process_author_ids(input_path: str):
    input_file_name = os.path.basename(input_path)
    input_file = open(input_path, 'r', encoding='utf-8')
    input_json = json.load(input_file)

    filtered_works = []
    works_without_institution = []
    n_works = 0

    for author in input_json:
        # get all works from author
        search_results = author['results']
        institution_id = author['institution_id']
        for search_result in search_results:
            author_id = search_result['id']
            author_works = get_works_with_author_id(author_id)
            # filter only works released at the authors institution id
            for work in author_works:
                n_works += 1
                found_institution = False
                for authorship in work['authorships']:
                    if author_id == authorship['author']['id']:
                        for institution in authorship['institutions']:
                            if institution_id == institution['id']:
                                filtered_works.append(work)
                                found_institution = True
                if not found_institution:
                    works_without_institution.append(work['id'])



    # write output json file
    output_file_path = os.path.join('2_get_works_output', input_file_name)
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(filtered_works, file, ensure_ascii=False, indent=4)

    # write report txt file
    report = 'Filtered works: Take only works with institution id corresponding to authors institution id: Got' + str(len(filtered_works)) + ' out of total:' + str(n_works) + '\n'
    report += 'Works without institution: ' + str(works_without_institution)
    report_file_name = input_file_name.split('.')[0] + '_report.txt'
    report_file_path = os.path.join('2_get_works_output', report_file_name)
    with open(report_file_path, 'w', encoding='utf-8') as file:
        file.write(report)


def main():
    # go through all json files in 'employee_input'-directory
    employee_input_file_paths = []
    for file in os.listdir('1_get_author_ids_output'):
        if file.endswith(".json"):
            path = os.path.join('1_get_author_ids_output', file)
            process_author_ids(path)


main()

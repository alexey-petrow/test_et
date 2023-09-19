def _sort_by_version(item: tuple[str, dict]) -> list[int]:
    """
    Help function for using in sorted() method.
    Retrieves information about version from provided data.
    Converts string '2.12.4', to list of ints [2, 12, 4]
    Args:
        item: (tuple[str, dict]) Example: ('ERROR number 1', {'ident': '2.2.11', 'value': 'test'})
    Returns:
        (list[int]) Data in the right format for sorting by them.
    """
    version_str = item[1]['ident']
    version_list = version_str.split('.')
    version_list_with_ints = list(map(int, version_list))
    return version_list_with_ints


def version_sorting_function(json_data: dict) -> dict[str, dict]:
    """
    Sorts data by versions (key 'ident' in json_data) and
    removes extra spaces from values (key 'value' in json_data)
    Args:
        json_data: (dict) Deserialized data from a json file.
    Returns:
        (dict) Sorted by versions and cleared of extra spaces dictionary.
    """
    data: dict[str, dict] = json_data['data']
    sorted_items: list[tuple] = sorted(data.items(), key=_sort_by_version)
    sorted_dict: dict[str, dict] = {key: value for key, value in sorted_items}

    for key, value in sorted_dict.items():
        value['value'] = value['value'].strip().split()

    return sorted_dict

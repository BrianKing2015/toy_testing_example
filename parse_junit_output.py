import pathlib

import pandas as pd
import lxml


def read_xml_and_return_df(xml_path: pathlib.Path, test_run_id: str) -> pd.DataFrame:
    data = pd.read_xml(xml_path)
    try:
        data[test_run_id] = test_run_id

    except KeyError:
        print(f"No failures or no failure column in {test_run_id}")
    return data


if __name__ == '__main__':
    '''
    To generate junit output use this call from the root of the project
        pytest ./tests --junitxml=out_report.xml 
    '''
    output_df = read_xml_and_return_df(xml_path=pathlib.Path("out_report.xml"), test_run_id="1")
    print(output_df)

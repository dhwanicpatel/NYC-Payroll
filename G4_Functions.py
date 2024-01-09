import pandas as pd
import numpy as np
import requests

def fetch_data(api_url):

    """
    Fetches JSON data from a given API URL and returns it as a pandas DataFrame.

    Parameters:
    api_url (str): The URL of the API from which to fetch data.

    Returns:
    DataFrame: A pandas DataFrame containing the parsed JSON data.
    """
    response = requests.get(api_url)

    if response.status_code == 200:
            data = response.json()
            return pd.DataFrame(data)
    else:
          print(f"Failed to retrieve data. Status code: {response.status_code}")

def import_csv(file_path):
    """
    Reads a CSV file and return a pandas DataFrame.

    Parameters:
    - file_path: str. The file path to the CSV file.

    Returns:
    - A pandas DataFrame containing the data from the CSV file.
    """
    df = pd.read_csv(filepath_or_buffer=file_path, header=0, thousands=',')

    return df

def categorize_job_type(df, title_col, keywords, default_keyword='OTHER'):
    """
    Categorizes job types based on the title description with multiple categories.

    Parameters:
    df (DataFrame): DataFrame containing the job titles.
    title_col (str): Column name in df that contains the job title descriptions.
    keywords (list): List of keywords to identify different job types.
    default_keyword (str): Default job type if none of the keywords are found.

    Returns:
    DataFrame: Updated DataFrame with a new 'job_type' column.

    Example usage:
    keywords = ['MANAGER', 'INTERN', 'ENGINEER', 'ANALYST']
    df_tech = categorize_job_type(df_tech, 'title_description', keywords)
    """
    conditions = [df[title_col].str.contains(keyword, case=False, na=False) for keyword in keywords]
    choices = [keyword.upper() for keyword in keywords]
    df['job_type'] = np.select(conditions, choices, default=default_keyword.upper())
    return df['job_type']

# Example usage:
# keywords = ['MANAGER', 'INTERN', 'ENGINEER', 'ANALYST']
# df_tech = categorize_job_type(df_tech, 'title_description', keywords)

if __name__ == '__main__':
      df = fetch_data('https://data.cityofnewyork.us/resource/k397-673e.json')
      print(df.head())
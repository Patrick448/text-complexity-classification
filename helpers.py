import os
import pandas as pd
import spacy
import textdescriptives as td
from timeit import default_timer as timer


def analyze_and_create_output_csv(input_dataset_path, output_path):
    """
    Creates a dataframe with the texts in the dataset and their respective categories, analyzes the texts and adds the
    analysis information as columns, and saves the dataframe as a csv file
    :param input_dataset_path: path of the dataset directory
    :param output_path: path of the output csv file
    :return: None
    """
    start = timer()
    df = create_dataframe(input_dataset_path)
    analyzed = analyze_text_append_result(df, 'text')
    end = timer()
    analyzed.to_csv(output_path, index=False)
    print(f'Output created. Elapsed time: {end - start}')


def create_category_map(dir_path):
    folders = os.listdir(dir_path)
    category_map = {}

    for i, folder in enumerate(folders):
        category_map[folder] = i

    return category_map


def create_dataframe(dir_path):
    """
    Reads the files in the dataset directory and creates a dataframe with the texts and their respective categories
    :param dir_path: path of the directory with the category folders
    :return: pandas dataframe with the columns: category, name, text
    """

    folders = os.listdir(dir_path)
    dataset = []

    #category_map = {}

    #for i, folder in enumerate(folders):
    #    category_map[folder] = bin(i)

    #print("Category folders were mapped to binary values as follows:")
   # print(category_map)

    for folder in folders:
        files = os.listdir(f'{dir_path}/{folder}')
        for file in files:
            with open(f'{dir_path}/{folder}/{file}', 'r', encoding='utf-8-sig') as f:
                dataset.append({"category": folder, "name": file, "text": f.read()})

    df = pd.DataFrame(dataset)
    return df


def analyze_text_append_result(df, column_name):
    """
    Analyzes the text in the column column_name of each row of the dataframe and adds the analysis information as columns
    :param df: dataframe with the texts
    :param column_name: name of the column with the texts
    :return: dataframe with the added analysis columns
    """

    analysis_dict_list = []
    nlp = spacy.load('pt_core_news_sm')
    nlp.add_pipe('textdescriptives/all')

    for index, row in df.iterrows():
        doc = nlp(row[column_name])
        text_info = td.extract_df(doc).iloc[0].to_dict()
        text_info = {**text_info, **row}
        analysis_dict_list.append(text_info)  # access some of the values
        print(f'Analyzing ({index+1} / {len(df)})', end='\r')

    analysis_df = pd.DataFrame(analysis_dict_list)
    return analysis_df

#pylint: disable=all
import os
import pandas as pd

from src.extract.extract_people import extract_to_save_people_data
from src.extract.extract_planets import extract_to_save_planets_data
from src.extract.extract_films import extract_to_save_films_data

from src.transform.transform_people import transform_people_data
from src.transform.transform_planets import transform_planets_data
from src.transform.transform_films import transform_films_data

def extract_to_save_raw():
    df_people = extract_to_save_people_data()
    df_planets = extract_to_save_planets_data()
    df_films = extract_to_save_films_data()

    current_directory = os.path.dirname(os.path.realpath(__file__))
    raw_directory = os.path.join(current_directory, 'raw')
    if not os.path.exists(raw_directory):
        os.makedirs(raw_directory)

    df_people.to_csv(os.path.join(raw_directory, 'df_people.csv'))
    df_planets.to_csv(os.path.join(raw_directory, 'df_planets.csv'))
    df_films.to_csv(os.path.join(raw_directory, 'df_films.csv'))




def transform_to_save_work():
    df_people_transform = transform_people_data()
    df_planets_transform = transform_planets_data() 
    df_films_transform = transform_films_data()

    current_directory = os.path.dirname(os.path.realpath(__file__))
    work_directory = os.path.join(current_directory, 'work')
    if not os.path.exists(work_directory):
        os.makedirs(work_directory)

    df_people_transform.to_csv(os.path.join(work_directory, 'df_people_transform.csv'))
    df_planets_transform.to_csv(os.path.join(work_directory, 'df_planets_transform.csv'))
    df_films_transform.to_csv(os.path.join(work_directory, 'df_films_transform.csv'))

extract_to_save_raw()
transform_to_save_work()
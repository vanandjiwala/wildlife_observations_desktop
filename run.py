from utils.dbutils import DbUtils
from utils.pathutils import PathUtils
import constants



if __name__ == '__main__':

    project_root = PathUtils.get_project_root()
    db_path = PathUtils.append_path(project_root,constants.DB_NAME)
    db = DbUtils()
    db.db_open(db_path)
    db.create_tables()

    # GET ALL SPECIES
    all_species = db.get_species()
    print(all_species)



    # GET SPECIES COMMON NAME FOR DROPDOWN
    desired_columns = ['common_name']
    filter = {
        'columns': desired_columns
    }

    # GET COMMON NAMES FOR
    dropdown_options = db.get_common_names()
    # Make sure that user has uploaded species data
    if len(dropdown_options) == 0:
        print("User must upload species list")

    #Get scientific name based on the ID
    db.get_scientific_name(1)


    #Add Observations
    observation_values = {
        'species_id' : 6 ,
        'country'    : 'India',
        'state'      : 'Gujarat',
        'place'      : 'GRK'
    }
    db.create_observation(values = observation_values)


    # GET DATA BASED ON COLUMNS
    db.db_close()









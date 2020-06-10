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
    db.get_species()

    # GET SPECIES COMMON NAME FOR DROPDOWN
    desired_columns = ['common_name']
    filter = {
        'columns': desired_columns
    }

    # GET COMMON NAMES FOR
    db.get_common_names()

    db.get_scientific_name(1)


    #Add Observations



    # GET DATA BASED ON COLUMNS
    db.db_close()









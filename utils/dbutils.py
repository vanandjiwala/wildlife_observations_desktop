import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, String, Column, Text, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, Session, load_only
from datetime import datetime


class DbUtils():

    def __init__(self):
        #DB settings
        self.db = None
        self.db_conn = None
        self.db_session = None

        #Tables
        self.species = None
        self.observations = None


    def db_open(self,db_path):
        """Setting database and establishing connection and session with DB engine"""
        self.db = create_engine('sqlite:///{}'.format(db_path),echo=True)
        self.db_conn = self.db.connect()
        Session = sessionmaker(bind=self.db)
        self.db_session = Session()


    def db_close(self):
        """Close Database Connection"""
        self.db_conn.close()

    def create_tables(self):
        """
        Create DB tables if required.
        There are 2 tables
        observations - To store observations
        Species - To maintain list of species
        """
        metadata = MetaData()


        self.species = Table('species', metadata,
                            Column('id', Integer(), primary_key=True),
                            Column('common_name', String(200), nullable=False),
                            Column('scientific_name', String(200), nullable=True)
                        )

        self.observations = Table('observations', metadata,
                             Column('id', Integer(), primary_key=True),
                             Column('species_id', String(200), nullable=False),
                             Column('Country', String(200), nullable=False),
                             Column('State', String(200), nullable=False),
                             Column('Place', String(200), nullable=False),
                             Column('Lat', String(200), nullable=True),
                             Column('Long', String(200), nullable=True),
                             Column('Observation_time', DateTime(), default=datetime.now),
                             Column('created_on', DateTime(), default=datetime.now),
                             Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now)
                         )


        metadata.create_all(self.db_conn)


    ###########################################################################################################
    ###############################################CRUD OPERATINS##############################################
    ###########################################################################################################


    def get_species(self):
        """Returns all species from species table"""
        # map = {
        #     'id': self.species.columns.id,
        #     'common_name': self.species.columns.common_name,
        #     'scientific_name': self.species.columns.scientific_name
        # }

        result = self.db_session.query(self.species).all()
        return result

    def get_common_names(self):
        """
        Returns common names and id column from species table
        TODO: Merge this method in get_species for optimization
        """
        result = self.db_session.query(self.species.columns.id, self.species.columns.common_name).all()
        return result



    def get_scientific_name(self,species_id):
        """Get the scientific name based on the """
        # result = sqlalchemy.select([self.species.columns.scientific_name]).where(self.species.columns.id == species_id)
        result = self.db_session.query(self.species.columns.scientific_name).filter(self.species.columns.id == species_id).all()
        return result



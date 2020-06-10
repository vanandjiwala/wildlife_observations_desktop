import os

class PathUtils():

    @staticmethod
    def get_project_root():
        """static method to obtain project root directory"""
        return os.getcwd()

    @staticmethod
    def append_path(base_path,*args):
        """Static method to append path with base path"""
        path = base_path
        for path_component in args:
            path = os.path.join(path,path_component)

        return path

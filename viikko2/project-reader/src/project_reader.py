from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        data = toml.loads(content)
        curr = data["tool"]["poetry"]

        name = curr["name"]
        description = curr["description"]
        license = curr["license"]
        authors = curr["authors"]
        dependencies = curr["dependencies"]
        dev_dep = curr["group"]["dev"]["dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, license, authors, dependencies, dev_dep)

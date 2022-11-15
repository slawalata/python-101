from voting.persistances import VotingDB
from voting.services import VotingService


class VotingUI:
    def __init__(self):
        vooting_db = self.create_vooting_db()
        self.__vooting_service: VotingService = self.create_vooting_services(vooting_db)

    def init(self):
        self.__vooting_service.init()

    def display_vooting(self):
        vooters = self.__vooting_service.get_all_votters()
        for vooter in vooters:
            print(f"Name: {vooter.name} ({vooter.numbers})")

    def start(self):
        while True:
            self.display_vooting()
            input("Press any key to continue !!")
            print("")

    def create_vooting_services(self, _vooting_db, _service_settings=None):
        return VotingService(_vooting_db, _service_settings)

    def create_vooting_db(self, db_settings=None):
        return VotingDB(db_settings)

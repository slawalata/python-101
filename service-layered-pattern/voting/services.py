from voting.persistances import VotingDB


class VotingService:
    def __init__(self, voting_db, _settings=None):
        self.voting_db: VotingDB = voting_db

    def init(self):
        self.voting_db.init()

    def get_all_votters(self):
        return self.voting_db.get_all_vooters()

    def insert_new_name(self, _name, _initial_vot):
        if not self.voting_db.find_by_name(_name):
            self.voting_db.insert_new_voot(_name, _initial_vot)
        else:
            return False, "Name is already exists"

from voting.dtos import VotersDTO


class VotingDB:
    def __init__(self, _dbsettings):
        self.voters = [
            {"John", 10},
            {"Paulus", 20},
        ]

    def init(self):
        pass

    def get_all_vooters(self):
        vooters_dtos = []

        for (k, v) in self.voters:
            vooters_dtos.append(VotersDTO(k, v))

        return vooters_dtos

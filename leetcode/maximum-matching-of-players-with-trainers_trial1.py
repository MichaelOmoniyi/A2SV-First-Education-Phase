class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        trainer, matchings = 0, 0

        for player in players:
            while trainer < len(trainers):
                if player <= trainers[trainer]:
                    matchings += 1
                    trainer += 1
                    break
                trainer += 1
        return matchings
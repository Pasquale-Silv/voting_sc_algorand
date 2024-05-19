from algopy import ARC4Contract, arc4, GlobalState


class VotingSc(ARC4Contract):
    
    voting_str: arc4.String

    @arc4.abimethod()
    def create_voting(self, voting_str: arc4.String) -> None:
        self.voting_str = voting_str
    
    @arc4.abimethod()
    def get_voting_str(self) -> arc4.String:
        return self.voting_str

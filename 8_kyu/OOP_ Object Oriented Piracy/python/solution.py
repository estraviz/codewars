class Ship:

    def __init__(self, draft: int, crew: int):
        self.draft = draft
        self.crew = crew

    def is_worth_it(self) -> bool:
        return self.draft - 1.5 * self.crew > 20

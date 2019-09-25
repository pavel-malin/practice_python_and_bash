class PublicPrivateExample:
    def __init__(self):
        self.public = "безопасно"
        self._unsafe = "опасно"

    def public_method(self):
        # клиенты могут это использовать 
        pass

    def _unsafe_method(self):
        # клиенты не должны это использвать
        pass
        self.public = "безопасно"
        self._unsafe = "опасно"
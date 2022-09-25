import spacy

class NamedEntityClient:

    def __init__(self, model: spacy.lang.en.English):
        self.model = model

    def get_ents(self, sentence):
        return {}
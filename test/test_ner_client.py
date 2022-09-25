import unittest

from ner_client import NamedEntityClient

class TestNERClient(unittest.TestCase):

    #  { ents: [{...}],
    #    html: "<span>..."}

    def test_get_ents_returns_dict_given_empty_string(self):
        model = NERModelTestDouble("eng")
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_list_given_nonempty_string(self):
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in Wisconsing")
        self.assertIsInstance(ents, dict)
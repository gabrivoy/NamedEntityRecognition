import unittest
# python -m pytest

from ner_client import NamedEntityClient
from test_doubles import NERModelTestDouble

class TestNERClient(unittest.TestCase):

    #  { ents: [{...}],
    #    html: "<span>..."}

    def test_get_ents_returns_dict_given_empty_string_causes_empty_spacy_doc_ents(self):
        model = NERModelTestDouble("eng")
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_dict_given_nonempty_string_causes_empty_spacy_doc_ents(self):
        model = NERModelTestDouble("eng")
        model.returns_doc_ents([])
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Madison is a city in Wisconsing")
        self.assertIsInstance(ents, dict)

    def test_get_ents_given_spacy_PERSON_is_returned_serializes_to_Person(self):
        model = NERModelTestDouble("eng")
        doc_ents = [{'text': 'Laurent Fressinet', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_result = {'ents': [{'ent': 'Laurent Fressinet', 'label': 'Person'}],
                           'html': "",}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_NORP_is_returned_serializes_to_Group(self):
        model = NERModelTestDouble("eng")
        doc_ents = [{'text': 'Lithuanian', 'label_': 'NORP'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_result = {'ents': [{'ent': 'Lithuanian', 'label': 'Group'}],
                           'html': "",}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LOC_is_returned_serializes_to_Location(self):
        model = NERModelTestDouble("eng")
        doc_ents = [{'text': 'the ocean', 'label_': 'LOC'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_result = {'ents': [{'ent': 'the ocean', 'label': 'Location'}],
                           'html': "",}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_LANGUAGE_is_returned_serializes_to_Language(self):
        model = NERModelTestDouble("eng")
        doc_ents = [{'text': 'ASL', 'label_': 'LANGUAGE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_result = {'ents': [{'ent': 'ASL', 'label': 'Language'}],
                           'html': "",}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_spacy_GPE_is_returned_serializes_to_Location(self):
        model = NERModelTestDouble("eng")
        doc_ents = [{'text': 'Australia', 'label_': 'GPE'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_result = {'ents': [{'ent': 'Australia', 'label': 'Location'}],
                           'html': "",}
        self.assertListEqual(result['ents'], expected_result['ents'])

    def test_get_ents_given_multiple_ents_serializes_all(self):
        model = NERModelTestDouble("eng")
        doc_ents = [{'text': 'Australia', 'label_': 'GPE'}, {'text': 'Judith Polgar', 'label_': 'PERSON'}]
        model.returns_doc_ents(doc_ents)
        ner = NamedEntityClient(model)
        result = ner.get_ents("...")
        expected_result = {'ents': [
            {'ent': 'Australia', 'label': 'Location'},
            {'ent': 'Judith Polgar', 'label': 'Person'},
            ],
                           'html': "",}
        self.assertListEqual(result['ents'], expected_result['ents'])
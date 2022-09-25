"""
Create a double that behaves like spaCy

> import spacy
> model = spacy.load("en_core_web_sm")
> type(model)
<class 'spacy.lang.en.English'>
> doc = model("Madison is a city in Wisconsing")
> type(doc)
<class 'spacy.tokens.doc.Doc'>
> doc.ents
(Madison, Wisconsing)
> [(ent.text, ent.label_) for ent in doc.ents]
[('Madison', 'PERSON'), ('Wisconsing', 'GPE')]
"""

class NERModelTestDouble:
    """
    Test double for spaCy NLP model
    """
    def __init__(self, model):
        self.model = model

    def returns_doc_ents(self, ents):
        self.ents = ents

    def __call__(self, sent):
        return DocTestDouble(sent, self.ents)

class DocTestDouble:
    """
    Test double for spaCy Doc
    """
    def __init__(self, sent, ents):
        self.ents = [SpanTestDouble(ent['text'], ent['label_']) for ent in ents]

    def patch_method(self, attr, return_value):
        def patched(): return return_value
        setattr(self, attr, patched)
        return self

class SpanTestDouble:
    """
    Test double for spaCy Span
    """
    def __init__(self, text, label):
        self.text = text
        self.label_ = label




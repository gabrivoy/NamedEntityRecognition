# Named Entity Recognition App | Test-Driven Development Studies

This repository contains a simple application using the Named Entity Recognition NER concept 
(you can read more about on the [wiki:NER](https://en.wikipedia.org/wiki/Named-entity_recognition))
to study and apply both tests and test-driven development 
(TDD, [wiki:TDD](https://pt.wikipedia.org/wiki/Test-driven_development)) in Python.

## How it works?

The application uses the [spaCy](https://spacy.io/)'s `"en_core_web_sm"` model to map the input
text on the application to the NER's labels. Also, the application uses Flask as a API to generate 
an endpoint to receive the text, and call the spaCy model. The application was developed using TDD 
concepts, with the tests being written before the code, using the red-green-refactor approach.

## How to run

To run, just create a virtual environment and install the `requirements.txt` file. This can be done
either via `conda envs` or `virtualenv` commands. After creating the environment, go to the folder where
you've cloned the project and install the requirements with the `pip install -r requirements.txt` command
(if you've created a `conda env`, there's a chance will need to install `pip`, you can do it with 
the `conda install pip` command).

From there, you need to install the app as a package on the editable mode. 
On the folder, just execute `pip install -e .` to install the app.

After that, you can execute the command `python app.py` to expose a port on `http://127.0.0.1/5000` and access 
the project on the browser.

## How to execute the tests

The tests are on the `/test/` subfolder, where you can navigate to and run the command below. If you're
using Visual Studio Code, you can access the tests menu on the left, on the symbol of the funnel flask.

```
python -m pytests
```

To execute all of them.

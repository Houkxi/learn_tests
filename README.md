# learn_tests

## Python folder

### Computor v1
**No Grade yet**

The goal of this project was to parse a second degree equation, simplifie it and send back the answer.
Project done to learn some ```Pytohn```. I mostly saw how to parse arguments with the ```argparse```[man](https://docs.python.org/3/library/argparse.html) module and pattern search with the ```re```[man](https://docs.python.org/2/library/re.html) module.

```python
# Create ArguemntParser object
parser = argparse.ArguemntParser(descrition="The start of this module")
# Adding a type of accepted argument
parser.add_argument('str', type=str, help="help message to indicate it\'s use")
# Convert each argument to the the specified type
args = parse.parse_args()

# Search for at least 1 number from the beginning till the end
re.search('\A[0-9]+\Z')
```

- *IN PROGRESS*

### Expert System
**No grade**
- *IN PROGRESS*

### API Tests

- *IN PROGRESS*
Learning how to create asimple api.
#### Flask tutorial

Followed the [flask](http://flask.pocoo.org/docs/1.0/tutorial/layout/) tutorial.

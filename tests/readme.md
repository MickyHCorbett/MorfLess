# Overview

The tests in this folder represent unit tests and mock aws tests. 

To run the tests you will need the mock boto3 library - **Moto**

[http://docs.getmoto.org/en/latest/docs/getting_started.html](http://docs.getmoto.org/en/latest/docs/getting_started.html)

The tests run everything except the main Lambda handlers as these are tested on deployment of your site anyway. Tests for Lambda layer libraries and lambda handler libraries are all included. The tests run as one. If you wish to run only one group of tests at a time edit the [test_handler_unit.py](test_handler_unit.py) file by commenting out the imports of test files.

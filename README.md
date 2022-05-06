# RESTful Date/ Keyword Storage and Retrevial 

## Requirements
* This application should run under both Linux and Windows opearting systems.
* The author of this application prefers to run it inside of a virual environment, but this is not strictly necessary.

## Installation

1. Clone this repository
``` bash
git clone https://github.com/aneugart/cs361-file_line_tool_microservice
```
2. Activate your python environment if using one (you really should be).
3. From within the "cs361-file_line_tool_microservice" directory, install the application and required python dependencies.
``` bash
pip install .
```
4. From the "cs361-file_line_tool_microservice" directory, run the following commands to initilize the databse.
``` bash
flask db init
flask db migrate
flask db upgrade
```
5. That should be it, you should now be ready to run teh application!

## Running the Application

If this application were to be deployed in a more permanent or larger environment, you would not wish to run it using the built in server.  However, for the purposes of this class this should be sufficient.

To run the application using the developement server, simply run the following command from the "cs361-file_line_tool_microservice" (ensuring that you have activated any environment that you may be using):
``` bash
flask run
```

## Requests

The following examples assume tha the application is running at localhost on port 5000.  Some test HTTP requests are provided in test_requests.http in the root of directory of this project.

### Creating a record

Entries may be created by sending a POST request to the server.

``` http
POST http://localhost:5000 HTTP/1.1
content-type: application/json

{
    "date": "2022-10-10",
    "keyword": "Hello!"
}
```

The server response will have a status code of 201 if the entry was successfully created, or a status code of 400 or 500 if there was an error.

### Retrieving all records.

All saved records may be retreived from the server by sending a GET request to the / endpoint.

``` http
GET http://localhost:5000/ HTTP/1.1
```

The server response will have a status of 200 and the body of the response will be a JSON object like the example below:
``` json
{
  "data": {
    "2022-10-10": "Hello!",
    "2022-11-10": "MEOW!",
    "2022-11-11": "CATS RULE!!!"
  }
}
```

### Retrieving a single record.

A single saved record may be retreived from the server by sending a GIT request to the /YYYY-MM-DD endpoint (where YYYY-MM-DD should be replaced by the date to retrieved).

```http
GET http://localhost:5000/2022-10-10 HTTP/1.1
```
The server response will have a status code of 200 if a matching entry was successfully found, 404 if the request was valid but no record was found, or a status code of 400 if the request was invalid.  The responce body will be a JSON object will look like the example below:  

``` json
{
  "data": {
    "2022-10-10": "Hello!"
  }
}
```

### Deleting a record
A record may be deleted by sending a DELETE request to the /YYYY-MM-DD endpoint (where YYYY-MM-DD should be replaced by the date to delete).
``` http
DELETE http://localhost:5000/2022-10-10 HTTP/1.1
```

The server response will have a status code of 204 if the entry was successfully created, or a status code of 400 or 500 if there was an error.  A status code of 404 indicates that the request was valid, but no record to delete could be found.
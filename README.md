# basic-docker-database
Contains the ability to throw up a basic docker container which will contain a database and api to run basic crud commands.

Requires Docker and Docker's Postgres image.

### SetUp And Run
Pull down this repo and run the following command to set it up. <br>
```docker-compose -f docker-compose.yml up```

To run the crud commands against the database you can curl (or use a web browser) to pass:<br>
```http://localhost:5000/<crud>/<row>```

* Crud can be a lowercase c, r, u or d.
* Row should be a dictionary including some of the following elements. Do not include in dictionary if there are not used.
|  | c | r | u | d |
|---|---|---|---|---|
| user_id | No | Maybe | Yes | Yes |
| forename | Yes | Maybe | Maybe | No |
| surname | Yes | Maybe | Maybe | No |
| email | Yes | Maybe | Maybe | No |
| phone_number | Yes | Maybe | Maybe | No |

```e.g.``` <br>
```http://localhost:5000/c/{"forename": "Matthew", "surname": "Colt", "email": "matt.colt@domain.co.uk", "phone_number": "00000000000"}``` <br>
```http://localhost:5000/r/{"user_id": "1", "email": "matt.colt@domain.co.uk"}```
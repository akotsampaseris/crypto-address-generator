# Crypto Wallet Generator

Generate a wallet for your favorite cryptocurrencies in seconds!

## Installation

Steps:

1. Clone this repo on your local dev environment
2. Install dependencies using `pip install -r requirements.txt`
3. Copy `.env.example` to `.env`
4. Change all relevant values in the `.env` file
5. Run `python manage.py migrate`
6. Run `python manage.py runserver`
7. You can access the API on `http://localhost:8000/api`. Use the documentation below to work with the Wallet Generator API.



## API

All API calls fall under the /api/ prefix. All requests are parsed using JSON and are rendered as JSON responses. All other types are not allowed.

**GET /addresses/**

Returns a paginated set of wallet addresses.

Query parameters:
- (optional) **coin_id**: String, eg *'btc`*. Filters addresses with specified *coin_id*.
- (optional) **page**: Integer, eg *2*. Defines the number of the page for the paginated results.
- (optional) **page_size**: Integer, eg *20*. Defaults to *100*. Defines the total number of paginated results per page. 

*Example Request*

```bash
$ curl GET http://localhost:8000/api/addresses/ \
    -H 'Accept: application/json' \
    -H 'Accept-Encoding: gzip, deflate' \
    -H 'Cache-Control: no-cache' \
    -H 'Connection: keep-alive' \
    -H 'Referer: http://localhost:8000/api/addresses' \
    -H 'cache-control: no-cache'
```

*Example Response*

```bash
{
    "count": 100,
    "next": "http://localhost:8000/api/addresses/",
    "previous": null,
    "results": [
        {
            "id": 1,
            "coin": "btc",
            "address": "173SwSBUy5UiVztyCcj44RGqFoMbaTtLqA"
        },
        ...
    ]
}
```

**GET /addresses/address/<int:id>**

Returns the details of a wallet address specified by the **id**.

Arguments:
- (Required) **id**: Integer, eg *1*. Specifies the wallet address on the database.

Query parameters:
- (optional) **coin_id**: String, eg *'btc`*. Filters addresses with specified *coin_id*.
- (optional) **page**: Integer, eg *2*. Defines the number of the page for the paginated results.
- (optional) **page_size**: Integer, eg *20*. Defaults to *100*. Defines the total number of paginated results per page. 

*Example Request*

```bash
$ curl GET http://localhost:8000/api/addresses/address/1 \
    -H 'Accept: application/json' \
    -H 'Accept-Encoding: gzip, deflate' \
    -H 'Cache-Control: no-cache' \
    -H 'Connection: keep-alive' \
    -H 'Referer: http://localhost:8000/api/addresses/address/1' \
    -H 'cache-control: no-cache'
```

*Example Response*

```bash
{
    "id": 1,
    "coin": "btc",
    "address": "173SwSBUy5UiVztyCcj44RGqFoMbaTtLqA",
    "created_at": "2022-10-02T00:33:25.670708Z",
    "updated_at": "2022-10-02T00:33:25.670739Z",
}
```

**POST /addresses/generate**

Creates a new wallet address. Returns a **201 Created** status along with the validated address object.

Request body: 
- (Required) **coin_id**: String, eg *'btc'*. Defines the type of wallet to be generated.

*Example Request*

```bash
$ curl POST http://localhost:8000/api/addresses/generate \
  -H 'Accept: application/json' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Authorization: secretkey' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/json' \
  -d '{
        "coin_id": "btc", 
    }'
```

*Example Response*

```bash
{
    "ID": "rs1000",
    "CHROM": "chr10",
    "POS": 1000,
    "ALT": "A",
    "REF": "G"
}
```

## Testing

Testing is being handled with *pytest*. All tests are stored in the *tests* directory and split among files per each Python class, eg `tests/test_services/test_some_service.py`.
To run all tests in the test suite, you can simply run 
```bash
$ pytest -q tests
```
in the root directory, or you can run each test class on its own, ie
```bash
$ pytest -q tests/test_services/test_some_service.py
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## License

[MIT](https://choosealicense.com/licenses/mit/)
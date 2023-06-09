class AddressesMocks:
    address_1 = {
        "number": 1,
        "street": "Rua1",
        "district": "Centro",
        "zipCode": "81000-000",
        "state": "SP",
        "city": "Santo André",
    }

    address_2 = {
        "number": 2,
        "street": "Rua2",
        "district": "Centro",
        "zipCode": "82000-000",
        "state": "CE",
        "city": "São Bernardo do Campo",
    }

    address_3 = {
        "number": 3,
        "street": "Rua3",
        "district": "Centro",
        "zipCode": "83000-000",
        "state": "SP",
        "city": "São Caetano",
    }

    address_fail_required_fields = {
        "street": "Rua1",
        "district": "Centro",
        "zipCode": 61,
        "state": "CE",
        "city": "Crato",
        "number": 48,
    }

    address_fail_wrong_types = {
        "street": "Rua1",
        "district": "Centro",
        "zipCode": 61,
        "state": "CE",
        "city": "Crato",
        "number": 48,
    }

    random_addresses = [
        {
            "number": 14,
            "street": "Berry Street",
            "district": "Veguita",
            "zipCode": "96526-987",
            "state": "TN",
            "city": "Venice",
        },
        {
            "number": 81,
            "street": "Beaver Street",
            "district": "Crisman",
            "zipCode": "72772-432",
            "state": "PR",
            "city": "Tonopah",
        },
        {
            "number": 69,
            "street": "Carroll Street",
            "district": "Bladensburg",
            "zipCode": "68954-762",
            "state": "NE",
            "city": "Sparkill",
        },
        {
            "number": 38,
            "street": "Lefferts Avenue",
            "district": "Nettie",
            "zipCode": "63852-869",
            "state": "MH",
            "city": "Southmont",
        },
        {
            "number": 69,
            "street": "Abbey Court",
            "district": "Nanafalia",
            "zipCode": "15416-147",
            "state": "UT",
            "city": "Emory",
        },
        {
            "number": 25,
            "street": "Beverly Road",
            "district": "Herlong",
            "zipCode": "79399-487",
            "state": "IL",
            "city": "Craig",
        },
        {
            "number": 39,
            "street": "Meeker Avenue",
            "district": "Movico",
            "zipCode": "34199-431",
            "state": "SC",
            "city": "Marion",
        },
        {
            "number": 52,
            "street": "Forest Place",
            "district": "Kilbourne",
            "zipCode": "27344-876",
            "state": "MA",
            "city": "Alfarata",
        },
        {
            "number": 13,
            "street": "Humboldt Street",
            "district": "Fingerville",
            "zipCode": "29927-787",
            "state": "AL",
            "city": "Malott",
        },
        {
            "number": 79,
            "street": "Flatlands Avenue",
            "district": "Blodgett",
            "zipCode": "64282-176",
            "state": "HI",
            "city": "Lund",
        },
        {
            "number": 75,
            "street": "Willow Place",
            "district": "Winfred",
            "zipCode": "98212-236",
            "state": "MI",
            "city": "Hiwasse",
        },
        {
            "number": 11,
            "street": "Vanderveer Street",
            "district": "Titanic",
            "zipCode": "25273-269",
            "state": "ND",
            "city": "Villarreal",
        },
        {
            "number": 58,
            "street": "Bridgewater Street",
            "district": "Hackneyville",
            "zipCode": "75753-755",
            "state": "AS",
            "city": "Nutrioso",
        },
        {
            "number": 40,
            "street": "Hart Street",
            "district": "Glenville",
            "zipCode": "72953-763",
            "state": "AK",
            "city": "Ypsilanti",
        },
        {
            "number": 57,
            "street": "Quentin Road",
            "district": "Cresaptown",
            "zipCode": "13279-255",
            "state": "IN",
            "city": "Konterra",
        },
        {
            "number": 79,
            "street": "Atlantic Avenue",
            "district": "Vowinckel",
            "zipCode": "17973-456",
            "state": "VT",
            "city": "Harborton",
        },
        {
            "number": 70,
            "street": "Vandervoort Avenue",
            "district": "Marienthal",
            "zipCode": "12183-649",
            "state": "WV",
            "city": "Wilsonia",
        },
        {
            "number": 71,
            "street": "Oceanview Avenue",
            "district": "Laurelton",
            "zipCode": "34992-371",
            "state": "MN",
            "city": "Downsville",
        },
        {
            "number": 22,
            "street": "Gem Street",
            "district": "Mayfair",
            "zipCode": "88136-262",
            "state": "KY",
            "city": "Naomi",
        },
        {
            "number": 13,
            "street": "Woodrow Court",
            "district": "Gorst",
            "zipCode": "12642-927",
            "state": "SD",
            "city": "Staples",
        },
        {
            "number": 9,
            "street": "Glenmore Avenue",
            "district": "Blandburg",
            "zipCode": "99532-527",
            "state": "NH",
            "city": "Riviera",
        },
        {
            "number": 20,
            "street": "Terrace Place",
            "district": "Waumandee",
            "zipCode": "66911-799",
            "state": "RI",
            "city": "Bluetown",
        },
        {
            "number": 63,
            "street": "Merit Court",
            "district": "Darlington",
            "zipCode": "82558-338",
            "state": "WA",
            "city": "Shelby",
        },
        {
            "number": 39,
            "street": "Bliss Terrace",
            "district": "Kent",
            "zipCode": "34112-384",
            "state": "DE",
            "city": "Como",
        },
        {
            "number": 73,
            "street": "Woodruff Avenue",
            "district": "Springdale",
            "zipCode": "63779-689",
            "state": "LA",
            "city": "Matheny",
        },
        {
            "number": 97,
            "street": "Amboy Street",
            "district": "Calvary",
            "zipCode": "96991-854",
            "state": "FL",
            "city": "Baden",
        },
        {
            "number": 31,
            "street": "Lake Avenue",
            "district": "Kersey",
            "zipCode": "14578-477",
            "state": "OR",
            "city": "Efland",
        },
        {
            "number": 17,
            "street": "Stockholm Street",
            "district": "Edgewater",
            "zipCode": "87124-468",
            "state": "CT",
            "city": "Celeryville",
        },
        {
            "number": 70,
            "street": "Hill Street",
            "district": "Gardners",
            "zipCode": "32162-845",
            "state": "NY",
            "city": "Winston",
        },
        {
            "number": 12,
            "street": "Reeve Place",
            "district": "Walland",
            "zipCode": "22514-281",
            "state": "OH",
            "city": "Falconaire",
        },
        {
            "number": 44,
            "street": "Montauk Court",
            "district": "Groton",
            "zipCode": "29399-748",
            "state": "PA",
            "city": "Shrewsbury",
        },
        {
            "number": 47,
            "street": "Cropsey Avenue",
            "district": "Nadine",
            "zipCode": "14222-464",
            "state": "NM",
            "city": "Websterville",
        },
        {
            "number": 60,
            "street": "Adler Place",
            "district": "Gorham",
            "zipCode": "53764-481",
            "state": "ID",
            "city": "Norwood",
        },
        {
            "number": 62,
            "street": "Moore Place",
            "district": "Idledale",
            "zipCode": "26994-848",
            "state": "OK",
            "city": "Martell",
        },
        {
            "number": 26,
            "street": "Dover Street",
            "district": "Sperryville",
            "zipCode": "58874-766",
            "state": "WI",
            "city": "Gallina",
        },
        {
            "number": 16,
            "street": "Colonial Road",
            "district": "Vale",
            "zipCode": "13488-147",
            "state": "NC",
            "city": "Elfrida",
        },
        {
            "number": 19,
            "street": "Barwell Terrace",
            "district": "Woodlake",
            "zipCode": "84292-244",
            "state": "MP",
            "city": "Irwin",
        },
        {
            "number": 96,
            "street": "Strauss Street",
            "district": "Kempton",
            "zipCode": "94659-231",
            "state": "MS",
            "city": "Bethpage",
        },
        {
            "number": 55,
            "street": "Underhill Avenue",
            "district": "Inkerman",
            "zipCode": "81341-392",
            "state": "ME",
            "city": "Dawn",
        },
        {
            "number": 77,
            "street": "Duryea Place",
            "district": "Drummond",
            "zipCode": "93783-618",
            "state": "VI",
            "city": "Geyserville",
        },
    ]

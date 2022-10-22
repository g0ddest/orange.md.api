# Orange Moldova API

Simple orange.md api that aims to activate options automatically.

## Authorization

For authorization you should register in [My Orange Moldova](https://my.orange.md) first.

Then you can get instance of authorized api this way:

```python
orange = Orange("email or phone number", "password", lang="EN")
```

Language could be English (`EN`), Moldovan(`MD`) or Russian(`RU`).

After authorization you can make all another operations.

## Balance

```python
orange.balance()
```

it returns:

```json
{
  "account": {
    "msisdn": "69000000",
    "plan": "Optim",
    "icon": "generic",
    "planType": "PREPAID",
    "status": "Active",
    "accountType": "voice",
    "relatedParty": []
  },
  "balance": {
    "dashboardGauges": [],
    "dashboardPanel": [
      {
        "available": "",
        "unlimited": false,
        "used": "",
        "remaining": "100.00 MDL",
        "nRemaining": 100.00,
        "availableText": "",
        "remainingText": "100.00 MDL",
        "unit": "MDL",
        "title": "Remaining Credit",
        "shortDescription": "",
        "transferable": true
      }
    ],
    "list": [
      {
        "available": "100 MB",
        "unlimited": false,
        "used": "0 MB",
        "remaining": "100 MB",
        "nUsed": 0,
        "nRemaining": 100,
        "availableText": "100 MB",
        "remainingText": "100 MB available",
        "unit": "MB",
        "title": "Total remaining data",
        "shortDescription": "",
        "transferable": false
      },
      {
        "available": "100 MB",
        "unlimited": false,
        "used": "0 MB",
        "remaining": "100 MB",
        "nUsed": 0,
        "nRemaining": 100,
        "availableText": "100 MB",
        "remainingText": "100 MB available",
        "unit": "MB",
        "title": "100 MB bonus \nfor 1 day",
        "shortDescription": "Until 01-01-2050",
        "transferable": false,
        "categoryId": "data"
      }
    ]
  }
}
```

## Services list

You can get all available to activate options this way:

```python
orange.services_list()
```

It returns:

```json

{
  "options": [
    {
      "description": "",
      "shortDescription": "Active",
      "id": "SPO_SSO_SERVICE",
      "name": "Orange Account",
      "desactivable": true,
      "activable": false,
      "renewable": false,
      "complientType": 0,
      "buttonName": "Deactivate"
    },
    {
      "description": "",
      "shortDescription": "Active",
      "id": "SPO_FORTUNE_100_MB",
      "name": "100 MB bonus \nfor 1 day",
      "desactivable": true,
      "activable": false,
      "renewable": false,
      "complientType": 0,
      "buttonName": "Deactivate"
    },
    {
      "description": "",
      "shortDescription": "Active",
      "id": "SPO_4G",
      "name": "4G Service",
      "desactivable": true,
      "activable": false,
      "renewable": false,
      "complientType": 0,
      "buttonName": "Deactivate"
    },
    {
      "category": "Roaming",
      "description": "15 minutes for outgoing and incoming calls towards Europe\n\nValidity: 30 days\n\n(Belgium, Bulgary, Switzerland, France, Germany, Greece, Italy, Poland, Romania, Spain, Hungry, Austria, Croatia, Great Britain, Russia, Turkey and Ukraine)",
      "shortDescription": "30 days",
      "id": "SPO_FAVORITE_COUNTRY",
      "name": "Favourite Country - Europe",
      "desactivable": false,
      "activable": true,
      "value": "80 MDL",
      "renewable": false,
      "complientType": 2,
      "buttonName": "Activate"
    }
  ]
}
```

It returns list of activated and available to activate options.

## Activate option

```python
orange.subscribe("SPO_FAVORITE_COUNTRY")
```

In parameter goes id of service from services list.

As a result you can get a text response like this one: `The option has been successfully activated.` or alternatively you can get an error text.

For activation daily bonus you can do this:

```python
orange.subscribe_daily_bonus()
```

It just calls `subscribe` with `SPO_DAILY_BONUS_25MB` option.

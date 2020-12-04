# Open States scrapers, adapted for Montana

Adapted from https://github.com/openstates/openstates-scrapers.

## Commands

This assumes Docker is installed and running. See the OpenStates [getting started guide](https://docs.openstates.org/en/latest/contributing/getting-started.html).

### Full scrape
```npm run scrape```
or
```docker-compose run --rm scrape mt bills --scrape```

Writes to `_cache` and `_data` folders (left untracked by version control). 

### Single bill scrape

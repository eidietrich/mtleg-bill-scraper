# Open States scrapers, adapted for Montana

Adapted from https://github.com/openstates/openstates-scrapers.

## Commands

This assumes Docker is installed and running. See the OpenStates [getting started guide](https://docs.openstates.org/en/latest/contributing/getting-started.html).

### Full scrape with vote event cache
```npm run scrape```

Writes to `_cache` and `_data` folders (left untracked by version control). 

If you have done a local scrape before, this script will create a temporary cache in `_cached_votes` of any vote events 
from your last scrape to avoid requesting and parsing the same vote events again. After a full scrape, this folder will be deleted.

### Full scrape without vote event cache
```npm run scrape-no-cache``` will ignore your previous scraped vote events and run a full scrape without using the cache. 
Once you run this, you can't get your previously scraped vote events back again.

### Single bill scrape
* [Contributor's Guide](https://docs.openstates.org/en/latest/contributing/getting-started.html)
* [Documentation](https://docs.openstates.org/en/latest/contributing/scrapers.html)
* [Open States Issues](https://github.com/openstates/issues/issues)
* [Open States Discussions](https://github.com/openstates/issues/discussions)
* [Code of Conduct](https://docs.openstates.org/en/latest/contributing/code-of-conduct.html)

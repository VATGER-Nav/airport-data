# Airport Data

Manages the airport data used on the VATSIM Germany homepage.

### Airport type:

```
[[airport]]
icao = "EDDY"

[[airport.links]]
category = "Scenery" | "Charts" | "Briefing" | NONE
name = "Display Name 1"
url = "https://example.url"
```

example:

```
[[airport]]
icao = "EDDY"

[[airport.links]]
category = "Scenery"
name = "Display Name 1"
url = "https://example.url"

[[airport.links]]
category = "Charts"
name = "Display Name 2"
url = "https://example2.url"

```

# Link Order+Description:

Freeware First and MSFS before X-Plane:
1. Charts:
- Charts (IFR)
- Charts (VFR)
2. Briefing:
- Pilotbriefing
- vACDM Pilot Guide (only if needed)
3. Scenery
- MSFS Freeware by XXX
- X-Plane Freeware by XXX
- MSFS Payware by XXX
- X-Plane Payware by XXX


4. Example:

```
[[airport]]
icao = "EXXX"

[[airport.links]]
category = "Charts"
name = "Charts (IFR)"
url = "https://chartfox.org/EXXX"

[[airport.links]]
category = "Charts"
name = "Charts (VFR)"
url = "https://aip.dfs.de/BasicVFR/pages/XXX.html"

[[airport.links]]
category = "Briefing"
name = "Pilotbriefing"
url = "https://vats.im/exxx"

[[airport.links]]
category = "Briefing"
name = "vACDM Pilot Guide"
url = "https://vacdm.net/docs/pilot"

[[airport.links]]
category = "Scenery"
name = "MSFS Freeware by XXX"
url = "https://example.com"

[[airport.links]]
category = "Scenery"
name = "X-Plane Freeware by XXX"
url = "https://example.com"

[[airport.links]]
category = "Scenery"
name = "MSFS Payware by XXX"
url = "https://example.com"

[[airport.links]]
category = "Scenery"
name = "X-Plane Payware by XXX"
url = "https://example.com"
```

# TODO:

- give warnings using PRs or Discord hook?

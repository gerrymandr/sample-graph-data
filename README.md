Sample Electoral Data
===

This repo contains sample electoral data, including adjacency graphs, units
at various scales, demographic data, and past election results. We’ve started
with [data from Minnesota’s Legislative Coordinating Commission](http://www.gis.leg.mn/html/download.html)
covering [an area to the north and west of Minneapolis](MN-sample-area.geojson)
with a mix of urban, rural, white, non-white, conservative, and liberal voters.

![Minnesota Sample Area](MN-sample-data.png)

Four layers are included: minor civil divisions (MCDs), Census tracts, voter
tabulation districts (VTDs), and Census blocks. Raw data and adjacency lists
for graph representations are included for each. Each includes demographic and
race data [detailed in _metadata_](http://www.gis.leg.mn/metadata/redist2010.htm).

Minor Civil Divisions
---

- Size: 24 units, 46 edges
- ID field: `MCD`
- Adjacency list: [mcd2010-graph.csv](mcd2010-graph.csv)
- Shapefile: [mcd2010-slice.zip](mcd2010-slice.zip)

![Minnesota MCDs Graph](mcd2010-graph.png)

Census Tracts
---

- Size: 94 units, 228 edges
- ID field: `TRACT`
- Adjacency list: [tracts2010-graph.csv](tracts2010-graph.csv)
- Shapefile: [tracts2010-slice.zip](tracts2010-slice.zip)

![Minnesota Tracts Graph](tracts2010-graph.png)

Voter Tabulation Districts
---

- Size: 133 units, 334 edges
- ID field: `VTD`
- Adjacency list: [vtd2010-graph.csv](vtd2010-graph.csv)
- Shapefile: [vtd2010-slice.zip](vtd2010-slice.zip)

![Minnesota VTD Graph](vtd2010-graph.png)

Census Blocks
---

- Size: 5,358 units, 12,802 edges
- ID field: `BLOCK`
- Adjacency list: [blk2010-graph.csv](blk2010-graph.csv)
- Shapefile: [blk2010-slice.zip](blk2010-slice.zip)

![Minnesota Blocks Graph](blk2010-graph.png)

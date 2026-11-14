# Vessel traffic in the Kattegat and Skagerrak, 5–11 October 2026

How many vessel-hours were spent inside Natura 2000 marine protected areas in the
Kattegat and Skagerrak during one week, by ship type, and how many of those hours
show apparent bottom-towed fishing — including inside the three closure zones of
Nordvästra Skånes havsområde, where bottom trawling has been prohibited since
6 July 2026.

Built from 117,612,138 rows of open AIS data.

## Results

- **116,262.1 vessel-hours** of AIS-reported presence inside the IHO limits of the
  two seas that week.
- **16,933.5 of them — 14.56% — inside Natura 2000 sites.** 111 of the 221 sites
  in the two seas carried vessel traffic; 110 carried none.
- Cargo is the largest category inside protected areas (26.85% of the hours),
  ahead of fishing (13.04%) and recreational traffic (24.08% for pleasure and
  sailing combined).
- **Apparent bottom-towed fishing: 4,872.2 vessel-hours**, of which 25.15% fell
  inside a protected area. As a share of the hours recorded in each, apparent
  trawling was 7.24% inside sites against 3.67% outside — but this is a share of
  traffic, not a density, and it is confounded by geography.
- **Inside the three closure zones, three vessels — one per zone — account for
  every apparent bottom-towed position in the week:** 36 positions, 1.80
  vessel-hours, across 815 km².

 "Apparent" throughout: AIS speed is a proxy for gear use, never evidence of it.
One post-closure week cannot distinguish compliance from an area that was never
fished.

## What is in this repository

| Path | Contents |
|---|---|
| `scripts/` | `first_lines.py`, `filter.py`, `thin.py` — the Python pipeline |
| `data/` | `zones_785_clean.csv`, the 68 closure-zone coordinates, transcribed; `schema.ini`, column types, needed on a comma-decimal locale |
| `figures/` | the two published figures, PNG at 300 dpi |

`data/zones_785_clean.csv` is the only part of this repository that cannot be
obtained elsewhere. No agency publishes a polygon of the three zones — not
Havs- och vattenmyndigheten, not its geodata service, not EMODnet. The 68
coordinate pairs were transcribed by hand from the Annex to Commission Delegated
Regulation (EU) 2026/785, entered twice independently, and compared in code; one
error was found and corrected against the PDF.

## The data is not here

The AIS data is not in this repository and must not be. Two reasons:

1. **Size.** 117,612,138 rows, about 4 GB zipped and five times that unzipped.
2. **The data policy.** The Swedish Maritime Administration AIS policy states the
   data must not be combined to identify individuals without permission from the
   Danish Data Protection Agency. Results here are reported in aggregate; no
   vessel is identified and no MMSI is published.

Download the seven daily files yourself from the Danish Maritime Authority:
<http://aisdata.ais.dk/> — `aisdk-2026-10-05.zip` through `aisdk-2026-10-11.zip`.

Other sources used:

| Layer | Source | Licence |
|---|---|---|
| Natura 2000, end 2024 | European Environment Agency / DG ENV | CC BY 4.0 |
| IHO Sea Areas v3 | Flanders Marine Institute, doi:10.14284/323 | CC BY-NC-SA 4.0 |
| Closure zones | Commission Delegated Regulation (EU) 2026/785, Annex | EU legal text |

## Reproducing it

1. Download the seven daily AIS files into `C:\GIS\Data\AIS\raw`, or your own path.
2. `python scripts/first_lines.py` — prints the header and first rows, to check
   the file structure.
3. `python scripts/filter.py` — keeps rows inside the study-area box
   (54.63–59.92 N, 6.99–13.07 E) and the nine columns used.
4. `python scripts/thin.py` — keeps Class A and B only, then one position per
   vessel per three-minute slot. Each retained position is 0.05 vessel-hours.
5. Load the thinned files into ArcGIS Pro, working in EPSG 3035 (ETRS89-LAEA), and
   build the closure zones from `data/zones_785_clean.csv` with `schema.ini`
   alongside it.

The full method, every check that was run, and the limitations are in the
workflow document.

## Licensing

- **Code** in `scripts/` — MIT, see `LICENSE`.
- **`data/zones_785_clean.csv`** — CC BY 4.0. Transcribed from an official EU
  legal text; reuse it, with attribution.
- **`figures/fig01_vessel_density_kattegat_skagerrak_2026-10-05_11.png`** —
  **CC BY-NC-SA 4.0.** This figure shows the IHO sea-area outlines, which come
  from IHO Sea Areas v3 under CC BY-NC-SA 4.0, so the figure inherits the
  non-commercial and share-alike conditions.
- **`figures/fig02_closure_zones_apparent_trawling_2026-10-05_11.png`** — CC BY
  4.0. It carries no IHO data. Basemap: Esri, TomTom, Garmin, FAO, NOAA, USGS,
  © OpenStreetMap contributors, GIS User Community.

The IHO shapefile itself is not redistributed here.

## Author

Analysis and cartography: Emem Archibong Ekong, November 2026.

AI assistance was used during this work, including in drafting this README, and is declared in full in the workflow document’s “AI use and checks” section, including the errors it introduced and what caught them. 

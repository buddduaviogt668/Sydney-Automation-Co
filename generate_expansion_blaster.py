import os
import re

# Read pristine masters
with open('c-bus-programmer-sydney.html', 'r', encoding='utf-8') as f:
    cbus_master = f.read()

with open('dynalite-programmer-sydney.html', 'r', encoding='utf-8') as f:
    dyn_master = f.read()

with open('automation-sydney.html', 'r', encoding='utf-8') as f:
    comm_master = f.read()

pages_data = [
    # Group 1: 4 Missing Regional Dynalite Hubs
    {
        "filename": "dynalite-programmer-hills-district.html",
        "type": "dyn",
        "sub_title": "Hills District",
        "title": "Signify Dynalite Programmer Hills District | Acreage Smart Home Specialists",
        "desc": "Accredited Signify Dynalite System Designers serving the Hills District. Specializing in expansive acreage estates, lighting control upgrades, and same-day fault finding. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Specializing in sprawling acreage smart homes and modern prestige estates across the Hills District. Based in Menai, we provide direct specialist same-day service without distributor delays.",
        "landmarks": "<p>We service premium residential acreage and modern luxury estates across the Hills District, providing expert automation support from Showground Road and Carrington Road to expansive properties along Old Northern Road and Memorial Avenue.</p>",
        "links": '<li><a href="/dynalite-programmer-castle-hill" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Castle Hill</a></li><li><a href="/dynalite-programmer-dural" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Dural</a></li><li><a href="/dynalite-programmer-bella-vista" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Bella Vista</a></li>'
    },
    {
        "filename": "dynalite-programmer-parramatta.html",
        "type": "dyn",
        "sub_title": "Parramatta",
        "title": "Signify Dynalite Programmer Parramatta | Commercial Tower Specialists",
        "desc": "Accredited Signify Dynalite Programmer Parramatta. Servicing commercial office towers, institutional facilities, and high-rise strata across Western Sydney. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Servicing commercial towers, institutional facilities, and high-rise strata across Parramatta Square and the Western Sydney growth corridor. Based in Menai, we provide rapid specialist response.",
        "landmarks": "<p>We provide specialized Dynalite support for commercial high-rises and institutional facilities across Parramatta, covering key precincts from Parramatta Square and Church Street to Victoria Road and the Westmead health corridor.</p>",
        "links": '<li><a href="/dynalite-programmer-penrith" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Penrith</a></li><li><a href="/dynalite-repair-silverwater" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Silverwater</a></li><li><a href="/lighting-control-sydney-olympic-park" style="color:#f07020;text-decoration:underline;">Lighting Control Sydney Olympic Park</a></li>'
    },
    {
        "filename": "dynalite-programmer-sydney-cbd.html",
        "type": "dyn",
        "sub_title": "Sydney CBD",
        "title": "Signify Dynalite Programmer Sydney CBD | Commercial &amp; Hospitality Strata",
        "desc": "Accredited Signify Dynalite System Designers serving Sydney CBD. Expert fault finding, boardroom automation, and architectural lighting control for commercial towers. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, boardroom automation, and architectural lighting control for commercial towers and hospitality venues across the Sydney CBD. Direct specialist same-day service.",
        "landmarks": "<p>We service premium commercial towers, executive boardrooms, and luxury hospitality venues across the Sydney CBD, providing dedicated support from Martin Place and George Street to Barangaroo and Circular Quay.</p>",
        "links": '<li><a href="/lighting-control-barangaroo" style="color:#f07020;text-decoration:underline;">Lighting Control Barangaroo</a></li><li><a href="/dynalite-programmer-darling-point" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Darling Point</a></li><li><a href="/hospitality-lighting-surry-hills" style="color:#f07020;text-decoration:underline;">Hospitality Lighting Surry Hills</a></li>'
    },
    {
        "filename": "dynalite-programmer-st-george.html",
        "type": "dyn",
        "sub_title": "St George",
        "title": "Signify Dynalite Programmer St George | Waterfront Strata &amp; Commercial",
        "desc": "Accredited Signify Dynalite Programmer St George. Servicing waterfront luxury apartments, commercial corridors, and architectural homes. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Servicing waterfront luxury apartments, commercial corridors, and architectural smart homes across the St George region. Based in Menai, we guarantee priority same-day response.",
        "landmarks": "<p>We provide expert Dynalite fault finding and system design across the St George region, supporting properties from the Princes Highway commercial corridor to waterfront enclaves along Grand Parade and Kogarah Bay.</p>",
        "links": '<li><a href="/dynalite-programmer-sutherland-shire" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Sutherland Shire</a></li><li><a href="/dynalite-programmer-cronulla" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Cronulla</a></li><li><a href="/c-bus-programmer-st-george" style="color:#f07020;text-decoration:underline;">C-Bus Programmer St George</a></li>'
    },

    # Group 2: Hills District & North West Prestige Acreage
    {
        "filename": "c-bus-programmer-castle-hill.html",
        "type": "cbus",
        "sub_title": "Castle Hill",
        "title": "C-Bus Programmer Castle Hill | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Castle Hill. Specializing in luxury residential estates, smart home upgrades, and same-day fault finding. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in luxury residential estates and modern smart home integration across Castle Hill. Based in Menai, we offer fixed-price programming and rapid fault finding.",
        "landmarks": "<p>We service premium residential properties and modern estates across Castle Hill, providing dedicated C-Bus support from Castle Street and Tuckwell Road to expansive homes along Showground Road and Old Northern Road.</p>",
        "links": '<li><a href="/dynalite-programmer-castle-hill" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Castle Hill</a></li><li><a href="/c-bus-programmer-dural" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Dural</a></li><li><a href="/c-bus-programmer-bella-vista" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Bella Vista</a></li>'
    },
    {
        "filename": "dynalite-programmer-castle-hill.html",
        "type": "dyn",
        "sub_title": "Castle Hill",
        "title": "Signify Dynalite Programmer Castle Hill | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Castle Hill. Specialist fault finding, architectural lighting repairs, and system integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Specialist fault finding, architectural lighting repairs, and advanced system integration for prestige properties across Castle Hill. Direct specialist same-day service.",
        "landmarks": "<p>We support high-end architectural smart homes across Castle Hill, delivering expert Dynalite solutions from the Gilbert Road residential precinct to luxury properties surrounding the Showground corridor.</p>",
        "links": '<li><a href="/c-bus-programmer-castle-hill" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Castle Hill</a></li><li><a href="/dynalite-programmer-dural" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Dural</a></li><li><a href="/dynalite-programmer-hills-district" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Hills District</a></li>'
    },
    {
        "filename": "c-bus-programmer-dural.html",
        "type": "cbus",
        "sub_title": "Dural",
        "title": "C-Bus Programmer Dural | Prestige Acreage Smart Home Specialist",
        "desc": "Accredited C-Bus Programmer Dural. Specializing in sprawling acreage smart homes, custom lighting control, and same-day fault finding. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in sprawling acreage smart homes and prestige country estates across Dural. Based in Menai, we provide expert same-day fault finding and custom system upgrades.",
        "landmarks": "<p>We service expansive acreage properties and luxury estates across Dural, providing comprehensive C-Bus automation support along Old Northern Road, New Line Road, and the surrounding prestige rural corridors.</p>",
        "links": '<li><a href="/dynalite-programmer-dural" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Dural</a></li><li><a href="/c-bus-programmer-castle-hill" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Castle Hill</a></li><li><a href="/c-bus-programmer-hills-district" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Hills District</a></li>'
    },
    {
        "filename": "dynalite-programmer-dural.html",
        "type": "dyn",
        "sub_title": "Dural",
        "title": "Signify Dynalite Programmer Dural | Acreage Lighting Control Specialists",
        "desc": "Accredited Signify Dynalite Programmer Dural. Expert fault finding, custom keypad programming, and lighting integration for luxury acreage. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, custom keypad programming, and architectural lighting integration for luxury acreage estates across Dural. Direct specialist same-day service.",
        "landmarks": "<p>We support prestige acreage smart homes across Dural, delivering expert Dynalite solutions from Kenthurst Road and Round Corner to expansive private properties throughout the Hills District rural fringe.</p>",
        "links": '<li><a href="/c-bus-programmer-dural" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Dural</a></li><li><a href="/dynalite-programmer-castle-hill" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Castle Hill</a></li><li><a href="/dynalite-programmer-hills-district" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Hills District</a></li>'
    },
    {
        "filename": "c-bus-programmer-bella-vista.html",
        "type": "cbus",
        "sub_title": "Bella Vista",
        "title": "C-Bus Programmer Bella Vista | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Bella Vista. Specializing in modern luxury mansions, waterside estates, and commercial integration. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in modern luxury mansions, waterside estates, and commercial integration across Bella Vista. Based in Menai, we provide rapid fault finding and fixed-price programming.",
        "landmarks": "<p>We service premium residential properties and commercial offices across Bella Vista, providing dedicated C-Bus support from Norwest Boulevard and Elizabeth Macarthur Drive to the exclusive waterside residential enclaves.</p>",
        "links": '<li><a href="/dynalite-programmer-bella-vista" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Bella Vista</a></li><li><a href="/lighting-control-norwest-commercial" style="color:#f07020;text-decoration:underline;">Lighting Control Norwest Commercial</a></li><li><a href="/c-bus-programmer-castle-hill" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Castle Hill</a></li>'
    },
    {
        "filename": "dynalite-programmer-bella-vista.html",
        "type": "dyn",
        "sub_title": "Bella Vista",
        "title": "Signify Dynalite Programmer Bella Vista | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Bella Vista. Expert fault finding, architectural lighting repairs, and commercial park integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, architectural lighting repairs, and advanced commercial park integration across Bella Vista. Direct specialist same-day service without distributor delays.",
        "landmarks": "<p>We support high-end residential mansions and commercial business park facilities across Bella Vista, delivering expert Dynalite solutions from Lexington Drive and Celebration Drive to the prestige residential sectors.</p>",
        "links": '<li><a href="/c-bus-programmer-bella-vista" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Bella Vista</a></li><li><a href="/lighting-control-norwest-commercial" style="color:#f07020;text-decoration:underline;">Lighting Control Norwest Commercial</a></li><li><a href="/dynalite-programmer-hills-district" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Hills District</a></li>'
    },
    {
        "filename": "lighting-control-norwest-commercial.html",
        "type": "comm",
        "sub_title": "Norwest Commercial",
        "title": "Lighting Control Norwest Commercial | Building Automation &amp; Repairs",
        "desc": "Specialist lighting control upgrades, DALI maintenance, and Dynalite/C-Bus repairs for commercial towers and business parks in Norwest. Call 0422 469 739.",
        "lead": "Accredited Building Automation Specialists. Providing specialist lighting control upgrades, DALI maintenance, and rapid Dynalite/C-Bus repairs for commercial towers and corporate headquarters across Norwest Business Park.",
        "landmarks": "<p>We service commercial high-rises, corporate centers, and business park facilities across Norwest, delivering expert lighting automation support along Norwest Boulevard, Brookhollow Avenue, and Solent Circuit.</p>",
        "links": '<li><a href="/dynalite-programmer-bella-vista" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Bella Vista</a></li><li><a href="/c-bus-programmer-bella-vista" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Bella Vista</a></li><li><a href="/dynalite-programmer-hills-district" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Hills District</a></li>'
    },

    # Group 3: Western Sydney & Industrial Corridors
    {
        "filename": "c-bus-programmer-penrith.html",
        "type": "cbus",
        "sub_title": "Penrith",
        "title": "C-Bus Programmer Penrith | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Penrith. Servicing institutional facilities, commercial corridors, and residential growth areas. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Servicing institutional facilities, commercial corridors, and modern residential growth areas across Penrith. Based in Menai, we provide rapid fault finding and system upgrades.",
        "landmarks": "<p>We provide specialized C-Bus support for commercial centers and institutional facilities across Penrith, covering key precincts from Mulgoa Road and High Street to the Nepean river residential developments.</p>",
        "links": '<li><a href="/dynalite-programmer-penrith" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Penrith</a></li><li><a href="/c-bus-programmer-parramatta" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Parramatta</a></li><li><a href="/cbus-repair-wetherill-park-industrial" style="color:#f07020;text-decoration:underline;">C-Bus Repair Wetherill Park Industrial</a></li>'
    },
    {
        "filename": "dynalite-programmer-penrith.html",
        "type": "dyn",
        "sub_title": "Penrith",
        "title": "Signify Dynalite Programmer Penrith | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Penrith. Expert fault finding, commercial lighting control repairs, and institutional integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, commercial lighting control repairs, and advanced institutional integration across Penrith. Direct specialist same-day service.",
        "landmarks": "<p>We support commercial and educational smart facilities across Penrith, delivering expert Dynalite solutions from Jamison Road and the central business district to expanding commercial sectors along the Great Western Highway.</p>",
        "links": '<li><a href="/c-bus-programmer-penrith" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Penrith</a></li><li><a href="/dynalite-programmer-parramatta" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Parramatta</a></li><li><a href="/dynalite-repair-silverwater" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Silverwater</a></li>'
    },
    {
        "filename": "cbus-repair-wetherill-park-industrial.html",
        "type": "cbus",
        "sub_title": "Wetherill Park Industrial",
        "title": "C-Bus Repair Wetherill Park Industrial | Warehouse Lighting Relays",
        "desc": "Specialist C-Bus repair for heavy industrial facilities, warehousing lighting relays, and manufacturing plants in Wetherill Park. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Providing specialist C-Bus repair for heavy industrial facilities, warehousing lighting relays, and large manufacturing plants across Wetherill Park. Same-day commercial response.",
        "landmarks": "<p>We service major industrial facilities, logistics hubs, and manufacturing plants across Wetherill Park, providing heavy-duty C-Bus automation support along Victoria Street, Cowpasture Road, and Elizabeth Street.</p>",
        "links": '<li><a href="/dynalite-repair-silverwater" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Silverwater</a></li><li><a href="/c-bus-programmer-parramatta" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Parramatta</a></li><li><a href="/c-bus-programmer-penrith" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Penrith</a></li>'
    },
    {
        "filename": "dynalite-repair-silverwater.html",
        "type": "dyn",
        "sub_title": "Silverwater",
        "title": "Signify Dynalite Repair Silverwater | Logistics &amp; Distribution Lighting",
        "desc": "Expert Signify Dynalite repair for logistics centers, distribution warehouses, and commercial facilities in Silverwater. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Providing expert Dynalite repair and lighting control maintenance for logistics centers, distribution warehouses, and commercial facilities across Silverwater. Priority response.",
        "landmarks": "<p>We support major logistics centers and distribution facilities across Silverwater, delivering expert Dynalite lighting control solutions from Silverwater Road and Derby Street to the surrounding central industrial corridors.</p>",
        "links": '<li><a href="/cbus-repair-wetherill-park-industrial" style="color:#f07020;text-decoration:underline;">C-Bus Repair Wetherill Park Industrial</a></li><li><a href="/dynalite-programmer-parramatta" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Parramatta</a></li><li><a href="/lighting-control-sydney-olympic-park" style="color:#f07020;text-decoration:underline;">Lighting Control Sydney Olympic Park</a></li>'
    },
    {
        "filename": "lighting-control-sydney-olympic-park.html",
        "type": "comm",
        "sub_title": "Sydney Olympic Park",
        "title": "Lighting Control Sydney Olympic Park | Commercial Venue Automation",
        "desc": "Specialist lighting control upgrades, DALI maintenance, and Dynalite/C-Bus repairs for commercial venues in Sydney Olympic Park. Call 0422 469 739.",
        "lead": "Accredited Building Automation Specialists. Providing specialist lighting control upgrades, DALI maintenance, and rapid Dynalite/C-Bus repairs for commercial venues, hotels, and infrastructure across Sydney Olympic Park.",
        "landmarks": "<p>We service major commercial venues, hotels, and corporate offices across Sydney Olympic Park, delivering expert lighting automation support along Herb Elliott Avenue, Australia Avenue, and Olympic Boulevard.</p>",
        "links": '<li><a href="/dynalite-repair-silverwater" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Silverwater</a></li><li><a href="/dynalite-programmer-parramatta" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Parramatta</a></li><li><a href="/c-bus-programmer-parramatta" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Parramatta</a></li>'
    },

    # Group 4: Sutherland Shire Expansion
    {
        "filename": "dynalite-programmer-caringbah.html",
        "type": "dyn",
        "sub_title": "Caringbah",
        "title": "Signify Dynalite Programmer Caringbah | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Caringbah. Expert fault finding, commercial lighting repairs, and luxury residential integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, commercial lighting repairs, and luxury residential integration across Caringbah. Based locally in Menai, we provide rapid same-day service.",
        "landmarks": "<p>We support commercial zones and luxury residential builds across Caringbah, delivering expert Dynalite solutions from Taren Point Road and the central commercial precinct to the surrounding waterside residential avenues.</p>",
        "links": '<li><a href="/c-bus-programmer-caringbah" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Caringbah</a></li><li><a href="/dynalite-programmer-caringbah-south" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Caringbah South</a></li><li><a href="/c-bus-programmer-miranda" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Miranda</a></li>'
    },
    {
        "filename": "dynalite-programmer-engadine.html",
        "type": "dyn",
        "sub_title": "Engadine",
        "title": "Signify Dynalite Programmer Engadine | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Engadine. Specialist fault finding, architectural lighting repairs, and system integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Specialist fault finding, architectural lighting repairs, and advanced system integration for established properties across Engadine. Based in Menai, we guarantee rapid response.",
        "landmarks": "<p>We service established residential properties and community hubs across Engadine, providing dedicated Dynalite support from Old Bush Road and the Princes Highway commercial center to the surrounding leafy residential sectors.</p>",
        "links": '<li><a href="/c-bus-programmer-engadine" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Engadine</a></li><li><a href="/dynalite-programmer-sutherland-shire" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Sutherland Shire</a></li><li><a href="/c-bus-dynalite-menai" style="color:#f07020;text-decoration:underline;">C-Bus &amp; Dynalite Menai</a></li>'
    },
    {
        "filename": "c-bus-programmer-miranda.html",
        "type": "cbus",
        "sub_title": "Miranda",
        "title": "C-Bus Programmer Miranda | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Miranda. Specializing in commercial retail hubs, high-rise strata, and residential smart homes. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in commercial retail hubs, high-rise strata, and residential smart homes across Miranda. Based locally in Menai, we offer fixed-price programming and rapid fault finding.",
        "landmarks": "<p>We provide specialized C-Bus support for commercial centers and residential complexes across Miranda, covering key precincts from Kingsway and Wandella Road to the bustling central retail and medical corridors.</p>",
        "links": '<li><a href="/c-bus-programmer-caringbah" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Caringbah</a></li><li><a href="/c-bus-programmer-sutherland-shire" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Sutherland Shire</a></li><li><a href="/c-bus-programmer-gymea-bay" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Gymea Bay</a></li>'
    },
    {
        "filename": "c-bus-programmer-sylvania.html",
        "type": "cbus",
        "sub_title": "Sylvania",
        "title": "C-Bus Programmer Sylvania | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Sylvania. Specializing in waterfront luxury homes, strata complexes, and smart home upgrades. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in waterfront luxury homes, strata complexes, and modern smart home integration across Sylvania. Based locally in Menai, we provide same-day fault finding.",
        "landmarks": "<p>We service premium waterfront properties and strata complexes across Sylvania, providing dedicated C-Bus support from Belgrave Esplanade and Princes Highway to the exclusive residential enclaves along Sylvania Waters.</p>",
        "links": '<li><a href="/dynalite-programmer-sylvania" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Sylvania</a></li><li><a href="/c-bus-programmer-miranda" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Miranda</a></li><li><a href="/c-bus-programmer-sutherland-shire" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Sutherland Shire</a></li>'
    },
    {
        "filename": "dynalite-programmer-sylvania.html",
        "type": "dyn",
        "sub_title": "Sylvania",
        "title": "Signify Dynalite Programmer Sylvania | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Sylvania. Expert fault finding, architectural lighting repairs, and waterside integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, architectural lighting repairs, and advanced waterside integration for prestige properties across Sylvania. Based locally in Menai, we guarantee rapid response.",
        "landmarks": "<p>We support high-end architectural smart homes across Sylvania, delivering expert Dynalite solutions from Evelyn Street and Port Hacking Road to the luxury waterfront properties surrounding the Georges River.</p>",
        "links": '<li><a href="/c-bus-programmer-sylvania" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Sylvania</a></li><li><a href="/dynalite-programmer-caringbah" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Caringbah</a></li><li><a href="/dynalite-programmer-sutherland-shire" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Sutherland Shire</a></li>'
    },
    {
        "filename": "c-bus-programmer-illawong.html",
        "type": "cbus",
        "sub_title": "Illawong",
        "title": "C-Bus Programmer Illawong | Prestige Waterfront Smart Home Specialist",
        "desc": "Accredited C-Bus Programmer Illawong. Specializing in prestige waterfront smart homes, custom lighting control, and same-day fault finding. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in prestige waterfront smart homes and expansive automated estates across Illawong. Based locally in Menai, we provide expert same-day fault finding and custom system upgrades.",
        "landmarks": "<p>We service expansive waterfront properties and luxury estates across Illawong, providing comprehensive C-Bus automation support along Fowler Road, Hobart Place, and the surrounding prestige riverfront enclaves.</p>",
        "links": '<li><a href="/dynalite-programmer-illawong" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Illawong</a></li><li><a href="/c-bus-dynalite-menai" style="color:#f07020;text-decoration:underline;">C-Bus &amp; Dynalite Menai</a></li><li><a href="/c-bus-programmer-sutherland-shire" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Sutherland Shire</a></li>'
    },
    {
        "filename": "dynalite-programmer-illawong.html",
        "type": "dyn",
        "sub_title": "Illawong",
        "title": "Signify Dynalite Programmer Illawong | Acreage &amp; Waterfront Specialists",
        "desc": "Accredited Signify Dynalite Programmer Illawong. Expert fault finding, custom keypad programming, and lighting integration for luxury homes. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, custom keypad programming, and architectural lighting integration for luxury waterfront estates across Illawong. Based locally in Menai, we offer rapid response.",
        "landmarks": "<p>We support prestige waterfront smart homes across Illawong, delivering expert Dynalite solutions from Cranbrook Place and Hobart Place to expansive private properties bordering Barden Ridge and the Georges River.</p>",
        "links": '<li><a href="/c-bus-programmer-illawong" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Illawong</a></li><li><a href="/c-bus-dynalite-menai" style="color:#f07020;text-decoration:underline;">C-Bus &amp; Dynalite Menai</a></li><li><a href="/dynalite-programmer-sutherland-shire" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Sutherland Shire</a></li>'
    },

    # Group 5: Eastern Suburbs & City Enclaves
    {
        "filename": "c-bus-programmer-paddington.html",
        "type": "cbus",
        "sub_title": "Paddington",
        "title": "C-Bus Programmer Paddington | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Paddington. Specializing in heritage terrace retrofits, boutique retail, and smart home upgrades. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in heritage terrace retrofits, boutique retail, and modern smart home integration across Paddington. Based in Menai, we provide rapid fault finding and fixed-price programming.",
        "landmarks": "<p>We service premium heritage terraces and boutique commercial spaces across Paddington, providing dedicated C-Bus support from Oxford Street and William Street to the exclusive residential enclaves along Underwood Street and Jersey Road.</p>",
        "links": '<li><a href="/dynalite-programmer-paddington" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Paddington</a></li><li><a href="/c-bus-programmer-woollahra" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Woollahra</a></li><li><a href="/c-bus-programmer-eastern-suburbs" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Eastern Suburbs</a></li>'
    },
    {
        "filename": "dynalite-programmer-paddington.html",
        "type": "dyn",
        "sub_title": "Paddington",
        "title": "Signify Dynalite Programmer Paddington | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Paddington. Expert fault finding, architectural lighting repairs, and gallery integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, architectural lighting repairs, and advanced gallery integration for prestige properties across Paddington. Direct specialist same-day service.",
        "landmarks": "<p>We support high-end architectural renovations and multi-level galleries across Paddington, delivering expert Dynalite solutions from Hargrave Street and Cascade Street to luxury properties throughout the art precinct.</p>",
        "links": '<li><a href="/c-bus-programmer-paddington" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Paddington</a></li><li><a href="/dynalite-programmer-woollahra" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Woollahra</a></li><li><a href="/dynalite-programmer-eastern-suburbs" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Eastern Suburbs</a></li>'
    },
    {
        "filename": "c-bus-programmer-potts-point.html",
        "type": "cbus",
        "sub_title": "Potts Point",
        "title": "C-Bus Programmer Potts Point | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Potts Point. Specializing in prestige high-rise strata, art deco apartments, and luxury penthouses. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in prestige high-rise strata, art deco apartments, and luxury penthouses across Potts Point. Based in Menai, we provide rapid fault finding and fixed-price programming.",
        "landmarks": "<p>We service premium strata complexes and luxury penthouses across Potts Point, providing dedicated C-Bus support from Macleay Street and Victoria Street to the exclusive residential enclaves overlooking Woolloomooloo Bay.</p>",
        "links": '<li><a href="/dynalite-programmer-darling-point" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Darling Point</a></li><li><a href="/c-bus-programmer-double-bay" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Double Bay</a></li><li><a href="/c-bus-programmer-sydney-cbd" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Sydney CBD</a></li>'
    },
    {
        "filename": "dynalite-programmer-darling-point.html",
        "type": "dyn",
        "sub_title": "Darling Point",
        "title": "Signify Dynalite Programmer Darling Point | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Darling Point. Expert fault finding, architectural lighting repairs, and harborfront integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, architectural lighting repairs, and advanced harborfront integration for ultra-luxury estates across Darling Point. Direct specialist same-day service.",
        "landmarks": "<p>We support ultra-luxury harborfront estates and prestige residential towers across Darling Point, delivering expert Dynalite solutions from Mona Road and New Beach Road to exclusive private waterfront properties.</p>",
        "links": '<li><a href="/c-bus-programmer-potts-point" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Potts Point</a></li><li><a href="/dynalite-programmer-double-bay" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Double Bay</a></li><li><a href="/dynalite-programmer-eastern-suburbs" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Eastern Suburbs</a></li>'
    },
    {
        "filename": "hospitality-lighting-surry-hills.html",
        "type": "comm",
        "sub_title": "Surry Hills Hospitality",
        "title": "Hospitality Lighting Surry Hills | Boutique Hotel &amp; Venue Automation",
        "desc": "Specialist lighting control upgrades, DALI maintenance, and Dynalite/C-Bus repairs for boutique hotels and venues in Surry Hills. Call 0422 469 739.",
        "lead": "Accredited Building Automation Specialists. Providing specialist lighting control upgrades, DALI maintenance, and rapid Dynalite/C-Bus repairs for boutique hotels, restaurants, and creative agencies across Surry Hills.",
        "landmarks": "<p>We service boutique hospitality venues, dining precincts, and commercial creative spaces across Surry Hills, delivering expert lighting automation support along Crown Street, Foveaux Street, and Campbell Street.</p>",
        "links": '<li><a href="/c-bus-programmer-sydney-cbd" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Sydney CBD</a></li><li><a href="/dynalite-programmer-sydney-cbd" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Sydney CBD</a></li><li><a href="/c-bus-programmer-paddington" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Paddington</a></li>'
    },
    {
        "filename": "lighting-control-barangaroo.html",
        "type": "comm",
        "sub_title": "Barangaroo Commercial",
        "title": "Lighting Control Barangaroo | Commercial Tower Automation",
        "desc": "Specialist lighting control upgrades, DALI maintenance, and Dynalite/C-Bus repairs for commercial towers in Barangaroo. Call 0422 469 739.",
        "lead": "Accredited Building Automation Specialists. Providing specialist lighting control upgrades, DALI maintenance, and rapid Dynalite/C-Bus repairs for premium commercial towers and waterfront dining precincts across Barangaroo.",
        "landmarks": "<p>We service commercial high-rises, corporate centers, and waterfront hospitality venues across Barangaroo, delivering expert lighting automation support along Hickson Road, Avenue of Americas, and the waterfront promenade.</p>",
        "links": '<li><a href="/dynalite-programmer-sydney-cbd" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Sydney CBD</a></li><li><a href="/c-bus-programmer-sydney-cbd" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Sydney CBD</a></li><li><a href="/dynalite-programmer-parramatta" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Parramatta</a></li>'
    },
    {
        "filename": "dynalite-programmer-tamarama.html",
        "type": "dyn",
        "sub_title": "Tamarama",
        "title": "Signify Dynalite Programmer Tamarama | Cliffside Lighting Specialists",
        "desc": "Accredited Signify Dynalite Programmer Tamarama. Expert fault finding, custom keypad programming, and lighting integration for luxury coastal homes. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, custom keypad programming, and architectural lighting integration for cliffside luxury homes across Tamarama. Direct specialist same-day service.",
        "landmarks": "<p>We support prestige coastal smart homes across Tamarama, delivering expert Dynalite solutions from Fletcher Street and Tamarama Marine Drive to expansive private properties overlooking the beach and coastal walk.</p>",
        "links": '<li><a href="/cbus-repair-tamarama" style="color:#f07020;text-decoration:underline;">C-Bus Repair Tamarama</a></li><li><a href="/dynalite-programmer-bronte" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Bronte</a></li><li><a href="/dynalite-programmer-bondi" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Bondi</a></li>'
    },

    # Group 6: North Shore & Waterfront Gaps
    {
        "filename": "c-bus-programmer-north-sydney.html",
        "type": "cbus",
        "sub_title": "North Sydney",
        "title": "C-Bus Programmer North Sydney | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer North Sydney. Servicing commercial office towers, executive strata, and boardroom automation. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Servicing commercial office towers, executive strata, and boardroom automation across North Sydney. Based in Menai, we provide rapid fault finding and system upgrades.",
        "landmarks": "<p>We provide specialized C-Bus support for commercial high-rises and executive complexes across North Sydney, covering key precincts from Miller Street and Pacific Highway to the bustling central business district.</p>",
        "links": '<li><a href="/dynalite-programmer-north-sydney" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer North Sydney</a></li><li><a href="/dynalite-programmer-kirribilli" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Kirribilli</a></li><li><a href="/c-bus-programmer-neutral-bay" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Neutral Bay</a></li>'
    },
    {
        "filename": "dynalite-programmer-north-sydney.html",
        "type": "dyn",
        "sub_title": "North Sydney",
        "title": "Signify Dynalite Programmer North Sydney | Commercial Tower Specialists",
        "desc": "Accredited Signify Dynalite Programmer North Sydney. Expert fault finding, commercial lighting control repairs, and corporate integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, commercial lighting control repairs, and advanced corporate boardroom integration across North Sydney. Direct specialist same-day service.",
        "landmarks": "<p>We support commercial towers and corporate facilities across North Sydney, delivering expert Dynalite solutions from Berry Street and Walker Street to expanding commercial sectors along the Mount Street corridor.</p>",
        "links": '<li><a href="/c-bus-programmer-north-sydney" style="color:#f07020;text-decoration:underline;">C-Bus Programmer North Sydney</a></li><li><a href="/dynalite-programmer-sydney-cbd" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Sydney CBD</a></li><li><a href="/dynalite-programmer-north-shore" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer North Shore</a></li>'
    },
    {
        "filename": "dynalite-programmer-kirribilli.html",
        "type": "dyn",
        "sub_title": "Kirribilli",
        "title": "Signify Dynalite Programmer Kirribilli | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Kirribilli. Expert fault finding, architectural lighting repairs, and waterfront integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, architectural lighting repairs, and advanced waterfront integration for prestige properties across Kirribilli. Direct specialist same-day service.",
        "landmarks": "<p>We support high-end waterfront apartments and historic residences across Kirribilli, delivering expert Dynalite solutions from Broughton Street and Carabella Street to luxury properties surrounding the harbor foreshore.</p>",
        "links": '<li><a href="/cbus-repair-kirribilli" style="color:#f07020;text-decoration:underline;">C-Bus Repair Kirribilli</a></li><li><a href="/dynalite-programmer-north-sydney" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer North Sydney</a></li><li><a href="/c-bus-programmer-kurraba-point" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Kurraba Point</a></li>'
    },
    {
        "filename": "c-bus-programmer-kurraba-point.html",
        "type": "cbus",
        "sub_title": "Kurraba Point",
        "title": "C-Bus Programmer Kurraba Point | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Kurraba Point. Specializing in luxury harborfront estates, boutique strata, and smart home upgrades. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in luxury harborfront estates, boutique strata, and modern smart home integration across Kurraba Point. Based in Menai, we provide rapid fault finding and fixed-price programming.",
        "landmarks": "<p>We service premium harborfront properties and boutique strata complexes across Kurraba Point, providing dedicated C-Bus support from Kurraba Road and Wycombe Road to exclusive residential enclaves along the peninsula.</p>",
        "links": '<li><a href="/dynalite-programmer-kirribilli" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Kirribilli</a></li><li><a href="/c-bus-programmer-neutral-bay" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Neutral Bay</a></li><li><a href="/c-bus-programmer-cremorne" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Cremorne</a></li>'
    },
    {
        "filename": "c-bus-programmer-hunters-hill.html",
        "type": "cbus",
        "sub_title": "Hunters Hill",
        "title": "C-Bus Programmer Hunters Hill | Prestige Waterfront Smart Home Specialist",
        "desc": "Accredited C-Bus Programmer Hunters Hill. Specializing in peninsula sandstone mansions, waterfront estates, and same-day fault finding. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in peninsula sandstone mansions, waterfront estates, and modern smart home integration across Hunters Hill. Based in Menai, we provide expert same-day fault finding.",
        "landmarks": "<p>We service expansive waterfront properties and historic sandstone mansions across Hunters Hill, providing comprehensive C-Bus automation support along Alexandra Street, Woolwich Road, and the surrounding prestige peninsula corridors.</p>",
        "links": '<li><a href="/dynalite-programmer-hunters-hill" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Hunters Hill</a></li><li><a href="/c-bus-programmer-drummoyne" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Drummoyne</a></li><li><a href="/c-bus-programmer-north-shore" style="color:#f07020;text-decoration:underline;">C-Bus Programmer North Shore</a></li>'
    },
    {
        "filename": "dynalite-programmer-hunters-hill.html",
        "type": "dyn",
        "sub_title": "Hunters Hill",
        "title": "Signify Dynalite Programmer Hunters Hill | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Hunters Hill. Expert fault finding, architectural lighting repairs, and heritage integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, architectural lighting repairs, and advanced heritage integration for prestige properties across Hunters Hill. Direct specialist same-day service.",
        "landmarks": "<p>We support prestige riverfront smart homes and historic estates across Hunters Hill, delivering expert Dynalite solutions from Ferry Street and Ernest Street to expansive private properties along the Lane Cove and Parramatta rivers.</p>",
        "links": '<li><a href="/c-bus-programmer-hunters-hill" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Hunters Hill</a></li><li><a href="/dynalite-programmer-drummoyne" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Drummoyne</a></li><li><a href="/dynalite-programmer-north-shore" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer North Shore</a></li>'
    },
    {
        "filename": "dynalite-programmer-pymble.html",
        "type": "dyn",
        "sub_title": "Pymble",
        "title": "Signify Dynalite Programmer Pymble | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Pymble. Expert fault finding, architectural lighting repairs, and luxury estate integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, architectural lighting repairs, and advanced luxury estate integration across Pymble. Direct specialist same-day service without distributor delays.",
        "landmarks": "<p>We support high-end residential estates and private grounds across Pymble, delivering expert Dynalite solutions from Telegraph Road and Mona Vale Road to prestige properties throughout the Upper North Shore.</p>",
        "links": '<li><a href="/c-bus-programmer-pymble" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Pymble</a></li><li><a href="/dynalite-programmer-turramurra" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Turramurra</a></li><li><a href="/dynalite-programmer-gordon" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Gordon</a></li>'
    },

    # Group 7: Northern Beaches & Inner West
    {
        "filename": "c-bus-programmer-curl-curl.html",
        "type": "cbus",
        "sub_title": "Curl Curl",
        "title": "C-Bus Programmer Curl Curl | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Curl Curl. Specializing in coastal luxury builds, beachfront smart homes, and same-day fault finding. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in coastal luxury builds, beachfront smart homes, and modern smart home integration across Curl Curl. Based in Menai, we provide rapid fault finding and fixed-price programming.",
        "landmarks": "<p>We service premium beachfront properties and modern architectural builds across Curl Curl, providing dedicated C-Bus support from Carrington Parade and Adams Street to exclusive residential enclaves overlooking the ocean.</p>",
        "links": '<li><a href="/c-bus-programmer-freshwater" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Freshwater</a></li><li><a href="/c-bus-programmer-queenscliff" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Queenscliff</a></li><li><a href="/c-bus-programmer-northern-beaches" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Northern Beaches</a></li>'
    },
    {
        "filename": "c-bus-programmer-queenscliff.html",
        "type": "cbus",
        "sub_title": "Queenscliff",
        "title": "C-Bus Programmer Queenscliff | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Queenscliff. Specializing in cliffside luxury apartments, panoramic residences, and smart home upgrades. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in cliffside luxury apartments, panoramic residences, and modern smart home integration across Queenscliff. Based in Menai, we provide rapid fault finding and fixed-price programming.",
        "landmarks": "<p>We service premium cliffside apartments and luxury residences across Queenscliff, providing dedicated C-Bus support from Queenscliff Road and Pavilion Street to exclusive properties overlooking Manly Beach and the lagoon.</p>",
        "links": '<li><a href="/c-bus-programmer-manly" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Manly</a></li><li><a href="/c-bus-programmer-curl-curl" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Curl Curl</a></li><li><a href="/c-bus-programmer-freshwater" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Freshwater</a></li>'
    },
    {
        "filename": "dynalite-programmer-bayview.html",
        "type": "dyn",
        "sub_title": "Bayview",
        "title": "Signify Dynalite Programmer Bayview | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Bayview. Expert fault finding, architectural lighting repairs, and Pittwater waterfront integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, architectural lighting repairs, and advanced Pittwater waterfront integration for prestige properties across Bayview. Direct specialist same-day service.",
        "landmarks": "<p>We support prestige waterfront smart homes and expansive hillside estates across Bayview, delivering expert Dynalite solutions from Pittwater Road and Cabarita Road to luxury private properties overlooking the marina.</p>",
        "links": '<li><a href="/cbus-repair-bayview" style="color:#f07020;text-decoration:underline;">C-Bus Repair Bayview</a></li><li><a href="/dynalite-programmer-mona-vale" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Mona Vale</a></li><li><a href="/dynalite-programmer-newport" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Newport</a></li>'
    },
    {
        "filename": "c-bus-programmer-cabarita.html",
        "type": "cbus",
        "sub_title": "Cabarita",
        "title": "C-Bus Programmer Cabarita | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Cabarita. Specializing in premium waterfront strata, parkside luxury homes, and smart home upgrades. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in premium waterfront strata, parkside luxury homes, and modern smart home integration across Cabarita. Based in Menai, we provide rapid fault finding and fixed-price programming.",
        "landmarks": "<p>We service premium waterfront properties and luxury strata complexes across Cabarita, providing dedicated C-Bus support from Cabarita Road and Kendall Inlet to exclusive residential enclaves surrounding the parklands.</p>",
        "links": '<li><a href="/c-bus-programmer-abbotsford" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Abbotsford</a></li><li><a href="/c-bus-programmer-drummoyne" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Drummoyne</a></li><li><a href="/c-bus-programmer-inner-west" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Inner West</a></li>'
    },
    {
        "filename": "c-bus-programmer-abbotsford.html",
        "type": "cbus",
        "sub_title": "Abbotsford",
        "title": "C-Bus Programmer Abbotsford | Accredited Clipsal Specialist",
        "desc": "Accredited C-Bus Programmer Abbotsford. Specializing in peninsula waterfront properties, boating enclaves, and smart home upgrades. Call 0422 469 739.",
        "lead": "Accredited C-Bus Programmers. Specializing in peninsula waterfront properties, boating enclaves, and modern smart home integration across Abbotsford. Based in Menai, we provide rapid fault finding and fixed-price programming.",
        "landmarks": "<p>We service premium waterfront properties and luxury boating enclaves across Abbotsford, providing dedicated C-Bus support from Great North Road and Blackwall Point Road to exclusive properties along the Parramatta River.</p>",
        "links": '<li><a href="/c-bus-programmer-cabarita" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Cabarita</a></li><li><a href="/c-bus-programmer-drummoyne" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Drummoyne</a></li><li><a href="/c-bus-programmer-inner-west" style="color:#f07020;text-decoration:underline;">C-Bus Programmer Inner West</a></li>'
    },
    {
        "filename": "dynalite-programmer-annandale.html",
        "type": "dyn",
        "sub_title": "Annandale",
        "title": "Signify Dynalite Programmer Annandale | System Design &amp; Repairs",
        "desc": "Accredited Signify Dynalite Programmer Annandale. Expert fault finding, architectural lighting repairs, and heritage warehouse integration. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Expert fault finding, architectural lighting repairs, and advanced heritage warehouse integration across Annandale. Direct specialist same-day service.",
        "landmarks": "<p>We support expansive heritage restorations and modern warehouse conversions across Annandale, delivering expert Dynalite solutions from Johnston Street and Booth Street to luxury properties throughout the Inner West.</p>",
        "links": '<li><a href="/dynalite-programmer-balmain" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Balmain</a></li><li><a href="/dynalite-programmer-drummoyne" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Drummoyne</a></li><li><a href="/dynalite-programmer-inner-west" style="color:#f07020;text-decoration:underline;">Signify Dynalite Programmer Inner West</a></li>'
    },

    # Group 8: Regional NSW Dynalite Equivalents
    {
        "filename": "dynalite-repair-bowral.html",
        "type": "dyn",
        "sub_title": "Bowral",
        "title": "Signify Dynalite Repair Bowral | Southern Highlands Country Estates",
        "desc": "Expert Signify Dynalite repair for luxury country estates, boutique hospitality venues, and architectural homes in Bowral. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Providing expert Dynalite repair and lighting control maintenance for luxury country estates, boutique hospitality venues, and architectural homes across Bowral. Priority response.",
        "landmarks": "<p>We support prestige country smart homes and boutique venues across Bowral, delivering expert Dynalite lighting control solutions from Bong Bong Street and Kangaloon Road to expansive private properties throughout the Southern Highlands.</p>",
        "links": '<li><a href="/cbus-repair-bowral" style="color:#f07020;text-decoration:underline;">C-Bus Repair Bowral</a></li><li><a href="/dynalite-repair-burradoo" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Burradoo</a></li><li><a href="/dynalite-repair-mittagong" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Mittagong</a></li>'
    },
    {
        "filename": "dynalite-repair-burradoo.html",
        "type": "dyn",
        "sub_title": "Burradoo",
        "title": "Signify Dynalite Repair Burradoo | Prestige Acreage Lighting",
        "desc": "Expert Signify Dynalite repair for prestige Southern Highlands acreage, architectural manors, and luxury estates in Burradoo. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Providing expert Dynalite repair and lighting control maintenance for prestige Southern Highlands acreage, architectural manors, and luxury estates across Burradoo. Priority response.",
        "landmarks": "<p>We support prestige acreage smart homes and architectural manors across Burradoo, delivering expert Dynalite lighting control solutions from Moss Vale Road and Werrington Street to expansive private properties in the Southern Highlands.</p>",
        "links": '<li><a href="/cbus-repair-burradoo" style="color:#f07020;text-decoration:underline;">C-Bus Repair Burradoo</a></li><li><a href="/dynalite-repair-bowral" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Bowral</a></li><li><a href="/dynalite-repair-mittagong" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Mittagong</a></li>'
    },
    {
        "filename": "dynalite-repair-mittagong.html",
        "type": "dyn",
        "sub_title": "Mittagong",
        "title": "Signify Dynalite Repair Mittagong | Southern Highlands Lighting",
        "desc": "Expert Signify Dynalite repair for historic Southern Highlands properties, commercial gateways, and architectural homes in Mittagong. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Providing expert Dynalite repair and lighting control maintenance for historic Southern Highlands properties, commercial gateways, and architectural homes across Mittagong. Priority response.",
        "landmarks": "<p>We support historic smart homes and commercial gateways across Mittagong, delivering expert Dynalite lighting control solutions from Old Hume Highway and Bowral Road to expansive private properties throughout the Northern Highlands.</p>",
        "links": '<li><a href="/cbus-repair-mittagong" style="color:#f07020;text-decoration:underline;">C-Bus Repair Mittagong</a></li><li><a href="/dynalite-repair-bowral" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Bowral</a></li><li><a href="/dynalite-repair-burradoo" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Burradoo</a></li>'
    },
    {
        "filename": "dynalite-repair-wollongong.html",
        "type": "dyn",
        "sub_title": "Wollongong",
        "title": "Signify Dynalite Repair Wollongong | Illawarra Coastal Strata",
        "desc": "Expert Signify Dynalite repair for Illawarra coastal high-rise strata, commercial centers, and architectural homes in Wollongong. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Providing expert Dynalite repair and lighting control maintenance for Illawarra coastal high-rise strata, commercial centers, and architectural homes across Wollongong. Priority response.",
        "landmarks": "<p>We support major commercial centers and coastal strata complexes across Wollongong, delivering expert Dynalite lighting control solutions from Crown Street and Cliff Road to the surrounding central business and coastal corridors.</p>",
        "links": '<li><a href="/dynalite-repair-thirroul" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Thirroul</a></li><li><a href="/dynalite-repair-kiama" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Kiama</a></li><li><a href="/cbus-repair-thirroul" style="color:#f07020;text-decoration:underline;">C-Bus Repair Thirroul</a></li>'
    },
    {
        "filename": "dynalite-repair-thirroul.html",
        "type": "dyn",
        "sub_title": "Thirroul",
        "title": "Signify Dynalite Repair Thirroul | Illawarra Coastal Lighting",
        "desc": "Expert Signify Dynalite repair for northern Illawarra luxury coastal homes, cliffside builds, and architectural manors in Thirroul. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Providing expert Dynalite repair and lighting control maintenance for northern Illawarra luxury coastal homes, cliffside builds, and architectural manors across Thirroul. Priority response.",
        "landmarks": "<p>We support prestige coastal smart homes across Thirroul, delivering expert Dynalite lighting control solutions from Lawrence Hargrave Drive and Bath Street to expansive private properties overlooking the northern Illawarra coastline.</p>",
        "links": '<li><a href="/cbus-repair-thirroul" style="color:#f07020;text-decoration:underline;">C-Bus Repair Thirroul</a></li><li><a href="/dynalite-repair-wollongong" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Wollongong</a></li><li><a href="/dynalite-repair-kiama" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Kiama</a></li>'
    },
    {
        "filename": "dynalite-repair-kiama.html",
        "type": "dyn",
        "sub_title": "Kiama",
        "title": "Signify Dynalite Repair Kiama | South Coast Luxury Retreats",
        "desc": "Expert Signify Dynalite repair for South Coast luxury retreats, boutique hospitality venues, and architectural homes in Kiama. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Providing expert Dynalite repair and lighting control maintenance for South Coast luxury retreats, boutique hospitality venues, and architectural homes across Kiama. Priority response.",
        "landmarks": "<p>We support prestige coastal smart homes and boutique venues across Kiama, delivering expert Dynalite lighting control solutions from Terralong Street and Manning Street to expansive private properties overlooking the harbor and coastline.</p>",
        "links": '<li><a href="/cbus-repair-kiama" style="color:#f07020;text-decoration:underline;">C-Bus Repair Kiama</a></li><li><a href="/dynalite-repair-wollongong" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Wollongong</a></li><li><a href="/dynalite-repair-thirroul" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Thirroul</a></li>'
    },
    {
        "filename": "dynalite-repair-terrigal.html",
        "type": "dyn",
        "sub_title": "Terrigal",
        "title": "Signify Dynalite Repair Terrigal | Central Coast Beachfront Strata",
        "desc": "Expert Signify Dynalite repair for Central Coast prestige beachfront apartments, luxury homes, and architectural manors in Terrigal. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Providing expert Dynalite repair and lighting control maintenance for Central Coast prestige beachfront apartments, luxury homes, and architectural manors across Terrigal. Priority response.",
        "landmarks": "<p>We support prestige coastal smart homes and beachfront strata across Terrigal, delivering expert Dynalite lighting control solutions from Scenic Highway and Terrigal Esplanade to expansive private properties overlooking the ocean.</p>",
        "links": '<li><a href="/cbus-repair-terrigal" style="color:#f07020;text-decoration:underline;">C-Bus Repair Terrigal</a></li><li><a href="/dynalite-repair-avoca-beach" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Avoca Beach</a></li><li><a href="/cbus-repair-avoca-beach" style="color:#f07020;text-decoration:underline;">C-Bus Repair Avoca Beach</a></li>'
    },
    {
        "filename": "dynalite-repair-avoca-beach.html",
        "type": "dyn",
        "sub_title": "Avoca Beach",
        "title": "Signify Dynalite Repair Avoca Beach | Coastal Architectural Lighting",
        "desc": "Expert Signify Dynalite repair for coastal architectural retreats, hillside smart homes, and luxury estates in Avoca Beach. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Providing expert Dynalite repair and lighting control maintenance for coastal architectural retreats, hillside smart homes, and luxury estates across Avoca Beach. Priority response.",
        "landmarks": "<p>We support prestige coastal smart homes across Avoca Beach, delivering expert Dynalite lighting control solutions from Avoca Drive and Cape Three Points Road to expansive private properties overlooking the beach and lagoon.</p>",
        "links": '<li><a href="/cbus-repair-avoca-beach" style="color:#f07020;text-decoration:underline;">C-Bus Repair Avoca Beach</a></li><li><a href="/dynalite-repair-terrigal" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Terrigal</a></li><li><a href="/cbus-repair-terrigal" style="color:#f07020;text-decoration:underline;">C-Bus Repair Terrigal</a></li>'
    },
    {
        "filename": "dynalite-repair-leura.html",
        "type": "dyn",
        "sub_title": "Leura",
        "title": "Signify Dynalite Repair Leura | Blue Mountains Historic Manors",
        "desc": "Expert Signify Dynalite repair for Blue Mountains historic manors, luxury hospitality retreats, and architectural homes in Leura. Call 0422 469 739.",
        "lead": "Accredited Signify Dynalite System Designers. Providing expert Dynalite repair and lighting control maintenance for Blue Mountains historic manors, luxury hospitality retreats, and architectural homes across Leura. Priority response.",
        "landmarks": "<p>We support historic smart homes and boutique hospitality retreats across Leura, delivering expert Dynalite lighting control solutions from Leura Mall and Megalong Street to expansive private properties throughout the Blue Mountains.</p>",
        "links": '<li><a href="/cbus-repair-leura" style="color:#f07020;text-decoration:underline;">C-Bus Repair Leura</a></li><li><a href="/cbus-repair-wentworth-falls" style="color:#f07020;text-decoration:underline;">C-Bus Repair Wentworth Falls</a></li><li><a href="/dynalite-repair-sydney" style="color:#f07020;text-decoration:underline;">Signify Dynalite Repair Sydney</a></li>'
    }
]

print(f"Generating {len(pages_data)} unique, high-intent expansion pages...")

generated = 0
for d in pages_data:
    t = d["type"]
    fn = d["filename"]
    st = d["sub_title"]
    title = d["title"]
    desc = d["desc"]
    lead = d["lead"]
    landmarks = d["landmarks"]
    links = d["links"]
    
    if t == "cbus":
        master = cbus_master
        master = re.sub(r'<title>.*?</title>', f"<title>{title}</title>", master)
        master = re.sub(r'<meta content="[^"]+" name="description"/>', f'<meta content="{desc}" name="description"/>', master)
        master = re.sub(r'<link rel="canonical" href="[^"]+"/>', f'<link rel="canonical" href="https://sydneyautomationco.com.au/{fn[:-5]}"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:url"/>', f'<meta content="https://sydneyautomationco.com.au/{fn[:-5]}" property="og:url"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:title"/>', f'<meta content="{title}" property="og:title"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:description"/>', f'<meta content="{desc}" property="og:description"/>', master)
        master = re.sub(r'<meta content="[^"]+" name="geo.placename"/>', f'<meta content="Menai, Sutherland Shire, {st}" name="geo.placename"/>', master)
        
        master = re.sub(r'"url": "https://sydneyautomationco.com.au/c-bus-programmer-sydney"', f'"url": "https://sydneyautomationco.com.au/{fn[:-5]}"', master)
        master = re.sub(r'"areaServed": "Sydney"', f'"areaServed": "{st}"', master)
        master = re.sub(r'"name": "C-Bus Programmer Sydney"', f'"name": "{title.split("|")[0].strip()}"', master)
        master = re.sub(r'"item": "https://sydneyautomationco.com.au/c-bus-programmer-sydney"', f'"item": "https://sydneyautomationco.com.au/{fn[:-5]}"', master)
        
        new_h1 = f'<h1>C-Bus Programmer<br/><span class="accent">{st}</span></h1>'
        master = re.sub(r'<h1>C-Bus Programming<br/><span class="accent">&amp; Commissioning</span></h1>', new_h1, master)
        new_lead = f'<p class="lead">{lead}</p>'
        master = re.sub(r'<p class="lead">.*?</p>', new_lead, master, count=1)
        
    elif t == "dyn":
        master = dyn_master
        master = re.sub(r'<title>.*?</title>', f"<title>{title}</title>", master)
        master = re.sub(r'<meta content="[^"]+" name="description"/>', f'<meta content="{desc}" name="description"/>', master)
        master = re.sub(r'<link rel="canonical" href="[^"]+"/>', f'<link rel="canonical" href="https://sydneyautomationco.com.au/{fn[:-5]}"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:url"/>', f'<meta content="https://sydneyautomationco.com.au/{fn[:-5]}" property="og:url"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:title"/>', f'<meta content="{title}" property="og:title"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:description"/>', f'<meta content="{desc}" property="og:description"/>', master)
        master = re.sub(r'<meta content="[^"]+" name="geo.placename"/>', f'<meta content="Menai, Sutherland Shire, {st}" name="geo.placename"/>', master)
        
        master = re.sub(r'"url": "https://sydneyautomationco.com.au/dynalite-programmer-sydney"', f'"url": "https://sydneyautomationco.com.au/{fn[:-5]}"', master)
        master = re.sub(r'"areaServed": "Sydney"', f'"areaServed": "{st}"', master)
        master = re.sub(r'"name": "Signify Dynalite Programmer Sydney"', f'"name": "{title.split("|")[0].strip()}"', master)
        master = re.sub(r'"item": "https://sydneyautomationco.com.au/dynalite-programmer-sydney"', f'"item": "https://sydneyautomationco.com.au/{fn[:-5]}"', master)
        
        new_h1 = f'<h1>Signify Dynalite Programmer<br/><span class="accent">{st}</span></h1>'
        master = re.sub(r'<h1>Signify Dynalite Programming<br/><span class="accent">.*?Sydney</span></h1>', new_h1, master, flags=re.DOTALL)
        new_lead = f'<p class="lead">{lead}</p>'
        master = re.sub(r'<p class="lead">.*?</p>', new_lead, master, count=1)
        
    elif t == "comm":
        master = comm_master
        master = re.sub(r'<title>.*?</title>', f"<title>{title}</title>", master)
        master = re.sub(r'<meta content="[^"]+" name="description"/>', f'<meta content="{desc}" name="description"/>', master)
        master = re.sub(r'<link rel="canonical" href="[^"]+"/>', f'<link rel="canonical" href="https://sydneyautomationco.com.au/{fn[:-5]}"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:url"/>', f'<meta content="https://sydneyautomationco.com.au/{fn[:-5]}" property="og:url"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:title"/>', f'<meta content="{title}" property="og:title"/>', master)
        master = re.sub(r'<meta content="[^"]+" property="og:description"/>', f'<meta content="{desc}" property="og:description"/>', master)
        master = re.sub(r'<meta content="[^"]+" name="geo.placename"/>', f'<meta content="Menai, Sutherland Shire, {st}" name="geo.placename"/>', master)
        
        master = re.sub(r'"url": "https://sydneyautomationco.com.au/automation-sydney"', f'"url": "https://sydneyautomationco.com.au/{fn[:-5]}"', master)
        master = re.sub(r'"areaServed": "Sydney"', f'"areaServed": "{st}"', master)
        master = re.sub(r'"name": "Premium Home & Commercial Automation Sydney"', f'"name": "{title.split("|")[0].strip()}"', master)
        master = re.sub(r'"item": "https://sydneyautomationco.com.au/automation-sydney"', f'"item": "https://sydneyautomationco.com.au/{fn[:-5]}"', master)
        
        new_h1 = f'<h1>Lighting &amp; Automation<br/><span class="accent">{st}</span></h1>'
        master = re.sub(r'<h1>Premium Home & Commercial<br/><span class="accent">Automation Sydney</span></h1>', new_h1, master)
        new_lead = f'<p class="lead">{lead}</p>'
        master = re.sub(r'<p class="lead">.*?</p>', new_lead, master, count=1)

    # Inject local geography and links
    match = re.search(r'(<h2.*?>.*?</h2>)', master)
    if match and "<!-- LOCAL CONTEXT INJECTED -->" not in master:
        injection = f"""
      <h3>Local Geography & Facilities</h3>
      {landmarks}
      
      <h3>Nearby Suburbs We Service</h3>
      <ul style="line-height:1.8; margin-bottom: 24px;">
        {links}
      </ul>
      <!-- LOCAL CONTEXT INJECTED -->
      
"""
        master = master[:match.start()] + injection + master[match.start():]
        
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(master)
        generated += 1
        print(f"Created: {fn}")

print(f"SUCCESS: Generated {generated} unique expansion pages.")

'''
Required Tests:
- [x] verify that correct count of citations needed is calculated
- [ ] verify that preceding passage  *it gets the same passages when I print it out... but test is not working
'''

import pytest
from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report


def test_version():
    assert __version__ == '0.1.0'

def test_get_citations_needed_count():
    url = "https://en.wikipedia.org/wiki/Times_Beach,_Missouri"
    actual = get_citations_needed_count(url)
    expected = 3
    assert actual == expected

# @pytest.mark.skip("pending")
def test_get_citations_needed_report():
    url = "https://en.wikipedia.org/wiki/Times_Beach,_Missouri"
    actual = get_citations_needed_report(url)
    expected = '''In its early years, the town was primarily a summer resort, but the Great Depression combined with gasoline rationing during World War II reduced the feasibility of summer homes.[4] The town became a community of mostly low-income housing, and a small population (1,240) lived in Times Beach by 1970.[4] In the years immediately before its evacuation, Times Beach had become a lower-middle-class town.[4] Historically, there had always been a small grocery store and gas station on Route 66 to serve the residents.[citation needed]

    In May and June 1982, the EPA decided to revisit the Shenandoah, Timberline, and Bubbling Springs stables, as well as the Minker and Stout properties. New soil samples revealed that concentrations of dioxin had not decreased since the last test results obtained by the CDC several years earlier. Although more than ten years had passed since the spraying, areas in the Shenandoah arena still contained as much as 1.8 ppm of dioxin. Regional EPA officials advised owners of the contaminated stables to temporarily close, and urged the national EPA office to begin cleanup operations at each of the contaminated locations. These cleanup requests were delayed when Rita Lavelle, an assistant administrator at EPA headquarters in Washington, announced that the EPA would be collecting and testing an additional six hundred soil samples in order to better understand the extent of contamination.[citation needed]

    In 1972, Times Beach hired Bliss to oil its twenty-three miles of dirt roads (due to lack of funding, Times Beach was unable to pave its roads). For $2,400, Bliss sprayed approximately 160,000 gallons of waste oil in Times Beach over a period of four years.[15] The release of the leaked EPA document in 1982 was the first time that Times Beach had learned of its contamination.[13] Residents felt betrayed and publicly criticized the EPA for not informing them of the toxic hazards around their homes.[15] Since Times Beach had the largest population out of the listed sites, Times Beach became the subject of national media and attention.[citation needed]'''
    assert actual == expected
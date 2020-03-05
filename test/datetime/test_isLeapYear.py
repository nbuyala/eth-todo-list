import pytest

LEAP_YEARS = {
    1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016,
    2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068,
    2072, 2076, 2080, 2084, 2088, 2092, 2096, 2104, 2108, 2112, 2116, 2120, 2124,
    2128, 2132, 2136, 2140, 2144, 2148, 2152, 2156, 2160, 2164, 2168, 2172, 2176,
    2180, 2184, 2188, 2192, 2196, 2204, 2208, 2212, 2216, 2220, 2224, 2228, 2232,
    2236, 2240, 2244, 2248, 2252, 2256, 2260, 2264, 2268, 2272, 2276, 2280, 2284,
    2288, 2292, 2296, 2304, 2308, 2312, 2316, 2320, 2324, 2328, 2332, 2336, 2340,
    2344, 2348, 2352, 2356, 2360, 2364, 2368, 2372, 2376, 2380, 2384, 2388, 2392,
    2396, 2400,
}


@pytest.mark.parametrize(
    'year', range(1970, 2401),
)
def test_is_leap_year(deployed_contracts, year):
    crontab = deployed_contracts.DateTime
    if year in LEAP_YEARS:
        assert crontab.isLeapYear(year) is True
    else:
        assert crontab.isLeapYear(year) is False

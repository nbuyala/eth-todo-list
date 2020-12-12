import pytest



@pytest.mark.parametrize(
    'timestamp,year',
    (
        (0, 1970),
        (31536000, 1971),
        (31535999, 1970),
        (63072000, 1972),
        (63071999, 1971),
        (94694400, 1973),
        (94694399, 1972),
        (126230400, 1974),
        (126230399, 1973),
        (157766400, 1975),
        (157766399, 1974),
        (189302400, 1976),
        (189302399, 1975),
        (220924800, 1977),
        (220924799, 1976),
        (252460800, 1978),
        (252460799, 1977),
        (283996800, 1979),
        (283996799, 1978),
        (315532800, 1980),
        (315532799, 1979),
        (347155200, 1981),
        (347155199, 1980),
        (378691200, 1982),
        (378691199, 1981),
        (410227200, 1983),
        (410227199, 1982),
        (441763200, 1984),
        (441763199, 1983),
        (473385600, 1985),
        (473385599, 1984),
        (504921600, 1986),
        (504921599, 1985),
        (536457600, 1987),
        (536457599, 1986),
        (567993600, 1988),
        (567993599, 1987),
        (599616000, 1989),
        (599615999, 1988),
        (631152000, 1990),
        (631151999, 1989),
        (662688000, 1991),
        (662687999, 1990),
        (694224000, 1992),
        (694223999, 1991),
        (725846400, 1993),
        (725846399, 1992),
        (757382400, 1994),
        (757382399, 1993),
        (788918400, 1995),
(788918399, 1994),
(820454400, 1996),
(820454399, 1995),
(852076800, 1997),
(852076799, 1996),
(883612800, 1998),
(883612799, 1997),
(915148800, 1999),
(915148799, 1998),
(946684800, 2000),
(946684799, 1999),
(978307200, 2001),
(978307199, 2000),
(1009843200, 2002),
(1009843199, 2001),
(1041379200, 2003),
(1041379199, 2002),
(1072915200, 2004),
(1072915199, 2003),
(1104537600, 2005),
(1104537599, 2004),
(1136073600, 2006),
(1136073599, 2005),
(1167609600, 2007),
(1167609599, 2006),
(1199145600, 2008),
(1199145599, 2007),
(1230768000, 2009),
(1230767999, 2008),
(1262304000, 2010),
(1262303999, 2009),
(1293840000, 2011),
(1293839999, 2010),
(1325376000, 2012),
(1325375999, 2011),
(1356998400, 2013),
(1356998399, 2012),
(1388534400, 2014),
(1388534399, 2013),
(1420070400, 2015),
(1420070399, 2014),
(1451606400, 2016),
(1451606399, 2015),
(1483228800, 2017),
(1483228799, 2016),
(1514764800, 2018),
(1514764799, 2017),
(1546300800, 2019),
(1546300799, 2018),
(1577836800, 2020),
(1577836799, 2019),
(1609459200, 2021),
(1609459199, 2020),
(1640995200, 2022),
(1640995199, 2021),
(1672531200, 2023),
(1672531199, 2022),
(1704067200, 2024),
(1704067199, 2023),
(1735689600, 2025),
(1735689599, 2024),
(1767225600, 2026),
(1767225599, 2025),
(1798761600, 2027),
(1798761599, 2026),
(1830297600, 2028),
(1830297599, 2027),
(1861920000, 2029),
(1861919999, 2028),
(1893456000, 2030),
(1893455999, 2029),
(1924992000, 2031),
(1924991999, 2030),
(1956528000, 2032),
(1956527999, 2031),
(1988150400, 2033),
(1988150399, 2032),
(2019686400, 2034),
(2019686399, 2033),
(2051222400, 2035),
(2051222399, 2034),
(2082758400, 2036),
(2082758399, 2035),
(2114380800, 2037),
(2114380799, 2036),
(2145916800, 2038),
(2145916799, 2037),
(2177452800, 2039),
(2177452799, 2038),
(2208988800, 2040),
(2208988799, 2039),
(2240611200, 2041),
(2240611199, 2040),
(2272147200, 2042),
(2272147199, 2041),
(2303683200, 2043),
(2303683199, 2042),
(2335219200, 2044),
(2335219199, 2043),
(2366841600, 2045),
(2366841599, 2044),
(2398377600, 2046),
(2398377599, 2045),
(2429913600, 2047),
(2429913599, 2046),
(2461449600, 2048),
(2461449599, 2047),
(2493072000, 2049),
(2493071999, 2048),
(2524608000, 2050),
(2524607999, 2049),
(2556144000, 2051),
(2556143999, 2050),
(2587680000, 2052),
(2587679999, 2051),
(2619302400, 2053),
(2619302399, 2052),
(2650838400, 2054),
(2650838399, 2053),
(2682374400, 2055),
(2682374399, 2054),
(2713910400, 2056),
(2713910399, 2055),
(2745532800, 2057),
(2745532799, 2056),
(2777068800, 2058),
(2777068799, 2057),
(2808604800, 2059),
(2808604799, 2058),
(2840140800, 2060),
(2840140799, 2059),
(2871763200, 2061),
(2871763199, 2060),
(2903299200, 2062),
(2903299199, 2061),
(2934835200, 2063),
(2934835199, 2062),
(2966371200, 2064),
(2966371199, 2063),
(2997993600, 2065),
(2997993599, 2064),
(3029529600, 2066),
(3029529599, 2065),
(3061065600, 2067),
(3061065599, 2066),
(3092601600, 2068),
(3092601599, 2067),
(3124224000, 2069),
(3124223999, 2068),
(3155760000, 2070),
(3155759999, 2069),
(3187296000, 2071),
(3187295999, 2070),
(3218832000, 2072),
(3218831999, 2071),
(3250454400, 2073),
(3250454399, 2072),
(3281990400, 2074),
(3281990399, 2073),
(3313526400, 2075),
(3313526399, 2074),
(3345062400, 2076),
(3345062399, 2075),
(3376684800, 2077),
(3376684799, 2076),
(3408220800, 2078),
(3408220799, 2077),
(3439756800, 2079),
(3439756799, 2078),
(3471292800, 2080),
(3471292799, 2079),
(3502915200, 2081),
(3502915199, 2080),
(3534451200, 2082),
(3534451199, 2081),
(3565987200, 2083),
(3565987199, 2082),
(3597523200, 2084),
(3597523199, 2083),
(3629145600, 2085),
(3629145599, 2084),
(3660681600, 2086),
(3660681599, 2085),
(3692217600, 2087),
(3692217599, 2086),
(3723753600, 2088),
(3723753599, 2087),
(3755376000, 2089),
(3755375999, 2088),
(3786912000, 2090),
(3786911999, 2089),
(3818448000, 2091),
(3818447999, 2090),
(3849984000, 2092),
(3849983999, 2091),
(3881606400, 2093),
(3881606399, 2092),
(3913142400, 2094),
(3913142399, 2093),
(3944678400, 2095),
(3944678399, 2094),
(3976214400, 2096),
(3976214399, 2095),
(4007836800, 2097),
(4007836799, 2096),
(4039372800, 2098),
(4039372799, 2097),
(4070908800, 2099),
(4070908799, 2098),
(4102444800, 2100),
(4102444799, 2099),
(4133980800, 2101),
(4133980799, 2100),
(4165516800, 2102),
(4165516799, 2101),
(4197052800, 2103),
(4197052799, 2102),
(4228588800, 2104),
(4228588799, 2103),
(4260211200, 2105),
(4260211199, 2104),
(4291747200, 2106),
(4291747199, 2105),
(4323283200, 2107),
(4323283199, 2106),
(4354819200, 2108),
(4354819199, 2107),
(4386441600, 2109),
(4386441599, 2108),
(4417977600, 2110),
(4417977599, 2109),
(4449513600, 2111),
(4449513599, 2110),
(4481049600, 2112),
(4481049599, 2111),
(4512672000, 2113),
(4512671999, 2112),
(4544208000, 2114),
(4544207999, 2113),
(4575744000, 2115),
(4575743999, 2114),
(4607280000, 2116),
(4607279999, 2115),
(4638902400, 2117),
(4638902399, 2116),
(4670438400, 2118),
(4670438399, 2117),
(4701974400, 2119),
(4701974399, 2118),
(4733510400, 2120),
(4733510399, 2119),
(4765132800, 2121),
(4765132799, 2120),
(4796668800, 2122),
(4796668799, 2121),
(4828204800, 2123),
(4828204799, 2122),
(4859740800, 2124),
(4859740799, 2123),
(4891363200, 2125),
(4891363199, 2124),
(4922899200, 2126),
(4922899199, 2125),
(4954435200, 2127),
(4954435199, 2126),
(4985971200, 2128),
(4985971199, 2127),
(5017593600, 2129),
(5017593599, 2128),
(5049129600, 2130),
(5049129599, 2129),
(5080665600, 2131),
(5080665599, 2130),
(5112201600, 2132),
(5112201599, 2131),
(5143824000, 2133),
(5143823999, 2132),
(5175360000, 2134),
(5175359999, 2133),
(5206896000, 2135),
(5206895999, 2134),
(5238432000, 2136),
(5238431999, 2135),
(5270054400, 2137),
(5270054399, 2136),
(5301590400, 2138),
(5301590399, 2137),
(5333126400, 2139),
(5333126399, 2138),
(5364662400, 2140),
(5364662399, 2139),
(5396284800, 2141),
(5396284799, 2140),
(5427820800, 2142),
(5427820799, 2141),
(5459356800, 2143),
(5459356799, 2142),
(5490892800, 2144),
(5490892799, 2143),
(5522515200, 2145),
(5522515199, 2144),
(5554051200, 2146),
(5554051199, 2145),
(5585587200, 2147),
(5585587199, 2146),
(5617123200, 2148),
(5617123199, 2147),
(5648745600, 2149),
(5648745599, 2148),
(5680281600, 2150),
(5680281599, 2149),
(5711817600, 2151),
(5711817599, 2150),
(5743353600, 2152),
(5743353599, 2151),
(5774976000, 2153),
(5774975999, 2152),
(5806512000, 2154),
(5806511999, 2153),
(5838048000, 2155),
(5838047999, 2154),
(5869584000, 2156),
(5869583999, 2155),
(5901206400, 2157),
(5901206399, 2156),
(5932742400, 2158),
(5932742399, 2157),
(5964278400, 2159),
(5964278399, 2158),
(5995814400, 2160),
(5995814399, 2159),
(6027436800, 2161),
(6027436799, 2160),
(6058972800, 2162),
(6058972799, 2161),
(6090508800, 2163),
(6090508799, 2162),
(6122044800, 2164),
(6122044799, 2163),
(6153667200, 2165),
(6153667199, 2164),
(6185203200, 2166),
(6185203199, 2165),
(6216739200, 2167),
(6216739199, 2166),
(6248275200, 2168),
(6248275199, 2167),
(6279897600, 2169),
(6279897599, 2168),
(6311433600, 2170),
(6311433599, 2169),
(6342969600, 2171),
(6342969599, 2170),
(6374505600, 2172),
(6374505599, 2171),
(6406128000, 2173),
(6406127999, 2172),
(6437664000, 2174),
(6437663999, 2173),
(6469200000, 2175),
(6469199999, 2174),
(6500736000, 2176),
(6500735999, 2175),
(6532358400, 2177),
(6532358399, 2176),
(6563894400, 2178),
(6563894399, 2177),
(6595430400, 2179),
(6595430399, 2178),
(6626966400, 2180),
(6626966399, 2179),
(6658588800, 2181),
(6658588799, 2180),
(6690124800, 2182),
(6690124799, 2181),
(6721660800, 2183),
(6721660799, 2182),
(6753196800, 2184),
(6753196799, 2183),
(6784819200, 2185),
(6784819199, 2184),
(6816355200, 2186),
(6816355199, 2185),
(6847891200, 2187),
(6847891199, 2186),
(6879427200, 2188),
(6879427199, 2187),
(6911049600, 2189),
(6911049599, 2188),
(6942585600, 2190),
(6942585599, 2189),
(6974121600, 2191),
(6974121599, 2190),
(7005657600, 2192),
(7005657599, 2191),
(7037280000, 2193),
(7037279999, 2192),
(7068816000, 2194),
(7068815999, 2193),
(7100352000, 2195),
(7100351999, 2194),
(7131888000, 2196),
(7131887999, 2195),
(7163510400, 2197),
(7163510399, 2196),
(7195046400, 2198),
(7195046399, 2197),
(7226582400, 2199),
(7226582399, 2198),
(7258118400, 2200),
(7258118399, 2199),
(7289654400, 2201),
(7289654399, 2200),
(7321190400, 2202),
(7321190399, 2201),
(7352726400, 2203),
(7352726399, 2202),
(7384262400, 2204),
(7384262399, 2203),
(7415884800, 2205),
(7415884799, 2204),
(7447420800, 2206),
(7447420799, 2205),
(7478956800, 2207),
(7478956799, 2206),
(7510492800, 2208),
(7510492799, 2207),
(7542115200, 2209),
(7542115199, 2208),
(7573651200, 2210),
(7573651199, 2209),
(7605187200, 2211),
(7605187199, 2210),
(7636723200, 2212),
(7636723199, 2211),
(7668345600, 2213),
(7668345599, 2212),
(7699881600, 2214),
(7699881599, 2213),
(7731417600, 2215),
(7731417599, 2214),
(7762953600, 2216),
(7762953599, 2215),
(7794576000, 2217),
(7794575999, 2216),
(7826112000, 2218),
(7826111999, 2217),
(7857648000, 2219),
(7857647999, 2218),
(7889184000, 2220),
(7889183999, 2219),
(7920806400, 2221),
(7920806399, 2220),
(7952342400, 2222),
(7952342399, 2221),
(7983878400, 2223),
(7983878399, 2222),
(8015414400, 2224),
(8015414399, 2223),
(8047036800, 2225),
(8047036799, 2224),
(8078572800, 2226),
(8078572799, 2225),
(8110108800, 2227),
(8110108799, 2226),
(8141644800, 2228),
(8141644799, 2227),
(8173267200, 2229),
(8173267199, 2228),
(8204803200, 2230),
(8204803199, 2229),
(8236339200, 2231),
(8236339199, 2230),
(8267875200, 2232),
(8267875199, 2231),
(8299497600, 2233),
(8299497599, 2232),
(8331033600, 2234),
(8331033599, 2233),
(8362569600, 2235),
(8362569599, 2234),
(8394105600, 2236),
(8394105599, 2235),
(8425728000, 2237),
(8425727999, 2236),
(8457264000, 2238),
(8457263999, 2237),
(8488800000, 2239),
(8488799999, 2238),
(8520336000, 2240),
(8520335999, 2239),
(8551958400, 2241),
(8551958399, 2240),
(8583494400, 2242),
(8583494399, 2241),
(8615030400, 2243),
(8615030399, 2242),
(8646566400, 2244),
(8646566399, 2243),
(8678188800, 2245),
(8678188799, 2244),
(8709724800, 2246),
(8709724799, 2245),
(8741260800, 2247),
(8741260799, 2246),
(8772796800, 2248),
(8772796799, 2247),
(8804419200, 2249),
(8804419199, 2248),
(8835955200, 2250),
(8835955199, 2249),
(8867491200, 2251),
(8867491199, 2250),
(8899027200, 2252),
(8899027199, 2251),
(8930649600, 2253),
(8930649599, 2252),
(8962185600, 2254),
(8962185599, 2253),
(8993721600, 2255),
(8993721599, 2254),
(9025257600, 2256),
(9025257599, 2255),
(9056880000, 2257),
(9056879999, 2256),
(9088416000, 2258),
(9088415999, 2257),
(9119952000, 2259),
(9119951999, 2258),
(9151488000, 2260),
(9151487999, 2259),
(9183110400, 2261),
(9183110399, 2260),
(9214646400, 2262),
(9214646399, 2261),
(9246182400, 2263),
(9246182399, 2262),
(9277718400, 2264),
(9277718399, 2263),
(9309340800, 2265),
(9309340799, 2264),
(9340876800, 2266),
(9340876799, 2265),
(9372412800, 2267),
(9372412799, 2266),
(9403948800, 2268),
(9403948799, 2267),
(9435571200, 2269),
(9435571199, 2268),
(9467107200, 2270),
(9467107199, 2269),
(9498643200, 2271),
(9498643199, 2270),
(9530179200, 2272),
(9530179199, 2271),
(9561801600, 2273),
(9561801599, 2272),
(9593337600, 2274),
(9593337599, 2273),
(9624873600, 2275),
(9624873599, 2274),
(9656409600, 2276),
(9656409599, 2275),
(9688032000, 2277),
(9688031999, 2276),
(9719568000, 2278),
(9719567999, 2277),
(9751104000, 2279),
(9751103999, 2278),
(9782640000, 2280),
(9782639999, 2279),
(9814262400, 2281),
(9814262399, 2280),
(9845798400, 2282),
(9845798399, 2281),
(9877334400, 2283),
(9877334399, 2282),
(9908870400, 2284),
(9908870399, 2283),
(9940492800, 2285),
(9940492799, 2284),
(9972028800, 2286),
(9972028799, 2285),
(10003564800, 2287),
(10003564799, 2286),
(10035100800, 2288),
(10035100799, 2287),
(10066723200, 2289),
(10066723199, 2288),
(10098259200, 2290),
(10098259199, 2289),
(10129795200, 2291),
(10129795199, 2290),
(10161331200, 2292),
(10161331199, 2291),
(10192953600, 2293),
(10192953599, 2292),
(10224489600, 2294),
(10224489599, 2293),
(10256025600, 2295),
(10256025599, 2294),
(10287561600, 2296),
(10287561599, 2295),
(10319184000, 2297),
(10319183999, 2296),
(10350720000, 2298),
(10350719999, 2297),
(10382256000, 2299),
(10382255999, 2298),
(10413792000, 2300),
(10413791999, 2299),
(10445328000, 2301),
(10445327999, 2300),
(10476864000, 2302),
(10476863999, 2301),
(10508400000, 2303),
(10508399999, 2302),
(10539936000, 2304),
(10539935999, 2303),
(10571558400, 2305),
(10571558399, 2304),
(10603094400, 2306),
(10603094399, 2305),
(10634630400, 2307),
(10634630399, 2306),
(10666166400, 2308),
(10666166399, 2307),
(10697788800, 2309),
(10697788799, 2308),
(10729324800, 2310),
(10729324799, 2309),
(10760860800, 2311),
(10760860799, 2310),
(10792396800, 2312),
(10792396799, 2311),
(10824019200, 2313),
(10824019199, 2312),
(10855555200, 2314),
(10855555199, 2313),
(10887091200, 2315),
(10887091199, 2314),
(10918627200, 2316),
(10918627199, 2315),
(10950249600, 2317),
(10950249599, 2316),
(10981785600, 2318),
(10981785599, 2317),
(11013321600, 2319),
(11013321599, 2318),
(11044857600, 2320),
(11044857599, 2319),
(11076480000, 2321),
(11076479999, 2320),
(11108016000, 2322),
(11108015999, 2321),
(11139552000, 2323),
(11139551999, 2322),
(11171088000, 2324),
(11171087999, 2323),
(11202710400, 2325),
(11202710399, 2324),
(11234246400, 2326),
(11234246399, 2325),
(11265782400, 2327),
(11265782399, 2326),
(11297318400, 2328),
(11297318399, 2327),
(11328940800, 2329),
(11328940799, 2328),
(11360476800, 2330),
(11360476799, 2329),
(11392012800, 2331),
(11392012799, 2330),
(11423548800, 2332),
(11423548799, 2331),
(11455171200, 2333),
(11455171199, 2332),
(11486707200, 2334),
(11486707199, 2333),
(11518243200, 2335),
(11518243199, 2334),
(11549779200, 2336),
(11549779199, 2335),
(11581401600, 2337),
(11581401599, 2336),
(11612937600, 2338),
(11612937599, 2337),
(11644473600, 2339),
(11644473599, 2338),
(11676009600, 2340),
(11676009599, 2339),
(11707632000, 2341),
(11707631999, 2340),
(11739168000, 2342),
(11739167999, 2341),
(11770704000, 2343),
(11770703999, 2342),
(11802240000, 2344),
(11802239999, 2343),
(11833862400, 2345),
(11833862399, 2344),
(11865398400, 2346),
(11865398399, 2345),
(11896934400, 2347),
(11896934399, 2346),
(11928470400, 2348),
(11928470399, 2347),
(11960092800, 2349),
(11960092799, 2348),
(11991628800, 2350),
(11991628799, 2349),
(12023164800, 2351),
(12023164799, 2350),
(12054700800, 2352),
(12054700799, 2351),
(12086323200, 2353),
(12086323199, 2352),
(12117859200, 2354),
(12117859199, 2353),
(12149395200, 2355),
(12149395199, 2354),
(12180931200, 2356),
(12180931199, 2355),
(12212553600, 2357),
(12212553599, 2356),
(12244089600, 2358),
(12244089599, 2357),
(12275625600, 2359),
(12275625599, 2358),
(12307161600, 2360),
(12307161599, 2359),
(12338784000, 2361),
(12338783999, 2360),
(12370320000, 2362),
(12370319999, 2361),
(12401856000, 2363),
(12401855999, 2362),
(12433392000, 2364),
(12433391999, 2363),
(12465014400, 2365),
(12465014399, 2364),
(12496550400, 2366),
(12496550399, 2365),
(12528086400, 2367),
(12528086399, 2366),
(12559622400, 2368),
(12559622399, 2367),
(12591244800, 2369),
(12591244799, 2368),
(12622780800, 2370),
(12622780799, 2369),
(12654316800, 2371),
(12654316799, 2370),
(12685852800, 2372),
(12685852799, 2371),
(12717475200, 2373),
(12717475199, 2372),
(12749011200, 2374),
(12749011199, 2373),
(12780547200, 2375),
(12780547199, 2374),
(12812083200, 2376),
(12812083199, 2375),
(12843705600, 2377),
(12843705599, 2376),
(12875241600, 2378),
(12875241599, 2377),
(12906777600, 2379),
(12906777599, 2378),
(12938313600, 2380),
(12938313599, 2379),
(12969936000, 2381),
(12969935999, 2380),
(13001472000, 2382),
(13001471999, 2381),
(13033008000, 2383),
(13033007999, 2382),
(13064544000, 2384),
(13064543999, 2383),
(13096166400, 2385),
(13096166399, 2384),
(13127702400, 2386),
(13127702399, 2385),
(13159238400, 2387),
(13159238399, 2386),
(13190774400, 2388),
(13190774399, 2387),
(13222396800, 2389),
(13222396799, 2388),
(13253932800, 2390),
(13253932799, 2389),
(13285468800, 2391),
(13285468799, 2390),
(13317004800, 2392),
(13317004799, 2391),
(13348627200, 2393),
(13348627199, 2392),
(13380163200, 2394),
(13380163199, 2393),
(13411699200, 2395),
(13411699199, 2394),
(13443235200, 2396),
(13443235199, 2395),
(13474857600, 2397),
(13474857599, 2396),
(13506393600, 2398),
(13506393599, 2397),
(13537929600, 2399),
(13537929599, 2398),
)
)
def test_get_year_from_timestamp(deployed_contracts, timestamp, year):
    crontab = deployed_contracts.DateTime
    assert crontab.getYear(timestamp) == year
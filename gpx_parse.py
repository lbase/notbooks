"""
setup for reading gpx file into pandas dataframe

"""
from lxml import etree
    import pandas as pd
    GSNAME = {"gpx": "http://www.topografix.com/GPX/1/0", "groundspeak": "http://www.groundspeak.com/cache/1/0/1"}


def getgpx(filename):
    # I  thought these lists would have to be inside the for loop, but runs
    # quite differently that way
    tree = etree.parse(filename)
    root = tree.getroot()
    gcid = []
    cachename = []
    longt = []
    latd = []
    timstmp = []
    bkmrk = []
    gid = []
    avail = []
    arch = []
    owner = []
    ownerid = []
    ctype = []
    cntanr = []
    diffclty = []
    terrain = []
    short_desc = []
    shortd_html = []
    long_desc = []
    long_html = []
    # not sure this count is needed....
    cnt = len(tree.findall('//gpx:wpt', namespaces=GSNAME))

    for elem_n in tree.findall('//gpx:wpt/gpx:name', namespaces=GSNAME):
        gcid.append(elem_n.text)

    for sname in tree.findall("//groundspeak:name", namespaces=GSNAME):
        cachename.append(sname.text)
    for lon2 in tree.findall("//gpx:wpt", namespaces=GSNAME):
        longt.append(lon2.attrib['lon'])
        latd.append(lon2.attrib['lat'])
    for elem5 in tree.findall("//gpx:wpt/gpx:time", namespaces=GSNAME):
        timstmp.append(elem5.text)
    for elem6 in tree.findall("//gpx:wpt/gpx:url", namespaces=GSNAME):
        bkmrk.append(elem6.text)
    for elem6 in tree.findall("//groundspeak:cache", namespaces=GSNAME):
        gid.append(elem6.attrib['id'])
        avail.append(elem6.attrib['available'])
        arch.append(elem6.attrib['archived'])
    for elem7 in tree.findall("//groundspeak:cache/groundspeak:owner", namespaces=GSNAME):
        owner.append(elem7.text)
        ownerid.append(elem7.attrib['id'])
    for elem8 in tree.findall("//groundspeak:cache/groundspeak:type", namespaces=GSNAME):
        ctype.append(elem8.text)
    for elem9 in tree.findall("//groundspeak:cache/groundspeak:container", namespaces=GSNAME):
        cntanr.append(elem9.text)
    for elem10 in tree.findall("//groundspeak:cache/groundspeak:difficulty", namespaces=GSNAME):
        diffclty.append(elem10.text)
    for elem11 in tree.findall("//groundspeak:cache/groundspeak:terrain", namespaces=GSNAME):
        terrain.append(elem11.text)
    for elem12 in tree.findall("//groundspeak:cache/groundspeak:short_description", namespaces=GSNAME):
        short_desc.append(elem12.text)
        shortd_html.append(elem12.attrib['html'])
    for elem13 in tree.findall("//groundspeak:cache/groundspeak:long_description", namespaces=GSNAME):
        long_desc.append(elem13.text)
        long_html.append(elem12.attrib['html'])

    ##
    ziplst = zip(
        gcid, cachename, longt, latd, timstmp, bkmrk, gid, avail, arch,
        owner, ownerid, ctype, cntanr, diffclty, terrain, short_desc, shortd_html, long_desc, long_html
    )
    gpxdf = pd.DataFrame(list(ziplst),
                         columns=['GCID', 'cachename', 'longitude', 'latitude', 'timestamp', 'url', 'cache id',
                                  'available', \
                                  'archived', 'owner', 'ownerid', 'cache type', 'container', 'difficulty', 'terrain',
                                  'short desc', 'short html',
                                  'long desc', 'long html'])

    return gpxdf

def getlogs(filename):
    tree = etree.parse(filename)
    root = tree.getroot()
    ldate = []
    ltype = []
    logfinder = []
    logtext = []
    loggcid = []

    cnt = len(tree.findall('//gpx:wpt', namespaces=GSNAME))

    for cache in tree.findall('//gpx:wpt', namespaces=GSNAME):

        cntlogs = len(cache.findall('.groundspeak:cache/groundspeak:logs/groundspeak:log', namespaces=GSNAME))
        gnumber = cache.find('gpx:name', namespaces=GSNAME).text

        # for   range in (0,cntlogs):
        loggcid.extend([gnumber] * cntlogs)
        for cachelogdate in cache.findall('groundspeak:cache/groundspeak:logs/groundspeak:log/groundspeak:date',
                                          namespaces=GSNAME):
            ldate.append(cachelogdate.text)
        for cachelogtype in cache.findall('groundspeak:cache/groundspeak:logs/groundspeak:log/groundspeak:type',
                                          namespaces=GSNAME):
            ltype.append(cachelogtype.text)
        for cachelogfinder in cache.findall('groundspeak:cache/groundspeak:logs/groundspeak:log/groundspeak:finder',
                                            namespaces=GSNAME):
            logfinder.append(cachelogfinder.text)
        for cachelogtext in cache.findall('groundspeak:cache/groundspeak:logs/groundspeak:log/groundspeak:text',
                                          namespaces=GSNAME):
            logtext.append(cachelogtext.text)

    ziplog = zip(loggcid, ldate, ltype, logfinder, logtext)
    logdf = pd.DataFrame(list(ziplog), columns=['GCID', 'date', 'type', 'finder', 'logtext'])
    return logdf

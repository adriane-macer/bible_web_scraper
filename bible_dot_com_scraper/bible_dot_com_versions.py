version_links = (
    "https://www.bible.com/bible/1588/GEN.1.AMP",
    "https://www.bible.com/bible/8/GEN.1.AMPC",
    "https://www.bible.com/bible/12/GEN.1.ASV",
    "https://www.bible.com/bible/31/GEN.1.BOOKS",
    "https://www.bible.com/bible/37/GEN.1.CEB",
    "https://www.bible.com/bible/392/GEN.1.CEV",
    "https://www.bible.com/bible/303/GEN.1.CEVDCI",
    "https://www.bible.com/bible/294/GEN.1.CEVUK",
    "https://www.bible.com/bible/1275/GEN.1.CJB",
    "https://www.bible.com/bible/42/GEN.1.CPDV",
    "https://www.bible.com/bible/1713/GEN.1.CSB",
    "https://www.bible.com/bible/478/GEN.1.DARBY",
    "https://www.bible.com/bible/55/GEN.1.DRC1752",
    "https://www.bible.com/bible/2079/GEN.1.EASY",
    "https://www.bible.com/bible/406/GEN.1.ERV",
    "https://www.bible.com/bible/59/GEN.1.ESV",
    "https://www.bible.com/bible/1932/GEN.1.FBVNTPSALMS",
    "https://www.bible.com/bible/296/GEN.1.GNB",
    "https://www.bible.com/bible/416/GEN.1.GNBDC",
    "https://www.bible.com/bible/431/GEN.1.GNBDK",
    "https://www.bible.com/bible/68/GEN.1.GNT",
    "https://www.bible.com/bible/69/GEN.1.GNTD",
    "https://www.bible.com/bible/2163/GEN.1.GNV",
    "https://www.bible.com/bible/70/GEN.1.GW",
    "https://www.bible.com/bible/1047/GEN.1.GWC",
    "https://www.bible.com/bible/72/GEN.1.HCSB",
    "https://www.bible.com/bible/1359/GEN.1.ICB",
    "https://www.bible.com/bible/1077/GEN.1.JUB",
    "https://www.bible.com/bible/1/GEN.1.KJV",
    "https://www.bible.com/bible/546/GEN.1.KJVA",
    "https://www.bible.com/bible/547/GEN.1.KJVA",
    "https://www.bible.com/bible/90/GEN.1.LEB",
    "https://www.bible.com/bible/1171/GEN.1.MEV",
    "https://www.bible.com/bible/1365/GEN.1.MP1650",
    "https://www.bible.com/bible/97/GEN.1.MSG",
    "https://www.bible.com/bible/463/GEN.1.NABRE",
    "https://www.bible.com/bible/100/GEN.1.NASB",
    "https://www.bible.com/bible/105/GEN.1.NCV",
    "https://www.bible.com/bible/107/GEN.1.NET",
    "https://www.bible.com/bible/110/GEN.1.NIRV",
    "https://www.bible.com/bible/111/GEN.1.NIV",
    "https://www.bible.com/bible/113/GEN.1.NIVUK",
    "https://www.bible.com/bible/114/GEN.1.NKJV",
    "https://www.bible.com/bible/116/GEN.1.NLT",
    "https://www.bible.com/bible/2135/GEN.1.NMV",
    "https://www.bible.com/bible/2016/GEN.1.NRSV",
    "https://www.bible.com/bible/2015/GEN.1.NRSV-CI",
    "https://www.bible.com/bible/130/GEN.1.OJB",
    "https://www.bible.com/bible/2020/GEN.1.RSV",
    "https://www.bible.com/bible/2017/GEN.1.RSV-CI",
    "https://www.bible.com/bible/477/GEN.1.RV1885",
    "https://www.bible.com/bible/1922/GEN.1.RV1895",
    "https://www.bible.com/bible/314/GEN.1.TLV",
    "https://www.bible.com/bible/1849/GEN.1.TPT",
    "https://www.bible.com/bible/316/GEN.1.TS2009",
    "https://www.bible.com/bible/2407/GEN.1.WBMS",
    "https://www.bible.com/bible/206/GEN.1.WEB",
    "https://www.bible.com/bible/1204/GEN.1.WEBBE",
    "https://www.bible.com/bible/1209/GEN.1.WMB",
    "https://www.bible.com/bible/1207/GEN.1.WMBBE",
    "https://www.bible.com/bible/821/GEN.1.YLT1898",
)


class Version:
    def __init__(self, link, version_name, short_version_name):
        self.link = link
        self.version_name = version_name
        self.short_version_name = short_version_name


versions = (
    Version('https://www.bible.com/bible/1588/GEN.1.AMP', "Amplified Bible", "AMP"),
    Version('https://www.bible.com/bible/8/GEN.1.AMPC', "Amplified Bible, Classic Edition", "AMPC"),
    Version('https://www.bible.com/bible/12/GEN.1.ASV', "American Standard Version", "ASV"),
    Version('https://www.bible.com/bible/31/GEN.1.BOOKS', "The Books of the Bible NT", "BOOKS"),
    Version('https://www.bible.com/bible/37/GEN.1.CEB', "Common English Bible", "CEB"),
    Version('https://www.bible.com/bible/392/GEN.1.CEV', "Contemporary English Version", "CEV"),
    Version('https://www.bible.com/bible/303/GEN.1.CEVDCI', "Contemporary English Version Interconfessional Edition",
            "CEVDCI"),
    Version('https://www.bible.com/bible/294/GEN.1.CEVUK', "Contemporary English Version (Anglicised) 2012", "CEVUK"),
    Version('https://www.bible.com/bible/1275/GEN.1.CJB', "Complete Jewish Bible", "CJB"),
    Version('https://www.bible.com/bible/42/GEN.1.CPDV', "Catholic Public Domain Version", "CPDV"),
    Version('https://www.bible.com/bible/1713/GEN.1.CSB', "Christian Standard Bible", "CSB"),
    Version('https://www.bible.com/bible/478/GEN.1.DARBY', "Darby's Translation 1890", "DARBY"),
    Version('https://www.bible.com/bible/55/GEN.1.DRC1752', "Douay-Rheims Challoner Revision 1752", "DRC1752"),
    Version('https://www.bible.com/bible/2079/GEN.1.EASY', "EasyEnglish Bible 2018", "EASY"),
    Version('https://www.bible.com/bible/406/GEN.1.ERV', " Easy-to-Read Version", "ERV"),
    Version('https://www.bible.com/bible/59/GEN.1.ESV', "English Standard Version", "ESV"),
    Version('https://www.bible.com/bible/1932/GEN.1.FBVNTPSALMS', "Free Bible Version New Testament with Psalms",
            "FBVNTPSALMS"),
    Version('https://www.bible.com/bible/296/GEN.1.GNB', "Good News Bible", "GNB"),
    Version('https://www.bible.com/bible/416/GEN.1.GNBDC', "Good News Bible (Anglicised)", "GNBDC"),
    Version('https://www.bible.com/bible/431/GEN.1.GNBDK', "Good News Bible (Catholic edition in Septuagint order)",
            "GNBDK"),
    Version('https://www.bible.com/bible/68/GEN.1.GNT', "Good News Translation", "GNT"),
    Version('https://www.bible.com/bible/69/GEN.1.GNTD', "Good News Translation (US Version)", "GNTD"),
    Version('https://www.bible.com/bible/2163/GEN.1.GNV', "Geneva Bible", "GNV"),
    Version('https://www.bible.com/bible/70/GEN.1.GW', "GOD'S WORD Translation", "GW"),
    Version('https://www.bible.com/bible/1047/GEN.1.GWC', "St Paul from the Trenches 1916", "GWC"),
    Version('https://www.bible.com/bible/72/GEN.1.HCSB', "Holman Christian Standard Bible", "HCSB"),
    Version('https://www.bible.com/bible/1359/GEN.1.ICB', "International Children’s Bible", "ICB"),
    Version('https://www.bible.com/bible/1077/GEN.1.JUB', "Jubilee Bible", "JUB"),
    Version('https://www.bible.com/bible/1/GEN.1.KJV', "King James Version", "KJV"),
    Version('https://www.bible.com/bible/546/GEN.1.KJVA', "King James Version with Apocrypha, American Edition",
            "KJVA"),
    Version('https://www.bible.com/bible/547/GEN.1.KJVA', "King James Version, American Edition", "KJVA"),
    Version('https://www.bible.com/bible/90/GEN.1.LEB', "Lexham English Bible", "LEB"),
    Version('https://www.bible.com/bible/1171/GEN.1.MEV', "Modern English Version", "MEV"),
    Version('https://www.bible.com/bible/1365/GEN.1.MP1650', "Metrical Psalms 1650", "MP1650"),
    Version('https://www.bible.com/bible/97/GEN.1.MSG', "The Message", "MSG"),
    Version('https://www.bible.com/bible/463/GEN.1.NABRE', "New American Bible, revised edition", "NABRE"),
    Version('https://www.bible.com/bible/100/GEN.1.NASB', "New American Standard Bible", "NASB"),
    Version('https://www.bible.com/bible/105/GEN.1.NCV', "New Century Version", "NCV"),
    Version('https://www.bible.com/bible/107/GEN.1.NET', "New English Translation", "NET"),
    Version('https://www.bible.com/bible/110/GEN.1.NIRV', "New International Reader’s Version", "NIRV"),
    Version('https://www.bible.com/bible/111/GEN.1.NIV', "New International Version", "NIV"),
    Version('https://www.bible.com/bible/113/GEN.1.NIVUK', "New International Version (Anglicised)", "NIVUK"),
    Version('https://www.bible.com/bible/114/GEN.1.NKJV', "New King James Version", "NKJV"),
    Version('https://www.bible.com/bible/116/GEN.1.NLT', "New Living Translation", "NLT"),
    Version('https://www.bible.com/bible/2135/GEN.1.NMV', "New Messianic Version Bible", "NMV"),
    Version('https://www.bible.com/bible/2016/GEN.1.NRSV', "New Revised Standard Version", "NRSV"),
    Version('https://www.bible.com/bible/2015/GEN.1.NRSV-CI', "New Revised Standard Version Catholic Interconfessional",
            "NRSV-CI"),
    Version('https://www.bible.com/bible/130/GEN.1.OJB', "Orthodox Jewish Bible", "OJB"),
    Version('https://www.bible.com/bible/2020/GEN.1.RSV', "Revised Standard Version", "RSV"),
    Version('https://www.bible.com/bible/2017/GEN.1.RSV-CI', "Revised Standard Version", "RSV-CI"),
    Version('https://www.bible.com/bible/477/GEN.1.RV1885', "Revised Version 1885", "RV1885"),
    Version('https://www.bible.com/bible/1922/GEN.1.RV1895', "Revised Version with Apocrypha 1895", "RV1895"),
    Version('https://www.bible.com/bible/314/GEN.1.TLV', "Tree of Life Version", "TLV"),
    Version('https://www.bible.com/bible/1849/GEN.1.TPT', "The Passion Translation", "TPT"),
    Version('https://www.bible.com/bible/316/GEN.1.TS2009', "The Scriptures 2009", "TS2009"),
    Version('https://www.bible.com/bible/2407/GEN.1.WBMS', "Wycliffe's Bible with Modern Spelling", "WBMS"),
    Version('https://www.bible.com/bible/206/GEN.1.WEB', "World English Bible", "WEB"),
    Version('https://www.bible.com/bible/1204/GEN.1.WEBBE', "World English Bible British Edition", "WEBBE"),
    Version('https://www.bible.com/bible/1209/GEN.1.WMB', "World Messianic Bible", "WMB"),
    Version('https://www.bible.com/bible/1207/GEN.1.WMBBE', "World Messianic Bible British Edition", "WMBBE"),
    Version('https://www.bible.com/bible/821/GEN.1.YLT1898', "Young's Literal Translation 3rd Revision 1898",
            "YLT1898"),
)

versions_map = {
    'https://www.bible.com/bible/1588/GEN.1.AMP': ("Amplified Bible", "AMP"),
    'https://www.bible.com/bible/8/GEN.1.AMPC': ("Amplified Bible, Classic Edition", "AMPC"),
    'https://www.bible.com/bible/12/GEN.1.ASV': ("American Standard Version", "ASV"),
    'https://www.bible.com/bible/31/GEN.1.BOOKS': ("The Books of the Bible NT", "BOOKS"),
    'https://www.bible.com/bible/37/GEN.1.CEB': ("Common English Bible", "CEB"),
    'https://www.bible.com/bible/392/GEN.1.CEV': ("Contemporary English Version", "CEV"),
    'https://www.bible.com/bible/303/GEN.1.CEVDCI': (
    "Contemporary English Version Interconfessional Edition", "CEVDCI"),
    'https://www.bible.com/bible/294/GEN.1.CEVUK': ("Contemporary English Version (Anglicised) 2012", "CEVUK"),
    'https://www.bible.com/bible/1275/GEN.1.CJB': ("Complete Jewish Bible", "CJB"),
    'https://www.bible.com/bible/42/GEN.1.CPDV': ("Catholic Public Domain Version", "CPDV"),
    'https://www.bible.com/bible/1713/GEN.1.CSB': ("Christian Standard Bible", "CSB"),
    'https://www.bible.com/bible/478/GEN.1.DARBY': ("Darby's Translation 1890", "DARBY"),
    'https://www.bible.com/bible/55/GEN.1.DRC1752': ("Douay-Rheims Challoner Revision 1752", "DRC1752"),
    'https://www.bible.com/bible/2079/GEN.1.EASY': ("EasyEnglish Bible 2018", "EASY"),
    'https://www.bible.com/bible/406/GEN.1.ERV': (" Easy-to-Read Version", "ERV"),
    'https://www.bible.com/bible/59/GEN.1.ESV': ("English Standard Version", "ESV"),
    'https://www.bible.com/bible/1932/GEN.1.FBVNTPSALMS': (
    "Free Bible Version New Testament with Psalms", "FBVNTPSALMS"),
    'https://www.bible.com/bible/296/GEN.1.GNB': ("Good News Bible", "GNB"),
    'https://www.bible.com/bible/416/GEN.1.GNBDC': ("Good News Bible (Anglicised)", "GNBDC"),
    'https://www.bible.com/bible/431/GEN.1.GNBDK': ("Good News Bible (Catholic edition in Septuagint order)", "GNBDK"),
    'https://www.bible.com/bible/68/GEN.1.GNT': ("Good News Translation", "GNT"),
    'https://www.bible.com/bible/69/GEN.1.GNTD': ("Good News Translation (US Version)", "GNTD"),
    'https://www.bible.com/bible/2163/GEN.1.GNV': ("Geneva Bible", "GNV"),
    'https://www.bible.com/bible/70/GEN.1.GW': ("GOD'S WORD Translation", "GW"),
    'https://www.bible.com/bible/1047/GEN.1.GWC': ("St Paul from the Trenches 1916", "GWC"),
    'https://www.bible.com/bible/72/GEN.1.HCSB': ("Holman Christian Standard Bible", "HCSB"),
    'https://www.bible.com/bible/1359/GEN.1.ICB': ("International Children’s Bible", "ICB"),
    'https://www.bible.com/bible/1077/GEN.1.JUB': ("Jubilee Bible", "JUB"),
    'https://www.bible.com/bible/1/GEN.1.KJV': ("King James Version", "KJV"),
    'https://www.bible.com/bible/546/GEN.1.KJVA': ("King James Version with Apocrypha, American Edition", "KJVA"),
    'https://www.bible.com/bible/547/GEN.1.KJVA': ("King James Version, American Edition", "KJVA"),
    'https://www.bible.com/bible/90/GEN.1.LEB': ("Lexham English Bible", "LEB"),
    'https://www.bible.com/bible/1171/GEN.1.MEV': ("Modern English Version", "MEV"),
    'https://www.bible.com/bible/1365/GEN.1.MP1650': ("Metrical Psalms 1650", "MP1650"),
    'https://www.bible.com/bible/97/GEN.1.MSG': ("The Message", "MSG"),
    'https://www.bible.com/bible/463/GEN.1.NABRE': ("New American Bible, revised edition", "NABRE"),
    'https://www.bible.com/bible/100/GEN.1.NASB': ("New American Standard Bible", "NASB"),
    'https://www.bible.com/bible/105/GEN.1.NCV': ("New Century Version", "NCV"),
    'https://www.bible.com/bible/107/GEN.1.NET': ("New English Translation", "NET"),
    'https://www.bible.com/bible/110/GEN.1.NIRV': ("New International Reader’s Version", "NIRV"),
    'https://www.bible.com/bible/111/GEN.1.NIV': ("New International Version", "NIV"),
    'https://www.bible.com/bible/113/GEN.1.NIVUK': ("New International Version (Anglicised)", "NIVUK"),
    'https://www.bible.com/bible/114/GEN.1.NKJV': ("New King James Version", "NKJV"),
    'https://www.bible.com/bible/116/GEN.1.NLT': ("New Living Translation", "NLT"),
    'https://www.bible.com/bible/2135/GEN.1.NMV': ("New Messianic Version Bible", "NMV"),
    'https://www.bible.com/bible/2016/GEN.1.NRSV': ("New Revised Standard Version", "NRSV"),
    'https://www.bible.com/bible/2015/GEN.1.NRSV-CI': (
    "New Revised Standard Version Catholic Interconfessional", "NRSV-CI"),
    'https://www.bible.com/bible/130/GEN.1.OJB': ("Orthodox Jewish Bible", "OJB"),
    'https://www.bible.com/bible/2020/GEN.1.RSV': ("Revised Standard Version", "RSV"),
    'https://www.bible.com/bible/2017/GEN.1.RSV-CI': ("Revised Standard Version", "RSV-CI"),
    'https://www.bible.com/bible/477/GEN.1.RV1885': ("Revised Version 1885", "RV1885"),
    'https://www.bible.com/bible/1922/GEN.1.RV1895': ("Revised Version with Apocrypha 1895", "RV1895"),
    'https://www.bible.com/bible/314/GEN.1.TLV': ("Tree of Life Version", "TLV"),
    'https://www.bible.com/bible/1849/GEN.1.TPT': ("The Passion Translation", "TPT"),
    'https://www.bible.com/bible/316/GEN.1.TS2009': ("The Scriptures 2009", "TS2009"),
    'https://www.bible.com/bible/2407/GEN.1.WBMS': ("Wycliffe's Bible with Modern Spelling", "WBMS"),
    'https://www.bible.com/bible/206/GEN.1.WEB': ("World English Bible", "WEB"),
    'https://www.bible.com/bible/1204/GEN.1.WEBBE': ("World English Bible British Edition", "WEBBE"),
    'https://www.bible.com/bible/1209/GEN.1.WMB': ("World Messianic Bible", "WMB"),
    'https://www.bible.com/bible/1207/GEN.1.WMBBE': ("World Messianic Bible British Edition", "WMBBE"),
    'https://www.bible.com/bible/821/GEN.1.YLT1898': ("Young's Literal Translation 3rd Revision 1898", "YLT1898"),

}

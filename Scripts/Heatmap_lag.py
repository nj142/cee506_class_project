#!/usr/bin/env python
# coding: utf-8

# In[1]:


total_avg_temp = [{'Year': 2001, 'Month': 'June', 'Avg_temp': 5.4097466},
 {'Year': 2001, 'Month': 'July', 'Avg_temp': 8.217645},
 {'Year': 2001, 'Month': 'August', 'Avg_temp': 7.877105},
 {'Year': 2001, 'Month': 'September', 'Avg_temp': 5.3338203},
 {'Year': 2001, 'Month': 'October', 'Avg_temp': 1.8484143},
 {'Year': 2001, 'Month': 'November', 'Avg_temp': -0.33630937},
 {'Year': 2001, 'Month': 'December', 'Avg_temp': -1.7121394},
 {'Year': 2001, 'Month': 'January', 'Avg_temp': -10.584751},
 {'Year': 2001, 'Month': 'February', 'Avg_temp': -5.642348},
 {'Year': 2001, 'Month': 'March', 'Avg_temp': -13.970791},
 {'Year': 2001, 'Month': 'April', 'Avg_temp': -6.626254},
 {'Year': 2001, 'Month': 'May', 'Avg_temp': -2.0598269},
 {'Year': 2001, 'Month': 'June', 'Avg_temp': 5.0365143},
 {'Year': 2002, 'Month': 'June', 'Avg_temp': 5.0365143},
 {'Year': 2002, 'Month': 'July', 'Avg_temp': 6.8589063},
 {'Year': 2002, 'Month': 'August', 'Avg_temp': 7.024844},
 {'Year': 2002, 'Month': 'September', 'Avg_temp': 5.2756495},
 {'Year': 2002, 'Month': 'October', 'Avg_temp': 0.08494436},
 {'Year': 2002, 'Month': 'November', 'Avg_temp': -2.9047754},
 {'Year': 2002, 'Month': 'December', 'Avg_temp': -20.829111},
 {'Year': 2002, 'Month': 'January', 'Avg_temp': -21.316244},
 {'Year': 2002, 'Month': 'February', 'Avg_temp': -16.807522},
 {'Year': 2002, 'Month': 'March', 'Avg_temp': -6.0401907},
 {'Year': 2002, 'Month': 'April', 'Avg_temp': -4.5120006},
 {'Year': 2002, 'Month': 'May', 'Avg_temp': 2.5585911},
 {'Year': 2002, 'Month': 'June', 'Avg_temp': 5.9386826},
 {'Year': 2003, 'Month': 'June', 'Avg_temp': 5.9386826},
 {'Year': 2003, 'Month': 'July', 'Avg_temp': 8.382964},
 {'Year': 2003, 'Month': 'August', 'Avg_temp': 8.75158},
 {'Year': 2003, 'Month': 'September', 'Avg_temp': 6.8233957},
 {'Year': 2003, 'Month': 'October', 'Avg_temp': 3.5563848},
 {'Year': 2003, 'Month': 'November', 'Avg_temp': -0.5712766},
 {'Year': 2003, 'Month': 'December', 'Avg_temp': -4.523753},
 {'Year': 2003, 'Month': 'January', 'Avg_temp': -12.354344},
 {'Year': 2003, 'Month': 'February', 'Avg_temp': -17.615503},
 {'Year': 2003, 'Month': 'March', 'Avg_temp': -12.26644},
 {'Year': 2003, 'Month': 'April', 'Avg_temp': -2.3227983},
 {'Year': 2003, 'Month': 'May', 'Avg_temp': 1.7792091},
 {'Year': 2003, 'Month': 'June', 'Avg_temp': 6.3388233},
 {'Year': 2004, 'Month': 'June', 'Avg_temp': 6.3388233},
 {'Year': 2004, 'Month': 'July', 'Avg_temp': 8.632833},
 {'Year': 2004, 'Month': 'August', 'Avg_temp': 8.931745},
 {'Year': 2004, 'Month': 'September', 'Avg_temp': 6.148286},
 {'Year': 2004, 'Month': 'October', 'Avg_temp': 2.9510765},
 {'Year': 2004, 'Month': 'November', 'Avg_temp': -0.83148944},
 {'Year': 2004, 'Month': 'December', 'Avg_temp': -10.754411},
 {'Year': 2004, 'Month': 'January', 'Avg_temp': -13.578468},
 {'Year': 2004, 'Month': 'February', 'Avg_temp': -17.682327},
 {'Year': 2004, 'Month': 'March', 'Avg_temp': -13.449618},
 {'Year': 2004, 'Month': 'April', 'Avg_temp': -4.896858},
 {'Year': 2004, 'Month': 'May', 'Avg_temp': 2.74943},
 {'Year': 2004, 'Month': 'June', 'Avg_temp': 6.6506634},
 {'Year': 2005, 'Month': 'June', 'Avg_temp': 6.6506634},
 {'Year': 2005, 'Month': 'July', 'Avg_temp': 10.114561},
 {'Year': 2005, 'Month': 'August', 'Avg_temp': 9.725485},
 {'Year': 2005, 'Month': 'September', 'Avg_temp': 6.32723},
 {'Year': 2005, 'Month': 'October', 'Avg_temp': 3.629316},
 {'Year': 2005, 'Month': 'November', 'Avg_temp': -0.49560508},
 {'Year': 2005, 'Month': 'December', 'Avg_temp': -7.451108},
 {'Year': 2005, 'Month': 'January', 'Avg_temp': -10.188564},
 {'Year': 2005, 'Month': 'February', 'Avg_temp': -18.106813},
 {'Year': 2005, 'Month': 'March', 'Avg_temp': -12.597992},
 {'Year': 2005, 'Month': 'April', 'Avg_temp': -11.368248},
 {'Year': 2005, 'Month': 'May', 'Avg_temp': 1.455485},
 {'Year': 2005, 'Month': 'June', 'Avg_temp': 6.4462733},
 {'Year': 2006, 'Month': 'June', 'Avg_temp': 6.4462733},
 {'Year': 2006, 'Month': 'July', 'Avg_temp': 9.025567},
 {'Year': 2006, 'Month': 'August', 'Avg_temp': 8.894059},
 {'Year': 2006, 'Month': 'September', 'Avg_temp': 6.6862507},
 {'Year': 2006, 'Month': 'October', 'Avg_temp': 2.5404968},
 {'Year': 2006, 'Month': 'November', 'Avg_temp': -3.2404745},
 {'Year': 2006, 'Month': 'December', 'Avg_temp': -19.434885},
 {'Year': 2006, 'Month': 'January', 'Avg_temp': -25.769815},
 {'Year': 2006, 'Month': 'February', 'Avg_temp': -12.105622},
 {'Year': 2006, 'Month': 'March', 'Avg_temp': -12.78111},
 {'Year': 2006, 'Month': 'April', 'Avg_temp': -13.915387},
 {'Year': 2006, 'Month': 'May', 'Avg_temp': 0.537199},
 {'Year': 2006, 'Month': 'June', 'Avg_temp': 4.5741553},
 {'Year': 2007, 'Month': 'June', 'Avg_temp': 4.5741553},
 {'Year': 2007, 'Month': 'July', 'Avg_temp': 7.9355907},
 {'Year': 2007, 'Month': 'August', 'Avg_temp': 8.262979},
 {'Year': 2007, 'Month': 'September', 'Avg_temp': 6.5946074},
 {'Year': 2007, 'Month': 'October', 'Avg_temp': 3.99117},
 {'Year': 2007, 'Month': 'November', 'Avg_temp': -0.25463226},
 {'Year': 2007, 'Month': 'December', 'Avg_temp': -10.94538},
 {'Year': 2007, 'Month': 'January', 'Avg_temp': -17.785202},
 {'Year': 2007, 'Month': 'February', 'Avg_temp': -9.408852},
 {'Year': 2007, 'Month': 'March', 'Avg_temp': -18.814636},
 {'Year': 2007, 'Month': 'April', 'Avg_temp': -6.940701},
 {'Year': 2007, 'Month': 'May', 'Avg_temp': 0.97539455},
 {'Year': 2007, 'Month': 'June', 'Avg_temp': 5.226213},
 {'Year': 2008, 'Month': 'June', 'Avg_temp': 5.226213},
 {'Year': 2008, 'Month': 'July', 'Avg_temp': 8.931126},
 {'Year': 2008, 'Month': 'August', 'Avg_temp': 10.136293},
 {'Year': 2008, 'Month': 'September', 'Avg_temp': 8.410982},
 {'Year': 2008, 'Month': 'October', 'Avg_temp': 2.5015469},
 {'Year': 2008, 'Month': 'November', 'Avg_temp': -0.6714986},
 {'Year': 2008, 'Month': 'December', 'Avg_temp': -5.666407},
 {'Year': 2008, 'Month': 'January', 'Avg_temp': -18.416307},
 {'Year': 2008, 'Month': 'February', 'Avg_temp': -21.918097},
 {'Year': 2008, 'Month': 'March', 'Avg_temp': -18.35386},
 {'Year': 2008, 'Month': 'April', 'Avg_temp': -8.300801},
 {'Year': 2008, 'Month': 'May', 'Avg_temp': 0.10169587},
 {'Year': 2008, 'Month': 'June', 'Avg_temp': 4.378625},
 {'Year': 2009, 'Month': 'June', 'Avg_temp': 4.378625},
 {'Year': 2009, 'Month': 'July', 'Avg_temp': 6.8456173},
 {'Year': 2009, 'Month': 'August', 'Avg_temp': 7.660202},
 {'Year': 2009, 'Month': 'September', 'Avg_temp': 6.361898},
 {'Year': 2009, 'Month': 'October', 'Avg_temp': 0.5627954},
 {'Year': 2009, 'Month': 'November', 'Avg_temp': -3.715251},
 {'Year': 2009, 'Month': 'December', 'Avg_temp': -9.376597},
 {'Year': 2009, 'Month': 'January', 'Avg_temp': -20.245045},
 {'Year': 2009, 'Month': 'February', 'Avg_temp': -17.43515},
 {'Year': 2009, 'Month': 'March', 'Avg_temp': -15.88515},
 {'Year': 2009, 'Month': 'April', 'Avg_temp': -7.477461},
 {'Year': 2009, 'Month': 'May', 'Avg_temp': 0.91595834},
 {'Year': 2009, 'Month': 'June', 'Avg_temp': 5.2202682},
 {'Year': 2010, 'Month': 'June', 'Avg_temp': 5.2202682},
 {'Year': 2010, 'Month': 'July', 'Avg_temp': 7.9027114},
 {'Year': 2010, 'Month': 'August', 'Avg_temp': 8.840032},
 {'Year': 2010, 'Month': 'September', 'Avg_temp': 5.832271},
 {'Year': 2010, 'Month': 'October', 'Avg_temp': 3.0293045},
 {'Year': 2010, 'Month': 'November', 'Avg_temp': -4.8902073},
 {'Year': 2010, 'Month': 'December', 'Avg_temp': -9.887342},
 {'Year': 2010, 'Month': 'January', 'Avg_temp': -19.539417},
 {'Year': 2010, 'Month': 'February', 'Avg_temp': -16.585154},
 {'Year': 2010, 'Month': 'March', 'Avg_temp': -20.67306},
 {'Year': 2010, 'Month': 'April', 'Avg_temp': -9.326827},
 {'Year': 2010, 'Month': 'May', 'Avg_temp': 0.69008493},
 {'Year': 2010, 'Month': 'June', 'Avg_temp': 3.9448676},
 {'Year': 2011, 'Month': 'June', 'Avg_temp': 3.9448676},
 {'Year': 2011, 'Month': 'July', 'Avg_temp': 8.34787},
 {'Year': 2011, 'Month': 'August', 'Avg_temp': 9.388893},
 {'Year': 2011, 'Month': 'September', 'Avg_temp': 7.786659},
 {'Year': 2011, 'Month': 'October', 'Avg_temp': 2.6585367},
 {'Year': 2011, 'Month': 'November', 'Avg_temp': -1.1300685},
 {'Year': 2011, 'Month': 'December', 'Avg_temp': -6.8761244},
 {'Year': 2011, 'Month': 'January', 'Avg_temp': -13.742546},
 {'Year': 2011, 'Month': 'February', 'Avg_temp': -12.685477},
 {'Year': 2011, 'Month': 'March', 'Avg_temp': -10.090178},
 {'Year': 2011, 'Month': 'April', 'Avg_temp': -9.074328},
 {'Year': 2011, 'Month': 'May', 'Avg_temp': 1.5679578},
 {'Year': 2011, 'Month': 'June', 'Avg_temp': 5.445138},
 {'Year': 2012, 'Month': 'June', 'Avg_temp': 5.445138},
 {'Year': 2012, 'Month': 'July', 'Avg_temp': 6.681894},
 {'Year': 2012, 'Month': 'August', 'Avg_temp': 7.1737304},
 {'Year': 2012, 'Month': 'September', 'Avg_temp': 5.6371017},
 {'Year': 2012, 'Month': 'October', 'Avg_temp': 2.2866335},
 {'Year': 2012, 'Month': 'November', 'Avg_temp': -3.9391313},
 {'Year': 2012, 'Month': 'December', 'Avg_temp': -13.077229},
 {'Year': 2012, 'Month': 'January', 'Avg_temp': -25.14576},
 {'Year': 2012, 'Month': 'February', 'Avg_temp': -16.066849},
 {'Year': 2012, 'Month': 'March', 'Avg_temp': -20.838469},
 {'Year': 2012, 'Month': 'April', 'Avg_temp': -8.380454},
 {'Year': 2012, 'Month': 'May', 'Avg_temp': -1.652326},
 {'Year': 2012, 'Month': 'June', 'Avg_temp': 4.878592},
 {'Year': 2013, 'Month': 'June', 'Avg_temp': 4.878592},
 {'Year': 2013, 'Month': 'July', 'Avg_temp': 7.7802777},
 {'Year': 2013, 'Month': 'August', 'Avg_temp': 8.351248},
 {'Year': 2013, 'Month': 'September', 'Avg_temp': 4.0942097},
 {'Year': 2013, 'Month': 'October', 'Avg_temp': 1.960774},
 {'Year': 2013, 'Month': 'November', 'Avg_temp': -2.6515613},
 {'Year': 2013, 'Month': 'December', 'Avg_temp': -13.981627},
 {'Year': 2013, 'Month': 'January', 'Avg_temp': -13.936165},
 {'Year': 2013, 'Month': 'February', 'Avg_temp': -23.491789},
 {'Year': 2013, 'Month': 'March', 'Avg_temp': -13.871995},
 {'Year': 2013, 'Month': 'April', 'Avg_temp': -7.307595},
 {'Year': 2013, 'Month': 'May', 'Avg_temp': -0.4307462},
 {'Year': 2013, 'Month': 'June', 'Avg_temp': 5.4317427},
 {'Year': 2014, 'Month': 'June', 'Avg_temp': 5.4317427},
 {'Year': 2014, 'Month': 'July', 'Avg_temp': 7.914892},
 {'Year': 2014, 'Month': 'August', 'Avg_temp': 9.212626},
 {'Year': 2014, 'Month': 'September', 'Avg_temp': 5.9122224},
 {'Year': 2014, 'Month': 'October', 'Avg_temp': 3.8602712},
 {'Year': 2014, 'Month': 'November', 'Avg_temp': -1.0418422},
 {'Year': 2014, 'Month': 'December', 'Avg_temp': -5.6148257},
 {'Year': 2014, 'Month': 'January', 'Avg_temp': -9.625387},
 {'Year': 2014, 'Month': 'February', 'Avg_temp': -12.644461},
 {'Year': 2014, 'Month': 'March', 'Avg_temp': -15.127072},
 {'Year': 2014, 'Month': 'April', 'Avg_temp': -4.409886},
 {'Year': 2014, 'Month': 'May', 'Avg_temp': 1.7748549},
 {'Year': 2014, 'Month': 'June', 'Avg_temp': 4.790356},
 {'Year': 2015, 'Month': 'June', 'Avg_temp': 4.790356},
 {'Year': 2015, 'Month': 'July', 'Avg_temp': 8.535373},
 {'Year': 2015, 'Month': 'August', 'Avg_temp': 10.757177},
 {'Year': 2015, 'Month': 'September', 'Avg_temp': 9.018251},
 {'Year': 2015, 'Month': 'October', 'Avg_temp': 2.3270102},
 {'Year': 2015, 'Month': 'November', 'Avg_temp': 0.63389605},
 {'Year': 2015, 'Month': 'December', 'Avg_temp': -4.7382517},
 {'Year': 2015, 'Month': 'January', 'Avg_temp': -9.419769},
 {'Year': 2015, 'Month': 'February', 'Avg_temp': -10.554323},
 {'Year': 2015, 'Month': 'March', 'Avg_temp': -15.276093},
 {'Year': 2015, 'Month': 'April', 'Avg_temp': -8.095114},
 {'Year': 2015, 'Month': 'May', 'Avg_temp': 2.2549112},
 {'Year': 2015, 'Month': 'June', 'Avg_temp': 5.2157536},
 {'Year': 2016, 'Month': 'June', 'Avg_temp': 5.2157536},
 {'Year': 2016, 'Month': 'July', 'Avg_temp': 8.9552},
 {'Year': 2016, 'Month': 'August', 'Avg_temp': 8.788336},
 {'Year': 2016, 'Month': 'September', 'Avg_temp': 6.144041},
 {'Year': 2016, 'Month': 'October', 'Avg_temp': 3.5435731},
 {'Year': 2016, 'Month': 'November', 'Avg_temp': -0.6881164},
 {'Year': 2016, 'Month': 'December', 'Avg_temp': -8.192713},
 {'Year': 2016, 'Month': 'January', 'Avg_temp': -9.130688},
 {'Year': 2016, 'Month': 'February', 'Avg_temp': -10.816253},
 {'Year': 2016, 'Month': 'March', 'Avg_temp': -16.427372},
 {'Year': 2016, 'Month': 'April', 'Avg_temp': -3.7337847},
 {'Year': 2016, 'Month': 'May', 'Avg_temp': 3.136929},
 {'Year': 2016, 'Month': 'June', 'Avg_temp': 6.4814034},
 {'Year': 2017, 'Month': 'June', 'Avg_temp': 6.4814034},
 {'Year': 2017, 'Month': 'July', 'Avg_temp': 10.114322},
 {'Year': 2017, 'Month': 'August', 'Avg_temp': 9.982373},
 {'Year': 2017, 'Month': 'September', 'Avg_temp': 7.7531285},
 {'Year': 2017, 'Month': 'October', 'Avg_temp': 5.90342},
 {'Year': 2017, 'Month': 'November', 'Avg_temp': -1.0793314},
 {'Year': 2017, 'Month': 'December', 'Avg_temp': -2.9976833},
 {'Year': 2017, 'Month': 'January', 'Avg_temp': -9.62602},
 {'Year': 2017, 'Month': 'February', 'Avg_temp': -16.325409},
 {'Year': 2017, 'Month': 'March', 'Avg_temp': -12.962978},
 {'Year': 2017, 'Month': 'April', 'Avg_temp': -2.8940709},
 {'Year': 2017, 'Month': 'May', 'Avg_temp': 1.8900373},
 {'Year': 2017, 'Month': 'June', 'Avg_temp': 6.644635},
 {'Year': 2018, 'Month': 'June', 'Avg_temp': 6.644635},
 {'Year': 2018, 'Month': 'July', 'Avg_temp': 9.1868},
 {'Year': 2018, 'Month': 'August', 'Avg_temp': 8.662188},
 {'Year': 2018, 'Month': 'September', 'Avg_temp': 6.1768217},
 {'Year': 2018, 'Month': 'October', 'Avg_temp': 3.2999792},
 {'Year': 2018, 'Month': 'November', 'Avg_temp': 0.8758048},
 {'Year': 2018, 'Month': 'December', 'Avg_temp': -1.4203005},
 {'Year': 2018, 'Month': 'January', 'Avg_temp': -6.9531264},
 {'Year': 2018, 'Month': 'February', 'Avg_temp': -4.058149},
 {'Year': 2018, 'Month': 'March', 'Avg_temp': -5.210637},
 {'Year': 2018, 'Month': 'April', 'Avg_temp': -0.89771146},
 {'Year': 2018, 'Month': 'May', 'Avg_temp': 1.4952558},
 {'Year': 2018, 'Month': 'June', 'Avg_temp': 5.709069},
 {'Year': 2019, 'Month': 'June', 'Avg_temp': 5.709069},
 {'Year': 2019, 'Month': 'July', 'Avg_temp': 9.241908},
 {'Year': 2019, 'Month': 'August', 'Avg_temp': 9.606358},
 {'Year': 2019, 'Month': 'September', 'Avg_temp': 8.619229},
 {'Year': 2019, 'Month': 'October', 'Avg_temp': 5.2317843},
 {'Year': 2019, 'Month': 'November', 'Avg_temp': 0.16236708},
 {'Year': 2019, 'Month': 'December', 'Avg_temp': -10.329429},
 {'Year': 2019, 'Month': 'January', 'Avg_temp': -12.752173},
 {'Year': 2019, 'Month': 'February', 'Avg_temp': -2.35333},
 {'Year': 2019, 'Month': 'March', 'Avg_temp': -3.4681716},
 {'Year': 2019, 'Month': 'April', 'Avg_temp': -3.25713},
 {'Year': 2019, 'Month': 'May', 'Avg_temp': 2.24764},
 {'Year': 2019, 'Month': 'June', 'Avg_temp': 6.4928484},
 {'Year': 2020, 'Month': 'June', 'Avg_temp': 6.4928484},
 {'Year': 2020, 'Month': 'July', 'Avg_temp': 10.598556},
 {'Year': 2020, 'Month': 'August', 'Avg_temp': 10.4001875},
 {'Year': 2020, 'Month': 'September', 'Avg_temp': 8.472397},
 {'Year': 2020, 'Month': 'October', 'Avg_temp': 4.0500283},
 {'Year': 2020, 'Month': 'November', 'Avg_temp': -0.6434326},
 {'Year': 2020, 'Month': 'December', 'Avg_temp': -4.8027124},
 {'Year': 2020, 'Month': 'January', 'Avg_temp': -18.014906},
 {'Year': 2020, 'Month': 'February', 'Avg_temp': -20.609003},
 {'Year': 2020, 'Month': 'March', 'Avg_temp': -8.668226},
 {'Year': 2020, 'Month': 'April', 'Avg_temp': -3.8674557},
 {'Year': 2020, 'Month': 'May', 'Avg_temp': 2.5895548},
 {'Year': 2020, 'Month': 'June', 'Avg_temp': 5.9047556},
 {'Year': 2021, 'Month': 'June', 'Avg_temp': 5.9047556},
 {'Year': 2021, 'Month': 'July', 'Avg_temp': 7.656275},
 {'Year': 2021, 'Month': 'August', 'Avg_temp': 9.131674},
 {'Year': 2021, 'Month': 'September', 'Avg_temp': 6.9827504},
 {'Year': 2021, 'Month': 'October', 'Avg_temp': 4.4435496},
 {'Year': 2021, 'Month': 'November', 'Avg_temp': 0.7646322},
 {'Year': 2021, 'Month': 'December', 'Avg_temp': -4.9281273},
 {'Year': 2021, 'Month': 'January', 'Avg_temp': -16.859837},
 {'Year': 2021, 'Month': 'February', 'Avg_temp': -18.286959},
 {'Year': 2021, 'Month': 'March', 'Avg_temp': -13.033643},
 {'Year': 2021, 'Month': 'April', 'Avg_temp': -5.3982053},
 {'Year': 2021, 'Month': 'May', 'Avg_temp': 2.0012753},
 {'Year': 2021, 'Month': 'June', 'Avg_temp': 5.132063},
 {'Year': 2022, 'Month': 'June', 'Avg_temp': 5.132063},
 {'Year': 2022, 'Month': 'July', 'Avg_temp': 8.156776},
 {'Year': 2022, 'Month': 'August', 'Avg_temp': 7.916508},
 {'Year': 2022, 'Month': 'September', 'Avg_temp': 6.6222525},
 {'Year': 2022, 'Month': 'October', 'Avg_temp': 1.6237544},
 {'Year': 2022, 'Month': 'November', 'Avg_temp': -4.9274416},
 {'Year': 2022, 'Month': 'December', 'Avg_temp': -8.936593},
 {'Year': 2022, 'Month': 'January', 'Avg_temp': -20.298811},
 {'Year': 2022, 'Month': 'February', 'Avg_temp': -16.206604},
 {'Year': 2022, 'Month': 'March', 'Avg_temp': -10.760368},
 {'Year': 2022, 'Month': 'April', 'Avg_temp': -3.969476},
 {'Year': 2022, 'Month': 'May', 'Avg_temp': 2.1855638},
 {'Year': 2022, 'Month': 'June', 'Avg_temp': 5.5237203}]


# In[2]:


ao_indices = {2001: [{'month_name': 'June', 'month_value': 0.586},
  {'month_name': 'July', 'month_value': -0.649},
  {'month_name': 'August', 'month_value': 0.14400000000000002},
  {'month_name': 'September', 'month_value': 0.395},
  {'month_name': 'October', 'month_value': 0.317},
  {'month_name': 'November', 'month_value': -1.581},
  {'month_name': 'December', 'month_value': -2.354},
  {'month_name': 'December', 'month_value': -0.9590000000000001},
  {'month_name': 'February', 'month_value': -0.622},
  {'month_name': 'March', 'month_value': -1.6869999999999998},
  {'month_name': 'April', 'month_value': 0.9059999999999999},
  {'month_name': 'May', 'month_value': 0.452},
  {'month_name': 'June', 'month_value': -0.015}],
 2002: [{'month_name': 'June', 'month_value': -0.015},
  {'month_name': 'July', 'month_value': -0.031},
  {'month_name': 'August', 'month_value': 0.521},
  {'month_name': 'September', 'month_value': -0.7070000000000001},
  {'month_name': 'October', 'month_value': 0.7070000000000001},
  {'month_name': 'November', 'month_value': 0.8190000000000001},
  {'month_name': 'December', 'month_value': -1.3219999999999998},
  {'month_name': 'December', 'month_value': 1.381},
  {'month_name': 'February', 'month_value': 1.304},
  {'month_name': 'March', 'month_value': 0.902},
  {'month_name': 'April', 'month_value': 0.748},
  {'month_name': 'May', 'month_value': 0.401},
  {'month_name': 'June', 'month_value': 0.573}],
 2003: [{'month_name': 'June', 'month_value': 0.573},
  {'month_name': 'July', 'month_value': 0.32799999999999996},
  {'month_name': 'August', 'month_value': -0.22899999999999998},
  {'month_name': 'September', 'month_value': -0.043},
  {'month_name': 'October', 'month_value': -1.489},
  {'month_name': 'November', 'month_value': -1.425},
  {'month_name': 'December', 'month_value': -1.5919999999999999},
  {'month_name': 'December', 'month_value': -0.47200000000000003},
  {'month_name': 'February', 'month_value': 0.128},
  {'month_name': 'March', 'month_value': 0.9329999999999999},
  {'month_name': 'April', 'month_value': -0.17800000000000002},
  {'month_name': 'May', 'month_value': 1.0170000000000001},
  {'month_name': 'June', 'month_value': -0.102}],
 2004: [{'month_name': 'June', 'month_value': -0.102},
  {'month_name': 'July', 'month_value': 0.075},
  {'month_name': 'August', 'month_value': -0.28},
  {'month_name': 'September', 'month_value': 0.467},
  {'month_name': 'October', 'month_value': -0.67},
  {'month_name': 'November', 'month_value': 0.642},
  {'month_name': 'December', 'month_value': 0.265},
  {'month_name': 'December', 'month_value': -1.686},
  {'month_name': 'February', 'month_value': -1.528},
  {'month_name': 'March', 'month_value': 0.318},
  {'month_name': 'April', 'month_value': -0.409},
  {'month_name': 'May', 'month_value': -0.094},
  {'month_name': 'June', 'month_value': -0.23600000000000002}],
 2005: [{'month_name': 'June', 'month_value': -0.23600000000000002},
  {'month_name': 'July', 'month_value': -0.201},
  {'month_name': 'August', 'month_value': -0.72},
  {'month_name': 'September', 'month_value': 0.855},
  {'month_name': 'October', 'month_value': -0.515},
  {'month_name': 'November', 'month_value': 0.6779999999999999},
  {'month_name': 'December', 'month_value': 1.23},
  {'month_name': 'December', 'month_value': 0.35600000000000004},
  {'month_name': 'February', 'month_value': -1.271},
  {'month_name': 'March', 'month_value': -1.348},
  {'month_name': 'April', 'month_value': -0.046},
  {'month_name': 'May', 'month_value': -0.763},
  {'month_name': 'June', 'month_value': -0.38299999999999995}],
 2006: [{'month_name': 'June', 'month_value': -0.38299999999999995},
  {'month_name': 'July', 'month_value': -0.03},
  {'month_name': 'August', 'month_value': 0.026000000000000002},
  {'month_name': 'September', 'month_value': 0.802},
  {'month_name': 'October', 'month_value': 0.03},
  {'month_name': 'November', 'month_value': 0.228},
  {'month_name': 'December', 'month_value': -2.104},
  {'month_name': 'December', 'month_value': -0.17},
  {'month_name': 'February', 'month_value': -0.156},
  {'month_name': 'March', 'month_value': -1.604},
  {'month_name': 'April', 'month_value': 0.138},
  {'month_name': 'May', 'month_value': 0.156},
  {'month_name': 'June', 'month_value': 1.071}],
 2007: [{'month_name': 'June', 'month_value': 1.071},
  {'month_name': 'July', 'month_value': 0.10300000000000001},
  {'month_name': 'August', 'month_value': -0.265},
  {'month_name': 'September', 'month_value': 0.606},
  {'month_name': 'October', 'month_value': -1.0290000000000001},
  {'month_name': 'November', 'month_value': 0.521},
  {'month_name': 'December', 'month_value': 2.282},
  {'month_name': 'December', 'month_value': 2.0340000000000003},
  {'month_name': 'February', 'month_value': -1.307},
  {'month_name': 'March', 'month_value': 1.182},
  {'month_name': 'April', 'month_value': 0.544},
  {'month_name': 'May', 'month_value': 0.894},
  {'month_name': 'June', 'month_value': -0.555}],
 2008: [{'month_name': 'June', 'month_value': -0.555},
  {'month_name': 'July', 'month_value': -0.397},
  {'month_name': 'August', 'month_value': -0.034},
  {'month_name': 'September', 'month_value': 0.179},
  {'month_name': 'October', 'month_value': 0.38299999999999995},
  {'month_name': 'November', 'month_value': -0.519},
  {'month_name': 'December', 'month_value': 0.821},
  {'month_name': 'December', 'month_value': 0.8190000000000001},
  {'month_name': 'February', 'month_value': 0.938},
  {'month_name': 'March', 'month_value': 0.586},
  {'month_name': 'April', 'month_value': -0.455},
  {'month_name': 'May', 'month_value': -1.205},
  {'month_name': 'June', 'month_value': -0.09}],
 2009: [{'month_name': 'June', 'month_value': -0.09},
  {'month_name': 'July', 'month_value': -0.48},
  {'month_name': 'August', 'month_value': -0.08},
  {'month_name': 'September', 'month_value': -0.327},
  {'month_name': 'October', 'month_value': 1.676},
  {'month_name': 'November', 'month_value': 0.092},
  {'month_name': 'December', 'month_value': 0.648},
  {'month_name': 'December', 'month_value': 0.8},
  {'month_name': 'February', 'month_value': -0.672},
  {'month_name': 'March', 'month_value': 0.121},
  {'month_name': 'April', 'month_value': 0.973},
  {'month_name': 'May', 'month_value': 1.194},
  {'month_name': 'June', 'month_value': -1.351}],
 2010: [{'month_name': 'June', 'month_value': -1.351},
  {'month_name': 'July', 'month_value': -1.3559999999999999},
  {'month_name': 'August', 'month_value': -0.054000000000000006},
  {'month_name': 'September', 'month_value': 0.875},
  {'month_name': 'October', 'month_value': -1.54},
  {'month_name': 'November', 'month_value': 0.45899999999999996},
  {'month_name': 'December', 'month_value': -3.4130000000000003},
  {'month_name': 'December', 'month_value': -2.5869999999999997},
  {'month_name': 'February', 'month_value': -4.266},
  {'month_name': 'March', 'month_value': -0.43200000000000005},
  {'month_name': 'April', 'month_value': -0.275},
  {'month_name': 'May', 'month_value': -0.919},
  {'month_name': 'June', 'month_value': -0.013000000000000001}],
 2011: [{'month_name': 'June', 'month_value': -0.013000000000000001},
  {'month_name': 'July', 'month_value': 0.435},
  {'month_name': 'August', 'month_value': -0.11699999999999999},
  {'month_name': 'September', 'month_value': -0.865},
  {'month_name': 'October', 'month_value': -0.467},
  {'month_name': 'November', 'month_value': -0.376},
  {'month_name': 'December', 'month_value': -2.6310000000000002},
  {'month_name': 'December', 'month_value': -1.683},
  {'month_name': 'February', 'month_value': 1.575},
  {'month_name': 'March', 'month_value': 1.4240000000000002},
  {'month_name': 'April', 'month_value': 2.275},
  {'month_name': 'May', 'month_value': -0.035},
  {'month_name': 'June', 'month_value': -0.858}],
 2012: [{'month_name': 'June', 'month_value': -0.858},
  {'month_name': 'July', 'month_value': -0.47200000000000003},
  {'month_name': 'August', 'month_value': -1.063},
  {'month_name': 'September', 'month_value': 0.665},
  {'month_name': 'October', 'month_value': 0.8},
  {'month_name': 'November', 'month_value': 1.459},
  {'month_name': 'December', 'month_value': 2.221},
  {'month_name': 'December', 'month_value': -0.22},
  {'month_name': 'February', 'month_value': -0.036000000000000004},
  {'month_name': 'March', 'month_value': 1.037},
  {'month_name': 'April', 'month_value': -0.035},
  {'month_name': 'May', 'month_value': 0.168},
  {'month_name': 'June', 'month_value': -0.672}],
 2013: [{'month_name': 'June', 'month_value': -0.672},
  {'month_name': 'July', 'month_value': 0.168},
  {'month_name': 'August', 'month_value': 0.013999999999999999},
  {'month_name': 'September', 'month_value': 0.772},
  {'month_name': 'October', 'month_value': -1.514},
  {'month_name': 'November', 'month_value': -0.111},
  {'month_name': 'December', 'month_value': -1.749},
  {'month_name': 'December', 'month_value': -0.61},
  {'month_name': 'February', 'month_value': -1.0070000000000001},
  {'month_name': 'March', 'month_value': -3.185},
  {'month_name': 'April', 'month_value': 0.322},
  {'month_name': 'May', 'month_value': 0.494},
  {'month_name': 'June', 'month_value': 0.5489999999999999}],
 2014: [{'month_name': 'June', 'month_value': 0.5489999999999999},
  {'month_name': 'July', 'month_value': -0.011000000000000001},
  {'month_name': 'August', 'month_value': 0.154},
  {'month_name': 'September', 'month_value': -0.461},
  {'month_name': 'October', 'month_value': 0.263},
  {'month_name': 'November', 'month_value': 2.029},
  {'month_name': 'December', 'month_value': 1.475},
  {'month_name': 'December', 'month_value': -0.9690000000000001},
  {'month_name': 'February', 'month_value': 0.044000000000000004},
  {'month_name': 'March', 'month_value': 1.206},
  {'month_name': 'April', 'month_value': 0.972},
  {'month_name': 'May', 'month_value': 0.46399999999999997},
  {'month_name': 'June', 'month_value': -0.507}],
 2015: [{'month_name': 'June', 'month_value': -0.507},
  {'month_name': 'July', 'month_value': -0.489},
  {'month_name': 'August', 'month_value': -0.37200000000000005},
  {'month_name': 'September', 'month_value': 0.102},
  {'month_name': 'October', 'month_value': -1.1340000000000001},
  {'month_name': 'November', 'month_value': -0.53},
  {'month_name': 'December', 'month_value': 0.413},
  {'month_name': 'December', 'month_value': 1.092},
  {'month_name': 'February', 'month_value': 1.043},
  {'month_name': 'March', 'month_value': 1.837},
  {'month_name': 'April', 'month_value': 1.216},
  {'month_name': 'May', 'month_value': 0.763},
  {'month_name': 'June', 'month_value': 0.42700000000000005}],
 2016: [{'month_name': 'June', 'month_value': 0.42700000000000005},
  {'month_name': 'July', 'month_value': -1.1079999999999999},
  {'month_name': 'August', 'month_value': -0.6890000000000001},
  {'month_name': 'September', 'month_value': -0.165},
  {'month_name': 'October', 'month_value': -0.25},
  {'month_name': 'November', 'month_value': 1.945},
  {'month_name': 'December', 'month_value': 1.444},
  {'month_name': 'December', 'month_value': -1.449},
  {'month_name': 'February', 'month_value': -0.024},
  {'month_name': 'March', 'month_value': 0.28},
  {'month_name': 'April', 'month_value': -1.051},
  {'month_name': 'May', 'month_value': -0.036000000000000004},
  {'month_name': 'June', 'month_value': 0.313}],
 2017: [{'month_name': 'June', 'month_value': 0.313},
  {'month_name': 'July', 'month_value': 0.085},
  {'month_name': 'August', 'month_value': 0.47200000000000003},
  {'month_name': 'September', 'month_value': 0.7809999999999999},
  {'month_name': 'October', 'month_value': -1.9169999999999998},
  {'month_name': 'November', 'month_value': -0.611},
  {'month_name': 'December', 'month_value': 1.786},
  {'month_name': 'December', 'month_value': 0.9420000000000001},
  {'month_name': 'February', 'month_value': 0.34},
  {'month_name': 'March', 'month_value': 1.365},
  {'month_name': 'April', 'month_value': -0.08900000000000001},
  {'month_name': 'May', 'month_value': -0.73},
  {'month_name': 'June', 'month_value': 0.402}],
 2018: [{'month_name': 'June', 'month_value': 0.402},
  {'month_name': 'July', 'month_value': 0.634},
  {'month_name': 'August', 'month_value': 0.15},
  {'month_name': 'September', 'month_value': -0.49200000000000005},
  {'month_name': 'October', 'month_value': 0.69},
  {'month_name': 'November', 'month_value': -0.078},
  {'month_name': 'December', 'month_value': -0.059000000000000004},
  {'month_name': 'December', 'month_value': -0.281},
  {'month_name': 'February', 'month_value': 0.113},
  {'month_name': 'March', 'month_value': -0.941},
  {'month_name': 'April', 'month_value': 0.544},
  {'month_name': 'May', 'month_value': 1.18},
  {'month_name': 'June', 'month_value': 0.38}],
 2019: [{'month_name': 'June', 'month_value': 0.38},
  {'month_name': 'July', 'month_value': 0.612},
  {'month_name': 'August', 'month_value': 0.836},
  {'month_name': 'September', 'month_value': 0.585},
  {'month_name': 'October', 'month_value': 0.413},
  {'month_name': 'November', 'month_value': -1.1159999999999999},
  {'month_name': 'December', 'month_value': 0.11},
  {'month_name': 'December', 'month_value': -0.713},
  {'month_name': 'February', 'month_value': 1.149},
  {'month_name': 'March', 'month_value': 2.116},
  {'month_name': 'April', 'month_value': -0.255},
  {'month_name': 'May', 'month_value': -1.2309999999999999},
  {'month_name': 'June', 'month_value': -0.601}],
 2020: [{'month_name': 'June', 'month_value': -0.601},
  {'month_name': 'July', 'month_value': -0.89},
  {'month_name': 'August', 'month_value': -0.722},
  {'month_name': 'September', 'month_value': 0.306},
  {'month_name': 'October', 'month_value': -0.08199999999999999},
  {'month_name': 'November', 'month_value': -1.193},
  {'month_name': 'December', 'month_value': 0.41200000000000003},
  {'month_name': 'December', 'month_value': 2.419},
  {'month_name': 'February', 'month_value': 3.417},
  {'month_name': 'March', 'month_value': 2.641},
  {'month_name': 'April', 'month_value': 0.9279999999999999},
  {'month_name': 'May', 'month_value': -0.027000000000000003},
  {'month_name': 'June', 'month_value': -0.122}],
 2021: [{'month_name': 'June', 'month_value': -0.122},
  {'month_name': 'July', 'month_value': -0.41200000000000003},
  {'month_name': 'August', 'month_value': -0.381},
  {'month_name': 'September', 'month_value': 0.631},
  {'month_name': 'October', 'month_value': -0.07200000000000001},
  {'month_name': 'November', 'month_value': 2.086},
  {'month_name': 'December', 'month_value': -1.736},
  {'month_name': 'December', 'month_value': -2.484},
  {'month_name': 'February', 'month_value': -1.1909999999999998},
  {'month_name': 'March', 'month_value': 2.109},
  {'month_name': 'April', 'month_value': -0.204},
  {'month_name': 'May', 'month_value': -0.161},
  {'month_name': 'June', 'month_value': 0.845}],
 2022: [{'month_name': 'June', 'month_value': 0.845},
  {'month_name': 'July', 'month_value': 0.63},
  {'month_name': 'August', 'month_value': -0.209},
  {'month_name': 'September', 'month_value': -0.252},
  {'month_name': 'October', 'month_value': -0.146},
  {'month_name': 'November', 'month_value': 0.09300000000000001},
  {'month_name': 'December', 'month_value': 0.198},
  {'month_name': 'December', 'month_value': 0.848},
  {'month_name': 'February', 'month_value': 1.544},
  {'month_name': 'March', 'month_value': 0.305},
  {'month_name': 'April', 'month_value': -0.603},
  {'month_name': 'May', 'month_value': 1.224},
  {'month_name': 'June', 'month_value': -0.07400000000000001}]}


# In[3]:


enso_indices = {2001: [{'month_name': 'June', 'month_value': 1.2},
  {'month_name': 'July', 'month_value': 0.3},
  {'month_name': 'August', 'month_value': -0.4},
  {'month_name': 'September', 'month_value': 0.1},
  {'month_name': 'October', 'month_value': -1.5},
  {'month_name': 'November', 'month_value': -2.2},
  {'month_name': 'December', 'month_value': -2.4},
  {'month_name': 'January', 'month_value': 1.0},
  {'month_name': 'February', 'month_value': -2.9},
  {'month_name': 'March', 'month_value': 0.5},
  {'month_name': 'April', 'month_value': 0.0},
  {'month_name': 'May', 'month_value': 1.3},
  {'month_name': 'June', 'month_value': -0.1}],
 2002: [{'month_name': 'June', 'month_value': -0.1},
  {'month_name': 'July', 'month_value': 0.6},
  {'month_name': 'August', 'month_value': 0.7},
  {'month_name': 'September', 'month_value': -0.1},
  {'month_name': 'October', 'month_value': -0.7},
  {'month_name': 'November', 'month_value': -0.3},
  {'month_name': 'December', 'month_value': 0.4},
  {'month_name': 'January', 'month_value': 1.0},
  {'month_name': 'February', 'month_value': 0.2},
  {'month_name': 'March', 'month_value': 1.7},
  {'month_name': 'April', 'month_value': 0.6},
  {'month_name': 'May', 'month_value': 1.2},
  {'month_name': 'June', 'month_value': 0.8}],
 2003: [{'month_name': 'June', 'month_value': 0.8},
  {'month_name': 'July', 'month_value': 1.8},
  {'month_name': 'August', 'month_value': 1.1},
  {'month_name': 'September', 'month_value': 1.1},
  {'month_name': 'October', 'month_value': -0.1},
  {'month_name': 'November', 'month_value': 1.1},
  {'month_name': 'December', 'month_value': 1.8},
  {'month_name': 'January', 'month_value': 0.7},
  {'month_name': 'February', 'month_value': 0.2},
  {'month_name': 'March', 'month_value': 1.1},
  {'month_name': 'April', 'month_value': 1.1},
  {'month_name': 'May', 'month_value': 0.6},
  {'month_name': 'June', 'month_value': 0.7}],
 2004: [{'month_name': 'June', 'month_value': 0.7},
  {'month_name': 'July', 'month_value': 0.6},
  {'month_name': 'August', 'month_value': 0.4},
  {'month_name': 'September', 'month_value': 0.2},
  {'month_name': 'October', 'month_value': -0.3},
  {'month_name': 'November', 'month_value': 0.6},
  {'month_name': 'December', 'month_value': -1.1},
  {'month_name': 'January', 'month_value': 1.4},
  {'month_name': 'February', 'month_value': -0.2},
  {'month_name': 'March', 'month_value': -0.6},
  {'month_name': 'April', 'month_value': 1.2},
  {'month_name': 'May', 'month_value': -0.3},
  {'month_name': 'June', 'month_value': 2.2}],
 2005: [{'month_name': 'June', 'month_value': 2.2},
  {'month_name': 'July', 'month_value': 1.1},
  {'month_name': 'August', 'month_value': 0.9},
  {'month_name': 'September', 'month_value': 1.2},
  {'month_name': 'October', 'month_value': 0.5},
  {'month_name': 'November', 'month_value': 0.5},
  {'month_name': 'December', 'month_value': 0.0},
  {'month_name': 'January', 'month_value': 0.1},
  {'month_name': 'February', 'month_value': 2.6},
  {'month_name': 'March', 'month_value': 1.1},
  {'month_name': 'April', 'month_value': 1.7},
  {'month_name': 'May', 'month_value': 1.4},
  {'month_name': 'June', 'month_value': -0.2}],
 2006: [{'month_name': 'June', 'month_value': -0.2},
  {'month_name': 'July', 'month_value': 0.4},
  {'month_name': 'August', 'month_value': 0.9},
  {'month_name': 'September', 'month_value': 0.0},
  {'month_name': 'October', 'month_value': -0.7},
  {'month_name': 'November', 'month_value': -0.4},
  {'month_name': 'December', 'month_value': 0.4},
  {'month_name': 'January', 'month_value': -1.5},
  {'month_name': 'February', 'month_value': 1.0},
  {'month_name': 'March', 'month_value': -1.2},
  {'month_name': 'April', 'month_value': -1.7},
  {'month_name': 'May', 'month_value': 1.2},
  {'month_name': 'June', 'month_value': 1.2}],
 2007: [{'month_name': 'June', 'month_value': 1.2},
  {'month_name': 'July', 'month_value': 1.6},
  {'month_name': 'August', 'month_value': 2.0},
  {'month_name': 'September', 'month_value': 1.4},
  {'month_name': 'October', 'month_value': 2.3},
  {'month_name': 'November', 'month_value': 1.1},
  {'month_name': 'December', 'month_value': 1.4},
  {'month_name': 'January', 'month_value': 0.5},
  {'month_name': 'February', 'month_value': 0.7},
  {'month_name': 'March', 'month_value': 0.3},
  {'month_name': 'April', 'month_value': 1.2},
  {'month_name': 'May', 'month_value': 0.9},
  {'month_name': 'June', 'month_value': -0.8}],
 2008: [{'month_name': 'June', 'month_value': -0.8},
  {'month_name': 'July', 'month_value': 1.4},
  {'month_name': 'August', 'month_value': 0.8},
  {'month_name': 'September', 'month_value': -0.4},
  {'month_name': 'October', 'month_value': -0.6},
  {'month_name': 'November', 'month_value': -1.1},
  {'month_name': 'December', 'month_value': -1.3},
  {'month_name': 'January', 'month_value': -1.3},
  {'month_name': 'February', 'month_value': -1.7},
  {'month_name': 'March', 'month_value': 1.0},
  {'month_name': 'April', 'month_value': 0.5},
  {'month_name': 'May', 'month_value': 1.3},
  {'month_name': 'June', 'month_value': 0.8}],
 2009: [{'month_name': 'June', 'month_value': 0.8},
  {'month_name': 'July', 'month_value': 0.6},
  {'month_name': 'August', 'month_value': 0.9},
  {'month_name': 'September', 'month_value': -0.2},
  {'month_name': 'October', 'month_value': 0.4},
  {'month_name': 'November', 'month_value': -0.6},
  {'month_name': 'December', 'month_value': -0.8},
  {'month_name': 'January', 'month_value': -0.2},
  {'month_name': 'February', 'month_value': -1.2},
  {'month_name': 'March', 'month_value': 1.1},
  {'month_name': 'April', 'month_value': -0.1},
  {'month_name': 'May', 'month_value': -0.3},
  {'month_name': 'June', 'month_value': 0.4}],
 2010: [{'month_name': 'June', 'month_value': 0.4},
  {'month_name': 'July', 'month_value': 0.3},
  {'month_name': 'August', 'month_value': 0.3},
  {'month_name': 'September', 'month_value': -0.6},
  {'month_name': 'October', 'month_value': 0.8},
  {'month_name': 'November', 'month_value': 0.2},
  {'month_name': 'December', 'month_value': 0.6},
  {'month_name': 'January', 'month_value': -0.3},
  {'month_name': 'February', 'month_value': 1.4},
  {'month_name': 'March', 'month_value': 1.5},
  {'month_name': 'April', 'month_value': 0.2},
  {'month_name': 'May', 'month_value': -0.7},
  {'month_name': 'June', 'month_value': 0.9}],
 2011: [{'month_name': 'June', 'month_value': 0.9},
  {'month_name': 'July', 'month_value': -0.4},
  {'month_name': 'August', 'month_value': -0.4},
  {'month_name': 'September', 'month_value': -1.1},
  {'month_name': 'October', 'month_value': -1.3},
  {'month_name': 'November', 'month_value': -0.2},
  {'month_name': 'December', 'month_value': -2.4},
  {'month_name': 'January', 'month_value': -1.1},
  {'month_name': 'February', 'month_value': -1.4},
  {'month_name': 'March', 'month_value': -1.1},
  {'month_name': 'April', 'month_value': -0.5},
  {'month_name': 'May', 'month_value': 1.1},
  {'month_name': 'June', 'month_value': 1.2}],
 2012: [{'month_name': 'June', 'month_value': 1.2},
  {'month_name': 'July', 'month_value': 0.4},
  {'month_name': 'August', 'month_value': 1.0},
  {'month_name': 'September', 'month_value': 0.7},
  {'month_name': 'October', 'month_value': -0.3},
  {'month_name': 'November', 'month_value': -0.1},
  {'month_name': 'December', 'month_value': -2.3},
  {'month_name': 'January', 'month_value': -0.2},
  {'month_name': 'February', 'month_value': 0.8},
  {'month_name': 'March', 'month_value': -1.1},
  {'month_name': 'April', 'month_value': 1.3},
  {'month_name': 'May', 'month_value': 0.4},
  {'month_name': 'June', 'month_value': 1.0}],
 2013: [{'month_name': 'June', 'month_value': 1.0},
  {'month_name': 'July', 'month_value': -0.0},
  {'month_name': 'August', 'month_value': 1.4},
  {'month_name': 'September', 'month_value': 0.3},
  {'month_name': 'October', 'month_value': 0.2},
  {'month_name': 'November', 'month_value': 0.6},
  {'month_name': 'December', 'month_value': 0.4},
  {'month_name': 'January', 'month_value': -0.4},
  {'month_name': 'February', 'month_value': 0.8},
  {'month_name': 'March', 'month_value': -0.2},
  {'month_name': 'April', 'month_value': 0.3},
  {'month_name': 'May', 'month_value': -0.1},
  {'month_name': 'June', 'month_value': -1.1}],
 2014: [{'month_name': 'June', 'month_value': -1.1},
  {'month_name': 'July', 'month_value': -0.3},
  {'month_name': 'August', 'month_value': 0.5},
  {'month_name': 'September', 'month_value': -0.3},
  {'month_name': 'October', 'month_value': 0.1},
  {'month_name': 'November', 'month_value': -1.0},
  {'month_name': 'December', 'month_value': 0.4},
  {'month_name': 'January', 'month_value': -1.2},
  {'month_name': 'February', 'month_value': -0.4},
  {'month_name': 'March', 'month_value': 1.7},
  {'month_name': 'April', 'month_value': -0.5},
  {'month_name': 'May', 'month_value': 0.8},
  {'month_name': 'June', 'month_value': 0.2}],
 2015: [{'month_name': 'June', 'month_value': 0.2},
  {'month_name': 'July', 'month_value': 1.1},
  {'month_name': 'August', 'month_value': 1.9},
  {'month_name': 'September', 'month_value': 1.2},
  {'month_name': 'October', 'month_value': 1.0},
  {'month_name': 'November', 'month_value': 1.2},
  {'month_name': 'December', 'month_value': 0.2},
  {'month_name': 'January', 'month_value': 0.3},
  {'month_name': 'February', 'month_value': 1.4},
  {'month_name': 'March', 'month_value': 1.5},
  {'month_name': 'April', 'month_value': 1.1},
  {'month_name': 'May', 'month_value': 2.2},
  {'month_name': 'June', 'month_value': 1.0}],
 2016: [{'month_name': 'June', 'month_value': 1.0},
  {'month_name': 'July', 'month_value': 2.2},
  {'month_name': 'August', 'month_value': 2.2},
  {'month_name': 'September', 'month_value': 2.0},
  {'month_name': 'October', 'month_value': 3.2},
  {'month_name': 'November', 'month_value': 0.8},
  {'month_name': 'December', 'month_value': -0.3},
  {'month_name': 'January', 'month_value': 4.0},
  {'month_name': 'February', 'month_value': 2.2},
  {'month_name': 'March', 'month_value': 1.8},
  {'month_name': 'April', 'month_value': 1.4},
  {'month_name': 'May', 'month_value': 0.0},
  {'month_name': 'June', 'month_value': -0.1}],
 2017: [{'month_name': 'June', 'month_value': -0.1},
  {'month_name': 'July', 'month_value': 0.3},
  {'month_name': 'August', 'month_value': -0.2},
  {'month_name': 'September', 'month_value': -0.9},
  {'month_name': 'October', 'month_value': -0.2},
  {'month_name': 'November', 'month_value': 0.1},
  {'month_name': 'December', 'month_value': -0.6},
  {'month_name': 'January', 'month_value': -0.2},
  {'month_name': 'February', 'month_value': 0.7},
  {'month_name': 'March', 'month_value': -0.0},
  {'month_name': 'April', 'month_value': 0.3},
  {'month_name': 'May', 'month_value': 0.8},
  {'month_name': 'June', 'month_value': 1.2}],
 2018: [{'month_name': 'June', 'month_value': 1.2},
  {'month_name': 'July', 'month_value': 0.4},
  {'month_name': 'August', 'month_value': 0.4},
  {'month_name': 'September', 'month_value': 0.4},
  {'month_name': 'October', 'month_value': -1.2},
  {'month_name': 'November', 'month_value': -1.3},
  {'month_name': 'December', 'month_value': 0.0},
  {'month_name': 'January', 'month_value': -1.4},
  {'month_name': 'February', 'month_value': 0.6},
  {'month_name': 'March', 'month_value': -1.3},
  {'month_name': 'April', 'month_value': 0.1},
  {'month_name': 'May', 'month_value': 1.3},
  {'month_name': 'June', 'month_value': 1.4}],
 2019: [{'month_name': 'June', 'month_value': 1.4},
  {'month_name': 'July', 'month_value': -0.0},
  {'month_name': 'August', 'month_value': 0.5},
  {'month_name': 'September', 'month_value': 0.4},
  {'month_name': 'October', 'month_value': 0.4},
  {'month_name': 'November', 'month_value': 0.7},
  {'month_name': 'December', 'month_value': -1.1},
  {'month_name': 'January', 'month_value': 0.6},
  {'month_name': 'February', 'month_value': 2.6},
  {'month_name': 'March', 'month_value': 1.0},
  {'month_name': 'April', 'month_value': 0.7},
  {'month_name': 'May', 'month_value': 1.4},
  {'month_name': 'June', 'month_value': 1.5}],
 2020: [{'month_name': 'June', 'month_value': 1.5},
  {'month_name': 'July', 'month_value': 1.4},
  {'month_name': 'August', 'month_value': 1.7},
  {'month_name': 'September', 'month_value': 2.6},
  {'month_name': 'October', 'month_value': 0.8},
  {'month_name': 'November', 'month_value': 1.0},
  {'month_name': 'December', 'month_value': 1.1},
  {'month_name': 'January', 'month_value': 1.0},
  {'month_name': 'February', 'month_value': 1.0},
  {'month_name': 'March', 'month_value': 1.7},
  {'month_name': 'April', 'month_value': 1.1},
  {'month_name': 'May', 'month_value': 1.5},
  {'month_name': 'June', 'month_value': 0.6}],
 2021: [{'month_name': 'June', 'month_value': 0.6},
  {'month_name': 'July', 'month_value': -0.1},
  {'month_name': 'August', 'month_value': -0.1},
  {'month_name': 'September', 'month_value': -0.3},
  {'month_name': 'October', 'month_value': -0.6},
  {'month_name': 'November', 'month_value': 0.3},
  {'month_name': 'December', 'month_value': -0.8},
  {'month_name': 'January', 'month_value': -0.6},
  {'month_name': 'February', 'month_value': -1.4},
  {'month_name': 'March', 'month_value': 0.7},
  {'month_name': 'April', 'month_value': 0.3},
  {'month_name': 'May', 'month_value': 0.4},
  {'month_name': 'June', 'month_value': 0.8}],
 2022: [{'month_name': 'June', 'month_value': 0.8},
  {'month_name': 'July', 'month_value': -0.5},
  {'month_name': 'August', 'month_value': 0.7},
  {'month_name': 'September', 'month_value': 0.1},
  {'month_name': 'October', 'month_value': -0.9},
  {'month_name': 'November', 'month_value': -0.4},
  {'month_name': 'December', 'month_value': -0.8},
  {'month_name': 'January', 'month_value': 0.3},
  {'month_name': 'February', 'month_value': 0.5},
  {'month_name': 'March', 'month_value': 0.1},
  {'month_name': 'April', 'month_value': -0.9},
  {'month_name': 'May', 'month_value': -0.5},
  {'month_name': 'June', 'month_value': -0.6}]}


# In[4]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = []
for year in total_avg_temp:
    for month in total_avg_temp:
        if year['Year'] == month['Year']:
            avg_temp = month['Avg_temp']
            ao_value = next((item['month_value'] for item in ao_indices[year['Year']] if item['month_name'] == month['Month']), None)
            enso_value = next((item['month_value'] for item in enso_indices[year['Year']] if item['month_name'] == month['Month']), None)
            data.append([year['Year'], month['Month'], avg_temp, ao_value, enso_value])

df = pd.DataFrame(data, columns=['Year', 'Month', 'Avg_temp', 'AO', 'ENSO'])

# Calculate the correlation matrix
corr_matrix = df[['Avg_temp', 'AO', 'ENSO']].corr()
print(corr_matrix)

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, annot_kws={"size": 20}, cmap='coolwarm', vmin=-1, vmax=1, fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix between Avg Temp, AO, and ENSO")
plt.tight_layout(pad=3.0)
plt.show()


# In[1]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

study_site_names = ["Nunam Iqua", "Stebbins", "Hooper Bay", "Mekoryuk", "Utqiagvik", 
                    "Kotzebue", "Elim", "Toksook Bay", "Shaktoolik", "Kwigillingok", 
                    "Scammon Bay", "Nome", "Point Hope", "Chefornak", "Tununak", 
                    "Kotlik", "Newtok", "Brevig Mission", "Wainwright", "Koyuk", 
                    "Alakanuk", "Quinhagak", "Kivalina", "Emmonak", "Golovin", 
                    "Kipnuk", "Unalakleet", "Point Lay", "Deering", "Wales", 
                    "Kongiganak"]

correlation_data = [
    [[1.0, -0.072666, 0.233112], [-0.072666, 1.0, 0.006068], [0.233112, 0.006068, 1.0]],
    [[1.0, -0.073174, 0.257911], [-0.073174, 1.0, 0.006068], [0.257911, 0.006068, 1.0]],
    [[1.0, -0.069597, 0.220507], [-0.069597, 1.0, 0.006068], [0.220507, 0.006068, 1.0]],
    [[1.0, -0.074713, 0.200840], [-0.074713, 1.0, 0.006068], [0.200840, 0.006068, 1.0]],
    [[1.0, -0.063154, 0.225470], [-0.063154, 1.0, -0.020321], [0.225470, -0.020321, 1.0]],
    [[1.0, -0.077815, 0.267075], [-0.077815, 1.0, -0.000846], [0.267075, -0.000846, 1.0]],
    [[1.0, -0.074548, 0.262103], [-0.074548, 1.0, 0.006068], [0.262103, 0.006068, 1.0]],
    [[1.0, -0.073832, 0.225165], [-0.073832, 1.0, 0.006068], [0.225165, 0.006068, 1.0]],
    [[1.0, -0.071696, 0.268982], [-0.071696, 1.0, 0.006068], [0.268982, 0.006068, 1.0]],
    [[1.0, -0.081325, 0.246581], [-0.081325, 1.0, 0.006068], [0.246581, 0.006068, 1.0]],
    [[1.0, -0.071085, 0.229478], [-0.071085, 1.0, 0.006068], [0.229478, 0.006068, 1.0]],
    [[1.0, -0.072278, 0.229911], [-0.072278, 1.0, 0.006068], [0.229911, 0.006068, 1.0]],
    [[1.0, -0.062358, 0.228299], [-0.062358, 1.0, -0.000846], [0.228299, -0.000846, 1.0]],
    [[1.0, -0.073146, 0.240504], [-0.073146, 1.0, 0.006068], [0.240504, 0.006068, 1.0]],
    [[1.0, -0.074092, 0.219503], [-0.074092, 1.0, 0.006068], [0.219503, 0.006068, 1.0]],
    [[1.0, -0.074198, 0.242586], [-0.074198, 1.0, 0.006068], [0.242586, 0.006068, 1.0]],
    [[1.0, -0.069118, 0.241154], [-0.069118, 1.0, 0.006068], [0.241154, 0.006068, 1.0]],
    [[1.0, -0.070265, 0.226009], [-0.070265, 1.0, -0.000846], [0.226009, -0.000846, 1.0]],
    [[1.0, -0.048306, 0.241895], [-0.048306, 1.0, -0.000846], [0.241895, -0.000846, 1.0]],
    [[1.0, -0.072250, 0.272066], [-0.072250, 1.0, 0.006068], [0.272066, 0.006068, 1.0]],
    [[1.0, -0.072666, 0.233112], [-0.072666, 1.0, 0.006068], [0.233112, 0.006068, 1.0]],
    [[1.0, -0.082357, 0.263565], [-0.082357, 1.0, 0.006068], [0.263565, 0.006068, 1.0]],
    [[1.0, -0.076762, 0.255954], [-0.076762, 1.0, -0.000846], [0.255954, -0.000846, 1.0]],
    [[1.0, -0.072666, 0.233112], [-0.072666, 1.0, 0.006068], [0.233112, 0.006068, 1.0]],
    [[1.0, -0.075574, 0.255490], [-0.075574, 1.0, 0.006068], [0.255490, 0.006068, 1.0]],
    [[1.0, -0.081586, 0.230079], [-0.081586, 1.0, 0.006068], [0.230079, 0.006068, 1.0]],
    [[1.0, -0.070519, 0.268738], [-0.070519, 1.0, 0.006068], [0.268738, 0.006068, 1.0]],
    [[1.0, -0.049327, 0.241712], [-0.049327, 1.0, -0.000846], [0.241712, -0.000846, 1.0]],
    [[1.0, -0.077790, 0.260173], [-0.077790, 1.0, -0.000846], [0.260173, -0.000846, 1.0]],
    [[1.0, -0.063546, 0.202190], [-0.063546, 1.0, -0.000846], [0.202190, -0.000846, 1.0]],
    [[1.0, -0.077982, 0.251355], [-0.077982, 1.0, 0.006068], [0.251355, 0.006068, 1.0]]
]

for site, corr_matrix in zip(study_site_names, correlation_data):
    # Create a DataFrame from the correlation matrix
    df_corr = pd.DataFrame(corr_matrix, columns=["Avg_temp", "AO", "ENSO"], index=["Avg_temp", "AO", "ENSO"])
    
    # Create a heatmap for the correlation matrix
    plt.figure(figsize=(8, 6))
    sns.heatmap(df_corr, annot=True, cmap="coolwarm", cbar=True, square=True, fmt=".2f", linewidths=0.5)
    
    # Title and labels
    plt.title(f"Correlation Matrix for {site}", fontsize=16)
    plt.xlabel("Variables", fontsize=12)
    plt.ylabel("Variables", fontsize=12)
    
    # Save the plot as an image
    #plt.savefig(f"{site}_correlation_heatmap.png")
    plt.close()  # Close the plot to prevent overlap in the next iteration

print("Heatmaps generated for each site.")


# In[2]:


study_site_dict = dict(zip(study_site_names, correlation_data))

# Print a sample of the dictionary to verify
for site, data in list(study_site_dict.items())[:5]:  # Show only the first 5 sites for brevity
    print(study_site_dict)


# In[9]:


selected_sites = ["Nunam Iqua", "Mekoryuk", "Utqiagvik", "Elim", "Toksook Bay", "Kwigillingok"]

plt.figure(figsize=(12, 8))
for site, i in selected_sites:
    if site in study_site_dict:
        data = study_site_dict[site]
        plt.subplot(3,2,i)
        sns.heatmap(data, annot=True, fmt=".3f", cmap="coolwarm", cbar=True)
        plt.title(f"Heatmap for {site}")
        plt.xlabel("Variables")
        plt.ylabel("Variables")
        plt.show()
    else:
        print(f"Data for {site} not found in study_site_dict.")


# In[5]:


selected_sites = ["Utqiagvik", "Deering", "Nunam Iqua", "Kwigillingok"]

n_sites = len(selected_sites)
n_cols = 2
n_rows = (n_sites + n_cols - 1) // n_cols

fig, axes = plt.subplots(n_rows, n_cols, figsize=(10, 4 * n_rows))
axes = axes.flatten()

for i, site in enumerate(selected_sites):
    if site in study_site_dict:
        data = study_site_dict[site]
        sns.heatmap(data, annot=True, fmt=".3f", cmap="coolwarm", cbar=True, ax=axes[i])
        axes[i].set_title(f"{site}")
        axes[i].set_xlabel("Variables")
        axes[i].set_ylabel("Variables")
    else:
        axes[i].axis("off")
        axes[i].text(0.5, 0.5, f"No data for {site}", ha='center', va='center')

for j in range(i + 1, len(axes)):
    axes[j].axis("off")

plt.tight_layout()
plt.savefig('/hpc/home/hk339/output/heatmap.png')
plt.show()


# In[58]:


from netCDF4 import Dataset
import numpy as np
import datetime

fp = '/hpc/home/hk339/ESDA506/Kwigillingok_raster_monthly.nc'
data = Dataset(fp,'r')
#print(data.variables.keys())

time = data.variables['valid_time'][:]
lat = data.variables['latitude'][:]
lon = data.variables['longitude'][:]
temperature = data.variables['t'][:] - 273.15
specific_humidity = data.variables['q'][:]
cloud_cover = data.variables['cc'][:]
temperature = temperature.squeeze(axis=1)
specific_humidity = specific_humidity.squeeze(axis=1)
cloud_cover = cloud_cover.squeeze(axis=1)
#print(temperature.shape)

start_date = datetime.datetime(1970,1,1)
dates = [start_date + datetime.timedelta(seconds=int(second)) for second in time]


# In[59]:


enso_data_dict = {datetime.datetime(1940, 1, 1, 0, 0): -0.5, datetime.datetime(1940, 2, 1, 0, 0): 0.1, datetime.datetime(1940, 3, 1, 0, 0): 1.3, datetime.datetime(1940, 4, 1, 0, 0): 1.3, datetime.datetime(1940, 5, 1, 0, 0): 1.3, datetime.datetime(1940, 6, 1, 0, 0): 1.7, datetime.datetime(1940, 7, 1, 0, 0): 1.5, datetime.datetime(1940, 8, 1, 0, 0): 1.5, datetime.datetime(1940, 9, 1, 0, 0): 2.2, datetime.datetime(1940, 10, 1, 0, 0): 3.2, datetime.datetime(1940, 11, 1, 0, 0): 0.9, datetime.datetime(1940, 12, 1, 0, 0): 2.6, datetime.datetime(1941, 1, 1, 0, 0): 1.6, datetime.datetime(1941, 2, 1, 0, 0): 3.3, datetime.datetime(1941, 3, 1, 0, 0): 1.3, datetime.datetime(1941, 4, 1, 0, 0): 1.2, datetime.datetime(1941, 5, 1, 0, 0): 0.3, datetime.datetime(1941, 6, 1, 0, 0): 1.4, datetime.datetime(1941, 7, 1, 0, 0): 2.6, datetime.datetime(1941, 8, 1, 0, 0): 1.9, datetime.datetime(1941, 9, 1, 0, 0): 0.8, datetime.datetime(1941, 10, 1, 0, 0): 1.3, datetime.datetime(1941, 11, 1, 0, 0): 0.5, datetime.datetime(1941, 12, 1, 0, 0): 1.5, datetime.datetime(1942, 1, 1, 0, 0): 2.3, datetime.datetime(1942, 2, 1, 0, 0): -0.1, datetime.datetime(1942, 3, 1, 0, 0): 1.2, datetime.datetime(1942, 4, 1, 0, 0): 0.9, datetime.datetime(1942, 5, 1, 0, 0): -1.1, datetime.datetime(1942, 6, 1, 0, 0): -0.5, datetime.datetime(1942, 7, 1, 0, 0): 0.4, datetime.datetime(1942, 8, 1, 0, 0): -0.5, datetime.datetime(1942, 9, 1, 0, 0): -0.8, datetime.datetime(1942, 10, 1, 0, 0): -1.1, datetime.datetime(1942, 11, 1, 0, 0): -0.4, datetime.datetime(1942, 12, 1, 0, 0): -0.6, datetime.datetime(1943, 1, 1, 0, 0): 0.1, datetime.datetime(1943, 2, 1, 0, 0): -1.5, datetime.datetime(1943, 3, 1, 0, 0): -0.0, datetime.datetime(1943, 4, 1, 0, 0): -0.6, datetime.datetime(1943, 5, 1, 0, 0): -0.1, datetime.datetime(1943, 6, 1, 0, 0): 0.8, datetime.datetime(1943, 7, 1, 0, 0): -0.2, datetime.datetime(1943, 8, 1, 0, 0): -0.6, datetime.datetime(1943, 9, 1, 0, 0): -0.8, datetime.datetime(1943, 10, 1, 0, 0): -0.9, datetime.datetime(1943, 11, 1, 0, 0): -0.3, datetime.datetime(1943, 12, 1, 0, 0): 0.4, datetime.datetime(1944, 1, 1, 0, 0): 1.0, datetime.datetime(1944, 2, 1, 0, 0): 0.3, datetime.datetime(1944, 3, 1, 0, 0): 0.2, datetime.datetime(1944, 4, 1, 0, 0): 0.8, datetime.datetime(1944, 5, 1, 0, 0): 0.7, datetime.datetime(1944, 6, 1, 0, 0): 0.8, datetime.datetime(1944, 7, 1, 0, 0): 1.2, datetime.datetime(1944, 8, 1, 0, 0): 0.9, datetime.datetime(1944, 9, 1, 0, 0): 0.5, datetime.datetime(1944, 10, 1, 0, 0): 0.7, datetime.datetime(1944, 11, 1, 0, 0): 0.3, datetime.datetime(1944, 12, 1, 0, 0): -1.0, datetime.datetime(1945, 1, 1, 0, 0): 0.3, datetime.datetime(1945, 2, 1, 0, 0): 0.0, datetime.datetime(1945, 3, 1, 0, 0): -1.6, datetime.datetime(1945, 4, 1, 0, 0): 0.9, datetime.datetime(1945, 5, 1, 0, 0): 0.4, datetime.datetime(1945, 6, 1, 0, 0): -0.5, datetime.datetime(1945, 7, 1, 0, 0): 0.6, datetime.datetime(1945, 8, 1, 0, 0): -0.4, datetime.datetime(1945, 9, 1, 0, 0): 0.0, datetime.datetime(1945, 10, 1, 0, 0): 0.5, datetime.datetime(1945, 11, 1, 0, 0): 0.6, datetime.datetime(1945, 12, 1, 0, 0): -0.1, datetime.datetime(1946, 1, 1, 0, 0): 0.1, datetime.datetime(1946, 2, 1, 0, 0): -0.9, datetime.datetime(1946, 3, 1, 0, 0): 1.2, datetime.datetime(1946, 4, 1, 0, 0): 1.0, datetime.datetime(1946, 5, 1, 0, 0): 0.7, datetime.datetime(1946, 6, 1, 0, 0): 0.9, datetime.datetime(1946, 7, 1, 0, 0): 1.0, datetime.datetime(1946, 8, 1, 0, 0): 0.8, datetime.datetime(1946, 9, 1, 0, 0): 0.8, datetime.datetime(1946, 10, 1, 0, 0): 1.2, datetime.datetime(1946, 11, 1, 0, 0): 0.5, datetime.datetime(1946, 12, 1, 0, 0): 0.0, datetime.datetime(1947, 1, 1, 0, 0): 1.3, datetime.datetime(1947, 2, 1, 0, 0): -0.1, datetime.datetime(1947, 3, 1, 0, 0): -0.4, datetime.datetime(1947, 4, 1, 0, 0): 0.2, datetime.datetime(1947, 5, 1, 0, 0): 1.5, datetime.datetime(1947, 6, 1, 0, 0): 0.3, datetime.datetime(1947, 7, 1, 0, 0): 0.4, datetime.datetime(1947, 8, 1, 0, 0): -1.0, datetime.datetime(1947, 9, 1, 0, 0): -0.4, datetime.datetime(1947, 10, 1, 0, 0): 0.0, datetime.datetime(1947, 11, 1, 0, 0): -0.5, datetime.datetime(1947, 12, 1, 0, 0): -0.6, datetime.datetime(1948, 1, 1, 0, 0): 1.1, datetime.datetime(1948, 2, 1, 0, 0): 0.1, datetime.datetime(1948, 3, 1, 0, 0): 0.2, datetime.datetime(1948, 4, 1, 0, 0): -0.4, datetime.datetime(1948, 5, 1, 0, 0): -0.1, datetime.datetime(1948, 6, 1, 0, 0): 0.4, datetime.datetime(1948, 7, 1, 0, 0): -0.5, datetime.datetime(1948, 8, 1, 0, 0): -0.4, datetime.datetime(1948, 9, 1, 0, 0): 0.3, datetime.datetime(1948, 10, 1, 0, 0): -0.2, datetime.datetime(1948, 11, 1, 0, 0): -1.1, datetime.datetime(1948, 12, 1, 0, 0): 0.4, datetime.datetime(1949, 1, 1, 0, 0): 1.1, datetime.datetime(1949, 2, 1, 0, 0): -0.8, datetime.datetime(1949, 3, 1, 0, 0): -1.2, datetime.datetime(1949, 4, 1, 0, 0): 0.7, datetime.datetime(1949, 5, 1, 0, 0): 0.2, datetime.datetime(1949, 6, 1, 0, 0): 1.2, datetime.datetime(1949, 7, 1, 0, 0): 0.2, datetime.datetime(1949, 8, 1, 0, 0): 0.8, datetime.datetime(1949, 9, 1, 0, 0): -0.1, datetime.datetime(1949, 10, 1, 0, 0): -0.8, datetime.datetime(1949, 11, 1, 0, 0): 0.3, datetime.datetime(1949, 12, 1, 0, 0): -2.1, datetime.datetime(1950, 1, 1, 0, 0): -1.5, datetime.datetime(1950, 2, 1, 0, 0): -2.1, datetime.datetime(1950, 3, 1, 0, 0): -0.9, datetime.datetime(1950, 4, 1, 0, 0): -1.7, datetime.datetime(1950, 5, 1, 0, 0): -1.0, datetime.datetime(1950, 6, 1, 0, 0): -1.6, datetime.datetime(1950, 7, 1, 0, 0): -0.7, datetime.datetime(1950, 8, 1, 0, 0): -0.6, datetime.datetime(1950, 9, 1, 0, 0): -0.2, datetime.datetime(1950, 10, 1, 0, 0): -1.1, datetime.datetime(1950, 11, 1, 0, 0): -2.2, datetime.datetime(1950, 12, 1, 0, 0): -2.9, datetime.datetime(1951, 1, 1, 0, 0): -0.9, datetime.datetime(1951, 2, 1, 0, 0): -1.3, datetime.datetime(1951, 3, 1, 0, 0): -0.4, datetime.datetime(1951, 4, 1, 0, 0): 0.0, datetime.datetime(1951, 5, 1, 0, 0): 1.0, datetime.datetime(1951, 6, 1, 0, 0): -1.1, datetime.datetime(1951, 7, 1, 0, 0): 0.5, datetime.datetime(1951, 8, 1, 0, 0): 0.6, datetime.datetime(1951, 9, 1, 0, 0): 0.6, datetime.datetime(1951, 10, 1, 0, 0): 0.8, datetime.datetime(1951, 11, 1, 0, 0): 0.8, datetime.datetime(1951, 12, 1, 0, 0): 1.6, datetime.datetime(1952, 1, 1, 0, 0): 0.5, datetime.datetime(1952, 2, 1, 0, 0): 0.7, datetime.datetime(1952, 3, 1, 0, 0): 0.9, datetime.datetime(1952, 4, 1, 0, 0): 0.9, datetime.datetime(1952, 5, 1, 0, 0): -0.6, datetime.datetime(1952, 6, 1, 0, 0): 0.2, datetime.datetime(1952, 7, 1, 0, 0): 0.2, datetime.datetime(1952, 8, 1, 0, 0): -0.0, datetime.datetime(1952, 9, 1, 0, 0): 0.2, datetime.datetime(1952, 10, 1, 0, 0): -0.7, datetime.datetime(1952, 11, 1, 0, 0): -1.0, datetime.datetime(1952, 12, 1, 0, 0): 1.1, datetime.datetime(1953, 1, 1, 0, 0): 0.7, datetime.datetime(1953, 2, 1, 0, 0): 0.9, datetime.datetime(1953, 3, 1, 0, 0): 0.6, datetime.datetime(1953, 4, 1, 0, 0): -0.5, datetime.datetime(1953, 5, 1, 0, 0): 2.2, datetime.datetime(1953, 6, 1, 0, 0): 0.2, datetime.datetime(1953, 7, 1, 0, 0): 1.1, datetime.datetime(1953, 8, 1, 0, 0): 0.4, datetime.datetime(1953, 9, 1, 0, 0): 1.3, datetime.datetime(1953, 10, 1, 0, 0): 0.2, datetime.datetime(1953, 11, 1, 0, 0): 0.7, datetime.datetime(1953, 12, 1, 0, 0): 0.8, datetime.datetime(1954, 1, 1, 0, 0): -1.3, datetime.datetime(1954, 2, 1, 0, 0): 0.9, datetime.datetime(1954, 3, 1, 0, 0): 0.3, datetime.datetime(1954, 4, 1, 0, 0): -1.7, datetime.datetime(1954, 5, 1, 0, 0): -0.8, datetime.datetime(1954, 6, 1, 0, 0): 0.0, datetime.datetime(1954, 7, 1, 0, 0): -0.4, datetime.datetime(1954, 8, 1, 0, 0): -0.8, datetime.datetime(1954, 9, 1, 0, 0): 0.0, datetime.datetime(1954, 10, 1, 0, 0): 0.1, datetime.datetime(1954, 11, 1, 0, 0): 0.4, datetime.datetime(1954, 12, 1, 0, 0): -0.8, datetime.datetime(1955, 1, 1, 0, 0): 2.1, datetime.datetime(1955, 2, 1, 0, 0): -2.7, datetime.datetime(1955, 3, 1, 0, 0): -0.7, datetime.datetime(1955, 4, 1, 0, 0): -0.5, datetime.datetime(1955, 5, 1, 0, 0): -1.5, datetime.datetime(1955, 6, 1, 0, 0): -1.4, datetime.datetime(1955, 7, 1, 0, 0): -1.1, datetime.datetime(1955, 8, 1, 0, 0): -1.2, datetime.datetime(1955, 9, 1, 0, 0): -1.0, datetime.datetime(1955, 10, 1, 0, 0): -1.3, datetime.datetime(1955, 11, 1, 0, 0): -1.1, datetime.datetime(1955, 12, 1, 0, 0): 0.3, datetime.datetime(1956, 1, 1, 0, 0): -1.4, datetime.datetime(1956, 2, 1, 0, 0): -1.7, datetime.datetime(1956, 3, 1, 0, 0): -0.5, datetime.datetime(1956, 4, 1, 0, 0): -1.1, datetime.datetime(1956, 5, 1, 0, 0): -1.8, datetime.datetime(1956, 6, 1, 0, 0): -1.0, datetime.datetime(1956, 7, 1, 0, 0): -1.6, datetime.datetime(1956, 8, 1, 0, 0): -1.1, datetime.datetime(1956, 9, 1, 0, 0): -0.5, datetime.datetime(1956, 10, 1, 0, 0): -0.9, datetime.datetime(1956, 11, 1, 0, 0): -0.0, datetime.datetime(1956, 12, 1, 0, 0): -1.7, datetime.datetime(1957, 1, 1, 0, 0): 0.3, datetime.datetime(1957, 2, 1, 0, 0): 0.0, datetime.datetime(1957, 3, 1, 0, 0): 0.4, datetime.datetime(1957, 4, 1, 0, 0): 0.1, datetime.datetime(1957, 5, 1, 0, 0): 1.4, datetime.datetime(1957, 6, 1, 0, 0): 0.2, datetime.datetime(1957, 7, 1, 0, 0): 0.1, datetime.datetime(1957, 8, 1, 0, 0): 0.7, datetime.datetime(1957, 9, 1, 0, 0): 1.2, datetime.datetime(1957, 10, 1, 0, 0): 0.9, datetime.datetime(1957, 11, 1, 0, 0): 1.1, datetime.datetime(1957, 12, 1, 0, 0): 0.4, datetime.datetime(1958, 1, 1, 0, 0): 2.3, datetime.datetime(1958, 2, 1, 0, 0): 0.7, datetime.datetime(1958, 3, 1, 0, 0): 0.7, datetime.datetime(1958, 4, 1, 0, 0): -0.5, datetime.datetime(1958, 5, 1, 0, 0): 0.0, datetime.datetime(1958, 6, 1, 0, 0): -0.7, datetime.datetime(1958, 7, 1, 0, 0): -0.4, datetime.datetime(1958, 8, 1, 0, 0): -1.0, datetime.datetime(1958, 9, 1, 0, 0): -0.4, datetime.datetime(1958, 10, 1, 0, 0): -1.0, datetime.datetime(1958, 11, 1, 0, 0): 0.4, datetime.datetime(1958, 12, 1, 0, 0): 1.0, datetime.datetime(1959, 1, 1, 0, 0): -0.1, datetime.datetime(1959, 2, 1, 0, 0): 2.3, datetime.datetime(1959, 3, 1, 0, 0): -0.5, datetime.datetime(1959, 4, 1, 0, 0): -0.5, datetime.datetime(1959, 5, 1, 0, 0): -0.5, datetime.datetime(1959, 6, 1, 0, 0): 0.5, datetime.datetime(1959, 7, 1, 0, 0): 0.7, datetime.datetime(1959, 8, 1, 0, 0): 0.5, datetime.datetime(1959, 9, 1, 0, 0): 0.0, datetime.datetime(1959, 10, 1, 0, 0): -0.1, datetime.datetime(1959, 11, 1, 0, 0): -1.0, datetime.datetime(1959, 12, 1, 0, 0): -1.2, datetime.datetime(1960, 1, 1, 0, 0): 0.3, datetime.datetime(1960, 2, 1, 0, 0): 0.3, datetime.datetime(1960, 3, 1, 0, 0): -0.3, datetime.datetime(1960, 4, 1, 0, 0): -0.9, datetime.datetime(1960, 5, 1, 0, 0): -0.9, datetime.datetime(1960, 6, 1, 0, 0): 0.2, datetime.datetime(1960, 7, 1, 0, 0): -0.3, datetime.datetime(1960, 8, 1, 0, 0): -0.1, datetime.datetime(1960, 9, 1, 0, 0): -1.4, datetime.datetime(1960, 10, 1, 0, 0): 0.1, datetime.datetime(1960, 11, 1, 0, 0): -0.0, datetime.datetime(1960, 12, 1, 0, 0): -0.1, datetime.datetime(1961, 1, 1, 0, 0): 1.0, datetime.datetime(1961, 2, 1, 0, 0): 0.0, datetime.datetime(1961, 3, 1, 0, 0): 2.2, datetime.datetime(1961, 4, 1, 0, 0): -0.2, datetime.datetime(1961, 5, 1, 0, 0): 0.2, datetime.datetime(1961, 6, 1, 0, 0): 0.5, datetime.datetime(1961, 7, 1, 0, 0): 0.3, datetime.datetime(1961, 8, 1, 0, 0): 0.6, datetime.datetime(1961, 9, 1, 0, 0): 0.2, datetime.datetime(1961, 10, 1, 0, 0): -0.2, datetime.datetime(1961, 11, 1, 0, 0): 0.5, datetime.datetime(1961, 12, 1, 0, 0): -0.6, datetime.datetime(1962, 1, 1, 0, 0): -1.1, datetime.datetime(1962, 2, 1, 0, 0): 1.0, datetime.datetime(1962, 3, 1, 0, 0): 1.0, datetime.datetime(1962, 4, 1, 0, 0): 0.4, datetime.datetime(1962, 5, 1, 0, 0): -0.8, datetime.datetime(1962, 6, 1, 0, 0): -0.8, datetime.datetime(1962, 7, 1, 0, 0): -0.5, datetime.datetime(1962, 8, 1, 0, 0): 0.7, datetime.datetime(1962, 9, 1, 0, 0): -0.8, datetime.datetime(1962, 10, 1, 0, 0): -0.9, datetime.datetime(1962, 11, 1, 0, 0): -0.6, datetime.datetime(1962, 12, 1, 0, 0): 0.0, datetime.datetime(1963, 1, 1, 0, 0): -0.3, datetime.datetime(1963, 2, 1, 0, 0): 1.6, datetime.datetime(1963, 3, 1, 0, 0): -0.7, datetime.datetime(1963, 4, 1, 0, 0): -0.9, datetime.datetime(1963, 5, 1, 0, 0): -0.6, datetime.datetime(1963, 6, 1, 0, 0): 1.0, datetime.datetime(1963, 7, 1, 0, 0): 0.7, datetime.datetime(1963, 8, 1, 0, 0): -0.2, datetime.datetime(1963, 9, 1, 0, 0): 0.8, datetime.datetime(1963, 10, 1, 0, 0): 1.8, datetime.datetime(1963, 11, 1, 0, 0): 1.6, datetime.datetime(1963, 12, 1, 0, 0): 1.7, datetime.datetime(1964, 1, 1, 0, 0): 1.1, datetime.datetime(1964, 2, 1, 0, 0): 0.7, datetime.datetime(1964, 3, 1, 0, 0): -0.4, datetime.datetime(1964, 4, 1, 0, 0): -0.3, datetime.datetime(1964, 5, 1, 0, 0): -0.4, datetime.datetime(1964, 6, 1, 0, 0): -0.5, datetime.datetime(1964, 7, 1, 0, 0): -0.8, datetime.datetime(1964, 8, 1, 0, 0): -0.5, datetime.datetime(1964, 9, 1, 0, 0): -1.5, datetime.datetime(1964, 10, 1, 0, 0): -1.1, datetime.datetime(1964, 11, 1, 0, 0): -0.9, datetime.datetime(1964, 12, 1, 0, 0): 0.3, datetime.datetime(1965, 1, 1, 0, 0): 0.1, datetime.datetime(1965, 2, 1, 0, 0): -0.7, datetime.datetime(1965, 3, 1, 0, 0): -0.5, datetime.datetime(1965, 4, 1, 0, 0): 1.8, datetime.datetime(1965, 5, 1, 0, 0): 0.3, datetime.datetime(1965, 6, 1, 0, 0): 1.7, datetime.datetime(1965, 7, 1, 0, 0): 2.7, datetime.datetime(1965, 8, 1, 0, 0): 1.1, datetime.datetime(1965, 9, 1, 0, 0): 1.4, datetime.datetime(1965, 10, 1, 0, 0): 1.8, datetime.datetime(1965, 11, 1, 0, 0): 1.7, datetime.datetime(1965, 12, 1, 0, 0): -0.7, datetime.datetime(1966, 1, 1, 0, 0): 1.3, datetime.datetime(1966, 2, 1, 0, 0): 0.3, datetime.datetime(1966, 3, 1, 0, 0): 1.2, datetime.datetime(1966, 4, 1, 0, 0): 0.5, datetime.datetime(1966, 5, 1, 0, 0): 1.4, datetime.datetime(1966, 6, 1, 0, 0): 1.0, datetime.datetime(1966, 7, 1, 0, 0): 0.1, datetime.datetime(1966, 8, 1, 0, 0): -0.0, datetime.datetime(1966, 9, 1, 0, 0): 0.2, datetime.datetime(1966, 10, 1, 0, 0): 0.7, datetime.datetime(1966, 11, 1, 0, 0): 0.2, datetime.datetime(1966, 12, 1, 0, 0): 0.3, datetime.datetime(1967, 1, 1, 0, 0): -1.2, datetime.datetime(1967, 2, 1, 0, 0): -0.8, datetime.datetime(1967, 3, 1, 0, 0): -0.2, datetime.datetime(1967, 4, 1, 0, 0): 1.3, datetime.datetime(1967, 5, 1, 0, 0): 0.1, datetime.datetime(1967, 6, 1, 0, 0): 0.2, datetime.datetime(1967, 7, 1, 0, 0): -0.0, datetime.datetime(1967, 8, 1, 0, 0): 0.2, datetime.datetime(1967, 9, 1, 0, 0): 0.8, datetime.datetime(1967, 10, 1, 0, 0): 0.2, datetime.datetime(1967, 11, 1, 0, 0): 0.2, datetime.datetime(1967, 12, 1, 0, 0): 0.5, datetime.datetime(1968, 1, 1, 0, 0): -2.1, datetime.datetime(1968, 2, 1, 0, 0): -1.3, datetime.datetime(1968, 3, 1, 0, 0): 0.8, datetime.datetime(1968, 4, 1, 0, 0): 0.3, datetime.datetime(1968, 5, 1, 0, 0): -1.4, datetime.datetime(1968, 6, 1, 0, 0): -0.1, datetime.datetime(1968, 7, 1, 0, 0): -0.1, datetime.datetime(1968, 8, 1, 0, 0): 0.1, datetime.datetime(1968, 9, 1, 0, 0): 0.3, datetime.datetime(1968, 10, 1, 0, 0): 0.4, datetime.datetime(1968, 11, 1, 0, 0): 1.1, datetime.datetime(1968, 12, 1, 0, 0): 0.0, datetime.datetime(1969, 1, 1, 0, 0): -0.4, datetime.datetime(1969, 2, 1, 0, 0): -0.1, datetime.datetime(1969, 3, 1, 0, 0): 0.9, datetime.datetime(1969, 4, 1, 0, 0): 1.5, datetime.datetime(1969, 5, 1, 0, 0): 0.1, datetime.datetime(1969, 6, 1, 0, 0): 0.4, datetime.datetime(1969, 7, 1, 0, 0): 0.7, datetime.datetime(1969, 8, 1, 0, 0): 0.8, datetime.datetime(1969, 9, 1, 0, 0): -0.1, datetime.datetime(1969, 10, 1, 0, 0): 0.9, datetime.datetime(1969, 11, 1, 0, 0): 0.4, datetime.datetime(1969, 12, 1, 0, 0): -0.4, datetime.datetime(1970, 1, 1, 0, 0): 2.0, datetime.datetime(1970, 2, 1, 0, 0): 0.8, datetime.datetime(1970, 3, 1, 0, 0): -0.2, datetime.datetime(1970, 4, 1, 0, 0): 0.6, datetime.datetime(1970, 5, 1, 0, 0): -0.3, datetime.datetime(1970, 6, 1, 0, 0): -0.5, datetime.datetime(1970, 7, 1, 0, 0): 1.0, datetime.datetime(1970, 8, 1, 0, 0): -0.6, datetime.datetime(1970, 9, 1, 0, 0): -1.8, datetime.datetime(1970, 10, 1, 0, 0): -1.9, datetime.datetime(1970, 11, 1, 0, 0): -1.2, datetime.datetime(1970, 12, 1, 0, 0): -2.1, datetime.datetime(1971, 1, 1, 0, 0): -0.4, datetime.datetime(1971, 2, 1, 0, 0): -1.9, datetime.datetime(1971, 3, 1, 0, 0): -1.4, datetime.datetime(1971, 4, 1, 0, 0): -1.4, datetime.datetime(1971, 5, 1, 0, 0): -0.5, datetime.datetime(1971, 6, 1, 0, 0): 0.7, datetime.datetime(1971, 7, 1, 0, 0): -0.3, datetime.datetime(1971, 8, 1, 0, 0): -0.9, datetime.datetime(1971, 9, 1, 0, 0): -1.1, datetime.datetime(1971, 10, 1, 0, 0): -1.1, datetime.datetime(1971, 11, 1, 0, 0): -0.4, datetime.datetime(1971, 12, 1, 0, 0): -1.5, datetime.datetime(1972, 1, 1, 0, 0): -0.4, datetime.datetime(1972, 2, 1, 0, 0): -1.3, datetime.datetime(1972, 3, 1, 0, 0): -0.7, datetime.datetime(1972, 4, 1, 0, 0): 1.2, datetime.datetime(1972, 5, 1, 0, 0): 2.8, datetime.datetime(1972, 6, 1, 0, 0): 0.5, datetime.datetime(1972, 7, 1, 0, 0): 1.0, datetime.datetime(1972, 8, 1, 0, 0): 1.2, datetime.datetime(1972, 9, 1, 0, 0): 1.8, datetime.datetime(1972, 10, 1, 0, 0): 2.0, datetime.datetime(1972, 11, 1, 0, 0): 1.1, datetime.datetime(1972, 12, 1, 0, 0): 2.3, datetime.datetime(1973, 1, 1, 0, 0): 1.1, datetime.datetime(1973, 2, 1, 0, 0): 1.9, datetime.datetime(1973, 3, 1, 0, 0): -0.4, datetime.datetime(1973, 4, 1, 0, 0): -0.4, datetime.datetime(1973, 5, 1, 0, 0): -0.1, datetime.datetime(1973, 6, 1, 0, 0): -1.3, datetime.datetime(1973, 7, 1, 0, 0): -0.4, datetime.datetime(1973, 8, 1, 0, 0): -1.1, datetime.datetime(1973, 9, 1, 0, 0): -0.5, datetime.datetime(1973, 10, 1, 0, 0): -0.6, datetime.datetime(1973, 11, 1, 0, 0): -3.0, datetime.datetime(1973, 12, 1, 0, 0): -0.7, datetime.datetime(1974, 1, 1, 0, 0): -2.2, datetime.datetime(1974, 2, 1, 0, 0): -2.0, datetime.datetime(1974, 3, 1, 0, 0): -1.9, datetime.datetime(1974, 4, 1, 0, 0): -0.6, datetime.datetime(1974, 5, 1, 0, 0): 0.1, datetime.datetime(1974, 6, 1, 0, 0): 0.1, datetime.datetime(1974, 7, 1, 0, 0): -0.2, datetime.datetime(1974, 8, 1, 0, 0): -0.5, datetime.datetime(1974, 9, 1, 0, 0): -0.9, datetime.datetime(1974, 10, 1, 0, 0): -1.0, datetime.datetime(1974, 11, 1, 0, 0): -1.0, datetime.datetime(1974, 12, 1, 0, 0): -1.2, datetime.datetime(1975, 1, 1, 0, 0): 0.2, datetime.datetime(1975, 2, 1, 0, 0): 0.5, datetime.datetime(1975, 3, 1, 0, 0): -0.8, datetime.datetime(1975, 4, 1, 0, 0): -1.6, datetime.datetime(1975, 5, 1, 0, 0): -0.5, datetime.datetime(1975, 6, 1, 0, 0): -0.9, datetime.datetime(1975, 7, 1, 0, 0): -1.1, datetime.datetime(1975, 8, 1, 0, 0): -1.3, datetime.datetime(1975, 9, 1, 0, 0): -1.5, datetime.datetime(1975, 10, 1, 0, 0): -1.7, datetime.datetime(1975, 11, 1, 0, 0): -0.7, datetime.datetime(1975, 12, 1, 0, 0): -1.8, datetime.datetime(1976, 1, 1, 0, 0): -1.1, datetime.datetime(1976, 2, 1, 0, 0): -1.0, datetime.datetime(1976, 3, 1, 0, 0): -1.8, datetime.datetime(1976, 4, 1, 0, 0): 0.5, datetime.datetime(1976, 5, 1, 0, 0): 1.1, datetime.datetime(1976, 6, 1, 0, 0): 0.3, datetime.datetime(1976, 7, 1, 0, 0): 1.2, datetime.datetime(1976, 8, 1, 0, 0): 1.5, datetime.datetime(1976, 9, 1, 0, 0): 1.0, datetime.datetime(1976, 10, 1, 0, 0): -0.7, datetime.datetime(1976, 11, 1, 0, 0): -0.9, datetime.datetime(1976, 12, 1, 0, 0): -0.8, datetime.datetime(1977, 1, 1, 0, 0): -0.3, datetime.datetime(1977, 2, 1, 0, 0): -0.8, datetime.datetime(1977, 3, 1, 0, 0): 0.7, datetime.datetime(1977, 4, 1, 0, 0): -0.1, datetime.datetime(1977, 5, 1, 0, 0): 0.4, datetime.datetime(1977, 6, 1, 0, 0): 1.2, datetime.datetime(1977, 7, 1, 0, 0): 0.8, datetime.datetime(1977, 8, 1, 0, 0): 1.0, datetime.datetime(1977, 9, 1, 0, 0): 1.0, datetime.datetime(1977, 10, 1, 0, 0): 1.7, datetime.datetime(1977, 11, 1, 0, 0): 1.3, datetime.datetime(1977, 12, 1, 0, 0): 0.8, datetime.datetime(1978, 1, 1, 0, 0): 2.0, datetime.datetime(1978, 2, 1, 0, 0): 2.5, datetime.datetime(1978, 3, 1, 0, 0): 2.1, datetime.datetime(1978, 4, 1, 0, 0): 0.7, datetime.datetime(1978, 5, 1, 0, 0): -1.6, datetime.datetime(1978, 6, 1, 0, 0): -1.2, datetime.datetime(1978, 7, 1, 0, 0): -1.5, datetime.datetime(1978, 8, 1, 0, 0): -0.7, datetime.datetime(1978, 9, 1, 0, 0): -0.3, datetime.datetime(1978, 10, 1, 0, 0): 0.1, datetime.datetime(1978, 11, 1, 0, 0): 0.4, datetime.datetime(1978, 12, 1, 0, 0): 0.1, datetime.datetime(1979, 1, 1, 0, 0): -0.2, datetime.datetime(1979, 2, 1, 0, 0): 0.5, datetime.datetime(1979, 3, 1, 0, 0): 0.5, datetime.datetime(1979, 4, 1, 0, 0): 0.3, datetime.datetime(1979, 5, 1, 0, 0): 0.3, datetime.datetime(1979, 6, 1, 0, 0): 0.3, datetime.datetime(1979, 7, 1, 0, 0): -1.7, datetime.datetime(1979, 8, 1, 0, 0): 0.7, datetime.datetime(1979, 9, 1, 0, 0): -0.2, datetime.datetime(1979, 10, 1, 0, 0): 0.4, datetime.datetime(1979, 11, 1, 0, 0): 0.4, datetime.datetime(1979, 12, 1, 0, 0): 1.2, datetime.datetime(1980, 1, 1, 0, 0): -0.3, datetime.datetime(1980, 2, 1, 0, 0): -0.1, datetime.datetime(1980, 3, 1, 0, 0): -0.2, datetime.datetime(1980, 4, 1, 0, 0): 0.3, datetime.datetime(1980, 5, 1, 0, 0): 0.4, datetime.datetime(1980, 6, 1, 0, 0): 0.2, datetime.datetime(1980, 7, 1, 0, 0): 0.4, datetime.datetime(1980, 8, 1, 0, 0): 0.8, datetime.datetime(1980, 9, 1, 0, 0): 0.8, datetime.datetime(1980, 10, 1, 0, 0): 0.1, datetime.datetime(1980, 11, 1, 0, 0): 0.4, datetime.datetime(1980, 12, 1, 0, 0): 0.0, datetime.datetime(1981, 1, 1, 0, 0): -1.1, datetime.datetime(1981, 2, 1, 0, 0): -0.2, datetime.datetime(1981, 3, 1, 0, 0): 2.5, datetime.datetime(1981, 4, 1, 0, 0): 0.5, datetime.datetime(1981, 5, 1, 0, 0): -0.4, datetime.datetime(1981, 6, 1, 0, 0): -0.8, datetime.datetime(1981, 7, 1, 0, 0): -1.0, datetime.datetime(1981, 8, 1, 0, 0): -0.2, datetime.datetime(1981, 9, 1, 0, 0): -0.4, datetime.datetime(1981, 10, 1, 0, 0): 0.5, datetime.datetime(1981, 11, 1, 0, 0): -0.3, datetime.datetime(1981, 12, 1, 0, 0): 0.2, datetime.datetime(1982, 1, 1, 0, 0): 0.1, datetime.datetime(1982, 2, 1, 0, 0): 0.6, datetime.datetime(1982, 3, 1, 0, 0): 0.1, datetime.datetime(1982, 4, 1, 0, 0): 0.7, datetime.datetime(1982, 5, 1, 0, 0): 1.0, datetime.datetime(1982, 6, 1, 0, 0): 1.6, datetime.datetime(1982, 7, 1, 0, 0): 1.7, datetime.datetime(1982, 8, 1, 0, 0): 2.1, datetime.datetime(1982, 9, 1, 0, 0): 2.1, datetime.datetime(1982, 10, 1, 0, 0): 1.9, datetime.datetime(1982, 11, 1, 0, 0): 2.4, datetime.datetime(1982, 12, 1, 0, 0): 2.0, datetime.datetime(1983, 1, 1, 0, 0): 3.6, datetime.datetime(1983, 2, 1, 0, 0): 3.9, datetime.datetime(1983, 3, 1, 0, 0): 2.7, datetime.datetime(1983, 4, 1, 0, 0): 0.7, datetime.datetime(1983, 5, 1, 0, 0): 0.8, datetime.datetime(1983, 6, 1, 0, 0): 1.0, datetime.datetime(1983, 7, 1, 0, 0): 1.6, datetime.datetime(1983, 8, 1, 0, 0): 1.5, datetime.datetime(1983, 9, 1, 0, 0): 0.2, datetime.datetime(1983, 10, 1, 0, 0): -0.1, datetime.datetime(1983, 11, 1, 0, 0): 1.0, datetime.datetime(1983, 12, 1, 0, 0): 1.2, datetime.datetime(1984, 1, 1, 0, 0): 0.9, datetime.datetime(1984, 2, 1, 0, 0): -1.1, datetime.datetime(1984, 3, 1, 0, 0): 0.7, datetime.datetime(1984, 4, 1, 0, 0): 0.7, datetime.datetime(1984, 5, 1, 0, 0): 0.2, datetime.datetime(1984, 6, 1, 0, 0): 0.9, datetime.datetime(1984, 7, 1, 0, 0): 0.4, datetime.datetime(1984, 8, 1, 0, 0): -0.4, datetime.datetime(1984, 9, 1, 0, 0): -0.1, datetime.datetime(1984, 10, 1, 0, 0): 0.7, datetime.datetime(1984, 11, 1, 0, 0): 0.6, datetime.datetime(1984, 12, 1, 0, 0): -2.2, datetime.datetime(1985, 1, 1, 0, 0): 1.3, datetime.datetime(1985, 2, 1, 0, 0): -1.0, datetime.datetime(1985, 3, 1, 0, 0): -1.3, datetime.datetime(1985, 4, 1, 0, 0): -1.9, datetime.datetime(1985, 5, 1, 0, 0): -1.5, datetime.datetime(1985, 6, 1, 0, 0): 0.3, datetime.datetime(1985, 7, 1, 0, 0): 0.8, datetime.datetime(1985, 8, 1, 0, 0): -0.2, datetime.datetime(1985, 9, 1, 0, 0): -0.4, datetime.datetime(1985, 10, 1, 0, 0): 0.1, datetime.datetime(1985, 11, 1, 0, 0): -0.3, datetime.datetime(1985, 12, 1, 0, 0): 0.3, datetime.datetime(1986, 1, 1, 0, 0): -1.5, datetime.datetime(1986, 2, 1, 0, 0): 0.5, datetime.datetime(1986, 3, 1, 0, 0): 1.0, datetime.datetime(1986, 4, 1, 0, 0): -0.1, datetime.datetime(1986, 5, 1, 0, 0): 0.7, datetime.datetime(1986, 6, 1, 0, 0): -1.3, datetime.datetime(1986, 7, 1, 0, 0): -0.0, datetime.datetime(1986, 8, 1, 0, 0): -0.6, datetime.datetime(1986, 9, 1, 0, 0): 0.3, datetime.datetime(1986, 10, 1, 0, 0): 0.3, datetime.datetime(1986, 11, 1, 0, 0): 0.6, datetime.datetime(1986, 12, 1, 0, 0): 2.4, datetime.datetime(1987, 1, 1, 0, 0): 0.9, datetime.datetime(1987, 2, 1, 0, 0): 1.0, datetime.datetime(1987, 3, 1, 0, 0): 3.3, datetime.datetime(1987, 4, 1, 0, 0): 2.1, datetime.datetime(1987, 5, 1, 0, 0): 1.7, datetime.datetime(1987, 6, 1, 0, 0): 0.8, datetime.datetime(1987, 7, 1, 0, 0): 1.9, datetime.datetime(1987, 8, 1, 0, 0): 1.7, datetime.datetime(1987, 9, 1, 0, 0): 1.6, datetime.datetime(1987, 10, 1, 0, 0): 0.6, datetime.datetime(1987, 11, 1, 0, 0): 0.2, datetime.datetime(1987, 12, 1, 0, 0): 0.5, datetime.datetime(1988, 1, 1, 0, 0): 1.6, datetime.datetime(1988, 2, 1, 0, 0): 0.3, datetime.datetime(1988, 3, 1, 0, 0): -0.6, datetime.datetime(1988, 4, 1, 0, 0): 0.7, datetime.datetime(1988, 5, 1, 0, 0): -0.1, datetime.datetime(1988, 6, 1, 0, 0): 1.6, datetime.datetime(1988, 7, 1, 0, 0): -0.0, datetime.datetime(1988, 8, 1, 0, 0): -0.1, datetime.datetime(1988, 9, 1, 0, 0): -1.3, datetime.datetime(1988, 10, 1, 0, 0): -1.5, datetime.datetime(1988, 11, 1, 0, 0): -1.3, datetime.datetime(1988, 12, 1, 0, 0): -0.8, datetime.datetime(1989, 1, 1, 0, 0): -0.8, datetime.datetime(1989, 2, 1, 0, 0): 0.4, datetime.datetime(1989, 3, 1, 0, 0): -0.1, datetime.datetime(1989, 4, 1, 0, 0): -1.8, datetime.datetime(1989, 5, 1, 0, 0): -0.8, datetime.datetime(1989, 6, 1, 0, 0): 0.5, datetime.datetime(1989, 7, 1, 0, 0): -0.7, datetime.datetime(1989, 8, 1, 0, 0): 0.7, datetime.datetime(1989, 9, 1, 0, 0): -0.2, datetime.datetime(1989, 10, 1, 0, 0): -0.7, datetime.datetime(1989, 11, 1, 0, 0): -0.0, datetime.datetime(1989, 12, 1, 0, 0): 1.6, datetime.datetime(1990, 1, 1, 0, 0): 0.7, datetime.datetime(1990, 2, 1, 0, 0): 3.6, datetime.datetime(1990, 3, 1, 0, 0): 0.9, datetime.datetime(1990, 4, 1, 0, 0): 0.3, datetime.datetime(1990, 5, 1, 0, 0): -0.6, datetime.datetime(1990, 6, 1, 0, 0): 0.1, datetime.datetime(1990, 7, 1, 0, 0): -0.0, datetime.datetime(1990, 8, 1, 0, 0): 0.9, datetime.datetime(1990, 9, 1, 0, 0): 1.4, datetime.datetime(1990, 10, 1, 0, 0): 0.3, datetime.datetime(1990, 11, 1, 0, 0): 0.4, datetime.datetime(1990, 12, 1, 0, 0): 0.4, datetime.datetime(1991, 1, 1, 0, 0): 0.1, datetime.datetime(1991, 2, 1, 0, 0): 0.1, datetime.datetime(1991, 3, 1, 0, 0): 2.1, datetime.datetime(1991, 4, 1, 0, 0): 0.5, datetime.datetime(1991, 5, 1, 0, 0): 1.7, datetime.datetime(1991, 6, 1, 0, 0): 1.0, datetime.datetime(1991, 7, 1, 0, 0): 0.6, datetime.datetime(1991, 8, 1, 0, 0): 1.4, datetime.datetime(1991, 9, 1, 0, 0): 1.4, datetime.datetime(1991, 10, 1, 0, 0): 0.5, datetime.datetime(1991, 11, 1, 0, 0): 1.4, datetime.datetime(1991, 12, 1, 0, 0): 1.2, datetime.datetime(1992, 1, 1, 0, 0): 3.9, datetime.datetime(1992, 2, 1, 0, 0): 1.3, datetime.datetime(1992, 3, 1, 0, 0): 3.1, datetime.datetime(1992, 4, 1, 0, 0): 1.6, datetime.datetime(1992, 5, 1, 0, 0): 0.2, datetime.datetime(1992, 6, 1, 0, 0): 0.2, datetime.datetime(1992, 7, 1, 0, 0): 2.1, datetime.datetime(1992, 8, 1, 0, 0): 0.2, datetime.datetime(1992, 9, 1, 0, 0): -0.7, datetime.datetime(1992, 10, 1, 0, 0): 0.6, datetime.datetime(1992, 11, 1, 0, 0): 0.8, datetime.datetime(1992, 12, 1, 0, 0): 0.0, datetime.datetime(1993, 1, 1, 0, 0): 0.6, datetime.datetime(1993, 2, 1, 0, 0): 0.0, datetime.datetime(1993, 3, 1, 0, 0): 2.7, datetime.datetime(1993, 4, 1, 0, 0): 2.0, datetime.datetime(1993, 5, 1, 0, 0): 1.5, datetime.datetime(1993, 6, 1, 0, 0): 1.6, datetime.datetime(1993, 7, 1, 0, 0): 0.7, datetime.datetime(1993, 8, 1, 0, 0): 2.5, datetime.datetime(1993, 9, 1, 0, 0): 1.5, datetime.datetime(1993, 10, 1, 0, 0): 1.4, datetime.datetime(1993, 11, 1, 0, 0): 0.3, datetime.datetime(1993, 12, 1, 0, 0): -0.3, datetime.datetime(1994, 1, 1, 0, 0): 0.5, datetime.datetime(1994, 2, 1, 0, 0): 0.1, datetime.datetime(1994, 3, 1, 0, 0): 2.0, datetime.datetime(1994, 4, 1, 0, 0): 1.4, datetime.datetime(1994, 5, 1, 0, 0): 1.1, datetime.datetime(1994, 6, 1, 0, 0): 0.6, datetime.datetime(1994, 7, 1, 0, 0): 1.3, datetime.datetime(1994, 8, 1, 0, 0): 2.3, datetime.datetime(1994, 9, 1, 0, 0): 1.6, datetime.datetime(1994, 10, 1, 0, 0): 1.3, datetime.datetime(1994, 11, 1, 0, 0): 1.1, datetime.datetime(1994, 12, 1, 0, 0): 2.0, datetime.datetime(1995, 1, 1, 0, 0): 0.8, datetime.datetime(1995, 2, 1, 0, 0): 1.4, datetime.datetime(1995, 3, 1, 0, 0): -0.2, datetime.datetime(1995, 4, 1, 0, 0): 0.2, datetime.datetime(1995, 5, 1, 0, 0): 0.7, datetime.datetime(1995, 6, 1, 0, 0): 0.7, datetime.datetime(1995, 7, 1, 0, 0): -0.1, datetime.datetime(1995, 8, 1, 0, 0): 0.6, datetime.datetime(1995, 9, 1, 0, 0): 0.1, datetime.datetime(1995, 10, 1, 0, 0): -0.4, datetime.datetime(1995, 11, 1, 0, 0): 0.1, datetime.datetime(1995, 12, 1, 0, 0): 0.2, datetime.datetime(1996, 1, 1, 0, 0): -0.5, datetime.datetime(1996, 2, 1, 0, 0): -0.2, datetime.datetime(1996, 3, 1, 0, 0): -0.0, datetime.datetime(1996, 4, 1, 0, 0): -0.4, datetime.datetime(1996, 5, 1, 0, 0): 1.3, datetime.datetime(1996, 6, 1, 0, 0): 0.1, datetime.datetime(1996, 7, 1, 0, 0): -0.3, datetime.datetime(1996, 8, 1, 0, 0): -0.2, datetime.datetime(1996, 9, 1, 0, 0): -1.6, datetime.datetime(1996, 10, 1, 0, 0): -0.9, datetime.datetime(1996, 11, 1, 0, 0): -0.3, datetime.datetime(1996, 12, 1, 0, 0): -1.7, datetime.datetime(1997, 1, 1, 0, 0): 1.1, datetime.datetime(1997, 2, 1, 0, 0): -1.6, datetime.datetime(1997, 3, 1, 0, 0): 1.2, datetime.datetime(1997, 4, 1, 0, 0): 2.5, datetime.datetime(1997, 5, 1, 0, 0): 1.0, datetime.datetime(1997, 6, 1, 0, 0): 2.4, datetime.datetime(1997, 7, 1, 0, 0): 1.5, datetime.datetime(1997, 8, 1, 0, 0): 2.5, datetime.datetime(1997, 9, 1, 0, 0): 2.8, datetime.datetime(1997, 10, 1, 0, 0): 2.8, datetime.datetime(1997, 11, 1, 0, 0): 2.7, datetime.datetime(1997, 12, 1, 0, 0): 1.3, datetime.datetime(1998, 1, 1, 0, 0): 1.6, datetime.datetime(1998, 2, 1, 0, 0): 3.8, datetime.datetime(1998, 3, 1, 0, 0): 2.6, datetime.datetime(1998, 4, 1, 0, 0): 1.7, datetime.datetime(1998, 5, 1, 0, 0): 0.6, datetime.datetime(1998, 6, 1, 0, 0): -0.2, datetime.datetime(1998, 7, 1, 0, 0): -0.2, datetime.datetime(1998, 8, 1, 0, 0): 0.1, datetime.datetime(1998, 9, 1, 0, 0): -0.3, datetime.datetime(1998, 10, 1, 0, 0): -1.0, datetime.datetime(1998, 11, 1, 0, 0): -1.4, datetime.datetime(1998, 12, 1, 0, 0): -1.4, datetime.datetime(1999, 1, 1, 0, 0): -1.3, datetime.datetime(1999, 2, 1, 0, 0): -0.2, datetime.datetime(1999, 3, 1, 0, 0): -1.1, datetime.datetime(1999, 4, 1, 0, 0): -0.7, datetime.datetime(1999, 5, 1, 0, 0): 1.2, datetime.datetime(1999, 6, 1, 0, 0): 0.8, datetime.datetime(1999, 7, 1, 0, 0): 0.4, datetime.datetime(1999, 8, 1, 0, 0): 1.4, datetime.datetime(1999, 9, 1, 0, 0): 0.5, datetime.datetime(1999, 10, 1, 0, 0): -0.3, datetime.datetime(1999, 11, 1, 0, 0): -0.7, datetime.datetime(1999, 12, 1, 0, 0): -0.7, datetime.datetime(2000, 1, 1, 0, 0): 0.5, datetime.datetime(2000, 2, 1, 0, 0): 0.2, datetime.datetime(2000, 3, 1, 0, 0): -0.0, datetime.datetime(2000, 4, 1, 0, 0): -0.8, datetime.datetime(2000, 5, 1, 0, 0): 0.8, datetime.datetime(2000, 6, 1, 0, 0): 1.2, datetime.datetime(2000, 7, 1, 0, 0): 0.3, datetime.datetime(2000, 8, 1, 0, 0): -0.4, datetime.datetime(2000, 9, 1, 0, 0): 0.1, datetime.datetime(2000, 10, 1, 0, 0): -1.5, datetime.datetime(2000, 11, 1, 0, 0): -2.2, datetime.datetime(2000, 12, 1, 0, 0): -2.4, datetime.datetime(2001, 1, 1, 0, 0): 1.0, datetime.datetime(2001, 2, 1, 0, 0): -2.9, datetime.datetime(2001, 3, 1, 0, 0): 0.5, datetime.datetime(2001, 4, 1, 0, 0): 0.0, datetime.datetime(2001, 5, 1, 0, 0): 1.3, datetime.datetime(2001, 6, 1, 0, 0): -0.1, datetime.datetime(2001, 7, 1, 0, 0): 0.6, datetime.datetime(2001, 8, 1, 0, 0): 0.7, datetime.datetime(2001, 9, 1, 0, 0): -0.1, datetime.datetime(2001, 10, 1, 0, 0): -0.7, datetime.datetime(2001, 11, 1, 0, 0): -0.3, datetime.datetime(2001, 12, 1, 0, 0): 0.4, datetime.datetime(2002, 1, 1, 0, 0): 1.0, datetime.datetime(2002, 2, 1, 0, 0): 0.2, datetime.datetime(2002, 3, 1, 0, 0): 1.7, datetime.datetime(2002, 4, 1, 0, 0): 0.6, datetime.datetime(2002, 5, 1, 0, 0): 1.2, datetime.datetime(2002, 6, 1, 0, 0): 0.8, datetime.datetime(2002, 7, 1, 0, 0): 1.8, datetime.datetime(2002, 8, 1, 0, 0): 1.1, datetime.datetime(2002, 9, 1, 0, 0): 1.1, datetime.datetime(2002, 10, 1, 0, 0): -0.1, datetime.datetime(2002, 11, 1, 0, 0): 1.1, datetime.datetime(2002, 12, 1, 0, 0): 1.8, datetime.datetime(2003, 1, 1, 0, 0): 0.7, datetime.datetime(2003, 2, 1, 0, 0): 0.2, datetime.datetime(2003, 3, 1, 0, 0): 1.1, datetime.datetime(2003, 4, 1, 0, 0): 1.1, datetime.datetime(2003, 5, 1, 0, 0): 0.6, datetime.datetime(2003, 6, 1, 0, 0): 0.7, datetime.datetime(2003, 7, 1, 0, 0): 0.6, datetime.datetime(2003, 8, 1, 0, 0): 0.4, datetime.datetime(2003, 9, 1, 0, 0): 0.2, datetime.datetime(2003, 10, 1, 0, 0): -0.3, datetime.datetime(2003, 11, 1, 0, 0): 0.6, datetime.datetime(2003, 12, 1, 0, 0): -1.1, datetime.datetime(2004, 1, 1, 0, 0): 1.4, datetime.datetime(2004, 2, 1, 0, 0): -0.2, datetime.datetime(2004, 3, 1, 0, 0): -0.6, datetime.datetime(2004, 4, 1, 0, 0): 1.2, datetime.datetime(2004, 5, 1, 0, 0): -0.3, datetime.datetime(2004, 6, 1, 0, 0): 2.2, datetime.datetime(2004, 7, 1, 0, 0): 1.1, datetime.datetime(2004, 8, 1, 0, 0): 0.9, datetime.datetime(2004, 9, 1, 0, 0): 1.2, datetime.datetime(2004, 10, 1, 0, 0): 0.5, datetime.datetime(2004, 11, 1, 0, 0): 0.5, datetime.datetime(2004, 12, 1, 0, 0): 0.0, datetime.datetime(2005, 1, 1, 0, 0): 0.1, datetime.datetime(2005, 2, 1, 0, 0): 2.6, datetime.datetime(2005, 3, 1, 0, 0): 1.1, datetime.datetime(2005, 4, 1, 0, 0): 1.7, datetime.datetime(2005, 5, 1, 0, 0): 1.4, datetime.datetime(2005, 6, 1, 0, 0): -0.2, datetime.datetime(2005, 7, 1, 0, 0): 0.4, datetime.datetime(2005, 8, 1, 0, 0): 0.9, datetime.datetime(2005, 9, 1, 0, 0): 0.0, datetime.datetime(2005, 10, 1, 0, 0): -0.7, datetime.datetime(2005, 11, 1, 0, 0): -0.4, datetime.datetime(2005, 12, 1, 0, 0): 0.4, datetime.datetime(2006, 1, 1, 0, 0): -1.5, datetime.datetime(2006, 2, 1, 0, 0): 1.0, datetime.datetime(2006, 3, 1, 0, 0): -1.2, datetime.datetime(2006, 4, 1, 0, 0): -1.7, datetime.datetime(2006, 5, 1, 0, 0): 1.2, datetime.datetime(2006, 6, 1, 0, 0): 1.2, datetime.datetime(2006, 7, 1, 0, 0): 1.6, datetime.datetime(2006, 8, 1, 0, 0): 2.0, datetime.datetime(2006, 9, 1, 0, 0): 1.4, datetime.datetime(2006, 10, 1, 0, 0): 2.3, datetime.datetime(2006, 11, 1, 0, 0): 1.1, datetime.datetime(2006, 12, 1, 0, 0): 1.4, datetime.datetime(2007, 1, 1, 0, 0): 0.5, datetime.datetime(2007, 2, 1, 0, 0): 0.7, datetime.datetime(2007, 3, 1, 0, 0): 0.3, datetime.datetime(2007, 4, 1, 0, 0): 1.2, datetime.datetime(2007, 5, 1, 0, 0): 0.9, datetime.datetime(2007, 6, 1, 0, 0): -0.8, datetime.datetime(2007, 7, 1, 0, 0): 1.4, datetime.datetime(2007, 8, 1, 0, 0): 0.8, datetime.datetime(2007, 9, 1, 0, 0): -0.4, datetime.datetime(2007, 10, 1, 0, 0): -0.6, datetime.datetime(2007, 11, 1, 0, 0): -1.1, datetime.datetime(2007, 12, 1, 0, 0): -1.3, datetime.datetime(2008, 1, 1, 0, 0): -1.3, datetime.datetime(2008, 2, 1, 0, 0): -1.7, datetime.datetime(2008, 3, 1, 0, 0): 1.0, datetime.datetime(2008, 4, 1, 0, 0): 0.5, datetime.datetime(2008, 5, 1, 0, 0): 1.3, datetime.datetime(2008, 6, 1, 0, 0): 0.8, datetime.datetime(2008, 7, 1, 0, 0): 0.6, datetime.datetime(2008, 8, 1, 0, 0): 0.9, datetime.datetime(2008, 9, 1, 0, 0): -0.2, datetime.datetime(2008, 10, 1, 0, 0): 0.4, datetime.datetime(2008, 11, 1, 0, 0): -0.6, datetime.datetime(2008, 12, 1, 0, 0): -0.8, datetime.datetime(2009, 1, 1, 0, 0): -0.2, datetime.datetime(2009, 2, 1, 0, 0): -1.2, datetime.datetime(2009, 3, 1, 0, 0): 1.1, datetime.datetime(2009, 4, 1, 0, 0): -0.1, datetime.datetime(2009, 5, 1, 0, 0): -0.3, datetime.datetime(2009, 6, 1, 0, 0): 0.4, datetime.datetime(2009, 7, 1, 0, 0): 0.3, datetime.datetime(2009, 8, 1, 0, 0): 0.3, datetime.datetime(2009, 9, 1, 0, 0): -0.6, datetime.datetime(2009, 10, 1, 0, 0): 0.8, datetime.datetime(2009, 11, 1, 0, 0): 0.2, datetime.datetime(2009, 12, 1, 0, 0): 0.6, datetime.datetime(2010, 1, 1, 0, 0): -0.3, datetime.datetime(2010, 2, 1, 0, 0): 1.4, datetime.datetime(2010, 3, 1, 0, 0): 1.5, datetime.datetime(2010, 4, 1, 0, 0): 0.2, datetime.datetime(2010, 5, 1, 0, 0): -0.7, datetime.datetime(2010, 6, 1, 0, 0): 0.9, datetime.datetime(2010, 7, 1, 0, 0): -0.4, datetime.datetime(2010, 8, 1, 0, 0): -0.4, datetime.datetime(2010, 9, 1, 0, 0): -1.1, datetime.datetime(2010, 10, 1, 0, 0): -1.3, datetime.datetime(2010, 11, 1, 0, 0): -0.2, datetime.datetime(2010, 12, 1, 0, 0): -2.4, datetime.datetime(2011, 1, 1, 0, 0): -1.1, datetime.datetime(2011, 2, 1, 0, 0): -1.4, datetime.datetime(2011, 3, 1, 0, 0): -1.1, datetime.datetime(2011, 4, 1, 0, 0): -0.5, datetime.datetime(2011, 5, 1, 0, 0): 1.1, datetime.datetime(2011, 6, 1, 0, 0): 1.2, datetime.datetime(2011, 7, 1, 0, 0): 0.4, datetime.datetime(2011, 8, 1, 0, 0): 1.0, datetime.datetime(2011, 9, 1, 0, 0): 0.7, datetime.datetime(2011, 10, 1, 0, 0): -0.3, datetime.datetime(2011, 11, 1, 0, 0): -0.1, datetime.datetime(2011, 12, 1, 0, 0): -2.3, datetime.datetime(2012, 1, 1, 0, 0): -0.2, datetime.datetime(2012, 2, 1, 0, 0): 0.8, datetime.datetime(2012, 3, 1, 0, 0): -1.1, datetime.datetime(2012, 4, 1, 0, 0): 1.3, datetime.datetime(2012, 5, 1, 0, 0): 0.4, datetime.datetime(2012, 6, 1, 0, 0): 1.0, datetime.datetime(2012, 7, 1, 0, 0): -0.0, datetime.datetime(2012, 8, 1, 0, 0): 1.4, datetime.datetime(2012, 9, 1, 0, 0): 0.3, datetime.datetime(2012, 10, 1, 0, 0): 0.2, datetime.datetime(2012, 11, 1, 0, 0): 0.6, datetime.datetime(2012, 12, 1, 0, 0): 0.4, datetime.datetime(2013, 1, 1, 0, 0): -0.4, datetime.datetime(2013, 2, 1, 0, 0): 0.8, datetime.datetime(2013, 3, 1, 0, 0): -0.2, datetime.datetime(2013, 4, 1, 0, 0): 0.3, datetime.datetime(2013, 5, 1, 0, 0): -0.1, datetime.datetime(2013, 6, 1, 0, 0): -1.1, datetime.datetime(2013, 7, 1, 0, 0): -0.3, datetime.datetime(2013, 8, 1, 0, 0): 0.5, datetime.datetime(2013, 9, 1, 0, 0): -0.3, datetime.datetime(2013, 10, 1, 0, 0): 0.1, datetime.datetime(2013, 11, 1, 0, 0): -1.0, datetime.datetime(2013, 12, 1, 0, 0): 0.4, datetime.datetime(2014, 1, 1, 0, 0): -1.2, datetime.datetime(2014, 2, 1, 0, 0): -0.4, datetime.datetime(2014, 3, 1, 0, 0): 1.7, datetime.datetime(2014, 4, 1, 0, 0): -0.5, datetime.datetime(2014, 5, 1, 0, 0): 0.8, datetime.datetime(2014, 6, 1, 0, 0): 0.2, datetime.datetime(2014, 7, 1, 0, 0): 1.1, datetime.datetime(2014, 8, 1, 0, 0): 1.9, datetime.datetime(2014, 9, 1, 0, 0): 1.2, datetime.datetime(2014, 10, 1, 0, 0): 1.0, datetime.datetime(2014, 11, 1, 0, 0): 1.2, datetime.datetime(2014, 12, 1, 0, 0): 0.2, datetime.datetime(2015, 1, 1, 0, 0): 0.3, datetime.datetime(2015, 2, 1, 0, 0): 1.4, datetime.datetime(2015, 3, 1, 0, 0): 1.5, datetime.datetime(2015, 4, 1, 0, 0): 1.1, datetime.datetime(2015, 5, 1, 0, 0): 2.2, datetime.datetime(2015, 6, 1, 0, 0): 1.0, datetime.datetime(2015, 7, 1, 0, 0): 2.2, datetime.datetime(2015, 8, 1, 0, 0): 2.2, datetime.datetime(2015, 9, 1, 0, 0): 2.0, datetime.datetime(2015, 10, 1, 0, 0): 3.2, datetime.datetime(2015, 11, 1, 0, 0): 0.8, datetime.datetime(2015, 12, 1, 0, 0): -0.3, datetime.datetime(2016, 1, 1, 0, 0): 4.0, datetime.datetime(2016, 2, 1, 0, 0): 2.2, datetime.datetime(2016, 3, 1, 0, 0): 1.8, datetime.datetime(2016, 4, 1, 0, 0): 1.4, datetime.datetime(2016, 5, 1, 0, 0): 0.0, datetime.datetime(2016, 6, 1, 0, 0): -0.1, datetime.datetime(2016, 7, 1, 0, 0): 0.3, datetime.datetime(2016, 8, 1, 0, 0): -0.2, datetime.datetime(2016, 9, 1, 0, 0): -0.9, datetime.datetime(2016, 10, 1, 0, 0): -0.2, datetime.datetime(2016, 11, 1, 0, 0): 0.1, datetime.datetime(2016, 12, 1, 0, 0): -0.6, datetime.datetime(2017, 1, 1, 0, 0): -0.2, datetime.datetime(2017, 2, 1, 0, 0): 0.7, datetime.datetime(2017, 3, 1, 0, 0): -0.0, datetime.datetime(2017, 4, 1, 0, 0): 0.3, datetime.datetime(2017, 5, 1, 0, 0): 0.8, datetime.datetime(2017, 6, 1, 0, 0): 1.2, datetime.datetime(2017, 7, 1, 0, 0): 0.4, datetime.datetime(2017, 8, 1, 0, 0): 0.4, datetime.datetime(2017, 9, 1, 0, 0): 0.4, datetime.datetime(2017, 10, 1, 0, 0): -1.2, datetime.datetime(2017, 11, 1, 0, 0): -1.3, datetime.datetime(2017, 12, 1, 0, 0): 0.0, datetime.datetime(2018, 1, 1, 0, 0): -1.4, datetime.datetime(2018, 2, 1, 0, 0): 0.6, datetime.datetime(2018, 3, 1, 0, 0): -1.3, datetime.datetime(2018, 4, 1, 0, 0): 0.1, datetime.datetime(2018, 5, 1, 0, 0): 1.3, datetime.datetime(2018, 6, 1, 0, 0): 1.4, datetime.datetime(2018, 7, 1, 0, 0): -0.0, datetime.datetime(2018, 8, 1, 0, 0): 0.5, datetime.datetime(2018, 9, 1, 0, 0): 0.4, datetime.datetime(2018, 10, 1, 0, 0): 0.4, datetime.datetime(2018, 11, 1, 0, 0): 0.7, datetime.datetime(2018, 12, 1, 0, 0): -1.1, datetime.datetime(2019, 1, 1, 0, 0): 0.6, datetime.datetime(2019, 2, 1, 0, 0): 2.6, datetime.datetime(2019, 3, 1, 0, 0): 1.0, datetime.datetime(2019, 4, 1, 0, 0): 0.7, datetime.datetime(2019, 5, 1, 0, 0): 1.4, datetime.datetime(2019, 6, 1, 0, 0): 1.5, datetime.datetime(2019, 7, 1, 0, 0): 1.4, datetime.datetime(2019, 8, 1, 0, 0): 1.7, datetime.datetime(2019, 9, 1, 0, 0): 2.6, datetime.datetime(2019, 10, 1, 0, 0): 0.8, datetime.datetime(2019, 11, 1, 0, 0): 1.0, datetime.datetime(2019, 12, 1, 0, 0): 1.1, datetime.datetime(2020, 1, 1, 0, 0): 1.0, datetime.datetime(2020, 2, 1, 0, 0): 1.0, datetime.datetime(2020, 3, 1, 0, 0): 1.7, datetime.datetime(2020, 4, 1, 0, 0): 1.1, datetime.datetime(2020, 5, 1, 0, 0): 1.5, datetime.datetime(2020, 6, 1, 0, 0): 0.6, datetime.datetime(2020, 7, 1, 0, 0): -0.1, datetime.datetime(2020, 8, 1, 0, 0): -0.1, datetime.datetime(2020, 9, 1, 0, 0): -0.3, datetime.datetime(2020, 10, 1, 0, 0): -0.6, datetime.datetime(2020, 11, 1, 0, 0): 0.3, datetime.datetime(2020, 12, 1, 0, 0): -0.8, datetime.datetime(2021, 1, 1, 0, 0): -0.6, datetime.datetime(2021, 2, 1, 0, 0): -1.4, datetime.datetime(2021, 3, 1, 0, 0): 0.7, datetime.datetime(2021, 4, 1, 0, 0): 0.3, datetime.datetime(2021, 5, 1, 0, 0): 0.4, datetime.datetime(2021, 6, 1, 0, 0): 0.8, datetime.datetime(2021, 7, 1, 0, 0): -0.5, datetime.datetime(2021, 8, 1, 0, 0): 0.7, datetime.datetime(2021, 9, 1, 0, 0): 0.1, datetime.datetime(2021, 10, 1, 0, 0): -0.9, datetime.datetime(2021, 11, 1, 0, 0): -0.4, datetime.datetime(2021, 12, 1, 0, 0): -0.8, datetime.datetime(2022, 1, 1, 0, 0): 0.3, datetime.datetime(2022, 2, 1, 0, 0): 0.5, datetime.datetime(2022, 3, 1, 0, 0): 0.1, datetime.datetime(2022, 4, 1, 0, 0): -0.9, datetime.datetime(2022, 5, 1, 0, 0): -0.5, datetime.datetime(2022, 6, 1, 0, 0): -0.6, datetime.datetime(2022, 7, 1, 0, 0): 0.3, datetime.datetime(2022, 8, 1, 0, 0): -0.4, datetime.datetime(2022, 9, 1, 0, 0): -0.6, datetime.datetime(2022, 10, 1, 0, 0): -1.3, datetime.datetime(2022, 11, 1, 0, 0): -0.1, datetime.datetime(2022, 12, 1, 0, 0): -1.7, datetime.datetime(2023, 1, 1, 0, 0): -0.2, datetime.datetime(2023, 2, 1, 0, 0): -1.1, datetime.datetime(2023, 3, 1, 0, 0): 1.0, datetime.datetime(2023, 4, 1, 0, 0): -0.3, datetime.datetime(2023, 5, 1, 0, 0): 2.2, datetime.datetime(2023, 6, 1, 0, 0): 0.5, datetime.datetime(2023, 7, 1, 0, 0): 1.3, datetime.datetime(2023, 8, 1, 0, 0): 2.5, datetime.datetime(2023, 9, 1, 0, 0): 1.7, datetime.datetime(2023, 10, 1, 0, 0): 2.3, datetime.datetime(2023, 11, 1, 0, 0): 1.5, datetime.datetime(2023, 12, 1, 0, 0): 0.7, datetime.datetime(2024, 1, 1, 0, 0): -0.0, datetime.datetime(2024, 2, 1, 0, 0): 1.8, datetime.datetime(2024, 3, 1, 0, 0): 0.9}
ao_data_dict = {datetime.datetime(1950, 1, 1, 0, 0): -0.06, datetime.datetime(1950, 2, 1, 0, 0): 0.627, datetime.datetime(1950, 3, 1, 0, 0): -0.008, datetime.datetime(1950, 4, 1, 0, 0): 0.555, datetime.datetime(1950, 5, 1, 0, 0): 0.07200000000000001, datetime.datetime(1950, 6, 1, 0, 0): 0.539, datetime.datetime(1950, 7, 1, 0, 0): -0.802, datetime.datetime(1950, 8, 1, 0, 0): -0.851, datetime.datetime(1950, 9, 1, 0, 0): 0.358, datetime.datetime(1950, 10, 1, 0, 0): -0.379, datetime.datetime(1950, 11, 1, 0, 0): -0.515, datetime.datetime(1950, 12, 1, 0, 0): -1.9280000000000002, datetime.datetime(1951, 1, 1, 0, 0): -0.085, datetime.datetime(1951, 2, 1, 0, 0): -0.4, datetime.datetime(1951, 3, 1, 0, 0): -1.9340000000000002, datetime.datetime(1951, 4, 1, 0, 0): -0.7759999999999999, datetime.datetime(1951, 5, 1, 0, 0): -0.863, datetime.datetime(1951, 6, 1, 0, 0): -0.9179999999999999, datetime.datetime(1951, 7, 1, 0, 0): 0.09, datetime.datetime(1951, 8, 1, 0, 0): -0.377, datetime.datetime(1951, 9, 1, 0, 0): -0.818, datetime.datetime(1951, 10, 1, 0, 0): -0.213, datetime.datetime(1951, 11, 1, 0, 0): -0.069, datetime.datetime(1951, 12, 1, 0, 0): 1.9869999999999999, datetime.datetime(1952, 1, 1, 0, 0): 0.368, datetime.datetime(1952, 2, 1, 0, 0): -1.7469999999999999, datetime.datetime(1952, 3, 1, 0, 0): -1.859, datetime.datetime(1952, 4, 1, 0, 0): 0.539, datetime.datetime(1952, 5, 1, 0, 0): -0.774, datetime.datetime(1952, 6, 1, 0, 0): -0.441, datetime.datetime(1952, 7, 1, 0, 0): 0.38299999999999995, datetime.datetime(1952, 8, 1, 0, 0): -0.03, datetime.datetime(1952, 9, 1, 0, 0): -0.38299999999999995, datetime.datetime(1952, 10, 1, 0, 0): -0.43700000000000006, datetime.datetime(1952, 11, 1, 0, 0): -1.891, datetime.datetime(1952, 12, 1, 0, 0): -1.827, datetime.datetime(1953, 1, 1, 0, 0): -1.036, datetime.datetime(1953, 2, 1, 0, 0): -0.249, datetime.datetime(1953, 3, 1, 0, 0): 1.068, datetime.datetime(1953, 4, 1, 0, 0): -1.256, datetime.datetime(1953, 5, 1, 0, 0): -0.562, datetime.datetime(1953, 6, 1, 0, 0): 0.023, datetime.datetime(1953, 7, 1, 0, 0): 0.33299999999999996, datetime.datetime(1953, 8, 1, 0, 0): 0.085, datetime.datetime(1953, 9, 1, 0, 0): 0.662, datetime.datetime(1953, 10, 1, 0, 0): -0.19399999999999998, datetime.datetime(1953, 11, 1, 0, 0): 0.354, datetime.datetime(1953, 12, 1, 0, 0): 0.575, datetime.datetime(1954, 1, 1, 0, 0): -0.14800000000000002, datetime.datetime(1954, 2, 1, 0, 0): -0.18100000000000002, datetime.datetime(1954, 3, 1, 0, 0): 0.47600000000000003, datetime.datetime(1954, 4, 1, 0, 0): 0.512, datetime.datetime(1954, 5, 1, 0, 0): -1.656, datetime.datetime(1954, 6, 1, 0, 0): -0.268, datetime.datetime(1954, 7, 1, 0, 0): 0.341, datetime.datetime(1954, 8, 1, 0, 0): -0.122, datetime.datetime(1954, 9, 1, 0, 0): 0.301, datetime.datetime(1954, 10, 1, 0, 0): 0.513, datetime.datetime(1954, 11, 1, 0, 0): -0.32799999999999996, datetime.datetime(1954, 12, 1, 0, 0): 0.5529999999999999, datetime.datetime(1955, 1, 1, 0, 0): -1.163, datetime.datetime(1955, 2, 1, 0, 0): -1.5419999999999998, datetime.datetime(1955, 3, 1, 0, 0): -1.568, datetime.datetime(1955, 4, 1, 0, 0): 0.19399999999999998, datetime.datetime(1955, 5, 1, 0, 0): 0.242, datetime.datetime(1955, 6, 1, 0, 0): -0.266, datetime.datetime(1955, 7, 1, 0, 0): 0.332, datetime.datetime(1955, 8, 1, 0, 0): 0.76, datetime.datetime(1955, 9, 1, 0, 0): 0.35700000000000004, datetime.datetime(1955, 10, 1, 0, 0): 0.099, datetime.datetime(1955, 11, 1, 0, 0): -1.3419999999999999, datetime.datetime(1955, 12, 1, 0, 0): -0.444, datetime.datetime(1956, 1, 1, 0, 0): -1.204, datetime.datetime(1956, 2, 1, 0, 0): -2.029, datetime.datetime(1956, 3, 1, 0, 0): 0.47, datetime.datetime(1956, 4, 1, 0, 0): -0.868, datetime.datetime(1956, 5, 1, 0, 0): 1.391, datetime.datetime(1956, 6, 1, 0, 0): 0.28, datetime.datetime(1956, 7, 1, 0, 0): -0.215, datetime.datetime(1956, 8, 1, 0, 0): -0.652, datetime.datetime(1956, 9, 1, 0, 0): -0.20199999999999999, datetime.datetime(1956, 10, 1, 0, 0): 1.139, datetime.datetime(1956, 11, 1, 0, 0): -0.066, datetime.datetime(1956, 12, 1, 0, 0): 0.001, datetime.datetime(1957, 1, 1, 0, 0): 2.062, datetime.datetime(1957, 2, 1, 0, 0): -1.5130000000000001, datetime.datetime(1957, 3, 1, 0, 0): -2.013, datetime.datetime(1957, 4, 1, 0, 0): 0.23800000000000002, datetime.datetime(1957, 5, 1, 0, 0): -0.966, datetime.datetime(1957, 6, 1, 0, 0): -0.76, datetime.datetime(1957, 7, 1, 0, 0): -0.6459999999999999, datetime.datetime(1957, 8, 1, 0, 0): 0.09699999999999999, datetime.datetime(1957, 9, 1, 0, 0): -0.956, datetime.datetime(1957, 10, 1, 0, 0): 0.903, datetime.datetime(1957, 11, 1, 0, 0): -1.38, datetime.datetime(1957, 12, 1, 0, 0): 0.828, datetime.datetime(1958, 1, 1, 0, 0): -1.4380000000000002, datetime.datetime(1958, 2, 1, 0, 0): -2.228, datetime.datetime(1958, 3, 1, 0, 0): -2.522, datetime.datetime(1958, 4, 1, 0, 0): -0.36, datetime.datetime(1958, 5, 1, 0, 0): -0.336, datetime.datetime(1958, 6, 1, 0, 0): -1.149, datetime.datetime(1958, 7, 1, 0, 0): -0.684, datetime.datetime(1958, 8, 1, 0, 0): -0.755, datetime.datetime(1958, 9, 1, 0, 0): -0.012, datetime.datetime(1958, 10, 1, 0, 0): 0.77, datetime.datetime(1958, 11, 1, 0, 0): -0.011000000000000001, datetime.datetime(1958, 12, 1, 0, 0): -1.6869999999999998, datetime.datetime(1959, 1, 1, 0, 0): -2.013, datetime.datetime(1959, 2, 1, 0, 0): 2.544, datetime.datetime(1959, 3, 1, 0, 0): 1.432, datetime.datetime(1959, 4, 1, 0, 0): 0.11900000000000001, datetime.datetime(1959, 5, 1, 0, 0): -0.341, datetime.datetime(1959, 6, 1, 0, 0): -0.033, datetime.datetime(1959, 7, 1, 0, 0): 0.105, datetime.datetime(1959, 8, 1, 0, 0): -0.745, datetime.datetime(1959, 9, 1, 0, 0): -0.281, datetime.datetime(1959, 10, 1, 0, 0): -0.249, datetime.datetime(1959, 11, 1, 0, 0): -1.411, datetime.datetime(1959, 12, 1, 0, 0): -0.042, datetime.datetime(1960, 1, 1, 0, 0): -2.484, datetime.datetime(1960, 2, 1, 0, 0): -2.2119999999999997, datetime.datetime(1960, 3, 1, 0, 0): -1.625, datetime.datetime(1960, 4, 1, 0, 0): -0.297, datetime.datetime(1960, 5, 1, 0, 0): -0.857, datetime.datetime(1960, 6, 1, 0, 0): 0.055, datetime.datetime(1960, 7, 1, 0, 0): -0.619, datetime.datetime(1960, 8, 1, 0, 0): -1.008, datetime.datetime(1960, 9, 1, 0, 0): -0.382, datetime.datetime(1960, 10, 1, 0, 0): -1.187, datetime.datetime(1960, 11, 1, 0, 0): -0.5529999999999999, datetime.datetime(1960, 12, 1, 0, 0): -0.34299999999999997, datetime.datetime(1961, 1, 1, 0, 0): -1.506, datetime.datetime(1961, 2, 1, 0, 0): 0.621, datetime.datetime(1961, 3, 1, 0, 0): 0.341, datetime.datetime(1961, 4, 1, 0, 0): -0.237, datetime.datetime(1961, 5, 1, 0, 0): 0.157, datetime.datetime(1961, 6, 1, 0, 0): 0.8370000000000001, datetime.datetime(1961, 7, 1, 0, 0): -0.10800000000000001, datetime.datetime(1961, 8, 1, 0, 0): 0.013000000000000001, datetime.datetime(1961, 9, 1, 0, 0): 0.815, datetime.datetime(1961, 10, 1, 0, 0): 0.203, datetime.datetime(1961, 11, 1, 0, 0): -0.01, datetime.datetime(1961, 12, 1, 0, 0): -1.6680000000000001, datetime.datetime(1962, 1, 1, 0, 0): 1.645, datetime.datetime(1962, 2, 1, 0, 0): -0.358, datetime.datetime(1962, 3, 1, 0, 0): -2.8480000000000003, datetime.datetime(1962, 4, 1, 0, 0): 1.169, datetime.datetime(1962, 5, 1, 0, 0): 0.068, datetime.datetime(1962, 6, 1, 0, 0): 0.287, datetime.datetime(1962, 7, 1, 0, 0): -0.927, datetime.datetime(1962, 8, 1, 0, 0): 0.152, datetime.datetime(1962, 9, 1, 0, 0): -0.055999999999999994, datetime.datetime(1962, 10, 1, 0, 0): -0.016, datetime.datetime(1962, 11, 1, 0, 0): -1.112, datetime.datetime(1962, 12, 1, 0, 0): -0.711, datetime.datetime(1963, 1, 1, 0, 0): -3.3110000000000004, datetime.datetime(1963, 2, 1, 0, 0): -1.7209999999999999, datetime.datetime(1963, 3, 1, 0, 0): 0.7240000000000001, datetime.datetime(1963, 4, 1, 0, 0): -0.348, datetime.datetime(1963, 5, 1, 0, 0): 0.7709999999999999, datetime.datetime(1963, 6, 1, 0, 0): -0.585, datetime.datetime(1963, 7, 1, 0, 0): -0.303, datetime.datetime(1963, 8, 1, 0, 0): -0.625, datetime.datetime(1963, 9, 1, 0, 0): 0.083, datetime.datetime(1963, 10, 1, 0, 0): 1.069, datetime.datetime(1963, 11, 1, 0, 0): -0.419, datetime.datetime(1963, 12, 1, 0, 0): -1.178, datetime.datetime(1964, 1, 1, 0, 0): 0.385, datetime.datetime(1964, 2, 1, 0, 0): -0.575, datetime.datetime(1964, 3, 1, 0, 0): -0.5579999999999999, datetime.datetime(1964, 4, 1, 0, 0): 0.6629999999999999, datetime.datetime(1964, 5, 1, 0, 0): 1.1740000000000002, datetime.datetime(1964, 6, 1, 0, 0): 0.142, datetime.datetime(1964, 7, 1, 0, 0): 0.7340000000000001, datetime.datetime(1964, 8, 1, 0, 0): -1.207, datetime.datetime(1964, 9, 1, 0, 0): -0.22699999999999998, datetime.datetime(1964, 10, 1, 0, 0): 0.342, datetime.datetime(1964, 11, 1, 0, 0): -0.344, datetime.datetime(1964, 12, 1, 0, 0): -0.24600000000000002, datetime.datetime(1965, 1, 1, 0, 0): -1.046, datetime.datetime(1965, 2, 1, 0, 0): -2.084, datetime.datetime(1965, 3, 1, 0, 0): -0.905, datetime.datetime(1965, 4, 1, 0, 0): 0.568, datetime.datetime(1965, 5, 1, 0, 0): -0.153, datetime.datetime(1965, 6, 1, 0, 0): 0.038, datetime.datetime(1965, 7, 1, 0, 0): -0.51, datetime.datetime(1965, 8, 1, 0, 0): -0.255, datetime.datetime(1965, 9, 1, 0, 0): -0.698, datetime.datetime(1965, 10, 1, 0, 0): 0.39399999999999996, datetime.datetime(1965, 11, 1, 0, 0): -1.341, datetime.datetime(1965, 12, 1, 0, 0): 0.163, datetime.datetime(1966, 1, 1, 0, 0): -3.2319999999999998, datetime.datetime(1966, 2, 1, 0, 0): -1.4380000000000002, datetime.datetime(1966, 3, 1, 0, 0): -0.9109999999999999, datetime.datetime(1966, 4, 1, 0, 0): -1.837, datetime.datetime(1966, 5, 1, 0, 0): 1.124, datetime.datetime(1966, 6, 1, 0, 0): 0.408, datetime.datetime(1966, 7, 1, 0, 0): 0.011000000000000001, datetime.datetime(1966, 8, 1, 0, 0): -0.945, datetime.datetime(1966, 9, 1, 0, 0): 0.011000000000000001, datetime.datetime(1966, 10, 1, 0, 0): -1.077, datetime.datetime(1966, 11, 1, 0, 0): 0.111, datetime.datetime(1966, 12, 1, 0, 0): -1.401, datetime.datetime(1967, 1, 1, 0, 0): -0.5760000000000001, datetime.datetime(1967, 2, 1, 0, 0): 1.18, datetime.datetime(1967, 3, 1, 0, 0): 1.9669999999999999, datetime.datetime(1967, 4, 1, 0, 0): 1.7, datetime.datetime(1967, 5, 1, 0, 0): 0.127, datetime.datetime(1967, 6, 1, 0, 0): 0.647, datetime.datetime(1967, 7, 1, 0, 0): 0.259, datetime.datetime(1967, 8, 1, 0, 0): -0.293, datetime.datetime(1967, 9, 1, 0, 0): 0.133, datetime.datetime(1967, 10, 1, 0, 0): 1.2990000000000002, datetime.datetime(1967, 11, 1, 0, 0): 0.33399999999999996, datetime.datetime(1967, 12, 1, 0, 0): -0.34700000000000003, datetime.datetime(1968, 1, 1, 0, 0): -0.409, datetime.datetime(1968, 2, 1, 0, 0): -2.154, datetime.datetime(1968, 3, 1, 0, 0): 1.7409999999999999, datetime.datetime(1968, 4, 1, 0, 0): 0.32799999999999996, datetime.datetime(1968, 5, 1, 0, 0): -0.24100000000000002, datetime.datetime(1968, 6, 1, 0, 0): 0.42, datetime.datetime(1968, 7, 1, 0, 0): -0.836, datetime.datetime(1968, 8, 1, 0, 0): -0.6709999999999999, datetime.datetime(1968, 9, 1, 0, 0): -1.0090000000000001, datetime.datetime(1968, 10, 1, 0, 0): -1.013, datetime.datetime(1968, 11, 1, 0, 0): -2.1830000000000003, datetime.datetime(1968, 12, 1, 0, 0): -0.7829999999999999, datetime.datetime(1969, 1, 1, 0, 0): -2.967, datetime.datetime(1969, 2, 1, 0, 0): -3.114, datetime.datetime(1969, 3, 1, 0, 0): -1.5819999999999999, datetime.datetime(1969, 4, 1, 0, 0): 0.43799999999999994, datetime.datetime(1969, 5, 1, 0, 0): -0.72, datetime.datetime(1969, 6, 1, 0, 0): -0.348, datetime.datetime(1969, 7, 1, 0, 0): 0.41, datetime.datetime(1969, 8, 1, 0, 0): -0.782, datetime.datetime(1969, 9, 1, 0, 0): -0.083, datetime.datetime(1969, 10, 1, 0, 0): 0.098, datetime.datetime(1969, 11, 1, 0, 0): 0.326, datetime.datetime(1969, 12, 1, 0, 0): -1.8559999999999999, datetime.datetime(1970, 1, 1, 0, 0): -2.412, datetime.datetime(1970, 2, 1, 0, 0): -1.325, datetime.datetime(1970, 3, 1, 0, 0): -2.084, datetime.datetime(1970, 4, 1, 0, 0): 0.302, datetime.datetime(1970, 5, 1, 0, 0): 0.531, datetime.datetime(1970, 6, 1, 0, 0): 0.875, datetime.datetime(1970, 7, 1, 0, 0): 0.139, datetime.datetime(1970, 8, 1, 0, 0): -0.263, datetime.datetime(1970, 9, 1, 0, 0): 0.03, datetime.datetime(1970, 10, 1, 0, 0): 0.098, datetime.datetime(1970, 11, 1, 0, 0): 0.37799999999999995, datetime.datetime(1970, 12, 1, 0, 0): -0.39899999999999997, datetime.datetime(1971, 1, 1, 0, 0): -0.163, datetime.datetime(1971, 2, 1, 0, 0): -0.922, datetime.datetime(1971, 3, 1, 0, 0): -1.091, datetime.datetime(1971, 4, 1, 0, 0): -0.583, datetime.datetime(1971, 5, 1, 0, 0): 0.679, datetime.datetime(1971, 6, 1, 0, 0): -0.6679999999999999, datetime.datetime(1971, 7, 1, 0, 0): -0.578, datetime.datetime(1971, 8, 1, 0, 0): 0.818, datetime.datetime(1971, 9, 1, 0, 0): 0.153, datetime.datetime(1971, 10, 1, 0, 0): 1.185, datetime.datetime(1971, 11, 1, 0, 0): 0.419, datetime.datetime(1971, 12, 1, 0, 0): 0.8240000000000001, datetime.datetime(1972, 1, 1, 0, 0): 0.166, datetime.datetime(1972, 2, 1, 0, 0): -0.195, datetime.datetime(1972, 3, 1, 0, 0): -0.141, datetime.datetime(1972, 4, 1, 0, 0): 1.0070000000000001, datetime.datetime(1972, 5, 1, 0, 0): 0.14, datetime.datetime(1972, 6, 1, 0, 0): -0.049, datetime.datetime(1972, 7, 1, 0, 0): -0.5529999999999999, datetime.datetime(1972, 8, 1, 0, 0): -0.08199999999999999, datetime.datetime(1972, 9, 1, 0, 0): -0.92, datetime.datetime(1972, 10, 1, 0, 0): 0.392, datetime.datetime(1972, 11, 1, 0, 0): -0.38, datetime.datetime(1972, 12, 1, 0, 0): 1.238, datetime.datetime(1973, 1, 1, 0, 0): 1.232, datetime.datetime(1973, 2, 1, 0, 0): 0.7859999999999999, datetime.datetime(1973, 3, 1, 0, 0): 0.537, datetime.datetime(1973, 4, 1, 0, 0): -1.126, datetime.datetime(1973, 5, 1, 0, 0): 0.073, datetime.datetime(1973, 6, 1, 0, 0): 0.531, datetime.datetime(1973, 7, 1, 0, 0): 0.27, datetime.datetime(1973, 8, 1, 0, 0): 0.313, datetime.datetime(1973, 9, 1, 0, 0): 0.114, datetime.datetime(1973, 10, 1, 0, 0): 0.337, datetime.datetime(1973, 11, 1, 0, 0): 0.002, datetime.datetime(1973, 12, 1, 0, 0): -0.18100000000000002, datetime.datetime(1974, 1, 1, 0, 0): 0.23199999999999998, datetime.datetime(1974, 2, 1, 0, 0): -0.489, datetime.datetime(1974, 3, 1, 0, 0): -0.746, datetime.datetime(1974, 4, 1, 0, 0): 0.309, datetime.datetime(1974, 5, 1, 0, 0): -0.507, datetime.datetime(1974, 6, 1, 0, 0): -0.048, datetime.datetime(1974, 7, 1, 0, 0): 0.39, datetime.datetime(1974, 8, 1, 0, 0): -0.5329999999999999, datetime.datetime(1974, 9, 1, 0, 0): -0.136, datetime.datetime(1974, 10, 1, 0, 0): -1.024, datetime.datetime(1974, 11, 1, 0, 0): -0.435, datetime.datetime(1974, 12, 1, 0, 0): 0.556, datetime.datetime(1975, 1, 1, 0, 0): 1.595, datetime.datetime(1975, 2, 1, 0, 0): 0.19399999999999998, datetime.datetime(1975, 3, 1, 0, 0): 0.151, datetime.datetime(1975, 4, 1, 0, 0): 0.409, datetime.datetime(1975, 5, 1, 0, 0): -0.614, datetime.datetime(1975, 6, 1, 0, 0): -0.32299999999999995, datetime.datetime(1975, 7, 1, 0, 0): 0.345, datetime.datetime(1975, 8, 1, 0, 0): 0.13, datetime.datetime(1975, 9, 1, 0, 0): 1.278, datetime.datetime(1975, 10, 1, 0, 0): 0.138, datetime.datetime(1975, 11, 1, 0, 0): 0.619, datetime.datetime(1975, 12, 1, 0, 0): 1.29, datetime.datetime(1976, 1, 1, 0, 0): 0.034, datetime.datetime(1976, 2, 1, 0, 0): 1.656, datetime.datetime(1976, 3, 1, 0, 0): 0.5870000000000001, datetime.datetime(1976, 4, 1, 0, 0): 0.44, datetime.datetime(1976, 5, 1, 0, 0): 0.06, datetime.datetime(1976, 6, 1, 0, 0): 0.32799999999999996, datetime.datetime(1976, 7, 1, 0, 0): -0.325, datetime.datetime(1976, 8, 1, 0, 0): 0.5589999999999999, datetime.datetime(1976, 9, 1, 0, 0): -0.743, datetime.datetime(1976, 10, 1, 0, 0): -0.804, datetime.datetime(1976, 11, 1, 0, 0): -0.087, datetime.datetime(1976, 12, 1, 0, 0): -2.074, datetime.datetime(1977, 1, 1, 0, 0): -3.767, datetime.datetime(1977, 2, 1, 0, 0): -2.01, datetime.datetime(1977, 3, 1, 0, 0): 0.344, datetime.datetime(1977, 4, 1, 0, 0): 1.329, datetime.datetime(1977, 5, 1, 0, 0): 0.10400000000000001, datetime.datetime(1977, 6, 1, 0, 0): -0.226, datetime.datetime(1977, 7, 1, 0, 0): -0.49200000000000005, datetime.datetime(1977, 8, 1, 0, 0): -1.412, datetime.datetime(1977, 9, 1, 0, 0): 0.586, datetime.datetime(1977, 10, 1, 0, 0): -0.009000000000000001, datetime.datetime(1977, 11, 1, 0, 0): 0.605, datetime.datetime(1977, 12, 1, 0, 0): -0.24, datetime.datetime(1978, 1, 1, 0, 0): -0.34700000000000003, datetime.datetime(1978, 2, 1, 0, 0): -3.014, datetime.datetime(1978, 3, 1, 0, 0): 0.502, datetime.datetime(1978, 4, 1, 0, 0): -0.9670000000000001, datetime.datetime(1978, 5, 1, 0, 0): 0.059000000000000004, datetime.datetime(1978, 6, 1, 0, 0): 0.635, datetime.datetime(1978, 7, 1, 0, 0): -0.604, datetime.datetime(1978, 8, 1, 0, 0): -0.354, datetime.datetime(1978, 9, 1, 0, 0): -0.099, datetime.datetime(1978, 10, 1, 0, 0): 0.895, datetime.datetime(1978, 11, 1, 0, 0): 2.47, datetime.datetime(1978, 12, 1, 0, 0): -0.98, datetime.datetime(1979, 1, 1, 0, 0): -2.233, datetime.datetime(1979, 2, 1, 0, 0): -0.6970000000000001, datetime.datetime(1979, 3, 1, 0, 0): -0.8140000000000001, datetime.datetime(1979, 4, 1, 0, 0): -1.157, datetime.datetime(1979, 5, 1, 0, 0): -0.25, datetime.datetime(1979, 6, 1, 0, 0): 0.9329999999999999, datetime.datetime(1979, 7, 1, 0, 0): 0.039, datetime.datetime(1979, 8, 1, 0, 0): -0.684, datetime.datetime(1979, 9, 1, 0, 0): -0.046, datetime.datetime(1979, 10, 1, 0, 0): -1.2429999999999999, datetime.datetime(1979, 11, 1, 0, 0): 0.475, datetime.datetime(1979, 12, 1, 0, 0): 1.295, datetime.datetime(1980, 1, 1, 0, 0): -2.066, datetime.datetime(1980, 2, 1, 0, 0): -0.934, datetime.datetime(1980, 3, 1, 0, 0): -1.433, datetime.datetime(1980, 4, 1, 0, 0): -0.419, datetime.datetime(1980, 5, 1, 0, 0): -1.155, datetime.datetime(1980, 6, 1, 0, 0): 0.721, datetime.datetime(1980, 7, 1, 0, 0): -0.622, datetime.datetime(1980, 8, 1, 0, 0): -0.185, datetime.datetime(1980, 9, 1, 0, 0): 0.313, datetime.datetime(1980, 10, 1, 0, 0): -0.521, datetime.datetime(1980, 11, 1, 0, 0): -1.361, datetime.datetime(1980, 12, 1, 0, 0): -0.057, datetime.datetime(1981, 1, 1, 0, 0): -0.11599999999999999, datetime.datetime(1981, 2, 1, 0, 0): -0.332, datetime.datetime(1981, 3, 1, 0, 0): -1.645, datetime.datetime(1981, 4, 1, 0, 0): 0.43, datetime.datetime(1981, 5, 1, 0, 0): 0.18, datetime.datetime(1981, 6, 1, 0, 0): -0.43799999999999994, datetime.datetime(1981, 7, 1, 0, 0): 0.561, datetime.datetime(1981, 8, 1, 0, 0): -0.244, datetime.datetime(1981, 9, 1, 0, 0): -1.04, datetime.datetime(1981, 10, 1, 0, 0): -1.167, datetime.datetime(1981, 11, 1, 0, 0): -0.188, datetime.datetime(1981, 12, 1, 0, 0): -1.216, datetime.datetime(1982, 1, 1, 0, 0): -0.883, datetime.datetime(1982, 2, 1, 0, 0): 0.9740000000000001, datetime.datetime(1982, 3, 1, 0, 0): 1.074, datetime.datetime(1982, 4, 1, 0, 0): 1.454, datetime.datetime(1982, 5, 1, 0, 0): -0.209, datetime.datetime(1982, 6, 1, 0, 0): -1.18, datetime.datetime(1982, 7, 1, 0, 0): 0.005, datetime.datetime(1982, 8, 1, 0, 0): 0.36200000000000004, datetime.datetime(1982, 9, 1, 0, 0): 0.5579999999999999, datetime.datetime(1982, 10, 1, 0, 0): -0.21100000000000002, datetime.datetime(1982, 11, 1, 0, 0): 0.6609999999999999, datetime.datetime(1982, 12, 1, 0, 0): 0.9670000000000001, datetime.datetime(1983, 1, 1, 0, 0): 1.359, datetime.datetime(1983, 2, 1, 0, 0): -1.806, datetime.datetime(1983, 3, 1, 0, 0): -0.5670000000000001, datetime.datetime(1983, 4, 1, 0, 0): -0.738, datetime.datetime(1983, 5, 1, 0, 0): -0.441, datetime.datetime(1983, 6, 1, 0, 0): 0.313, datetime.datetime(1983, 7, 1, 0, 0): 0.131, datetime.datetime(1983, 8, 1, 0, 0): 1.0979999999999999, datetime.datetime(1983, 9, 1, 0, 0): 0.16699999999999998, datetime.datetime(1983, 10, 1, 0, 0): 1.369, datetime.datetime(1983, 11, 1, 0, 0): -0.688, datetime.datetime(1983, 12, 1, 0, 0): 0.18600000000000003, datetime.datetime(1984, 1, 1, 0, 0): 0.905, datetime.datetime(1984, 2, 1, 0, 0): -0.303, datetime.datetime(1984, 3, 1, 0, 0): -2.386, datetime.datetime(1984, 4, 1, 0, 0): -0.284, datetime.datetime(1984, 5, 1, 0, 0): 0.479, datetime.datetime(1984, 6, 1, 0, 0): 0.006999999999999999, datetime.datetime(1984, 7, 1, 0, 0): 0.019, datetime.datetime(1984, 8, 1, 0, 0): 0.466, datetime.datetime(1984, 9, 1, 0, 0): -0.413, datetime.datetime(1984, 10, 1, 0, 0): -0.27, datetime.datetime(1984, 11, 1, 0, 0): -0.966, datetime.datetime(1984, 12, 1, 0, 0): 0.446, datetime.datetime(1985, 1, 1, 0, 0): -2.806, datetime.datetime(1985, 2, 1, 0, 0): -1.44, datetime.datetime(1985, 3, 1, 0, 0): 0.551, datetime.datetime(1985, 4, 1, 0, 0): 0.652, datetime.datetime(1985, 5, 1, 0, 0): -0.43200000000000005, datetime.datetime(1985, 6, 1, 0, 0): -0.34700000000000003, datetime.datetime(1985, 7, 1, 0, 0): -0.39, datetime.datetime(1985, 8, 1, 0, 0): -0.001, datetime.datetime(1985, 9, 1, 0, 0): 0.114, datetime.datetime(1985, 10, 1, 0, 0): 1.035, datetime.datetime(1985, 11, 1, 0, 0): -1.218, datetime.datetime(1985, 12, 1, 0, 0): -1.9480000000000002, datetime.datetime(1986, 1, 1, 0, 0): -0.568, datetime.datetime(1986, 2, 1, 0, 0): -2.904, datetime.datetime(1986, 3, 1, 0, 0): 1.931, datetime.datetime(1986, 4, 1, 0, 0): 0.10300000000000001, datetime.datetime(1986, 5, 1, 0, 0): 0.36700000000000005, datetime.datetime(1986, 6, 1, 0, 0): 0.535, datetime.datetime(1986, 7, 1, 0, 0): -0.008, datetime.datetime(1986, 8, 1, 0, 0): -0.826, datetime.datetime(1986, 9, 1, 0, 0): -0.023, datetime.datetime(1986, 10, 1, 0, 0): 1.425, datetime.datetime(1986, 11, 1, 0, 0): 0.9259999999999999, datetime.datetime(1986, 12, 1, 0, 0): 0.06, datetime.datetime(1987, 1, 1, 0, 0): -1.148, datetime.datetime(1987, 2, 1, 0, 0): -1.473, datetime.datetime(1987, 3, 1, 0, 0): -1.746, datetime.datetime(1987, 4, 1, 0, 0): 0.387, datetime.datetime(1987, 5, 1, 0, 0): 0.325, datetime.datetime(1987, 6, 1, 0, 0): -0.71, datetime.datetime(1987, 7, 1, 0, 0): -0.466, datetime.datetime(1987, 8, 1, 0, 0): -0.836, datetime.datetime(1987, 9, 1, 0, 0): 0.287, datetime.datetime(1987, 10, 1, 0, 0): -0.08, datetime.datetime(1987, 11, 1, 0, 0): -0.536, datetime.datetime(1987, 12, 1, 0, 0): -0.534, datetime.datetime(1988, 1, 1, 0, 0): 0.265, datetime.datetime(1988, 2, 1, 0, 0): -1.0659999999999998, datetime.datetime(1988, 3, 1, 0, 0): -0.19699999999999998, datetime.datetime(1988, 4, 1, 0, 0): -0.561, datetime.datetime(1988, 5, 1, 0, 0): -0.846, datetime.datetime(1988, 6, 1, 0, 0): 0.061, datetime.datetime(1988, 7, 1, 0, 0): -0.14300000000000002, datetime.datetime(1988, 8, 1, 0, 0): 0.255, datetime.datetime(1988, 9, 1, 0, 0): 1.0390000000000001, datetime.datetime(1988, 10, 1, 0, 0): 0.032, datetime.datetime(1988, 11, 1, 0, 0): -0.035, datetime.datetime(1988, 12, 1, 0, 0): 1.679, datetime.datetime(1989, 1, 1, 0, 0): 3.1060000000000003, datetime.datetime(1989, 2, 1, 0, 0): 3.279, datetime.datetime(1989, 3, 1, 0, 0): 1.53, datetime.datetime(1989, 4, 1, 0, 0): -0.25, datetime.datetime(1989, 5, 1, 0, 0): 0.889, datetime.datetime(1989, 6, 1, 0, 0): 0.345, datetime.datetime(1989, 7, 1, 0, 0): 0.866, datetime.datetime(1989, 8, 1, 0, 0): 0.551, datetime.datetime(1989, 9, 1, 0, 0): 0.703, datetime.datetime(1989, 10, 1, 0, 0): 0.991, datetime.datetime(1989, 11, 1, 0, 0): 0.034, datetime.datetime(1989, 12, 1, 0, 0): -0.644, datetime.datetime(1990, 1, 1, 0, 0): 1.001, datetime.datetime(1990, 2, 1, 0, 0): 3.4019999999999997, datetime.datetime(1990, 3, 1, 0, 0): 2.99, datetime.datetime(1990, 4, 1, 0, 0): 1.879, datetime.datetime(1990, 5, 1, 0, 0): 0.943, datetime.datetime(1990, 6, 1, 0, 0): 0.304, datetime.datetime(1990, 7, 1, 0, 0): -0.29600000000000004, datetime.datetime(1990, 8, 1, 0, 0): -0.18, datetime.datetime(1990, 9, 1, 0, 0): -0.21, datetime.datetime(1990, 10, 1, 0, 0): 0.66, datetime.datetime(1990, 11, 1, 0, 0): 0.521, datetime.datetime(1990, 12, 1, 0, 0): 1.2770000000000001, datetime.datetime(1991, 1, 1, 0, 0): 0.723, datetime.datetime(1991, 2, 1, 0, 0): -0.8759999999999999, datetime.datetime(1991, 3, 1, 0, 0): -0.527, datetime.datetime(1991, 4, 1, 0, 0): 0.53, datetime.datetime(1991, 5, 1, 0, 0): 0.486, datetime.datetime(1991, 6, 1, 0, 0): -0.115, datetime.datetime(1991, 7, 1, 0, 0): -0.188, datetime.datetime(1991, 8, 1, 0, 0): 0.797, datetime.datetime(1991, 9, 1, 0, 0): -0.11199999999999999, datetime.datetime(1991, 10, 1, 0, 0): -0.252, datetime.datetime(1991, 11, 1, 0, 0): 0.285, datetime.datetime(1991, 12, 1, 0, 0): 1.6130000000000002, datetime.datetime(1992, 1, 1, 0, 0): 0.55, datetime.datetime(1992, 2, 1, 0, 0): 1.122, datetime.datetime(1992, 3, 1, 0, 0): 0.9840000000000001, datetime.datetime(1992, 4, 1, 0, 0): -0.521, datetime.datetime(1992, 5, 1, 0, 0): 1.341, datetime.datetime(1992, 6, 1, 0, 0): -0.302, datetime.datetime(1992, 7, 1, 0, 0): 0.191, datetime.datetime(1992, 8, 1, 0, 0): 0.535, datetime.datetime(1992, 9, 1, 0, 0): -0.64, datetime.datetime(1992, 10, 1, 0, 0): -0.366, datetime.datetime(1992, 11, 1, 0, 0): 0.7170000000000001, datetime.datetime(1992, 12, 1, 0, 0): 1.6269999999999998, datetime.datetime(1993, 1, 1, 0, 0): 3.495, datetime.datetime(1993, 2, 1, 0, 0): 0.184, datetime.datetime(1993, 3, 1, 0, 0): 0.764, datetime.datetime(1993, 4, 1, 0, 0): -0.435, datetime.datetime(1993, 5, 1, 0, 0): -1.607, datetime.datetime(1993, 6, 1, 0, 0): -0.52, datetime.datetime(1993, 7, 1, 0, 0): -0.511, datetime.datetime(1993, 8, 1, 0, 0): -0.39299999999999996, datetime.datetime(1993, 9, 1, 0, 0): -0.361, datetime.datetime(1993, 10, 1, 0, 0): -0.565, datetime.datetime(1993, 11, 1, 0, 0): 1.002, datetime.datetime(1993, 12, 1, 0, 0): -0.10400000000000001, datetime.datetime(1994, 1, 1, 0, 0): -0.28800000000000003, datetime.datetime(1994, 2, 1, 0, 0): -0.862, datetime.datetime(1994, 3, 1, 0, 0): 1.881, datetime.datetime(1994, 4, 1, 0, 0): 0.225, datetime.datetime(1994, 5, 1, 0, 0): -0.115, datetime.datetime(1994, 6, 1, 0, 0): 1.6059999999999999, datetime.datetime(1994, 7, 1, 0, 0): 0.35100000000000003, datetime.datetime(1994, 8, 1, 0, 0): 0.828, datetime.datetime(1994, 9, 1, 0, 0): -0.084, datetime.datetime(1994, 10, 1, 0, 0): 0.174, datetime.datetime(1994, 11, 1, 0, 0): 1.7790000000000001, datetime.datetime(1994, 12, 1, 0, 0): 0.894, datetime.datetime(1995, 1, 1, 0, 0): -0.154, datetime.datetime(1995, 2, 1, 0, 0): 1.429, datetime.datetime(1995, 3, 1, 0, 0): 0.39299999999999996, datetime.datetime(1995, 4, 1, 0, 0): -0.963, datetime.datetime(1995, 5, 1, 0, 0): -0.8909999999999999, datetime.datetime(1995, 6, 1, 0, 0): -0.11199999999999999, datetime.datetime(1995, 7, 1, 0, 0): -0.217, datetime.datetime(1995, 8, 1, 0, 0): 0.544, datetime.datetime(1995, 9, 1, 0, 0): -0.5489999999999999, datetime.datetime(1995, 10, 1, 0, 0): 0.075, datetime.datetime(1995, 11, 1, 0, 0): -0.723, datetime.datetime(1995, 12, 1, 0, 0): -2.127, datetime.datetime(1996, 1, 1, 0, 0): -1.2, datetime.datetime(1996, 2, 1, 0, 0): 0.163, datetime.datetime(1996, 3, 1, 0, 0): -1.483, datetime.datetime(1996, 4, 1, 0, 0): -1.525, datetime.datetime(1996, 5, 1, 0, 0): -0.226, datetime.datetime(1996, 6, 1, 0, 0): 0.49700000000000005, datetime.datetime(1996, 7, 1, 0, 0): 0.715, datetime.datetime(1996, 8, 1, 0, 0): 0.125, datetime.datetime(1996, 9, 1, 0, 0): -1.14, datetime.datetime(1996, 10, 1, 0, 0): 0.183, datetime.datetime(1996, 11, 1, 0, 0): 0.136, datetime.datetime(1996, 12, 1, 0, 0): -1.7209999999999999, datetime.datetime(1997, 1, 1, 0, 0): -0.457, datetime.datetime(1997, 2, 1, 0, 0): 1.889, datetime.datetime(1997, 3, 1, 0, 0): 1.091, datetime.datetime(1997, 4, 1, 0, 0): 0.324, datetime.datetime(1997, 5, 1, 0, 0): -0.961, datetime.datetime(1997, 6, 1, 0, 0): -0.815, datetime.datetime(1997, 7, 1, 0, 0): -0.431, datetime.datetime(1997, 8, 1, 0, 0): 0.121, datetime.datetime(1997, 9, 1, 0, 0): 0.195, datetime.datetime(1997, 10, 1, 0, 0): -0.7, datetime.datetime(1997, 11, 1, 0, 0): -0.6609999999999999, datetime.datetime(1997, 12, 1, 0, 0): -0.071, datetime.datetime(1998, 1, 1, 0, 0): -2.081, datetime.datetime(1998, 2, 1, 0, 0): -0.183, datetime.datetime(1998, 3, 1, 0, 0): -0.254, datetime.datetime(1998, 4, 1, 0, 0): -0.038, datetime.datetime(1998, 5, 1, 0, 0): 0.429, datetime.datetime(1998, 6, 1, 0, 0): -0.711, datetime.datetime(1998, 7, 1, 0, 0): -0.212, datetime.datetime(1998, 8, 1, 0, 0): 0.65, datetime.datetime(1998, 9, 1, 0, 0): -1.05, datetime.datetime(1998, 10, 1, 0, 0): 0.294, datetime.datetime(1998, 11, 1, 0, 0): -1.449, datetime.datetime(1998, 12, 1, 0, 0): 1.3530000000000002, datetime.datetime(1999, 1, 1, 0, 0): 0.11, datetime.datetime(1999, 2, 1, 0, 0): 0.48200000000000004, datetime.datetime(1999, 3, 1, 0, 0): -1.492, datetime.datetime(1999, 4, 1, 0, 0): 0.284, datetime.datetime(1999, 5, 1, 0, 0): 0.226, datetime.datetime(1999, 6, 1, 0, 0): 0.7070000000000001, datetime.datetime(1999, 7, 1, 0, 0): -0.002, datetime.datetime(1999, 8, 1, 0, 0): -0.672, datetime.datetime(1999, 9, 1, 0, 0): 0.059000000000000004, datetime.datetime(1999, 10, 1, 0, 0): -0.006, datetime.datetime(1999, 11, 1, 0, 0): 0.611, datetime.datetime(1999, 12, 1, 0, 0): 1.043, datetime.datetime(2000, 1, 1, 0, 0): 1.27, datetime.datetime(2000, 2, 1, 0, 0): 1.0759999999999998, datetime.datetime(2000, 3, 1, 0, 0): -0.451, datetime.datetime(2000, 4, 1, 0, 0): -0.27899999999999997, datetime.datetime(2000, 5, 1, 0, 0): 0.9690000000000001, datetime.datetime(2000, 6, 1, 0, 0): 0.586, datetime.datetime(2000, 7, 1, 0, 0): -0.649, datetime.datetime(2000, 8, 1, 0, 0): 0.14400000000000002, datetime.datetime(2000, 9, 1, 0, 0): 0.395, datetime.datetime(2000, 10, 1, 0, 0): 0.317, datetime.datetime(2000, 11, 1, 0, 0): -1.581, datetime.datetime(2000, 12, 1, 0, 0): -2.354, datetime.datetime(2001, 1, 1, 0, 0): -0.9590000000000001, datetime.datetime(2001, 2, 1, 0, 0): -0.622, datetime.datetime(2001, 3, 1, 0, 0): -1.6869999999999998, datetime.datetime(2001, 4, 1, 0, 0): 0.9059999999999999, datetime.datetime(2001, 5, 1, 0, 0): 0.452, datetime.datetime(2001, 6, 1, 0, 0): -0.015, datetime.datetime(2001, 7, 1, 0, 0): -0.031, datetime.datetime(2001, 8, 1, 0, 0): 0.521, datetime.datetime(2001, 9, 1, 0, 0): -0.7070000000000001, datetime.datetime(2001, 10, 1, 0, 0): 0.7070000000000001, datetime.datetime(2001, 11, 1, 0, 0): 0.8190000000000001, datetime.datetime(2001, 12, 1, 0, 0): -1.3219999999999998, datetime.datetime(2002, 1, 1, 0, 0): 1.381, datetime.datetime(2002, 2, 1, 0, 0): 1.304, datetime.datetime(2002, 3, 1, 0, 0): 0.902, datetime.datetime(2002, 4, 1, 0, 0): 0.748, datetime.datetime(2002, 5, 1, 0, 0): 0.401, datetime.datetime(2002, 6, 1, 0, 0): 0.573, datetime.datetime(2002, 7, 1, 0, 0): 0.32799999999999996, datetime.datetime(2002, 8, 1, 0, 0): -0.22899999999999998, datetime.datetime(2002, 9, 1, 0, 0): -0.043, datetime.datetime(2002, 10, 1, 0, 0): -1.489, datetime.datetime(2002, 11, 1, 0, 0): -1.425, datetime.datetime(2002, 12, 1, 0, 0): -1.5919999999999999, datetime.datetime(2003, 1, 1, 0, 0): -0.47200000000000003, datetime.datetime(2003, 2, 1, 0, 0): 0.128, datetime.datetime(2003, 3, 1, 0, 0): 0.9329999999999999, datetime.datetime(2003, 4, 1, 0, 0): -0.17800000000000002, datetime.datetime(2003, 5, 1, 0, 0): 1.0170000000000001, datetime.datetime(2003, 6, 1, 0, 0): -0.102, datetime.datetime(2003, 7, 1, 0, 0): 0.075, datetime.datetime(2003, 8, 1, 0, 0): -0.28, datetime.datetime(2003, 9, 1, 0, 0): 0.467, datetime.datetime(2003, 10, 1, 0, 0): -0.67, datetime.datetime(2003, 11, 1, 0, 0): 0.642, datetime.datetime(2003, 12, 1, 0, 0): 0.265, datetime.datetime(2004, 1, 1, 0, 0): -1.686, datetime.datetime(2004, 2, 1, 0, 0): -1.528, datetime.datetime(2004, 3, 1, 0, 0): 0.318, datetime.datetime(2004, 4, 1, 0, 0): -0.409, datetime.datetime(2004, 5, 1, 0, 0): -0.094, datetime.datetime(2004, 6, 1, 0, 0): -0.23600000000000002, datetime.datetime(2004, 7, 1, 0, 0): -0.201, datetime.datetime(2004, 8, 1, 0, 0): -0.72, datetime.datetime(2004, 9, 1, 0, 0): 0.855, datetime.datetime(2004, 10, 1, 0, 0): -0.515, datetime.datetime(2004, 11, 1, 0, 0): 0.6779999999999999, datetime.datetime(2004, 12, 1, 0, 0): 1.23, datetime.datetime(2005, 1, 1, 0, 0): 0.35600000000000004, datetime.datetime(2005, 2, 1, 0, 0): -1.271, datetime.datetime(2005, 3, 1, 0, 0): -1.348, datetime.datetime(2005, 4, 1, 0, 0): -0.046, datetime.datetime(2005, 5, 1, 0, 0): -0.763, datetime.datetime(2005, 6, 1, 0, 0): -0.38299999999999995, datetime.datetime(2005, 7, 1, 0, 0): -0.03, datetime.datetime(2005, 8, 1, 0, 0): 0.026000000000000002, datetime.datetime(2005, 9, 1, 0, 0): 0.802, datetime.datetime(2005, 10, 1, 0, 0): 0.03, datetime.datetime(2005, 11, 1, 0, 0): 0.228, datetime.datetime(2005, 12, 1, 0, 0): -2.104, datetime.datetime(2006, 1, 1, 0, 0): -0.17, datetime.datetime(2006, 2, 1, 0, 0): -0.156, datetime.datetime(2006, 3, 1, 0, 0): -1.604, datetime.datetime(2006, 4, 1, 0, 0): 0.138, datetime.datetime(2006, 5, 1, 0, 0): 0.156, datetime.datetime(2006, 6, 1, 0, 0): 1.071, datetime.datetime(2006, 7, 1, 0, 0): 0.10300000000000001, datetime.datetime(2006, 8, 1, 0, 0): -0.265, datetime.datetime(2006, 9, 1, 0, 0): 0.606, datetime.datetime(2006, 10, 1, 0, 0): -1.0290000000000001, datetime.datetime(2006, 11, 1, 0, 0): 0.521, datetime.datetime(2006, 12, 1, 0, 0): 2.282, datetime.datetime(2007, 1, 1, 0, 0): 2.0340000000000003, datetime.datetime(2007, 2, 1, 0, 0): -1.307, datetime.datetime(2007, 3, 1, 0, 0): 1.182, datetime.datetime(2007, 4, 1, 0, 0): 0.544, datetime.datetime(2007, 5, 1, 0, 0): 0.894, datetime.datetime(2007, 6, 1, 0, 0): -0.555, datetime.datetime(2007, 7, 1, 0, 0): -0.397, datetime.datetime(2007, 8, 1, 0, 0): -0.034, datetime.datetime(2007, 9, 1, 0, 0): 0.179, datetime.datetime(2007, 10, 1, 0, 0): 0.38299999999999995, datetime.datetime(2007, 11, 1, 0, 0): -0.519, datetime.datetime(2007, 12, 1, 0, 0): 0.821, datetime.datetime(2008, 1, 1, 0, 0): 0.8190000000000001, datetime.datetime(2008, 2, 1, 0, 0): 0.938, datetime.datetime(2008, 3, 1, 0, 0): 0.586, datetime.datetime(2008, 4, 1, 0, 0): -0.455, datetime.datetime(2008, 5, 1, 0, 0): -1.205, datetime.datetime(2008, 6, 1, 0, 0): -0.09, datetime.datetime(2008, 7, 1, 0, 0): -0.48, datetime.datetime(2008, 8, 1, 0, 0): -0.08, datetime.datetime(2008, 9, 1, 0, 0): -0.327, datetime.datetime(2008, 10, 1, 0, 0): 1.676, datetime.datetime(2008, 11, 1, 0, 0): 0.092, datetime.datetime(2008, 12, 1, 0, 0): 0.648, datetime.datetime(2009, 1, 1, 0, 0): 0.8, datetime.datetime(2009, 2, 1, 0, 0): -0.672, datetime.datetime(2009, 3, 1, 0, 0): 0.121, datetime.datetime(2009, 4, 1, 0, 0): 0.973, datetime.datetime(2009, 5, 1, 0, 0): 1.194, datetime.datetime(2009, 6, 1, 0, 0): -1.351, datetime.datetime(2009, 7, 1, 0, 0): -1.3559999999999999, datetime.datetime(2009, 8, 1, 0, 0): -0.054000000000000006, datetime.datetime(2009, 9, 1, 0, 0): 0.875, datetime.datetime(2009, 10, 1, 0, 0): -1.54, datetime.datetime(2009, 11, 1, 0, 0): 0.45899999999999996, datetime.datetime(2009, 12, 1, 0, 0): -3.4130000000000003, datetime.datetime(2010, 1, 1, 0, 0): -2.5869999999999997, datetime.datetime(2010, 2, 1, 0, 0): -4.266, datetime.datetime(2010, 3, 1, 0, 0): -0.43200000000000005, datetime.datetime(2010, 4, 1, 0, 0): -0.275, datetime.datetime(2010, 5, 1, 0, 0): -0.919, datetime.datetime(2010, 6, 1, 0, 0): -0.013000000000000001, datetime.datetime(2010, 7, 1, 0, 0): 0.435, datetime.datetime(2010, 8, 1, 0, 0): -0.11699999999999999, datetime.datetime(2010, 9, 1, 0, 0): -0.865, datetime.datetime(2010, 10, 1, 0, 0): -0.467, datetime.datetime(2010, 11, 1, 0, 0): -0.376, datetime.datetime(2010, 12, 1, 0, 0): -2.6310000000000002, datetime.datetime(2011, 1, 1, 0, 0): -1.683, datetime.datetime(2011, 2, 1, 0, 0): 1.575, datetime.datetime(2011, 3, 1, 0, 0): 1.4240000000000002, datetime.datetime(2011, 4, 1, 0, 0): 2.275, datetime.datetime(2011, 5, 1, 0, 0): -0.035, datetime.datetime(2011, 6, 1, 0, 0): -0.858, datetime.datetime(2011, 7, 1, 0, 0): -0.47200000000000003, datetime.datetime(2011, 8, 1, 0, 0): -1.063, datetime.datetime(2011, 9, 1, 0, 0): 0.665, datetime.datetime(2011, 10, 1, 0, 0): 0.8, datetime.datetime(2011, 11, 1, 0, 0): 1.459, datetime.datetime(2011, 12, 1, 0, 0): 2.221, datetime.datetime(2012, 1, 1, 0, 0): -0.22, datetime.datetime(2012, 2, 1, 0, 0): -0.036000000000000004, datetime.datetime(2012, 3, 1, 0, 0): 1.037, datetime.datetime(2012, 4, 1, 0, 0): -0.035, datetime.datetime(2012, 5, 1, 0, 0): 0.168, datetime.datetime(2012, 6, 1, 0, 0): -0.672, datetime.datetime(2012, 7, 1, 0, 0): 0.168, datetime.datetime(2012, 8, 1, 0, 0): 0.013999999999999999, datetime.datetime(2012, 9, 1, 0, 0): 0.772, datetime.datetime(2012, 10, 1, 0, 0): -1.514, datetime.datetime(2012, 11, 1, 0, 0): -0.111, datetime.datetime(2012, 12, 1, 0, 0): -1.749, datetime.datetime(2013, 1, 1, 0, 0): -0.61, datetime.datetime(2013, 2, 1, 0, 0): -1.0070000000000001, datetime.datetime(2013, 3, 1, 0, 0): -3.185, datetime.datetime(2013, 4, 1, 0, 0): 0.322, datetime.datetime(2013, 5, 1, 0, 0): 0.494, datetime.datetime(2013, 6, 1, 0, 0): 0.5489999999999999, datetime.datetime(2013, 7, 1, 0, 0): -0.011000000000000001, datetime.datetime(2013, 8, 1, 0, 0): 0.154, datetime.datetime(2013, 9, 1, 0, 0): -0.461, datetime.datetime(2013, 10, 1, 0, 0): 0.263, datetime.datetime(2013, 11, 1, 0, 0): 2.029, datetime.datetime(2013, 12, 1, 0, 0): 1.475, datetime.datetime(2014, 1, 1, 0, 0): -0.9690000000000001, datetime.datetime(2014, 2, 1, 0, 0): 0.044000000000000004, datetime.datetime(2014, 3, 1, 0, 0): 1.206, datetime.datetime(2014, 4, 1, 0, 0): 0.972, datetime.datetime(2014, 5, 1, 0, 0): 0.46399999999999997, datetime.datetime(2014, 6, 1, 0, 0): -0.507, datetime.datetime(2014, 7, 1, 0, 0): -0.489, datetime.datetime(2014, 8, 1, 0, 0): -0.37200000000000005, datetime.datetime(2014, 9, 1, 0, 0): 0.102, datetime.datetime(2014, 10, 1, 0, 0): -1.1340000000000001, datetime.datetime(2014, 11, 1, 0, 0): -0.53, datetime.datetime(2014, 12, 1, 0, 0): 0.413, datetime.datetime(2015, 1, 1, 0, 0): 1.092, datetime.datetime(2015, 2, 1, 0, 0): 1.043, datetime.datetime(2015, 3, 1, 0, 0): 1.837, datetime.datetime(2015, 4, 1, 0, 0): 1.216, datetime.datetime(2015, 5, 1, 0, 0): 0.763, datetime.datetime(2015, 6, 1, 0, 0): 0.42700000000000005, datetime.datetime(2015, 7, 1, 0, 0): -1.1079999999999999, datetime.datetime(2015, 8, 1, 0, 0): -0.6890000000000001, datetime.datetime(2015, 9, 1, 0, 0): -0.165, datetime.datetime(2015, 10, 1, 0, 0): -0.25, datetime.datetime(2015, 11, 1, 0, 0): 1.945, datetime.datetime(2015, 12, 1, 0, 0): 1.444, datetime.datetime(2016, 1, 1, 0, 0): -1.449, datetime.datetime(2016, 2, 1, 0, 0): -0.024, datetime.datetime(2016, 3, 1, 0, 0): 0.28, datetime.datetime(2016, 4, 1, 0, 0): -1.051, datetime.datetime(2016, 5, 1, 0, 0): -0.036000000000000004, datetime.datetime(2016, 6, 1, 0, 0): 0.313, datetime.datetime(2016, 7, 1, 0, 0): 0.085, datetime.datetime(2016, 8, 1, 0, 0): 0.47200000000000003, datetime.datetime(2016, 9, 1, 0, 0): 0.7809999999999999, datetime.datetime(2016, 10, 1, 0, 0): -1.9169999999999998, datetime.datetime(2016, 11, 1, 0, 0): -0.611, datetime.datetime(2016, 12, 1, 0, 0): 1.786, datetime.datetime(2017, 1, 1, 0, 0): 0.9420000000000001, datetime.datetime(2017, 2, 1, 0, 0): 0.34, datetime.datetime(2017, 3, 1, 0, 0): 1.365, datetime.datetime(2017, 4, 1, 0, 0): -0.08900000000000001, datetime.datetime(2017, 5, 1, 0, 0): -0.73, datetime.datetime(2017, 6, 1, 0, 0): 0.402, datetime.datetime(2017, 7, 1, 0, 0): 0.634, datetime.datetime(2017, 8, 1, 0, 0): 0.15, datetime.datetime(2017, 9, 1, 0, 0): -0.49200000000000005, datetime.datetime(2017, 10, 1, 0, 0): 0.69, datetime.datetime(2017, 11, 1, 0, 0): -0.078, datetime.datetime(2017, 12, 1, 0, 0): -0.059000000000000004, datetime.datetime(2018, 1, 1, 0, 0): -0.281, datetime.datetime(2018, 2, 1, 0, 0): 0.113, datetime.datetime(2018, 3, 1, 0, 0): -0.941, datetime.datetime(2018, 4, 1, 0, 0): 0.544, datetime.datetime(2018, 5, 1, 0, 0): 1.18, datetime.datetime(2018, 6, 1, 0, 0): 0.38, datetime.datetime(2018, 7, 1, 0, 0): 0.612, datetime.datetime(2018, 8, 1, 0, 0): 0.836, datetime.datetime(2018, 9, 1, 0, 0): 0.585, datetime.datetime(2018, 10, 1, 0, 0): 0.413, datetime.datetime(2018, 11, 1, 0, 0): -1.1159999999999999, datetime.datetime(2018, 12, 1, 0, 0): 0.11, datetime.datetime(2019, 1, 1, 0, 0): -0.713, datetime.datetime(2019, 2, 1, 0, 0): 1.149, datetime.datetime(2019, 3, 1, 0, 0): 2.116, datetime.datetime(2019, 4, 1, 0, 0): -0.255, datetime.datetime(2019, 5, 1, 0, 0): -1.2309999999999999, datetime.datetime(2019, 6, 1, 0, 0): -0.601, datetime.datetime(2019, 7, 1, 0, 0): -0.89, datetime.datetime(2019, 8, 1, 0, 0): -0.722, datetime.datetime(2019, 9, 1, 0, 0): 0.306, datetime.datetime(2019, 10, 1, 0, 0): -0.08199999999999999, datetime.datetime(2019, 11, 1, 0, 0): -1.193, datetime.datetime(2019, 12, 1, 0, 0): 0.41200000000000003, datetime.datetime(2020, 1, 1, 0, 0): 2.419, datetime.datetime(2020, 2, 1, 0, 0): 3.417, datetime.datetime(2020, 3, 1, 0, 0): 2.641, datetime.datetime(2020, 4, 1, 0, 0): 0.9279999999999999, datetime.datetime(2020, 5, 1, 0, 0): -0.027000000000000003, datetime.datetime(2020, 6, 1, 0, 0): -0.122, datetime.datetime(2020, 7, 1, 0, 0): -0.41200000000000003, datetime.datetime(2020, 8, 1, 0, 0): -0.381, datetime.datetime(2020, 9, 1, 0, 0): 0.631, datetime.datetime(2020, 10, 1, 0, 0): -0.07200000000000001, datetime.datetime(2020, 11, 1, 0, 0): 2.086, datetime.datetime(2020, 12, 1, 0, 0): -1.736, datetime.datetime(2021, 1, 1, 0, 0): -2.484, datetime.datetime(2021, 2, 1, 0, 0): -1.1909999999999998, datetime.datetime(2021, 3, 1, 0, 0): 2.109, datetime.datetime(2021, 4, 1, 0, 0): -0.204, datetime.datetime(2021, 5, 1, 0, 0): -0.161, datetime.datetime(2021, 6, 1, 0, 0): 0.845, datetime.datetime(2021, 7, 1, 0, 0): 0.63, datetime.datetime(2021, 8, 1, 0, 0): -0.209, datetime.datetime(2021, 9, 1, 0, 0): -0.252, datetime.datetime(2021, 10, 1, 0, 0): -0.146, datetime.datetime(2021, 11, 1, 0, 0): 0.09300000000000001, datetime.datetime(2021, 12, 1, 0, 0): 0.198, datetime.datetime(2022, 1, 1, 0, 0): 0.848, datetime.datetime(2022, 2, 1, 0, 0): 1.544, datetime.datetime(2022, 3, 1, 0, 0): 0.305, datetime.datetime(2022, 4, 1, 0, 0): -0.603, datetime.datetime(2022, 5, 1, 0, 0): 1.224, datetime.datetime(2022, 6, 1, 0, 0): -0.07400000000000001, datetime.datetime(2022, 7, 1, 0, 0): 0.025, datetime.datetime(2022, 8, 1, 0, 0): -0.17, datetime.datetime(2022, 9, 1, 0, 0): -0.655, datetime.datetime(2022, 10, 1, 0, 0): 1.3459999999999999, datetime.datetime(2022, 11, 1, 0, 0): 0.33899999999999997, datetime.datetime(2022, 12, 1, 0, 0): -2.719, datetime.datetime(2023, 1, 1, 0, 0): -0.674, datetime.datetime(2023, 2, 1, 0, 0): 1.6, datetime.datetime(2023, 3, 1, 0, 0): 0.28, datetime.datetime(2023, 4, 1, 0, 0): -0.973, datetime.datetime(2023, 5, 1, 0, 0): 1.1340000000000001, datetime.datetime(2023, 6, 1, 0, 0): -0.28600000000000003, datetime.datetime(2023, 7, 1, 0, 0): -0.154, datetime.datetime(2023, 8, 1, 0, 0): -0.602, datetime.datetime(2023, 9, 1, 0, 0): 0.318, datetime.datetime(2023, 10, 1, 0, 0): -0.414, datetime.datetime(2023, 11, 1, 0, 0): -0.036000000000000004, datetime.datetime(2023, 12, 1, 0, 0): -0.221, datetime.datetime(2024, 1, 1, 0, 0): -0.21, datetime.datetime(2024, 2, 1, 0, 0): 0.635, datetime.datetime(2024, 3, 1, 0, 0): -0.61, datetime.datetime(2024, 4, 1, 0, 0): 0.465, datetime.datetime(2024, 5, 1, 0, 0): -0.048, datetime.datetime(2024, 6, 1, 0, 0): 0.136, datetime.datetime(2024, 7, 1, 0, 0): 0.5870000000000001, datetime.datetime(2024, 8, 1, 0, 0): 1.284, datetime.datetime(2024, 9, 1, 0, 0): -0.624}


# In[60]:


temp_dict = {}
sh_dict = {}
cc_dict = {}
for i, date in enumerate(dates):
    temp_dict[date] = temperature[i,:,:]
    sh_dict[date] = specific_humidity[i,:,:]
    cc_dict[date] = cloud_cover[i,:,:]


# In[61]:


#Standardization
data_dicts = {'temp': temp_dict, 'sh': sh_dict, 'cc': cc_dict}

standardized_data = {}

for data_name, data_dict in data_dicts.items():
    monthly_data = {month: [] for month in range(1, 13)}
    for dt, values in data_dict.items():
        monthly_data[dt.month].append(values)

    monthly_mean = {}
    monthly_std = {}
    for month, values in monthly_data.items():
        stacked_values = np.stack(values, axis=0)
        monthly_mean[month] = np.mean(stacked_values, axis=0)
        monthly_std[month] = np.std(stacked_values, axis=0)

    standardized = {}
    for dt, values in data_dict.items():
        month = dt.month
        anomaly = values - monthly_mean[month]
        standardized[dt] = anomaly / monthly_std[month]

    standardized_data[data_name] = standardized
#print(len(standardized_data))


# In[62]:


temp_standardized = standardized_data['temp']
sh_standardized = standardized_data['sh']
cc_standardized = standardized_data['cc']


# In[63]:


#Lag correlation for enso
import numpy as np
from scipy.stats import pearsonr
from dateutil.relativedelta import relativedelta

max_lag = 12
enso_lag_correlation_results = {var: {lag: [] for lag in range(max_lag + 1)} for var in ['temp', 'sh', 'cc']}

for var, data_dict in standardized_data.items():
    for lag in range(max_lag + 1):
        common_dates = set(enso_data_dict.keys()).intersection(data_dict.keys())
        shifted_enso = {dt + relativedelta(months=lag): value for dt, value in enso_data_dict.items()}
        valid_dates = set(shifted_enso.keys()).intersection(common_dates)

        enso_values = np.array([shifted_enso[dt] for dt in sorted(valid_dates)])
        data_values = np.array([data_dict[dt] for dt in sorted(valid_dates)])
        data_values = data_values.reshape(len(enso_values),-1)
        #print(enso_values.shape)

        correlation_map = np.array([
            pearsonr(enso_values, data_values[:, i])[0]
            for i in range(data_values.shape[1])
        ]).reshape(len(temperature[0,:,0]), len(temperature[0,0,:]))
        
        enso_lag_correlation_results[var][lag] = correlation_map
        
enso_lag_corr = {var: [] for var in ['temp', 'sh', 'cc']}

# Iterate over the items of the enso_lag_correlation_results dictionary
for var, data_dict in standardized_data.items():
    for lag in range(max_lag + 1):
        correlation_map = enso_lag_correlation_results[var][lag]
        
        # Compute the spatial mean (average over the (8, 16) grid)
        spatial_mean = np.mean(correlation_map)
        
        # Store the spatial mean in the dictionary
        enso_lag_corr[var].append(spatial_mean)


# In[64]:


#Lag correlation for ao
import numpy as np
from scipy.stats import pearsonr
from dateutil.relativedelta import relativedelta

max_lag = 12
ao_lag_correlation_results = {var: {lag: [] for lag in range(max_lag + 1)} for var in ['temp', 'sh', 'cc']}

for var, data_dict in standardized_data.items():
    for lag in range(max_lag + 1):
        common_dates = set(ao_data_dict.keys()).intersection(data_dict.keys())
        shifted_ao = {dt + relativedelta(months=lag): value for dt, value in ao_data_dict.items()}
        valid_dates = set(shifted_ao.keys()).intersection(common_dates)

        ao_values = np.array([shifted_ao[dt] for dt in sorted(valid_dates)])
        data_values = np.array([data_dict[dt] for dt in sorted(valid_dates)])
        data_values = data_values.reshape(len(ao_values),-1)
        #print(ao_values.shape)

        correlation_map = np.array([
            pearsonr(ao_values, data_values[:, i])[0]
            for i in range(data_values.shape[1])
        ]).reshape(len(temperature[0,:,0]), len(temperature[0,0,:]))
        
        ao_lag_correlation_results[var][lag] = correlation_map
        
ao_lag_corr = {var: [] for var in ['temp', 'sh', 'cc']}

# Iterate over the items of the enso_lag_correlation_results dictionary
for var, data_dict in standardized_data.items():
    for lag in range(max_lag + 1):
        correlation_map = ao_lag_correlation_results[var][lag]
        
        # Compute the spatial mean (average over the (8, 16) grid)
        spatial_mean = np.mean(correlation_map)
        
        # Store the spatial mean in the dictionary
        ao_lag_corr[var].append(spatial_mean)


# In[65]:


#El Nino months
threshold = 0.4
min_consecutive_months = 6

el_nino_months = []
current_period = []

for date, value in sorted(enso_data_dict.items()):
    if value >= threshold:
        current_period.append(date)
    else:
        if len(current_period) >= min_consecutive_months:
            el_nino_months.append(current_period)
        current_period = []

# Check the last period if it ended with a high value
if len(current_period) >= min_consecutive_months:
    el_nino_months.append(current_period)

el_nino_data_dict = {}

# Extract the data corresponding to the El Niño months
for period in el_nino_months:
    for date in period:
        el_nino_data_dict[date] = enso_data_dict[date]


# In[66]:


#La Nina months
threshold = - 0.4
min_consecutive_months = 6

la_nina_months = []
current_period = []

for date, value in sorted(enso_data_dict.items()):
    if value <= threshold:
        current_period.append(date)
    else:
        if len(current_period) >= min_consecutive_months:
            la_nina_months.append(current_period)
        current_period = []

# Check the last period if it ended with a high value
if len(current_period) >= min_consecutive_months:
    la_nina_months.append(current_period)

la_nina_data_dict = {}

# Extract the data corresponding to the El Niño months
for period in la_nina_months:
    for date in period:
        la_nina_data_dict[date] = enso_data_dict[date]


# In[67]:


#El Nino
import numpy as np
from scipy.stats import pearsonr
from dateutil.relativedelta import relativedelta

# Assuming el_nino_data_dict, standardized_data (temp, sh, cc) are defined

max_lag = 12  # Example: lag from 0 to 12 months
el_nino_lag_correlation_results = {var: {lag: [] for lag in range(max_lag + 1)} for var in ['temp', 'sh', 'cc']}

for var, data_dict in standardized_data.items():
    for lag in range(max_lag + 1):
        # Shift the El Nino data by the lag
        shifted_enso = {dt + relativedelta(months=lag): value for dt, value in el_nino_data_dict.items()}
        
        # Find the common dates between shifted El Nino data and the data_dict
        common_dates = set(shifted_enso.keys()).intersection(data_dict.keys())
        #print(len(common_dates))
        # Ensure data is ordered by date
        shifted_enso_sorted = [shifted_enso[dt] for dt in sorted(common_dates)]
        data_values_sorted = [data_dict[dt] for dt in sorted(common_dates)]
        
        # Convert to numpy arrays for correlation calculation
        enso_values = np.array(shifted_enso_sorted)
        data_values = np.array(data_values_sorted)
        
        # Reshape data values if necessary (flattening for correlation)
        data_values = data_values.reshape(len(enso_values), -1)
        
        # Calculate the correlation map for each variable
        correlation_map = np.array([
            pearsonr(enso_values, data_values[:, i])[0] for i in range(data_values.shape[1])
        ]).reshape(data_values.shape[1:])
        
        # Store the result
        el_nino_lag_correlation_results[var][lag] = correlation_map
        
el_nino_lag_corr = {var: [] for var in ['temp', 'sh', 'cc']}

# Iterate over the items of the enso_lag_correlation_results dictionary
for var, data_dict in standardized_data.items():
    for lag in range(max_lag + 1):
        correlation_map = el_nino_lag_correlation_results[var][lag]
        
        # Compute the spatial mean (average over the (8, 16) grid)
        spatial_mean = np.mean(correlation_map)
        
        # Store the spatial mean in the dictionary
        el_nino_lag_corr[var].append(spatial_mean)


# In[68]:


#La Nina
import numpy as np
from scipy.stats import pearsonr
from dateutil.relativedelta import relativedelta

# Assuming el_nino_data_dict, standardized_data (temp, sh, cc) are defined

max_lag = 12  # Example: lag from 0 to 12 months
la_nina_lag_correlation_results = {var: {lag: [] for lag in range(max_lag + 1)} for var in ['temp', 'sh', 'cc']}

for var, data_dict in standardized_data.items():
    for lag in range(max_lag + 1):
        # Shift the El Nino data by the lag
        shifted_enso = {dt + relativedelta(months=lag): value for dt, value in la_nina_data_dict.items()}
        
        # Find the common dates between shifted El Nino data and the data_dict
        common_dates = set(shifted_enso.keys()).intersection(data_dict.keys())
        #print(len(common_dates))
        # Ensure data is ordered by date
        shifted_enso_sorted = [shifted_enso[dt] for dt in sorted(common_dates)]
        data_values_sorted = [data_dict[dt] for dt in sorted(common_dates)]
        
        # Convert to numpy arrays for correlation calculation
        enso_values = np.array(shifted_enso_sorted)
        data_values = np.array(data_values_sorted)
        
        # Reshape data values if necessary (flattening for correlation)
        data_values = data_values.reshape(len(enso_values), -1)
        
        # Calculate the correlation map for each variable
        correlation_map = np.array([
            pearsonr(enso_values, data_values[:, i])[0] for i in range(data_values.shape[1])
        ]).reshape(data_values.shape[1:])
        
        # Store the result
        la_nina_lag_correlation_results[var][lag] = correlation_map
        
la_nina_lag_corr = {var: [] for var in ['temp', 'sh', 'cc']}

# Iterate over the items of the enso_lag_correlation_results dictionary
for var, data_dict in standardized_data.items():
    for lag in range(max_lag + 1):
        correlation_map = la_nina_lag_correlation_results[var][lag]
        
        # Compute the spatial mean (average over the (8, 16) grid)
        spatial_mean = np.mean(correlation_map)
        
        # Store the spatial mean in the dictionary
        la_nina_lag_corr[var].append(spatial_mean)


# In[69]:


import matplotlib.pyplot as plt

lag_correlation_data = {
    "ENSO": enso_lag_corr,
    "AO": ao_lag_corr,
    "El Nino": el_nino_lag_corr,
    "La Nina": la_nina_lag_corr
}

plt.figure(figsize=(10, 6))

subplot_index = 1

for label, data_dict in lag_correlation_data.items():
    plt.subplot(2,2,subplot_index)
    for var_name, values in data_dict.items():
        plt.plot(values, label=f'{var_name}', marker='o')

    plt.xlabel('Lag (Months)', fontsize=12)
    plt.ylabel('Correlation', fontsize=12)
    plt.title(f'Lag Correlation of {label} with Variables', fontsize=14)
    
    plt.gca().invert_xaxis()
    
    plt.xticks()  # Ensure x-ticks correspond to reversed lags
    plt.grid(True)
    plt.legend(title="Variables")
    
    subplot_index += 1
    
plt.tight_layout()
#plt.savefig('lag_analysis.png')
plt.show()


# In[31]:


Utqiagvik_enso = enso_lag_corr
Utqiagvik_ao = ao_lag_corr


# In[44]:


Deering_enso = enso_lag_corr
Deering_ao = ao_lag_corr


# In[57]:


Nunam_Iqua_enso = enso_lag_corr
Nunam_Iqua_ao = ao_lag_corr


# In[70]:


Kwigillingok_enso = enso_lag_corr
Kwigillingok_ao = ao_lag_corr


# In[73]:


selected_sites = ["Utqiagvik", "Deering", "Nunam Iqua", "Kwigillingok"]

enso_dict = {}
for site in selected_sites:
    var_name = f"{site.replace(' ', '_')}_enso"
    if var_name in globals():
        enso_dict[site] = globals()[var_name]

print(enso_dict)


# In[79]:


selected_sites = ["Utqiagvik", "Deering", "Nunam Iqua", "Kwigillingok"]

ao_dict = {}
for site in selected_sites:
    var_name = f"{site.replace(' ', '_')}_ao"
    if var_name in globals():
        ao_dict[site] = globals()[var_name]

print(ao_dict)


# In[78]:


import matplotlib.pyplot as plt

selected_sites = ["Utqiagvik", "Deering", "Nunam Iqua", "Kwigillingok"]

plt.figure(figsize=(10, 6))

subplot_index = 1

for site in selected_sites:
    dict_enso = enso_dict[site]
    plt.subplot(2,2,subplot_index)
    for var_name, values in dict_enso.items():
        plt.plot(values, label=f'{var_name}', marker='o')

    plt.xlabel('Lag (Months)', fontsize=12)
    plt.ylabel('Correlation', fontsize=12)
    plt.title(f'Lag Correlation of ENSO in {site}', fontsize=12)
    
    plt.gca().invert_xaxis()
    
    plt.xticks()  # Ensure x-ticks correspond to reversed lags
    plt.grid(True)
    plt.legend(title="Variables")
    
    subplot_index += 1
    
plt.tight_layout()
plt.savefig('lag_analysis.png')
plt.show()


# In[80]:


import matplotlib.pyplot as plt

selected_sites = ["Utqiagvik", "Deering", "Nunam Iqua", "Kwigillingok"]

plt.figure(figsize=(10, 6))

subplot_index = 1

for site in selected_sites:
    dict_ao = ao_dict[site]
    plt.subplot(2,2,subplot_index)
    for var_name, values in dict_ao.items():
        plt.plot(values, label=f'{var_name}', marker='o')

    plt.xlabel('Lag (Months)', fontsize=12)
    plt.ylabel('Correlation', fontsize=12)
    plt.title(f'Lag Correlation of AO in {site}', fontsize=12)
    
    plt.gca().invert_xaxis()
    
    plt.xticks()  # Ensure x-ticks correspond to reversed lags
    plt.grid(True)
    plt.legend(title="Variables")
    
    subplot_index += 1
    
plt.tight_layout()
plt.savefig('lag_analysis_ao.png')
plt.show()


# In[ ]:





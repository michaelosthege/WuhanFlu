import pandas
import numpy

def get_pooled() -> pandas.DataFrame:

    dates = pandas.date_range('2020-01-10','2020-01-27')
    #Missing data from the 14
    dates = dates[dates!='2020-01-14']

    df = pandas.DataFrame(
        index=dates,
        columns=['I', 'Rd', 'Rr', 'R']
    )
    df['I'] = [
        41,
        41,
        41,
        41,
        numpy.NaN,
        45,
        62,
        121,
        198,
        291,
        440,
        571,
        830,
        1287,
        1975,
        2744,
        4515
    ]
    df['Rd'] = [
        1,
        1,
        1,
        1,
        2,
        numpy.NaN,
        2,
        numpy.NaN,
        3,
        6,
        9,
        17,
        25,
        41,
        56,
        80,
        106
    ]
    df['Rr'] = [
        numpy.NaN,
        numpy.NaN, 
        numpy.NaN,
        numpy.NaN,
        7,
        12,
        15,
        19,
        25,
        25,
        numpy.NaN, 
        numpy.NaN,
        34,
        38,
        49,
        51,
        60
    ]
    df['R'] = df.Rd + df.Rr
    
    return df
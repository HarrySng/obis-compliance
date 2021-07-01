from .setup import *
from .helpers import *
from.generate_report import *

def format_dt(dt):
    """[summary]

    Args:
        dt ([type]): [description]
    """
    
    dt_formatted = None
    try:
        dt_formatted = datetime.strptime(dt,'%Y-%m-%dT%H:%M:%SZ')
    except:
        pass
    
    return dt_formatted

def check_date_format(col):
    """[summary]
    """

    df = pd.read_csv(tmp_path + 'event.csv')
    
    dt_correct = []
    dt_incorrect = []
    for dt in df[col]:
        if '/' in dt:
            for d in dt.split('/'):
                d_formatted = format_dt(d)
                if d_formatted is not None:
                    dt_correct.append(d_formatted)
                else:
                    dt_incorrect.append(df.loc[df[col]==d,'eventID'].iloc[0])
        else:
            dt_formatted = format_dt(dt)
            if dt_formatted is not None:
                    dt_correct.append(dt_formatted)
            else:
                dt_incorrect.append(df.loc[df[col]==dt,'eventID'].iloc[0])
    
    msgs = []
    msgs.append("\n### Date Checks for '{}' field.\n".format(col))
    msgs.append('* Earliest Date: {}\n'.format(min(dt_correct).strftime('%Y-%m-%d %H:%M:%S')))
    msgs.append('* Latest Date: {}\n'.format(max(dt_correct).strftime('%Y-%m-%d %H:%M:%S')))
    if len(dt_incorrect) > 0:
        msgs.append('* The date formats for the following eventIDs are incorrect:\n')
        for id in dt_incorrect:
            msgs.append('\t* {}\n'.format(id))

    write_message(msgs)
    
    return
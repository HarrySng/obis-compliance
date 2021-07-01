from .setup import *
from .helpers import *

def create_report(file):
    """[summary]

    Args:
        file ([type]): [description]
    """

    remove_all_files(out_path) # Remove existing reports
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " local time."
    f = open(out_path + file.split(".")[0] + "_Report.md", "w")
    f.write("# OBIS Compliance Check Report\n")
    f.write("\nOBIS Package Name: **{}**\n".format(file))
    f.write('\nPackage uploaded at {}\n'.format(dt))
    f.write('\n---\n')
    f.write("This report is generated using the obis-compliance package.\n")
    f.write("For more details, please go to the following link: https://github.com/HarrySng/obis-compliance\n")
    f.write('\n---\n')
    f.close()
    
    return

def write_message(msgs):
    """[summary]

    Args:
        msgs ([type]): [description]
    """

    report = os.listdir(out_path)[0]
    with open(out_path + report, 'a') as f:
        for msg in msgs:
            f.write(msg)
    
    return


def write_missing_fields(core, mf):
    """[summary]

    Args:
        core ([type]): [description]
        mf ([type]): [description]
    """

    msgs = []
    msgs.append('\n---\n')
    msgs.append('### Missing fields for the **{}** core\n\n'.format(core))
    msgs.append('Required by | Field | No. of missing values\n')
    msgs.append(':---: | :---: | :---:\n')
    
    for k in list(mf.keys()):
        v = mf[k]
        if len(v) < 1:
            continue
        else:
            for i in range(len(v)):
                msgs.append(k + " | " + list(v[i].keys())[0] + " | "+ str(len(list(v[i].values())[0])) + "\n")
    
    write_message(msgs)
    
    return

def write_coordinates_depth(crd):
    """[summary]

    Args:
        crd ([type]): [description]
    """

    msgs = []
    msgs.append('### Bounding Coordinates and Depth of the records.\n\n')
    msgs.append('&nbsp; | Latitude | Longitude | Minimum Depth (m) | Maximum Depth (m)\n')
    msgs.append(':---: | :---: | :---: | :---: | :---:\n')
    msgs.append('**Minimum** | ' + str(crd['decimalLatitude'][0]) + ' | ' + str(crd['decimalLongitude'][0]) + ' | ' + str(crd['minimumDepthInMeters'][0]) + ' | ' + str(crd['maximumDepthInMeters'][0]) + '\n')
    msgs.append('**Maximum** | ' + str(crd['decimalLatitude'][1]) + ' | ' + str(crd['decimalLongitude'][1]) + ' | ' + str(crd['minimumDepthInMeters'][1]) + ' | ' + str(crd['maximumDepthInMeters'][1]) + '\n')
    write_message(msgs)
    
    return
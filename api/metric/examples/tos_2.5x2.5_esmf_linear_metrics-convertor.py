# -*- coding: utf-8 -*-
import collections, json, os



# Set path to metrics file.
_FPATH = os.path.abspath(__file__).replace("-convertor.py", ".json")

# Load input file.
with open(_FPATH, 'r') as ifile:
    data = ifile.read()

# Replace NaN with "nan" as this is against JSON spec and fails jquery parsing.
data = data.replace("NaN", '"nan"')

# Set input metrics.
metrics_in = json.loads(data, object_pairs_hook=collections.OrderedDict)

# Set group.
group = "tos_2-5x2-5_esmf_linear_metrics"

# Set fields.
fields = []
fields += metrics_in["GFDL-ESM2G"]["SimulationDescription"].keys()
fields += ["realm", "source", "RegionalMasking"]
fields += metrics_in["GFDL-ESM2G"]["defaultReference"]["r1i1p1"]["global"].keys()

# Set lines.
lines = []
for realm, metrics in metrics_in["GFDL-ESM2G"]["defaultReference"]["r1i1p1"].iteritems():
    line = []
    line += metrics_in["GFDL-ESM2G"]["SimulationDescription"].values()
    line.append(realm)
    line.append(metrics_in["GFDL-ESM2G"]["defaultReference"]["source"])
    line.append(metrics_in["RegionalMasking"][realm])
    line += metrics_in["GFDL-ESM2G"]["defaultReference"]["r1i1p1"][realm].values()
    lines.append(line)

# Set output metrics.
metrics_out = {
    "group": group,
    "columns": fields,
    "metrics": lines
}

# Set output filename.
fname, fext = os.path.splitext(_FPATH)
ofpath = "{0}-converted{1}".format(fname, fext)

# Write output.
with open(ofpath, 'w') as ofile:
    ofile.write(json.dumps(metrics_out))

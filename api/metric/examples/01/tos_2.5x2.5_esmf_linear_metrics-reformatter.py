# -*- coding: utf-8 -*-
import collections, json, os



# Set I/O paths.
_INPUT_FILE = os.path.abspath(__file__).replace("-reformatter.py", ".json")
_OUTPUT_FILENAME, _OUTPUT_FILEEXT = os.path.splitext(_INPUT_FILE)
_OUTPUT_FILE = "{0}-reformatted{1}".format(_OUTPUT_FILENAME, _OUTPUT_FILEEXT)


# Load input data.
with open(_INPUT_FILE, 'r') as ifile:
    input_data = ifile.read()
input_data = input_data.replace("NaN", '"nan"')
input_data = json.loads(input_data,
                        object_pairs_hook=collections.OrderedDict)

# Initialize output data.
output_data = {
    "group": "tos_2-5x2-5_esmf_linear_metrics",
    "columns": [],
    "metrics": []
}

# Set columns.
output_data["columns"] += input_data["GFDL-ESM2G"]["SimulationDescription"].keys()
output_data["columns"] += ["realm", "source", "RegionalMasking"]
output_data["columns"] += input_data["GFDL-ESM2G"]["defaultReference"]["r1i1p1"]["global"].keys()

# Set metrics.
for realm, metrics in input_data["GFDL-ESM2G"]["defaultReference"]["r1i1p1"].iteritems():
    metric = []
    metric += input_data["GFDL-ESM2G"]["SimulationDescription"].values()
    metric.append(realm)
    metric.append(input_data["GFDL-ESM2G"]["defaultReference"]["source"])
    metric.append(input_data["RegionalMasking"][realm])
    metric += input_data["GFDL-ESM2G"]["defaultReference"]["r1i1p1"][realm].values()
    output_data["metrics"].append(metric)

# Write output.
with open(_OUTPUT_FILE, 'w') as output_file:
    output_file.write(json.dumps(output_data))

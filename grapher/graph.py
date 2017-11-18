from operator import itemgetter
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import pylab


# Parses server/value_to_parse tuples from RESULTS.md
# Example output: [('go/go', 100), ('go/fasthttp', 200)]
def parse_results_file(value_to_parse):
    print('Parsing RESULTS.md for', value_to_parse)
    results_file = open('RESULTS.md')
    at_benchmarks = False
    results = []
    server = ''

    for line in results_file:
        # Iterate until after Benchmarks line
        if at_benchmarks == False:
            if ('# Benchmarks' in line):
                at_benchmarks = True

        # Iterate until server
        if (line.startswith('## ')):
            server = line.lstrip('## ').strip()

        # Iterate until value and save
        if (line.startswith(value_to_parse)):
            req_per_sec = line.lstrip(value_to_parse).strip()
            req_per_sec = round(float(req_per_sec))
            results.append((server, req_per_sec))

    results_file.close()

    # Sort result and return
    return sorted(results, key=itemgetter(1))


# Builds and saves bar chart
def build_bar_chart(x_axis_label, parsed_values):
    print('Building bar chart...')

    # Split tuple server/values
    servers, values = zip(*parsed_values)

    y_pos = np.arange(len(servers))
    plt.barh(y_pos, values, align='center', alpha=1.0)
    plt.yticks(y_pos, servers)
    plt.xlabel(x_axis_label)
    plt.tick_params(axis='y', pad=2)
    plt.tight_layout()
    plt.savefig('RESULTS.png')


def main():
    print('Running grapher...')

    # Values to parse from RESULTS.md
    # First val in tuple is the line to look for in RESULTS.md
    # Second val in tuple is the X-axis label in graph
    values_to_parse = [('Requests/sec:', 'Requests per second')]

    for vtp in values_to_parse:
        parsed_values = parse_results_file(vtp[0])
        build_bar_chart(vtp[1], parsed_values)

    print('Done!')


main()

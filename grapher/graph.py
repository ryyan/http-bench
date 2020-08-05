from operator import itemgetter

from ascii_graph import Pyasciigraph


# Parses (server, value_to_parse) tuples from RESULTS.md
# Example output: [('go/go', 100), ('go/fasthttp', 200)]
def parse_results_file(value_to_parse):
    print('Parsing RESULTS.md for', value_to_parse)
    results_file = open('../RESULTS.md')
    results = []

    for line in results_file:
        # Parse server
        if (line.startswith('## ')):
            server = line.lstrip('## ').strip()

        # Parse value
        if (line.startswith(value_to_parse)):
            parsed_value = line.lstrip(value_to_parse).strip()
            parsed_value = round(float(parsed_value))
            results.append((server, parsed_value))

    results_file.close()

    # Return sorted results
    return sorted(results, key=itemgetter(1), reverse=True)


def main():
    print('Running grapher')

    # Values to parse from RESULTS.md
    # First val in tuple is the line to look for in RESULTS.md
    # Second val in tuple is the X-axis label in graph
    values_to_parse = [('Requests/sec:', 'Requests per second')]


    for vtp in values_to_parse:
        parsed_values = parse_results_file(vtp[0])
        graph = Pyasciigraph(
                line_length=1,
                human_readable="si",
                float_format="{0:,.1f}",
            )
        for line in graph.graph(vtp[1], parsed_values):
            print(line.strip() + "\n")
        #build_bar_chart(vtp[1], parsed_values)

    print('Done!')


main()

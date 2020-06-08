import re
import sys
import pprint
# sys.path.insert(0,'')
# from nlp import Text
import importlib.util
spec_0 = importlib.util.spec_from_file_location("Text", "/home/chinmay/Documents/data_science/modules/nlp.py")
NLP = importlib.util.module_from_spec(spec_0)
spec_0.loader.exec_module(NLP)





class Graph:
    graph = {}
    graph_nodes = []

    def add_nodes_interactive(self):
        # Interactive, one-by-one
        node_name = str(input("What is the name of the node?\t"))
        if(node_name in self.graph_nodes):
            print("This node already exists.")
        else:
            self.graph[node_name] = []
            self.graph_nodes.append(node_name)
        print('\t'.join(self.graph_nodes))
        return

    def add_nodes(self, list_nodes):
        self.graph_nodes = list_nodes
        return

    def add_edges_interactive(self, graph_nodes, is_weighted):
        text = NLP.Text()
        # Interactive
        print(graph_nodes)

        # Create a string to show progress.
        list_progress = []
        for x in graph_nodes:
            for y in graph_nodes:
                if(x !=y):
                    if(not is_weighted):
                        list_progress.append("{} --> {} ___".format(x, y))
                    else:
                        list_progress.append("{} --___--> {} ___".format(x, y))
        progress = '\n'.join(list_progress)

        for i in range(0, len(graph_nodes)):
            self.graph[graph_nodes[i]] = []
            
            j = 0

            while j < len(graph_nodes):
                # print(i,j, self.graph)
                pprint.pprint(progress)
                if(graph_nodes[i] != graph_nodes[j]):
                    is_connected = str(input("{} --> {}? y or n?\t".format(graph_nodes[i], graph_nodes[j])))[0]
                    if(is_connected in ('y', 'n')):
                        if(is_connected == 'y'):
                            if(not is_weighted):
                                self.graph[graph_nodes[i]].append(graph_nodes[j])
                                j += 1
                                # Update progress
                                progress = text.find_and_replace(
                                    string = progress,
                                    substring = '___',
                                    replacement = is_connected,
                                    number_of_occurrence = 1
                                )

                            else:
                                try:
                                    weight = int(input("Weight?\n"))
                                    if(weight <=0):
                                        print("Please enter positive weight.")
                                    else:
                                        dict_ = {
                                            graph_nodes[j] : weight
                                        }
                                        self.graph[graph_nodes[i]].append(dict_)
                                        j += 1
                                        # Update progress
                                        progress = text.find_and_replace(
                                            string = progress,
                                            substring = '___',
                                            replacement = str(weight),
                                            number_of_occurrence = 1
                                        )
                                        progress = text.find_and_replace(
                                            string = progress,
                                            substring = '___',
                                            replacement = is_connected,
                                            number_of_occurrence = 1
                                        )
                                except ValueError:
                                    print("Please enter integer value.")
                        else:
                            j += 1
                            if( not is_weighted):
                                # Update progress
                                progress = text.find_and_replace(
                                    string = progress,
                                    substring = '___',
                                    replacement = is_connected,
                                    number_of_occurrence = 1
                                )
                            else:
                                # Update progress
                                progress = text.find_and_replace(
                                    string = progress,
                                    substring = '___',
                                    replacement = 'X',
                                    number_of_occurrence = 1
                                )
                                # Update progress
                                progress = text.find_and_replace(
                                    string = progress,
                                    substring = '___',
                                    replacement = is_connected,
                                    number_of_occurrence = 1
                                )
                    else:
                        print("Please enter y or n.")
                else:
                    j += 1
                print("\n\n")
                print(self.graph)
        return

    def create_graph_interactive(self):

        # messages = {
        #     "is_weighted": "Is this a weighted graph? y or n",
        #     "welcome": "Welcome. What is the starting node?"
        # }
        values = {
            "is_weighted": False,
            "is_directional": False
        }

        while True:
            all_nodes = str(input("Enter all the nodes separated by at least one space.\t"))
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            
            if(regex.search(all_nodes) == None):
                break
            else:
                print("Special characters not allowed. Try again.")

        
        list_nodes = all_nodes.split()
        self.add_nodes(list_nodes)

        is_weighted = str(input("Is this a weighted graph? y or n\t"))[0]
        # Determine if the node is weighted
        while True:
            if(is_weighted.isalpha() and is_weighted in ('y', 'n')):
                if(is_weighted == 'y'):
                    values['is_weighted'] = True
                break
            else:
                print("Please enter y or n only.")

        # Remove duplicates
        list_nodes = list(dict.fromkeys(list_nodes))

        # Add edges
        self.add_edges_interactive(list_nodes, values['is_weighted'])

        print(self.graph_nodes)
        return

    def display_graph_edges(self, graph):
        if(len(list(graph.keys())) == 0):
            print("Empty graph!")
            return
        else:

            # Check if all nodes do not have an edge
            if(self.number_of_edges(graph) == 0):
                print("No edges")
                return
            # Check if it is weighted graph
            if(isinstance(graph[list(graph.keys())[0]][0], str)):
                for a in list(graph.keys()):
                    for b in list(graph.keys()):
                        if(self.is_edge_direct(graph, a, b)):
                            print('{} --> {}'.format(a,b))
            else:
                for a in list(graph.keys()):
                    for b in list(graph.keys()):
                        if(self.is_edge_direct(graph, a, b)):
                            for s in filter(lambda x: list(x.keys())[0] == b, graph[a]):
                                weight = list(s.values())[0]
                            print('{} -{}-> {}'.format(a, weight, b))
            return

    def is_edge_direct(self, graph, a, b, bi_directional = True):
        # Check if there is a direct edge between a and b
        # if((a not in list(graph.keys())) or (b not in list(graph.keys()))):
        #     return(False)
        if(a == b):
            return(False)
        else:
            if(isinstance(graph[list(graph.keys())[0]][0], str)):
                is_string = True
            else:
                is_string = False
            if(is_string):
                if(b in graph[a]):
                    return(True)
            else:
                for item in graph[a]:
                    if(list(item.keys())[0] == b):
                        return(True)
            return(False)
    
    def number_of_edges(self, graph):
        count = 0
        for a in list(graph.keys()):
            for b in list(graph.keys()):
                if(self.is_edge_direct(graph, a, b)):
                    # print('{} --> {}'.format(a,b))
                    count += 1 

        return(count)

    def graph2coordinates(self, graph):
        coordinates = []

        def recurse(list_prev_coord, weight, dictionary):
            result = []
            for key, value in dictionary.items():
                if(not isinstance(dictionary[key], dict)):
                    list_prev_coord.append(key)
                    weight = value
                    result.append([list_prev_coord, weight])
                else:
                    recurse(
                        list_prev_coord.append(key), 
                        None, 
                        {key: {} for key,value in dictionary.items()}[key]
                        )
            return(result)

        return(recurse(coordinates, None, graph))


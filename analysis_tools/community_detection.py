import community
import networkx as nx
import matplotlib.pyplot as plt
import psycopg2
import csv

colors = ['#FAF0E6', '#00CED1', '#A52A2A', '#FFE4C4', '#FFFACD', '#F0E68C', '#556B2F'
    , '#9370DB', '#CD853F', '#00BFFF', '#778899', '#FF8C00', '#87CEFA', '#808080', '#800080', '#4B0082', '#A52A2A']

conn_string = "host='localhost' dbname='indoor_position' user='postgres' password='tiancai' port='5432' "
conn = psycopg2.connect(conn_string)
cur  = conn.cursor()

query = '''select distinct(zone_id) from gare_st_lazare.zone_lookup '''
cur.execute(query)
results1 = cur.fetchall()
conn.commit()

query = '''select * from gare_st_lazare.links '''
cur.execute(query)
results2 = cur.fetchall()
conn.commit()

#better with karate_graph() as defined in networkx example.
#erdos renyi don't have true community structure
G = nx.Graph()
for i in results1:
    G.add_node(i[0])

G.add_weighted_edges_from([(item[0], item[1], item[3]) for item in results2 ])

#first compute the best partition
partition = community.best_partition(G)

#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
print(partition)

with open('cluster.csv', 'w+') as csvfile:  
    writer = csv.writer(csvfile)
    for com in set(partition.values()) :
        count = count + 1.
        list_nodes = [nodes for nodes in partition.keys()
                                    if partition[nodes] == com]
        print(count)    
        for node in list_nodes:
            writer.writerow([str(com), str(node)])
            print(com, node)

        nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 70,
                            node_color = colors[int(count)], with_labels=True)

nx.draw_networkx_edges(G, pos, alpha=0.01)
# plt.show()
plt.savefig('./cluster.png', dpi = 800, transparent=True)

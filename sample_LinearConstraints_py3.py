# 同じトポロジで、リンクの重みを変えて、最短経路からの集合
# とAND、ORを求める

# ライブラリの読み込み
import matplotlib.pyplot as plt
import networkx as nx
from graphillion import GraphSet

# トポロジを設定
node = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

edge = [(1, 2), (1, 5), (2, 3), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 9), (6, 7), (6, 10), (7, 8), (7, 11), (8, 12), (9, 10), (9, 13), (10, 14), (10, 11), (11, 12), (11, 15), (12, 16), (13, 14), (14, 15), (15, 16)]

pos = {1:(1, 10), 2:(4, 10), 3: (7, 10), 4:(10, 10), 5:(1, 7), 6:(4, 7), 7:(7, 7), 8:(10, 7), 9:(1, 4), 10:(4, 4), 11:(7, 4), 12:(10, 4), 13:(1, 1), 14:(4, 1), 15:(7, 1), 16:(10, 1)}

# コスト
lc1 = [([(1, 2), (1, 5), (2, 3), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 9), (6, 7), (6, 10), (7, 8), (7, 11), (8, 12), (9, 10), (9, 13), (10, 14), (10, 11), (11, 12), (11, 15), (12, 16), (13, 14), (14, 15), (15, 16)],(6.0, 10.0))]

c1 = {(1, 2):1.0, (1, 5):1.0, (2, 3):1.0, (2, 6):1.0, (3, 4):1.0, (3, 7):1.0, (4, 8):1.0, (5, 6):1.0, (5, 9):1.0, (6, 7):1.0, (6, 10):1.0, (7, 8):1.0, (7, 11):1.0, (8, 12):1.0, (9, 10):1.0, (9, 13):1.0, (10, 14):1.0, (10, 11):1.0, (11, 12):1.0, (11, 15):1.0, (12, 16):1.0, (13, 14):1.0, (14, 15):1.0, (15, 16):1.0}

lc2 = [([(1, 2), (1, 5), (2, 3), (2, 6), (3, 4), (3, 7), (4, 8), (5, 6), (5, 9), (6, 7, 3.0), (6, 10, 3.0), (7, 8), (7, 11,3.0), (8, 12), (9, 10), (9, 13), (10, 14), (10, 11, 3.0), (11, 12), (11, 15), (12, 16), (13, 14), (14, 15), (15, 16)],(6.0, 10.0))]

c2 = {(1, 2):1.0, (1, 5):1.0, (2, 3):1.0, (2, 6):1.0, (3, 4):1.0, (3, 7):1.0, (4, 8):1.0, (5, 6):1.0, (5, 9):1.0, (6, 7):3.0, (6, 10):3.0, (7, 8):1.0, (7, 11):3.0, (8, 12):1.0, (9, 10):1.0, (9, 13):1.0, (10, 14):1.0, (10, 11):3.0, (11, 12):1.0, (11, 15):1.0, (12, 16):1.0, (13, 14):1.0, (14, 15):1.0, (15, 16):1.0}

# 関数の定義

# グラフを描画（gはエッジ情報)
def DrawGraph(g):
    global node

    GX = nx.Graph()
    GX.add_nodes_from(node)
    GX.add_edges_from(g)
    plt.figure(figsize=(11.69, 8.27))
    nx.draw(GX, pos, with_labels=True, node_size=800, node_color="w", width=2.0, linewidth=2)
    plt.show()

# 指定した複数のグラフを表示
def DrawNGraphMin(path, n):
    i = 0
    for p in path.min_iter():
            DrawGraph(p)
            i = i + 1
            if(i==n):
                    break

# コスト計算
def CalcCost(path, w):
    cost = 0.0
    for e in path:
            cost = cost + w[e]
    return cost



DrawGraph(edge)

# GraphillionへExport
GraphSet.set_universe(edge)

# パスマッチング計算
start = 1
goal = 16

zero_or_two = range(0, 3, 2)

dc = {}

for v in node:
    dc[v] = zero_or_two
dc[start] = 1
dc[goal] = 1

paths = GraphSet.paths(start, goal)
print('paths size', len(paths))

pathx = GraphSet.graphs(vertex_groups=[[start, goal]],degree_constraints=dc, no_loop=True)
print('pathx size', len(pathx))

# 通常のパスマッチング
pathA = GraphSet.graphs(vertex_groups=[[start, goal]],degree_constraints=dc, no_loop=True, linear_constraints=lc1)

print('pathA size', len(pathA))

# 別のコストでパスマッチングを計算
pathB = GraphSet.graphs(vertex_groups=[[start, goal]], degree_constraints=dc, no_loop=True, linear_constraints=lc2)

print('pathB size', len(pathB))

i=0
for p in pathA.min_iter(c1):
    DrawGraph(p)
    cost = CalcCost(p, c1)
    print('Graph1-',i,'=',cost)
    i = i + 1
    if(i==10):
            break

i = 0
for p in pathB.min_iter(c2):
    DrawGraph(p)
    cost = CalcCost(p, c2)
    print('Graph2-',i,'=',cost)
    i = i + 1
    if(i==10):
            break

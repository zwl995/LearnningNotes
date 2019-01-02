# Ambiguous Datasets Reconstruction compare

## 1. Statistics
|  Dataset  | Images | COLMAP(Images) |   Ours(Images)  |   Baseline(Images) |  Ours-vg(Images) |
| :-------- | :----- |     :----:     |      :----:     |        :----       |      :----       |
|   Books   |   21   |       21       |         21      |                    |        21        |
|  Cereal   |   25   |       25       |      failure    |          -         |        25        |
|    Cup    |   64   |       64       |        46       |                    |        7         |
|   Desk    |   31   |       31       |        31       |                    |        31        |
|    fc     |   150  |       150      |        7        |                    |        -         |
|  Indoor   |   153  |       152      |        147      |                    |        -         |
|   oats    |   24   |       24       |        23       |          -         |        24        |
|  Street   |   19   |       19       |        18       |         19         |        19        |

## 2. Visualization Comparison

**ConMatch(Baseline)** 

From top to bottom are repectively ```Cup```, ```Books```, ```Desk```, ```fc```, ```Indoor```, ```Street``` dataset.

<div style=center>

![con_match](compare/gt.jpeg)

![gt_street](compare/gt_failure.jpeg)

</div>

**COLMAP**
- Books

![colmap_books](compare/books/books_colmap.png)

- Cup

![colmap_cup](compare/cup/cup_colmap.png)

- Desk

![colmap_cup](compare/desk/desk_colmap.png)

- fc

![colmap_fc](compare/fc/fc_colmap.png)

- Indoor

![colmap_indoor](compare/indoor/indoor_colmap.png)

- Street

![colmap_street](compare/street/street_colmap.png)

**OpenMVG**

- Books

![openmvg_books](compare/books/books_openmvg.png)

**Viewing Graph**
![vg_books](compare/books/geometric_matches.svg)

- Cereal

**Viewing Graph**
![vg_cereal](compare/cereal/geometric_matches.svg)

- Cup

![openmvg_cup](compare/cup/cup_openmvg.png)

**Viewing Graph**
![vg_cup](compare/cup/geometric_matches.svg)

- Desk

![openmvg_desk](compare/desk/desk_openmvg.png)

**Viewing Graph**
![vg_desk](compare/desk/geometric_matches.svg)

- fc

![openmvg_fc](compare/fc/fc_openmvg.png)

**Viewing Graph**
![vg_fcs](compare/fc/geometric_matches.svg)

- Indoor

![openmvg_indoor](compare/indoor/indoor_openmvg.png)

**Viewing Graph**
![vg_indoor](compare/indoor/geometric_matches.svg)

- Oats

**Viewing Graph**
![vg_boats](compare/oats/geometric_matches.svg)

- Street

![openmvg_street](compare/street/street_openmvg.png)

**Viewing Graph**
![vg_street](compare/street/geometric_matches.svg)

**Ours(with viewing graph)**
- Books

![ours_vg_books](compare/books/books_ours_vg.png)

**MST**
![](compare/books/online_mst_graph.svg)

**Triplet Expansion**
![](compare/books/triplet_expansion_graph.svg)

**Graph Reinforcement**
![](compare/books/graph_reinforcement_graph.svg)

- Cereal

![ours_vg_cereal](compare/cereal/cereal_ours_vg.png)

**MST**
![](compare/cereal/online_mst_graph.svg)

**Triplet Expansion**
![](compare/cereal/triplet_expansion_graph.svg)

**Graph Reinforcement**
![](compare/cereal/graph_reinforcement_graph.svg)

- Desk

![ours_vg_desk](compare/desk/desk_ours_vg.png)

**MST**
![](compare/Desk/online_mst_graph.svg)

**Triplet Expansion**
![](compare/Desk/triplet_expansion_graph.svg)

**Graph Reinforcement**
![](compare/Desk/graph_reinforcement_graph.svg)


- Oats

![ours_vg_oats](compare/oats/oats_ours_vg.png)

**MST**
![](compare/oats/online_mst_graph.svg)

**Triplet Expansion**
![](compare/oats/triplet_expansion_graph.svg)

**Graph Reinforcement**
![](compare/oats/graph_reinforcement_graph.svg)

- Street

![ours_vg_street](compare/street/street_ours_vg.png)

**MST**
![](compare/street/online_mst_graph.svg)

**Triplet Expansion**
![](compare/street/triplet_expansion_graph.svg)

**Graph Reinforcement**
![](compare/street/graph_reinforcement_graph.svg)



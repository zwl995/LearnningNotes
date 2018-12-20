# Ambiguous Datasets Reconstruction compare

## 1. Statistics
|  Dataset  | Images | COLMAP(Images) | OpenMVG(Images) |   ConMatch(Images) |
| :-------- | :----- |     :----:     |      :----:     |        :----       |
|   Books   |   21   |       21       |         21      |                    |
|  Cereal   |   25   |       25       |      failure    |          -         |
|    Cup    |   64   |       64       |        46       |                    |
|   Desk    |   31   |       31       |        31       |                    |
|    fc     |   150  |       150      |        7        |                    |
|  Indoor   |   153  |       152      |        147      |                    |
|   oats    |   24   |       24       |        23       |          -         |
|  Street   |   19   |       19       |        18       |         19         |

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

- Cup

![openmvg_cup](compare/cup/cup_openmvg.png)

- Desk

![openmvg_desk](compare/desk/desk_openmvg.png)

- fc

![openmvg_fc](compare/fc/fc_openmvg.png)

- Indoor

![openmvg_indoor](compare/indoor/indoor_openmvg.png)

- Street

![openmvg_street](compare/street/street_openmvg.png)



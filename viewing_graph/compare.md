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

**Vocabulary Tree VS Fisher Vector**
|  Dataset  | Images | Vocabulary Tree |   Fisher Vector (cosine)  |   Baseline(Images) |  Ours-vg(Images) |


<table>
    <caption>Vocabulary Tree VS Fisher Vector</caption>
    <tr>
        <th rowspan="2">Dataset</th>
        <th rowspan="2">Images</th>
        <th colspan="4">Vocabulary Tree</th>
        <th colspan="4">Fisher Vector (cosine)</th>
    </tr>
    <tr>
        <th>Cam</th>
        <th>Tried Matches</th>
        <th>Passed Pairs</th>
        <th>Final Matches</th>
        <th>Cam</th>
        <th>Tried Matches</th>
        <th>Passed Pairs</th>
        <th>Final Matches</th>
    </tr>
    <tr>
        <td>Books</td>
        <td>21</td>
        <td>14</td>
        <td>19</td>
        <td>19</td>
        <td>8513</td>
        <td>16</td>
        <td>23</td>
        <td>19</td>
        <td>3642</td>
    </tr>
    <tr>
        <td>Cereal</td>
        <td>25</td>
        <td>8</td>
        <td>21</td>
        <td>21</td>
        <td>10370</td>
        <td>17</td>
        <td>24</td>
        <td>21</td>
        <td>4323</td>
    </tr>
    <tr>
        <td>Cup</td>
        <td>64</td>
        <td>10</td>
        <td>64</td>
        <td>62</td>
        <td>12773</td>
        <td>4</td>
        <td>104</td>
        <td>58</td>
        <td>4890</td>
    </tr>
    <tr>
        <td>Desk</td>
        <td>31</td>
        <td>12</td>
        <td>29</td>
        <td>28</td>
        <td>16160</td>
        <td>17</td>
        <td>48</td>
        <td>27</td>
        <td>8409</td>
    </tr>
    <tr>
        <td>Forbiden city</td>
        <td>150</td>
        <td>13</td>
        <td>149</td>
        <td>139</td>
        <td>22456</td>
        <td>5</td>
        <td>715</td>
        <td>126</td>
        <td>7989</td>
    </tr>
    <tr>
        <td>Indoor</td>
        <td>153</td>
        <td>15</td>
        <td>150</td>
        <td>143</td>
        <td>53974</td>
        <td>2</td>
        <td>481</td>
        <td>129</td>
        <td>16864</td>
    </tr>
    <tr>
        <td>oats</td>
        <td>24</td>
        <td>11</td>
        <td>22</td>
        <td>22</td>
        <td>9347</td>
        <td>14</td>
        <td>26</td>
        <td>22</td>
        <td>3378</td>
    </tr>
    <tr>
        <td>Street</td>
        <td>19</td>
        <td>5</td>
        <td>20</td>
        <td>18</td>
        <td>3901</td>
        <td>9</td>
        <td>22</td>
        <td>17</td>
        <td>2007</td>
    </tr>
</table>

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

![](compare/desk/online_mst_graph.svg)

**Triplet Expansion**

![](compare/desk/triplet_expansion_graph.svg)

**Graph Reinforcement**

![](compare/desk/graph_reinforcement_graph.svg)

- fc

**Triplet Expansion**

![](compare/fc/triplet_expansion_graph.svg)

**Graph Reinforcement**

![](compare/fc/graph_reinforcement_graph.svg)

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



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

### **Vocabulary Tree VS Fisher Vector**

**N_tm**: number of tried matches

**N_pp**: number of passed geometric verification

**N_fm**: number of final correspondences

- ***Only tested at MST Building Stage!***
<table>
    <tr>
        <th rowspan="2" colspan="2">Dataset</th>
        <th rowspan="2">Images</th>
        <th colspan="3">Vocabulary Tree</th>
        <th colspan="3">Fisher Vector (cosine)</th>
        <th colspan="3">Fisher Vector (L2-norm)</th>
        <th colspan="3">Fisher Vector (dot-product)</th>
    </tr>
    <tr>
        <th>Cam</th>
        <th>N_tm/N_pp</th>
        <th>N_fm</th>
        <th>Cam</th>
        <th>N_tm/N_pp</th>
        <th>N_fm</th>
        <th>Cam</th>
        <th>N_tm/N_pp</th>
        <th>N_fm</th>
        <th>Cam</th>
        <th>N_tm/N_pp</th>
        <th>N_fm</th>
    </tr>
    <tr>
        <td rowspan="9">Ambiguous Datasets</td>
    </tr>
    <tr>
        <td>Books</td>
        <td>21</td>
        <td>14</td>
        <td><b>19/19</b></td>
        <td><b>8513</b></td>
        <td> <b>20</b> </td>
        <td><b>19/19</b></td>
        <td>5469</td>
        <td>15</td>
        <td>20/19</td>
        <td>5652</td>
        <td>19</td>
        <td>20/19</td>
        <td>6625</td>
    </tr>
    <tr>
        <td>Cereal</td>
        <td>25</td>
        <td>8</td>
        <td><b>21/21</b></td>
        <td><b>10370</b></td>
        <td><b>17</b></td>
        <td>32/23</td>
        <td>6150</td>        
        <td>16</td>
        <td>24/22</td>
        <td>3602</td>
        <td>13</td>
        <td>28/23</td>
        <td>3162</td>
    </tr>
    <tr>
        <td>Cup</td>
        <td>64</td>
        <td><b>10</b></td>
        <td><b>64/62</b></td>
        <td><b>12773</b></td>
        <td>3</td>
        <td>96/56</td>
        <td>4041</td>
        <td>2</td>
        <td>96/56</td>
        <td>4041</td>
        <td>2</td>
        <td>115/58</td>
        <td>4072</td>
    </tr>
    <tr>
        <td>Desk</td>
        <td>31</td>
        <td><b>12</b></td>
        <td><b>29/28</b></td>
        <td><b>16160</b></td>
        <td>5</td>
        <td>42/27</td>
        <td>6510</td>
        <td>6</td>
        <td>40/27</td>
        <td>7046</td>
        <td>2</td>
        <td>50/28</td>
        <td>7229</td>
    </tr>
    <tr>
        <td>Forbiden city</td>
        <td>150</td>
        <td><b>13</b></td>
        <td><b>149/139</b></td>
        <td><b>22456</b></td>
        <td>8</td>
        <td>601/124</td>
        <td>8268</td>
        <td>2</td>
        <td>601/125</td>
        <td>9013</td>
        <td>2</td>
        <td>573/125</td>
        <td>8150</td>
    </tr>
    <tr>
        <td>Indoor</td>
        <td>153</td>
        <td><b>15</b></td>
        <td><b>150/143</b></td>
        <td><b>53974</b></td>
        <td>4</td>
        <td>491/128</td>
        <td>13813</td>
        <td>6</td>
        <td>457/127</td>
        <td>15884</td>
        <td>2</td>
        <td>504/134</td>
        <td>14018</td>
    </tr>
    <tr>
        <td>oats</td>
        <td>24</td>
        <td>11</td>
        <td><b>22/22</b></td>
        <td><b>9347</b></td>
        <td>16</td>
        <td>24/22</td>
        <td>3840</td>
        <td><b>19</b></td>
        <td>22/22</td>
        <td>4224</td>
        <td>15</td>
        <td>30/21</td>
        <td>4286</td>
    </tr>
    <tr>
        <td>Street</td>
        <td>19</td>
        <td>5</td>
        <td><b>20/18</b></td>
        <td><b>3901</b></td>
        <td>2</td>
        <td>21/17</td>
        <td>1958</td>
        <td><b>8</b></td>
        <td>28/17</td>
        <td>1785</td>
        <td>3</td>
        <td>20/17</td>
        <td>2315</td>
    </tr>
    <tr>
        <td rowspan="6">COLMAP Dataset</td>
    </tr>
    <tr>
        <td>Gerrard Hall</td>
        <td>100</td>
        <td>20</td>
        <td><b>116/92</b></td>
        <td><b>1073104</b></td>
        <td><b>27</b></td>
        <td>400/81</td>
        <td>343626</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Person Hall</td>
        <td>330</td>
        <td>18</td>
        <td>299/279</td>
        <td>4056988</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>South Building</td>
        <td>128</td>
        <td><b>24</b></td>
        <td><b>119/117</b></td>
        <td><b>483379</b></td>
        <td>4</td>
        <td>435/106</td>
        <td>151727</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Graham Hall - Exterior</td>
        <td>562</td>
        <td>15</td>
        <td>482/461</td>
        <td>3677348</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
    <tr>
        <td>Graham Hall - Interior</td>
        <td>711</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>12</td>
        <td>7187/466</td>
        <td>128462</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
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



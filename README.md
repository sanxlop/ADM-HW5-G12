# Homework 5 - Visit the Wikipedia hyperlinks graph!
# [NBVIEWER HW5](https://nbviewer.jupyter.org/github/sanxlop/ADM-HW5-G12/blob/master/Homework_5.ipynb)

----

## Description

In this assignment we perform an analysis of the Wikipedia Hyperlink graph. In particular, given extra information about the categories to which an article belongs to, we are curious to rank the articles according to some criteria. For this purpose we use the Wikipedia graph released by the SNAP group.

### · Import libraries

### · Reading data

 We are reading all files given:

    1. Reading reduced edges file with pandas
    2. Reading and proccessing page names file with 'read_names_list' function
    3. Reading and proccessing categories file with 'read_categories_list' function. 
    We are taking only categories with more than 3500 nodes (articles) and only nodes 
    included in the reduced edges file.

### · [RQ1] Build the graph

 In this RQ we are going to build the graph G=(V, E), where V is the set of articles and E the hyperlinks among them. For this RQ we are using networkx library following this steps:

    1. Create directed graph and insert nodes and edges
    2. Evaluating resulting graph using 'nx.info' and 'nx.density'
    3. Analyze results
 
### · [RQ2] Block Ranking and Node Ranking

In this RQ we are going to test the different algorithm methods created to compute shortest path and use the most efficient to compute block ranking and node ranking.

 2.0. Test speed and reliability of ShortestPath algorithms [THIS PART IS NOT ASKED]

    1. Test 1 (using networkX algorithm=
    2. Test 2 (using own implementation algorithm)
    3. Test 3 (using other own implementation algorithm)
    4. Testing results analtysis

 2.1. Building Block_Ranking

    Build block ranking using our own implementation of shortest path algorithm based in test 2. 
    We are going to compare 50 nodes of C0 with all nodes in CI to build the block ranking. 
    With our algorithm it will take approximately 27 hours to compute for all nodes.

 2.2. Ranking nodes of each category

    1. Adding attribute information of weight to all nodes to 0
    2. Computing steps 1, 2 and 3 defined in the instructions
    3. Print the results obtained.

----

## Files

1. __`Homework_5.ipynb`__:
      > A Jupyter notebook which provides the code of the and steps of the reading data, processing data, testing algorithms, building block ranking, rank nodes of each category.
      
2. __`libgraph.py`__:
      > A python script which provides all the functions used in the `Homework_5.ipynb` notebook. 
      
       

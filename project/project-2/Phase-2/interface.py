from neo4j import GraphDatabase

class Interface:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)
        self._driver.verify_connectivity()

    def close(self):
        self._driver.close()

    def bfs(self, start_node, last_node):
        # TODO: Implement this method
        # raise NotImplementedError

        is_exist = '''
                RETURN gds.graph.exists('myGraph_bfs')
                '''
        drop_graph = '''
                CALL gds.graph.drop('myGraph_bfs')
                '''

        with self._driver.session() as session:
            res = session.run(is_exist).data()
            # print(res)
            # print(res[0]["gds.graph.exists('myGraph')"])
            if(res[0]["gds.graph.exists('myGraph_bfs')"]):
                session.run(drop_graph)       

        creat_project_query = '''
                CALL gds.graph.project('myGraph_bfs','Location','TRIP',{relationshipProperties: 'distance'})
                '''
        calc_bfs = f'''
            MATCH (start:Location {{name: {start_node}}}), (end:Location {{name: {last_node}}})
            WITH id(start) AS source, id(end) AS targetNodes
            CALL gds.bfs.stream('myGraph_bfs', {{
            sourceNode: source,
            targetNodes: targetNodes
            }})
            YIELD path
            RETURN path
            '''
        with self._driver.session() as session:
            session.run(creat_project_query)
            result = session.run(calc_bfs).data()
            # print(result)
            return result
        


    def pagerank(self, max_iterations, weight_property):
        # TODO: Implement this method
        # raise NotImplementedError
        is_exist = '''
                RETURN gds.graph.exists('myGraph')
                '''
        drop_graph = '''
                CALL gds.graph.drop('myGraph')
                '''

        with self._driver.session() as session:
            res = session.run(is_exist).data()
            # print(res)
            # print(res[0]["gds.graph.exists('myGraph')"])
            if(res[0]["gds.graph.exists('myGraph')"]):
                session.run(drop_graph)

        creat_project_query = f'''
            CALL gds.graph.project('myGraph','Location','TRIP',{{relationshipProperties: '{weight_property}'}})
            '''
        
        calc_pagerank_max = f'''
        CALL gds.pageRank.stream('myGraph', {{maxIterations: {max_iterations}, relationshipWeightProperty: '{weight_property}'}})
        YIELD nodeId, score
        RETURN gds.util.asNode(nodeId).name AS name, score
        ORDER BY score DESC LIMIT 1
        '''

        calc_pagerank_min = f'''
        CALL gds.pageRank.stream('myGraph', {{maxIterations: {max_iterations}, relationshipWeightProperty: '{weight_property}'}})
        YIELD nodeId, score
        RETURN gds.util.asNode(nodeId).name AS name, score
        ORDER BY score ASC LIMIT 1
        '''
        result= []
        with self._driver.session() as session:
            session.run(creat_project_query).data()
            max = session.run(calc_pagerank_max).data()
            min = session.run(calc_pagerank_min).data()
            result.append(max[0])
            result.append(min[0])
            return result

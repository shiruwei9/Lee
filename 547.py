class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = set()

        def dfs(cityI):
            #cityIConnections is a row in isConnected, which contains the city i's connections
            cityIConnections = isConnected[cityI]
            visited.add(cityI) #add cityI to seen, so we won't dfs it again (because we called it just now!)
            #we want to take all 1's in cityIConnections to put together into a province
            for cityJ in range(N):
                #check cityJ's connections first before finishing cityI's connections
                if (cityJ not in visited) and (cityIConnections[cityJ] == 1) and (cityI != cityJ):
                    dfs(cityJ)
            #we're done searching cityI's direct connections
            return  
        
        numProvinces = 0
        for cityI in range(N):
            #each entire dfs recursion set is going to be one province
            if cityI not in visited:
                dfs(cityI)
                numProvinces += 1
        return numProvinces        
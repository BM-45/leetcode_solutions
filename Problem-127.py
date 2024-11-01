from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while queue:
            current_word, level = queue.popleft()
            if current_word == endWord:
                return level
            
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]
                    if next_word in word_set and next_word not in visited:
                        queue.append((next_word, level + 1))
                        visited.add(next_word)
        
        return 0

""" 
Used dfs here, problem here is it finds optimal path with more time than bfs.
Upgrade the solution to Breadth first search.

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        # Check if two words are present in the set. else return 0
        if endWord not in wordList:
            return 0

        result = self.dfs(beginWord, endWord, 0, [], wordList)

        return 0 if result == math.inf else result + 1

    def dfs(self, beginWord, endWord, level, visited, wordList):
        # Base condition.
        if beginWord == endWord:
            return level
        if beginWord in visited:
            return 0
        result = math.inf 
        for i in range(len(beginWord)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                nextWord = beginWord[:i] + j + beginWord[i+1:]

                #if nextWord is in wordlist and also not visited.
                if (nextWord not in visited) and (nextWord in wordList):
                    visited.append(nextWord)
                    result = min(result, self.dfs(nextWord, endWord, level + 1, visited, wordList))
                    visited.pop()


        return result
"""
"""
In this solution firsts created a graph, and did dfs for it.
Problem with this solution is that creating a graph takes O(n^2) 
So, it was exceeding the time limit.
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        # Create the word graph
        word_graph = self.create_word_graph(wordList + [beginWord])

        if endWord not in word_graph:
            return 0

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])

        while queue:
            current_word, level = queue.popleft()
            if current_word == endWord:
                return level

            for neighbor in word_graph[current_word]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, level + 1))

        return 0

    def create_word_graph(self, words):
        graph = defaultdict(list)
        for word in words:
            graph[word] = []

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.is_one_letter_diff(words[i], words[j]):
                    graph[words[i]].append(words[j])
                    graph[words[j]].append(words[i])

        return graph

    def is_one_letter_diff(self, word1, word2):
        return sum(c1 != c2 for c1, c2 in zip(word1, word2)) == 1

## Example usage
#solution = Solution()
#wordList = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
#result = solution.ladderLength('hit', 'cog', wordList)
#print(f"The shortest transformation sequence length is: {result}")
"""

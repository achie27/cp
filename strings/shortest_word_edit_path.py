def shortestWordEditPath(beginWord, endWord, wordList):
  targetPresent = False
  for word in wordList:
      if word == endWord: targetPresent = True

  if not targetPresent: return -1

  if beginWord == endWord: return -1

  queue = [[beginWord, 0]]
  queuePresenceMap = {}

  while len(queue) > 0:
      head = queue.pop(0)

      if head[0] == endWord:
          return head[1]

      for word in wordList:

          charDiff = 0
          for i in range(len(word)):
              if head[0][i] != word[i]: charDiff += 1

          if charDiff == 1:
              if word not in queuePresenceMap:
                  queue.append([word, head[1] + 1])
                  queuePresenceMap[word] = 1

  return -1

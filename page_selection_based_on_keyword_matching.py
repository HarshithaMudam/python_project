pages = []
queries = []

while True:
    text = [ele.lower() for ele in input().split()]
    if 'e' in text:
        break
    if 'p'in text:
        pages += [text[1:]]
    if 'q' in text:
        queries += [text[1:]]
        
def similarities(query):
    similarity = [[0, i] for i in range(len(pages))]
    for i in range(len(pages)):
        for j in range(len(query)):
            if query[j] in pages[i]:
                index_query = pages[i].index(query[j])
                similarity[i][0] += (8 - index_query) * (8 - j)
    return similarity

for ele in queries:
    list_sims = similarities(ele)
    list_finals = [ele for ele in list_sims if ele[0] != 0]
    list_finals.sort(reverse = True)
    limit = min(5, len(list_finals))
    list_ans = []
    i = 0
    while i < len(list_finals):
        list_working = [(ele[1]) for ele in list_finals 
        if ele[0] == list_finals[i][0]]
        list_working.sort()
        list_ans += list_working
        length = len(list_working)
        if len(list_ans) >= limit:
            break
        i += length
    
    for i in range(limit):
        print(f"P{list_ans[i] + 1}", end = " ")
    
    print()

import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    result = {}
    n = n = len(corpus)

    if len(corpus[page]) == 0:
        for page_name in corpus:
            result[page_name] = 1 / len(corpus)
        return result
    
    static_probability = (1-damping_factor)/n
    link_probability = damping_factor/len(corpus[page])
    for page_name in corpus:
        result[page_name] = static_probability
        if (page_name in corpus[page]):
            result[page_name]+= link_probability

    return result





def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    times_to_node = {}
    #initialize to 0 each node
    for node in corpus:
        times_to_node[node] = 0

    node = random.choice(list(corpus.keys()))
    result = {}

    for _ in range(n):
        transitional = transition_model(corpus, node, damping_factor)
        probabilitys = list(transitional.values())
        pages = list(transitional.keys())

        node = random.choices(pages, weights=probabilitys, k=1)[0]
        times_to_node[node]+=1

    #computes the result of the page ranks for each page in the corpus
    for page in times_to_node:
        result[page] = times_to_node[page]/n
    return result





def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    corpus = corpus.copy()
    n = len(corpus)
    not_linked_probability = (1-damping_factor)/n
    result = {}
    for page in corpus:
        result[page] = 1/n

    #page without conections
    for page in corpus:
        if len(corpus[page]) == 0:
            corpus[page] = set(corpus.keys())

    finish = False
    while not finish:
        new_result = result.copy()
        for page in corpus:
            linked_probability = 0
            for conection in corpus:
                if page in corpus[conection]:
                    linked_probability += new_result[conection]/len(corpus[conection])

            new_result[page] = not_linked_probability + damping_factor*linked_probability
        finish = isFinished(result, new_result)
        result = new_result.copy()

    return result
    

def isFinished(result, new_result):
    for page in result:
        difference = abs(result[page] - new_result[page])
        if difference > 0.001:
            return False
    return True


if __name__ == "__main__":
    main()

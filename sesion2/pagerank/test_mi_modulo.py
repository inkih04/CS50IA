from pagerank import transition_model, iterate_pagerank
import pytest


def test_transition_model():
    corpus = {
        "1.html": {"2.html", "3.html"},
        "2.html": {"3.html"},
        "3.html": {"2.html"}
    }
    page = "1.html"
    damping_factor = 0.85
    result = transition_model(corpus, page, damping_factor)

    # Verificar que las probabilidades sumen aproximadamente 1
    assert pytest.approx(sum(result.values()), 0.01) == 1.0

    # Comprobar valores específicos
    assert pytest.approx(result["1.html"], 0.01) == 0.05
    assert pytest.approx(result["2.html"], 0.01) == 0.475
    assert pytest.approx(result["3.html"], 0.01) == 0.475


def test_iterate_pagerank():
    corpus = {
        "1.html": {"2.html", "3.html"},
        "2.html": {"3.html"},
        "3.html": {"2.html"}
    }
    damping_factor = 0.85
    result = iterate_pagerank(corpus, damping_factor)


    # Comprobar valores específicos
    assert pytest.approx(result["1.html"], 0.01) == 0.05
    assert pytest.approx(result["2.html"], 0.01) == 0.432
    assert pytest.approx(result["3.html"], 0.01) == 0.518



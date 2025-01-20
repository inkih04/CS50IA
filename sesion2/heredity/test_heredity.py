import pytest
from heredity import joint_probability

# Definir las probabilidades del problema
PROBS = {
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },
    "trait": {
        2: {
            True: 0.65,
            False: 0.35
        },
        1: {
            True: 0.56,
            False: 0.44
        },
        0: {
            True: 0.01,
            False: 0.99
        }
    },
    "mutation": 0.01
}

# Definición de la estructura de datos de la familia
people = {
    'Harry': {'name': 'Harry', 'mother': 'Lily', 'father': 'James', 'trait': None},
    'James': {'name': 'James', 'mother': None, 'father': None, 'trait': True},
    'Lily': {'name': 'Lily', 'mother': None, 'father': None, 'trait': False}
}

# Conjuntos de personas con 1 y 2 genes y con el rasgo
one_gene = {"Harry"}
two_genes = {"James"}
have_trait = {"James"}

# Valor esperado basado en el ejemplo explicado
expected_probability = 0.0026643247488

def test_joint_probability():
    """Prueba la función joint_probability con datos de ejemplo."""
    result = joint_probability(people, one_gene, two_genes, have_trait)
    assert pytest.approx(result, rel=1e-9) == expected_probability, f"Resultado esperado: {expected_probability}, pero se obtuvo {result}"

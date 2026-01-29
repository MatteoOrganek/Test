import random


def test_random_seed_reproducibility():
    """Verify that seeding `random` makes generation reproducible."""
    random.seed(12345)
    seq1 = [random.random() for _ in range(5)]
    random.seed(12345)
    seq2 = [random.random() for _ in range(5)]
    assert seq1 == seq2


def test_random_within_range():
    """A simple check that `randint` produces values inside the requested range."""
    random.seed(0)
    for _ in range(10):
        v = random.randint(1, 10)
        assert 1 <= v <= 10

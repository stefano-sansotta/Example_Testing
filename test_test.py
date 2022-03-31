from pytest import approx


def Add(a, b):
    return a + b


def test_Add():
#    assert abs(Add(0.1, 0.2)-0.3) < 0.00000000000000000001
#    assert Add(0.1, 0.2) == approx(0.3)
    assert Add(0.1, 0.2) == 0.3
    assert Add("Star", "wars") == "Starwars"


Number = Add(0.5,0.7)
Example = 0.1

print("sum=%.25f single=%.25f" % (Number,Example))


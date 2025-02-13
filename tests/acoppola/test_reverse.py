import sys 
sys.path.append("packages/mastrogpt/reverse")
import reverse

def test_reverse():
    args = { "input": "Test"}
    res = reverse.reverse(args)
    assert res["output"] == "tseT"

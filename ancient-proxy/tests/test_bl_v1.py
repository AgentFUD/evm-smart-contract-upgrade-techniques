def test_business_logic_v1_works(accounts, bl_v1):
    owner = accounts[0]
    assert bl_v1.getUint() == 0
    bl_v1.setUint(131, {'from': owner})
    assert bl_v1.getUint() == 131

def test_replace_business_logic_works(accounts, bl_v1):
    pass
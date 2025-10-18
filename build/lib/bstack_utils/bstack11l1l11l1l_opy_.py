# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import re
from bstack_utils.bstack1l1lll11l1_opy_ import bstack11ll1111lll_opy_
def bstack11l111l1111_opy_(fixture_name):
    if fixture_name.startswith(bstack11ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬫ")):
        return bstack11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬬ")
    elif fixture_name.startswith(bstack11ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬭ")):
        return bstack11ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳࡭ࡰࡦࡸࡰࡪ࠭ᬮ")
    elif fixture_name.startswith(bstack11ll_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬯ")):
        return bstack11ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬰ")
    elif fixture_name.startswith(bstack11ll_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᬱ")):
        return bstack11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳࡭ࡰࡦࡸࡰࡪ࠭ᬲ")
def bstack11l111lll11_opy_(fixture_name):
    return bool(re.match(bstack11ll_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࠫࡪࡺࡴࡣࡵ࡫ࡲࡲࢁࡳ࡯ࡥࡷ࡯ࡩ࠮ࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᬳ"), fixture_name))
def bstack11l111l1l1l_opy_(fixture_name):
    return bool(re.match(bstack11ll_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰᬴ࠧ"), fixture_name))
def bstack11l111ll1ll_opy_(fixture_name):
    return bool(re.match(bstack11ll_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰ࠧᬵ"), fixture_name))
def bstack11l111ll1l1_opy_(fixture_name):
    if fixture_name.startswith(bstack11ll_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬶ")):
        return bstack11ll_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᬷ"), bstack11ll_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᬸ")
    elif fixture_name.startswith(bstack11ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬹ")):
        return bstack11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬺ"), bstack11ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪᬻ")
    elif fixture_name.startswith(bstack11ll_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬼ")):
        return bstack11ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬽ"), bstack11ll_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᬾ")
    elif fixture_name.startswith(bstack11ll_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬿ")):
        return bstack11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳࡭ࡰࡦࡸࡰࡪ࠭ᭀ"), bstack11ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨᭁ")
    return None, None
def bstack11l111l1ll1_opy_(hook_name):
    if hook_name in [bstack11ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᭂ"), bstack11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᭃ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111l1lll_opy_(hook_name):
    if hook_name in [bstack11ll_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯᭄ࠩ"), bstack11ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᭅ")]:
        return bstack11ll_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᭆ")
    elif hook_name in [bstack11ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᭇ"), bstack11ll_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪᭈ")]:
        return bstack11ll_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪᭉ")
    elif hook_name in [bstack11ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᭊ"), bstack11ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪᭋ")]:
        return bstack11ll_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᭌ")
    elif hook_name in [bstack11ll_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬ᭍"), bstack11ll_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬ᭎")]:
        return bstack11ll_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨ᭏")
    return hook_name
def bstack11l111ll11l_opy_(node, scenario):
    if hasattr(node, bstack11ll_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨ᭐")):
        parts = node.nodeid.rsplit(bstack11ll_opy_ (u"ࠢ࡜ࠤ᭑"))
        params = parts[-1]
        return bstack11ll_opy_ (u"ࠣࡽࢀࠤࡠࢁࡽࠣ᭒").format(scenario.name, params)
    return scenario.name
def bstack11l111l11l1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11ll_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫ᭓")):
            examples = list(node.callspec.params[bstack11ll_opy_ (u"ࠪࡣࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡧࡻࡥࡲࡶ࡬ࡦࠩ᭔")].values())
        return examples
    except:
        return []
def bstack11l111l111l_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111ll111_opy_(report):
    try:
        status = bstack11ll_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᭕")
        if report.passed or (report.failed and hasattr(report, bstack11ll_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢ᭖"))):
            status = bstack11ll_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭᭗")
        elif report.skipped:
            status = bstack11ll_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ᭘")
        bstack11ll1111lll_opy_(status)
    except:
        pass
def bstack11ll1l11l_opy_(status):
    try:
        bstack11l111l11ll_opy_ = bstack11ll_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᭙")
        if status == bstack11ll_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ᭚"):
            bstack11l111l11ll_opy_ = bstack11ll_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ᭛")
        elif status == bstack11ll_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ᭜"):
            bstack11l111l11ll_opy_ = bstack11ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭᭝")
        bstack11ll1111lll_opy_(bstack11l111l11ll_opy_)
    except:
        pass
def bstack11l111l1l11_opy_(item=None, report=None, summary=None, extra=None):
    return
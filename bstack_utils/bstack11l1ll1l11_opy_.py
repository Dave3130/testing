# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import re
from bstack_utils.bstack1l11111ll1_opy_ import bstack11ll111ll1l_opy_
def bstack11l11l11l1l_opy_(fixture_name):
    if fixture_name.startswith(bstack111111l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᫼")):
        return bstack111111l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨ᫽")
    elif fixture_name.startswith(bstack111111l_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᫾")):
        return bstack111111l_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮࡯ࡲࡨࡺࡲࡥࠨ᫿")
    elif fixture_name.startswith(bstack111111l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᬀ")):
        return bstack111111l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬁ")
    elif fixture_name.startswith(bstack111111l_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬂ")):
        return bstack111111l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮࡯ࡲࡨࡺࡲࡥࠨᬃ")
def bstack11l11l111l1_opy_(fixture_name):
    return bool(re.match(bstack111111l_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣ࠭࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࡼ࡮ࡱࡧࡹࡱ࡫ࠩࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᬄ"), fixture_name))
def bstack11l111ll1ll_opy_(fixture_name):
    return bool(re.match(bstack111111l_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᬅ"), fixture_name))
def bstack11l11l1111l_opy_(fixture_name):
    return bool(re.match(bstack111111l_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥࡣ࡭ࡣࡶࡷࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᬆ"), fixture_name))
def bstack11l111lllll_opy_(fixture_name):
    if fixture_name.startswith(bstack111111l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬇ")):
        return bstack111111l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬈ"), bstack111111l_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᬉ")
    elif fixture_name.startswith(bstack111111l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬊ")):
        return bstack111111l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳࡭ࡰࡦࡸࡰࡪ࠭ᬋ"), bstack111111l_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡃࡏࡐࠬᬌ")
    elif fixture_name.startswith(bstack111111l_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬍ")):
        return bstack111111l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᬎ"), bstack111111l_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᬏ")
    elif fixture_name.startswith(bstack111111l_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᬐ")):
        return bstack111111l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮࡯ࡲࡨࡺࡲࡥࠨᬑ"), bstack111111l_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪᬒ")
    return None, None
def bstack11l11l11111_opy_(hook_name):
    if hook_name in [bstack111111l_opy_ (u"ࠨࡵࡨࡸࡺࡶࠧᬓ"), bstack111111l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࠫᬔ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l11l111ll_opy_(hook_name):
    if hook_name in [bstack111111l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᬕ"), bstack111111l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡪࡺࡨࡰࡦࠪᬖ")]:
        return bstack111111l_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡋࡁࡄࡊࠪᬗ")
    elif hook_name in [bstack111111l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࠬᬘ"), bstack111111l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡣ࡭ࡣࡶࡷࠬᬙ")]:
        return bstack111111l_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡃࡏࡐࠬᬚ")
    elif hook_name in [bstack111111l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬛ"), bstack111111l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳࡥࡵࡪࡲࡨࠬᬜ")]:
        return bstack111111l_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡉࡆࡉࡈࠨᬝ")
    elif hook_name in [bstack111111l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡱࡧࡹࡱ࡫ࠧᬞ"), bstack111111l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡥ࡯ࡥࡸࡹࠧᬟ")]:
        return bstack111111l_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡁࡍࡎࠪᬠ")
    return hook_name
def bstack11l11l11ll1_opy_(node, scenario):
    if hasattr(node, bstack111111l_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᬡ")):
        parts = node.nodeid.rsplit(bstack111111l_opy_ (u"ࠤ࡞ࠦᬢ"))
        params = parts[-1]
        return bstack111111l_opy_ (u"ࠥࡿࢂ࡛ࠦࡼࡿࠥᬣ").format(scenario.name, params)
    return scenario.name
def bstack11l11l11l11_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack111111l_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭ᬤ")):
            examples = list(node.callspec.params[bstack111111l_opy_ (u"ࠬࡥࡰࡺࡶࡨࡷࡹࡥࡢࡥࡦࡢࡩࡽࡧ࡭ࡱ࡮ࡨࠫᬥ")].values())
        return examples
    except:
        return []
def bstack11l111ll1l1_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111llll1_opy_(report):
    try:
        status = bstack111111l_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᬦ")
        if report.passed or (report.failed and hasattr(report, bstack111111l_opy_ (u"ࠢࡸࡣࡶࡼ࡫ࡧࡩ࡭ࠤᬧ"))):
            status = bstack111111l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᬨ")
        elif report.skipped:
            status = bstack111111l_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᬩ")
        bstack11ll111ll1l_opy_(status)
    except:
        pass
def bstack111l1111l1_opy_(status):
    try:
        bstack11l111lll11_opy_ = bstack111111l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᬪ")
        if status == bstack111111l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᬫ"):
            bstack11l111lll11_opy_ = bstack111111l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᬬ")
        elif status == bstack111111l_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᬭ"):
            bstack11l111lll11_opy_ = bstack111111l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᬮ")
        bstack11ll111ll1l_opy_(bstack11l111lll11_opy_)
    except:
        pass
def bstack11l111lll1l_opy_(item=None, report=None, summary=None, extra=None):
    return
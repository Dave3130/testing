# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import re
from bstack_utils.bstack11ll1l1l1l_opy_ import bstack11ll11l111l_opy_
def bstack11l111ll1l1_opy_(fixture_name):
    if fixture_name.startswith(bstack1ll1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬁ")):
        return bstack1ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬂ")
    elif fixture_name.startswith(bstack1ll1l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬃ")):
        return bstack1ll1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳࡭ࡰࡦࡸࡰࡪ࠭ᬄ")
    elif fixture_name.startswith(bstack1ll1l_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬅ")):
        return bstack1ll1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬆ")
    elif fixture_name.startswith(bstack1ll1l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᬇ")):
        return bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳࡭ࡰࡦࡸࡰࡪ࠭ᬈ")
def bstack11l111lll1l_opy_(fixture_name):
    return bool(re.match(bstack1ll1l_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࠫࡪࡺࡴࡣࡵ࡫ࡲࡲࢁࡳ࡯ࡥࡷ࡯ࡩ࠮ࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᬉ"), fixture_name))
def bstack11l11l1111l_opy_(fixture_name):
    return bool(re.match(bstack1ll1l_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰ࠧᬊ"), fixture_name))
def bstack11l11l11ll1_opy_(fixture_name):
    return bool(re.match(bstack1ll1l_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰ࠧᬋ"), fixture_name))
def bstack11l11l111l1_opy_(fixture_name):
    if fixture_name.startswith(bstack1ll1l_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬌ")):
        return bstack1ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᬍ"), bstack1ll1l_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᬎ")
    elif fixture_name.startswith(bstack1ll1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬏ")):
        return bstack1ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬐ"), bstack1ll1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪᬑ")
    elif fixture_name.startswith(bstack1ll1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬒ")):
        return bstack1ll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬓ"), bstack1ll1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᬔ")
    elif fixture_name.startswith(bstack1ll1l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬕ")):
        return bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳࡭ࡰࡦࡸࡰࡪ࠭ᬖ"), bstack1ll1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨᬗ")
    return None, None
def bstack11l111ll1ll_opy_(hook_name):
    if hook_name in [bstack1ll1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᬘ"), bstack1ll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᬙ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l11l111ll_opy_(hook_name):
    if hook_name in [bstack1ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᬚ"), bstack1ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᬛ")]:
        return bstack1ll1l_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᬜ")
    elif hook_name in [bstack1ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᬝ"), bstack1ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪᬞ")]:
        return bstack1ll1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪᬟ")
    elif hook_name in [bstack1ll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᬠ"), bstack1ll1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦࠪᬡ")]:
        return bstack1ll1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᬢ")
    elif hook_name in [bstack1ll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬᬣ"), bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬᬤ")]:
        return bstack1ll1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨᬥ")
    return hook_name
def bstack11l111lllll_opy_(node, scenario):
    if hasattr(node, bstack1ll1l_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨᬦ")):
        parts = node.nodeid.rsplit(bstack1ll1l_opy_ (u"ࠢ࡜ࠤᬧ"))
        params = parts[-1]
        return bstack1ll1l_opy_ (u"ࠣࡽࢀࠤࡠࢁࡽࠣᬨ").format(scenario.name, params)
    return scenario.name
def bstack11l11l11111_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1ll1l_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫᬩ")):
            examples = list(node.callspec.params[bstack1ll1l_opy_ (u"ࠪࡣࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡧࡻࡥࡲࡶ࡬ࡦࠩᬪ")].values())
        return examples
    except:
        return []
def bstack11l11l11l11_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111llll1_opy_(report):
    try:
        status = bstack1ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᬫ")
        if report.passed or (report.failed and hasattr(report, bstack1ll1l_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢᬬ"))):
            status = bstack1ll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᬭ")
        elif report.skipped:
            status = bstack1ll1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᬮ")
        bstack11ll11l111l_opy_(status)
    except:
        pass
def bstack11lll1lll1_opy_(status):
    try:
        bstack11l11l11l1l_opy_ = bstack1ll1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨᬯ")
        if status == bstack1ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᬰ"):
            bstack11l11l11l1l_opy_ = bstack1ll1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᬱ")
        elif status == bstack1ll1l_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᬲ"):
            bstack11l11l11l1l_opy_ = bstack1ll1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᬳ")
        bstack11ll11l111l_opy_(bstack11l11l11l1l_opy_)
    except:
        pass
def bstack11l111lll11_opy_(item=None, report=None, summary=None, extra=None):
    return
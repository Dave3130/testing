# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import re
from bstack_utils.bstack11l11ll11_opy_ import bstack11ll11l111l_opy_
def bstack11l11l11111_opy_(fixture_name):
    if fixture_name.startswith(bstack1l_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬉ")):
        return bstack1l_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᬊ")
    elif fixture_name.startswith(bstack1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬋ")):
        return bstack1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧᬌ")
    elif fixture_name.startswith(bstack1l_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬍ")):
        return bstack1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᬎ")
    elif fixture_name.startswith(bstack1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬏ")):
        return bstack1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭࡮ࡱࡧࡹࡱ࡫ࠧᬐ")
def bstack11l111llll1_opy_(fixture_name):
    return bool(re.match(bstack1l_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࠬ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࢂ࡭ࡰࡦࡸࡰࡪ࠯࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠ࠰࠭ࠫᬑ"), fixture_name))
def bstack11l11l11lll_opy_(fixture_name):
    return bool(re.match(bstack1l_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᬒ"), fixture_name))
def bstack11l11l11ll1_opy_(fixture_name):
    return bool(re.match(bstack1l_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᬓ"), fixture_name))
def bstack11l11l1111l_opy_(fixture_name):
    if fixture_name.startswith(bstack1l_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬔ")):
        return bstack1l_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬕ"), bstack1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᬖ")
    elif fixture_name.startswith(bstack1l_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬗ")):
        return bstack1l_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬘ"), bstack1l_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡂࡎࡏࠫᬙ")
    elif fixture_name.startswith(bstack1l_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬚ")):
        return bstack1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬛ"), bstack1l_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧᬜ")
    elif fixture_name.startswith(bstack1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬝ")):
        return bstack1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭࡮ࡱࡧࡹࡱ࡫ࠧᬞ"), bstack1l_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩᬟ")
    return None, None
def bstack11l11l111l1_opy_(hook_name):
    if hook_name in [bstack1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᬠ"), bstack1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪᬡ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111lll11_opy_(hook_name):
    if hook_name in [bstack1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᬢ"), bstack1l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩᬣ")]:
        return bstack1l_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᬤ")
    elif hook_name in [bstack1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᬥ"), bstack1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫᬦ")]:
        return bstack1l_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡂࡎࡏࠫᬧ")
    elif hook_name in [bstack1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬨ"), bstack1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫᬩ")]:
        return bstack1l_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧᬪ")
    elif hook_name in [bstack1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭ᬫ"), bstack1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭ᬬ")]:
        return bstack1l_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩᬭ")
    return hook_name
def bstack11l11l11l11_opy_(node, scenario):
    if hasattr(node, bstack1l_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩᬮ")):
        parts = node.nodeid.rsplit(bstack1l_opy_ (u"ࠣ࡝ࠥᬯ"))
        params = parts[-1]
        return bstack1l_opy_ (u"ࠤࡾࢁࠥࡡࡻࡾࠤᬰ").format(scenario.name, params)
    return scenario.name
def bstack11l11l11l1l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1l_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬᬱ")):
            examples = list(node.callspec.params[bstack1l_opy_ (u"ࠫࡤࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡨࡼࡦࡳࡰ࡭ࡧࠪᬲ")].values())
        return examples
    except:
        return []
def bstack11l111lllll_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l11l111ll_opy_(report):
    try:
        status = bstack1l_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᬳ")
        if report.passed or (report.failed and hasattr(report, bstack1l_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬᬴ࠣ"))):
            status = bstack1l_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᬵ")
        elif report.skipped:
            status = bstack1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᬶ")
        bstack11ll11l111l_opy_(status)
    except:
        pass
def bstack1ll1111lll_opy_(status):
    try:
        bstack11l111lll1l_opy_ = bstack1l_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᬷ")
        if status == bstack1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᬸ"):
            bstack11l111lll1l_opy_ = bstack1l_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᬹ")
        elif status == bstack1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᬺ"):
            bstack11l111lll1l_opy_ = bstack1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᬻ")
        bstack11ll11l111l_opy_(bstack11l111lll1l_opy_)
    except:
        pass
def bstack11l11l1l111_opy_(item=None, report=None, summary=None, extra=None):
    return
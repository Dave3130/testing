# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import re
from bstack_utils.bstack1l111l11ll_opy_ import bstack11ll111ll1l_opy_
def bstack11l111llll1_opy_(fixture_name):
    if fixture_name.startswith(bstack1l1lll1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬂ")):
        return bstack1l1lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᬃ")
    elif fixture_name.startswith(bstack1l1lll1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬄ")):
        return bstack1l1lll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧᬅ")
    elif fixture_name.startswith(bstack1l1lll1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬆ")):
        return bstack1l1lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᬇ")
    elif fixture_name.startswith(bstack1l1lll1_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬈ")):
        return bstack1l1lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭࡮ࡱࡧࡹࡱ࡫ࠧᬉ")
def bstack11l11l11l1l_opy_(fixture_name):
    return bool(re.match(bstack1l1lll1_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࠬ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࢂ࡭ࡰࡦࡸࡰࡪ࠯࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠ࠰࠭ࠫᬊ"), fixture_name))
def bstack11l11l1111l_opy_(fixture_name):
    return bool(re.match(bstack1l1lll1_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᬋ"), fixture_name))
def bstack11l111lll1l_opy_(fixture_name):
    return bool(re.match(bstack1l1lll1_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤࡩ࡬ࡢࡵࡶࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᬌ"), fixture_name))
def bstack11l111ll1l1_opy_(fixture_name):
    if fixture_name.startswith(bstack1l1lll1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬍ")):
        return bstack1l1lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬎ"), bstack1l1lll1_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᬏ")
    elif fixture_name.startswith(bstack1l1lll1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬐ")):
        return bstack1l1lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬑ"), bstack1l1lll1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡂࡎࡏࠫᬒ")
    elif fixture_name.startswith(bstack1l1lll1_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬓ")):
        return bstack1l1lll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬔ"), bstack1l1lll1_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧᬕ")
    elif fixture_name.startswith(bstack1l1lll1_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬖ")):
        return bstack1l1lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭࡮ࡱࡧࡹࡱ࡫ࠧᬗ"), bstack1l1lll1_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩᬘ")
    return None, None
def bstack11l111ll11l_opy_(hook_name):
    if hook_name in [bstack1l1lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠭ᬙ"), bstack1l1lll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࠪᬚ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l11l111l1_opy_(hook_name):
    if hook_name in [bstack1l1lll1_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᬛ"), bstack1l1lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡩࡹ࡮࡯ࡥࠩᬜ")]:
        return bstack1l1lll1_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡊࡇࡃࡉࠩᬝ")
    elif hook_name in [bstack1l1lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࠫᬞ"), bstack1l1lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡩ࡬ࡢࡵࡶࠫᬟ")]:
        return bstack1l1lll1_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡂࡎࡏࠫᬠ")
    elif hook_name in [bstack1l1lll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬡ"), bstack1l1lll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲ࡫ࡴࡩࡱࡧࠫᬢ")]:
        return bstack1l1lll1_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡈࡅࡈࡎࠧᬣ")
    elif hook_name in [bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡰࡦࡸࡰࡪ࠭ᬤ"), bstack1l1lll1_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡤ࡮ࡤࡷࡸ࠭ᬥ")]:
        return bstack1l1lll1_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡇࡌࡍࠩᬦ")
    return hook_name
def bstack11l111lll11_opy_(node, scenario):
    if hasattr(node, bstack1l1lll1_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩᬧ")):
        parts = node.nodeid.rsplit(bstack1l1lll1_opy_ (u"ࠣ࡝ࠥᬨ"))
        params = parts[-1]
        return bstack1l1lll1_opy_ (u"ࠤࡾࢁࠥࡡࡻࡾࠤᬩ").format(scenario.name, params)
    return scenario.name
def bstack11l11l11l11_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1l1lll1_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬᬪ")):
            examples = list(node.callspec.params[bstack1l1lll1_opy_ (u"ࠫࡤࡶࡹࡵࡧࡶࡸࡤࡨࡤࡥࡡࡨࡼࡦࡳࡰ࡭ࡧࠪᬫ")].values())
        return examples
    except:
        return []
def bstack11l111ll1ll_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111lllll_opy_(report):
    try:
        status = bstack1l1lll1_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᬬ")
        if report.passed or (report.failed and hasattr(report, bstack1l1lll1_opy_ (u"ࠨࡷࡢࡵࡻࡪࡦ࡯࡬ࠣᬭ"))):
            status = bstack1l1lll1_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᬮ")
        elif report.skipped:
            status = bstack1l1lll1_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᬯ")
        bstack11ll111ll1l_opy_(status)
    except:
        pass
def bstack1ll1ll1ll_opy_(status):
    try:
        bstack11l11l111ll_opy_ = bstack1l1lll1_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᬰ")
        if status == bstack1l1lll1_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪᬱ"):
            bstack11l11l111ll_opy_ = bstack1l1lll1_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᬲ")
        elif status == bstack1l1lll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᬳ"):
            bstack11l11l111ll_opy_ = bstack1l1lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪ᬴ࠧ")
        bstack11ll111ll1l_opy_(bstack11l11l111ll_opy_)
    except:
        pass
def bstack11l11l11111_opy_(item=None, report=None, summary=None, extra=None):
    return
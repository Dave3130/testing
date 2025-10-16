# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import re
from bstack_utils.bstack11l111l1l1_opy_ import bstack11ll111lll1_opy_
def bstack11l11l11ll1_opy_(fixture_name):
    if fixture_name.startswith(bstack1ll11_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬆ")):
        return bstack1ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬇ")
    elif fixture_name.startswith(bstack1ll11_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬈ")):
        return bstack1ll11_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬉ")
    elif fixture_name.startswith(bstack1ll11_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬊ")):
        return bstack1ll11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬋ")
    elif fixture_name.startswith(bstack1ll11_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬌ")):
        return bstack1ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬍ")
def bstack11l111llll1_opy_(fixture_name):
    return bool(re.match(bstack1ll11_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࠩࡨࡸࡲࡨࡺࡩࡰࡰࡿࡱࡴࡪࡵ࡭ࡧࠬࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᬎ"), fixture_name))
def bstack11l11l1111l_opy_(fixture_name):
    return bool(re.match(bstack1ll11_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᬏ"), fixture_name))
def bstack11l11l11111_opy_(fixture_name):
    return bool(re.match(bstack1ll11_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᬐ"), fixture_name))
def bstack11l11l1l111_opy_(fixture_name):
    if fixture_name.startswith(bstack1ll11_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᬑ")):
        return bstack1ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬒ"), bstack1ll11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᬓ")
    elif fixture_name.startswith(bstack1ll11_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬔ")):
        return bstack1ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᬕ"), bstack1ll11_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᬖ")
    elif fixture_name.startswith(bstack1ll11_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬗ")):
        return bstack1ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᬘ"), bstack1ll11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᬙ")
    elif fixture_name.startswith(bstack1ll11_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬚ")):
        return bstack1ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬛ"), bstack1ll11_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ᬜ")
    return None, None
def bstack11l11l11lll_opy_(hook_name):
    if hook_name in [bstack1ll11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᬝ"), bstack1ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᬞ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l11l111l1_opy_(hook_name):
    if hook_name in [bstack1ll11_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᬟ"), bstack1ll11_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᬠ")]:
        return bstack1ll11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᬡ")
    elif hook_name in [bstack1ll11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨᬢ"), bstack1ll11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᬣ")]:
        return bstack1ll11_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᬤ")
    elif hook_name in [bstack1ll11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᬥ"), bstack1ll11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨᬦ")]:
        return bstack1ll11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᬧ")
    elif hook_name in [bstack1ll11_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᬨ"), bstack1ll11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᬩ")]:
        return bstack1ll11_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ᬪ")
    return hook_name
def bstack11l11l11l1l_opy_(node, scenario):
    if hasattr(node, bstack1ll11_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭ᬫ")):
        parts = node.nodeid.rsplit(bstack1ll11_opy_ (u"ࠧࡡࠢᬬ"))
        params = parts[-1]
        return bstack1ll11_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨᬭ").format(scenario.name, params)
    return scenario.name
def bstack11l111lll11_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1ll11_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩᬮ")):
            examples = list(node.callspec.params[bstack1ll11_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧᬯ")].values())
        return examples
    except:
        return []
def bstack11l11l11l11_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l11l111ll_opy_(report):
    try:
        status = bstack1ll11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᬰ")
        if report.passed or (report.failed and hasattr(report, bstack1ll11_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᬱ"))):
            status = bstack1ll11_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᬲ")
        elif report.skipped:
            status = bstack1ll11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᬳ")
        bstack11ll111lll1_opy_(status)
    except:
        pass
def bstack111llll111_opy_(status):
    try:
        bstack11l111lllll_opy_ = bstack1ll11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ᬴࠭")
        if status == bstack1ll11_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᬵ"):
            bstack11l111lllll_opy_ = bstack1ll11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᬶ")
        elif status == bstack1ll11_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᬷ"):
            bstack11l111lllll_opy_ = bstack1ll11_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᬸ")
        bstack11ll111lll1_opy_(bstack11l111lllll_opy_)
    except:
        pass
def bstack11l111lll1l_opy_(item=None, report=None, summary=None, extra=None):
    return
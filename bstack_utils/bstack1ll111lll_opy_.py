# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import re
from bstack_utils.bstack1111l1l11_opy_ import bstack11ll111ll1l_opy_
def bstack11l11l11l1l_opy_(fixture_name):
    if fixture_name.startswith(bstack11l1l11_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᫿")):
        return bstack11l1l11_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬀ")
    elif fixture_name.startswith(bstack11l1l11_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬁ")):
        return bstack11l1l11_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬂ")
    elif fixture_name.startswith(bstack11l1l11_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬃ")):
        return bstack11l1l11_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬄ")
    elif fixture_name.startswith(bstack11l1l11_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬅ")):
        return bstack11l1l11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬆ")
def bstack11l11l111ll_opy_(fixture_name):
    return bool(re.match(bstack11l1l11_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࠩࡨࡸࡲࡨࡺࡩࡰࡰࡿࡱࡴࡪࡵ࡭ࡧࠬࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᬇ"), fixture_name))
def bstack11l111ll1ll_opy_(fixture_name):
    return bool(re.match(bstack11l1l11_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᬈ"), fixture_name))
def bstack11l11l1111l_opy_(fixture_name):
    return bool(re.match(bstack11l1l11_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᬉ"), fixture_name))
def bstack11l111lll1l_opy_(fixture_name):
    if fixture_name.startswith(bstack11l1l11_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᬊ")):
        return bstack11l1l11_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬋ"), bstack11l1l11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᬌ")
    elif fixture_name.startswith(bstack11l1l11_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬍ")):
        return bstack11l1l11_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᬎ"), bstack11l1l11_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᬏ")
    elif fixture_name.startswith(bstack11l1l11_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬐ")):
        return bstack11l1l11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᬑ"), bstack11l1l11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᬒ")
    elif fixture_name.startswith(bstack11l1l11_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬓ")):
        return bstack11l1l11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬔ"), bstack11l1l11_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ᬕ")
    return None, None
def bstack11l11l11l11_opy_(hook_name):
    if hook_name in [bstack11l1l11_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᬖ"), bstack11l1l11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᬗ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111lll11_opy_(hook_name):
    if hook_name in [bstack11l1l11_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᬘ"), bstack11l1l11_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᬙ")]:
        return bstack11l1l11_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᬚ")
    elif hook_name in [bstack11l1l11_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨᬛ"), bstack11l1l11_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᬜ")]:
        return bstack11l1l11_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᬝ")
    elif hook_name in [bstack11l1l11_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᬞ"), bstack11l1l11_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨᬟ")]:
        return bstack11l1l11_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᬠ")
    elif hook_name in [bstack11l1l11_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᬡ"), bstack11l1l11_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᬢ")]:
        return bstack11l1l11_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ᬣ")
    return hook_name
def bstack11l11l111l1_opy_(node, scenario):
    if hasattr(node, bstack11l1l11_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭ᬤ")):
        parts = node.nodeid.rsplit(bstack11l1l11_opy_ (u"ࠧࡡࠢᬥ"))
        params = parts[-1]
        return bstack11l1l11_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨᬦ").format(scenario.name, params)
    return scenario.name
def bstack11l11l11ll1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11l1l11_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩᬧ")):
            examples = list(node.callspec.params[bstack11l1l11_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧᬨ")].values())
        return examples
    except:
        return []
def bstack11l111lllll_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l11l11111_opy_(report):
    try:
        status = bstack11l1l11_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩᬩ")
        if report.passed or (report.failed and hasattr(report, bstack11l1l11_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧᬪ"))):
            status = bstack11l1l11_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫᬫ")
        elif report.skipped:
            status = bstack11l1l11_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᬬ")
        bstack11ll111ll1l_opy_(status)
    except:
        pass
def bstack1lll11ll11_opy_(status):
    try:
        bstack11l111ll1l1_opy_ = bstack11l1l11_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᬭ")
        if status == bstack11l1l11_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᬮ"):
            bstack11l111ll1l1_opy_ = bstack11l1l11_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᬯ")
        elif status == bstack11l1l11_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᬰ"):
            bstack11l111ll1l1_opy_ = bstack11l1l11_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᬱ")
        bstack11ll111ll1l_opy_(bstack11l111ll1l1_opy_)
    except:
        pass
def bstack11l111llll1_opy_(item=None, report=None, summary=None, extra=None):
    return
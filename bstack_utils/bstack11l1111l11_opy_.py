# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import re
from bstack_utils.bstack1lll1111l_opy_ import bstack11ll111ll11_opy_
def bstack11l111ll111_opy_(fixture_name):
    if fixture_name.startswith(bstack11l111_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᫶")):
        return bstack11l111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ᫷")
    elif fixture_name.startswith(bstack11l111_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᫸")):
        return bstack11l111_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩ᫹")
    elif fixture_name.startswith(bstack11l111_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᫺")):
        return bstack11l111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ᫻")
    elif fixture_name.startswith(bstack11l111_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᫼")):
        return bstack11l111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩ᫽")
def bstack11l11l111ll_opy_(fixture_name):
    return bool(re.match(bstack11l111_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭᫾"), fixture_name))
def bstack11l11l111l1_opy_(fixture_name):
    return bool(re.match(bstack11l111_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪ᫿"), fixture_name))
def bstack11l11l11111_opy_(fixture_name):
    return bool(re.match(bstack11l111_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᬀ"), fixture_name))
def bstack11l111ll11l_opy_(fixture_name):
    if fixture_name.startswith(bstack11l111_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬁ")):
        return bstack11l111_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬂ"), bstack11l111_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᬃ")
    elif fixture_name.startswith(bstack11l111_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬄ")):
        return bstack11l111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧᬅ"), bstack11l111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᬆ")
    elif fixture_name.startswith(bstack11l111_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᬇ")):
        return bstack11l111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬈ"), bstack11l111_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᬉ")
    elif fixture_name.startswith(bstack11l111_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬊ")):
        return bstack11l111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᬋ"), bstack11l111_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᬌ")
    return None, None
def bstack11l11l11l11_opy_(hook_name):
    if hook_name in [bstack11l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᬍ"), bstack11l111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᬎ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111lllll_opy_(hook_name):
    if hook_name in [bstack11l111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬏ"), bstack11l111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫᬐ")]:
        return bstack11l111_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᬑ")
    elif hook_name in [bstack11l111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᬒ"), bstack11l111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᬓ")]:
        return bstack11l111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᬔ")
    elif hook_name in [bstack11l111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᬕ"), bstack11l111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᬖ")]:
        return bstack11l111_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᬗ")
    elif hook_name in [bstack11l111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᬘ"), bstack11l111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᬙ")]:
        return bstack11l111_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᬚ")
    return hook_name
def bstack11l111lll11_opy_(node, scenario):
    if hasattr(node, bstack11l111_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫᬛ")):
        parts = node.nodeid.rsplit(bstack11l111_opy_ (u"ࠥ࡟ࠧᬜ"))
        params = parts[-1]
        return bstack11l111_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦᬝ").format(scenario.name, params)
    return scenario.name
def bstack11l111ll1l1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11l111_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᬞ")):
            examples = list(node.callspec.params[bstack11l111_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬᬟ")].values())
        return examples
    except:
        return []
def bstack11l111lll1l_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l11l1111l_opy_(report):
    try:
        status = bstack11l111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᬠ")
        if report.passed or (report.failed and hasattr(report, bstack11l111_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥᬡ"))):
            status = bstack11l111_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᬢ")
        elif report.skipped:
            status = bstack11l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᬣ")
        bstack11ll111ll11_opy_(status)
    except:
        pass
def bstack1ll11l111_opy_(status):
    try:
        bstack11l111llll1_opy_ = bstack11l111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᬤ")
        if status == bstack11l111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᬥ"):
            bstack11l111llll1_opy_ = bstack11l111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᬦ")
        elif status == bstack11l111_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᬧ"):
            bstack11l111llll1_opy_ = bstack11l111_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᬨ")
        bstack11ll111ll11_opy_(bstack11l111llll1_opy_)
    except:
        pass
def bstack11l111ll1ll_opy_(item=None, report=None, summary=None, extra=None):
    return
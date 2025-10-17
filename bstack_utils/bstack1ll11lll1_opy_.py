# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import re
from bstack_utils.bstack11ll11l1l1_opy_ import bstack11ll11l1111_opy_
def bstack11l111lllll_opy_(fixture_name):
    if fixture_name.startswith(bstack11111_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᫶")):
        return bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ᫷")
    elif fixture_name.startswith(bstack11111_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᫸")):
        return bstack11111_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩ᫹")
    elif fixture_name.startswith(bstack11111_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᫺")):
        return bstack11111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ᫻")
    elif fixture_name.startswith(bstack11111_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᫼")):
        return bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩ᫽")
def bstack11l11l11l1l_opy_(fixture_name):
    return bool(re.match(bstack11111_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭᫾"), fixture_name))
def bstack11l11l111l1_opy_(fixture_name):
    return bool(re.match(bstack11111_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪ᫿"), fixture_name))
def bstack11l111lll1l_opy_(fixture_name):
    return bool(re.match(bstack11111_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᬀ"), fixture_name))
def bstack11l111lll11_opy_(fixture_name):
    if fixture_name.startswith(bstack11111_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬁ")):
        return bstack11111_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬂ"), bstack11111_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᬃ")
    elif fixture_name.startswith(bstack11111_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬄ")):
        return bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧᬅ"), bstack11111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᬆ")
    elif fixture_name.startswith(bstack11111_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᬇ")):
        return bstack11111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬈ"), bstack11111_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᬉ")
    elif fixture_name.startswith(bstack11111_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬊ")):
        return bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᬋ"), bstack11111_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᬌ")
    return None, None
def bstack11l111ll11l_opy_(hook_name):
    if hook_name in [bstack11111_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᬍ"), bstack11111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᬎ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l11l11l11_opy_(hook_name):
    if hook_name in [bstack11111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬏ"), bstack11111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫᬐ")]:
        return bstack11111_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᬑ")
    elif hook_name in [bstack11111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᬒ"), bstack11111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭ᬓ")]:
        return bstack11111_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᬔ")
    elif hook_name in [bstack11111_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᬕ"), bstack11111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᬖ")]:
        return bstack11111_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᬗ")
    elif hook_name in [bstack11111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᬘ"), bstack11111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᬙ")]:
        return bstack11111_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᬚ")
    return hook_name
def bstack11l11l111ll_opy_(node, scenario):
    if hasattr(node, bstack11111_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫᬛ")):
        parts = node.nodeid.rsplit(bstack11111_opy_ (u"ࠥ࡟ࠧᬜ"))
        params = parts[-1]
        return bstack11111_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦᬝ").format(scenario.name, params)
    return scenario.name
def bstack11l11l1111l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11111_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᬞ")):
            examples = list(node.callspec.params[bstack11111_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬᬟ")].values())
        return examples
    except:
        return []
def bstack11l11l11111_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111llll1_opy_(report):
    try:
        status = bstack11111_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᬠ")
        if report.passed or (report.failed and hasattr(report, bstack11111_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥᬡ"))):
            status = bstack11111_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᬢ")
        elif report.skipped:
            status = bstack11111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᬣ")
        bstack11ll11l1111_opy_(status)
    except:
        pass
def bstack11l11l1l1_opy_(status):
    try:
        bstack11l111ll1l1_opy_ = bstack11111_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫᬤ")
        if status == bstack11111_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᬥ"):
            bstack11l111ll1l1_opy_ = bstack11111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᬦ")
        elif status == bstack11111_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨᬧ"):
            bstack11l111ll1l1_opy_ = bstack11111_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᬨ")
        bstack11ll11l1111_opy_(bstack11l111ll1l1_opy_)
    except:
        pass
def bstack11l111ll1ll_opy_(item=None, report=None, summary=None, extra=None):
    return
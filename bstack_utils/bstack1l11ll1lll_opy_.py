# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import re
from bstack_utils.bstack1l1ll111l1_opy_ import bstack11ll11111l1_opy_
def bstack11l111ll1ll_opy_(fixture_name):
    if fixture_name.startswith(bstack1lllll1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬧ")):
        return bstack1lllll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᬨ")
    elif fixture_name.startswith(bstack1lllll1l_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬩ")):
        return bstack1lllll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᬪ")
    elif fixture_name.startswith(bstack1lllll1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬫ")):
        return bstack1lllll1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᬬ")
    elif fixture_name.startswith(bstack1lllll1l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬭ")):
        return bstack1lllll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᬮ")
def bstack11l111ll111_opy_(fixture_name):
    return bool(re.match(bstack1lllll1l_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᬯ"), fixture_name))
def bstack11l111ll1l1_opy_(fixture_name):
    return bool(re.match(bstack1lllll1l_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᬰ"), fixture_name))
def bstack11l111l111l_opy_(fixture_name):
    return bool(re.match(bstack1lllll1l_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᬱ"), fixture_name))
def bstack11l111l1lll_opy_(fixture_name):
    if fixture_name.startswith(bstack1lllll1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬲ")):
        return bstack1lllll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬳ"), bstack1lllll1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋ᬴ࠫ")
    elif fixture_name.startswith(bstack1lllll1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬵ")):
        return bstack1lllll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧᬶ"), bstack1lllll1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᬷ")
    elif fixture_name.startswith(bstack1lllll1l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᬸ")):
        return bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬹ"), bstack1lllll1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᬺ")
    elif fixture_name.startswith(bstack1lllll1l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬻ")):
        return bstack1lllll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᬼ"), bstack1lllll1l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᬽ")
    return None, None
def bstack11l111l1ll1_opy_(hook_name):
    if hook_name in [bstack1lllll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨᬾ"), bstack1lllll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬᬿ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111l1l11_opy_(hook_name):
    if hook_name in [bstack1lllll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᭀ"), bstack1lllll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫᭁ")]:
        return bstack1lllll1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫᭂ")
    elif hook_name in [bstack1lllll1l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭ᭃ"), bstack1lllll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ᭄࠭")]:
        return bstack1lllll1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭ᭅ")
    elif hook_name in [bstack1lllll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᭆ"), bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᭇ")]:
        return bstack1lllll1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩᭈ")
    elif hook_name in [bstack1lllll1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨᭉ"), bstack1lllll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨᭊ")]:
        return bstack1lllll1l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫᭋ")
    return hook_name
def bstack11l111lll11_opy_(node, scenario):
    if hasattr(node, bstack1lllll1l_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫᭌ")):
        parts = node.nodeid.rsplit(bstack1lllll1l_opy_ (u"ࠥ࡟ࠧ᭍"))
        params = parts[-1]
        return bstack1lllll1l_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦ᭎").format(scenario.name, params)
    return scenario.name
def bstack11l111l1l1l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1lllll1l_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧ᭏")):
            examples = list(node.callspec.params[bstack1lllll1l_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩࠬ᭐")].values())
        return examples
    except:
        return []
def bstack11l111l11l1_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111l11ll_opy_(report):
    try:
        status = bstack1lllll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᭑")
        if report.passed or (report.failed and hasattr(report, bstack1lllll1l_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ᭒"))):
            status = bstack1lllll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ᭓")
        elif report.skipped:
            status = bstack1lllll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ᭔")
        bstack11ll11111l1_opy_(status)
    except:
        pass
def bstack11ll11llll_opy_(status):
    try:
        bstack11l111lll1l_opy_ = bstack1lllll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᭕")
        if status == bstack1lllll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ᭖"):
            bstack11l111lll1l_opy_ = bstack1lllll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭᭗")
        elif status == bstack1lllll1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ᭘"):
            bstack11l111lll1l_opy_ = bstack1lllll1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ᭙")
        bstack11ll11111l1_opy_(bstack11l111lll1l_opy_)
    except:
        pass
def bstack11l111ll11l_opy_(item=None, report=None, summary=None, extra=None):
    return
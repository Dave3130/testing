# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import re
from bstack_utils.bstack1lll1l1l11_opy_ import bstack11ll11111ll_opy_
def bstack11l111lll11_opy_(fixture_name):
    if fixture_name.startswith(bstack11l111_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬩ")):
        return bstack11l111_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬪ")
    elif fixture_name.startswith(bstack11l111_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬫ")):
        return bstack11l111_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬬ")
    elif fixture_name.startswith(bstack11l111_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬭ")):
        return bstack11l111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬮ")
    elif fixture_name.startswith(bstack11l111_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬯ")):
        return bstack11l111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬰ")
def bstack11l111l1lll_opy_(fixture_name):
    return bool(re.match(bstack11l111_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࠩࡨࡸࡲࡨࡺࡩࡰࡰࡿࡱࡴࡪࡵ࡭ࡧࠬࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨᬱ"), fixture_name))
def bstack11l111l1l1l_opy_(fixture_name):
    return bool(re.match(bstack11l111_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᬲ"), fixture_name))
def bstack11l111ll1ll_opy_(fixture_name):
    return bool(re.match(bstack11l111_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬᬳ"), fixture_name))
def bstack11l111l11ll_opy_(fixture_name):
    if fixture_name.startswith(bstack11l111_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᬴")):
        return bstack11l111_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬵ"), bstack11l111_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭ᬶ")
    elif fixture_name.startswith(bstack11l111_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬷ")):
        return bstack11l111_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᬸ"), bstack11l111_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᬹ")
    elif fixture_name.startswith(bstack11l111_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬺ")):
        return bstack11l111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᬻ"), bstack11l111_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᬼ")
    elif fixture_name.startswith(bstack11l111_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬽ")):
        return bstack11l111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬾ"), bstack11l111_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭ᬿ")
    return None, None
def bstack11l111l1l11_opy_(hook_name):
    if hook_name in [bstack11l111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪᭀ"), bstack11l111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧᭁ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111l111l_opy_(hook_name):
    if hook_name in [bstack11l111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧᭂ"), bstack11l111_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭ᭃ")]:
        return bstack11l111_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ᭄࠭")
    elif hook_name in [bstack11l111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨᭅ"), bstack11l111_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨᭆ")]:
        return bstack11l111_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨᭇ")
    elif hook_name in [bstack11l111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᭈ"), bstack11l111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨᭉ")]:
        return bstack11l111_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫᭊ")
    elif hook_name in [bstack11l111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪᭋ"), bstack11l111_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪᭌ")]:
        return bstack11l111_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭᭍")
    return hook_name
def bstack11l111ll1l1_opy_(node, scenario):
    if hasattr(node, bstack11l111_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭᭎")):
        parts = node.nodeid.rsplit(bstack11l111_opy_ (u"ࠧࡡࠢ᭏"))
        params = parts[-1]
        return bstack11l111_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨ᭐").format(scenario.name, params)
    return scenario.name
def bstack11l111l11l1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11l111_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩ᭑")):
            examples = list(node.callspec.params[bstack11l111_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧ᭒")].values())
        return examples
    except:
        return []
def bstack11l111ll111_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111l1ll1_opy_(report):
    try:
        status = bstack11l111_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ᭓")
        if report.passed or (report.failed and hasattr(report, bstack11l111_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧ᭔"))):
            status = bstack11l111_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ᭕")
        elif report.skipped:
            status = bstack11l111_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭᭖")
        bstack11ll11111ll_opy_(status)
    except:
        pass
def bstack1ll11l111_opy_(status):
    try:
        bstack11l111lll1l_opy_ = bstack11l111_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭᭗")
        if status == bstack11l111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧ᭘"):
            bstack11l111lll1l_opy_ = bstack11l111_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ᭙")
        elif status == bstack11l111_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪ᭚"):
            bstack11l111lll1l_opy_ = bstack11l111_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ᭛")
        bstack11ll11111ll_opy_(bstack11l111lll1l_opy_)
    except:
        pass
def bstack11l111ll11l_opy_(item=None, report=None, summary=None, extra=None):
    return
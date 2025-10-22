# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import re
from bstack_utils.bstack1lll111l11_opy_ import bstack11ll11111ll_opy_
def bstack11l111l1111_opy_(fixture_name):
    if fixture_name.startswith(bstack111l1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬤ")):
        return bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬥ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬦ")):
        return bstack111l1l_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳࡭ࡰࡦࡸࡰࡪ࠭ᬧ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬨ")):
        return bstack111l1l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭ᬩ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨᬪ")):
        return bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳࡭ࡰࡦࡸࡰࡪ࠭ᬫ")
def bstack11l111l111l_opy_(fixture_name):
    return bool(re.match(bstack111l1l_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࠫࡪࡺࡴࡣࡵ࡫ࡲࡲࢁࡳ࡯ࡥࡷ࡯ࡩ࠮ࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᬬ"), fixture_name))
def bstack11l111l1lll_opy_(fixture_name):
    return bool(re.match(bstack111l1l_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰ࠧᬭ"), fixture_name))
def bstack11l111l11l1_opy_(fixture_name):
    return bool(re.match(bstack111l1l_opy_ (u"ࠧ࡟ࡡࡻࡹࡳ࡯ࡴࡠࠪࡶࡩࡹࡻࡰࡽࡶࡨࡥࡷࡪ࡯ࡸࡰࠬࡣࡨࡲࡡࡴࡵࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰ࠧᬮ"), fixture_name))
def bstack11l1111llll_opy_(fixture_name):
    if fixture_name.startswith(bstack111l1l_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬯ")):
        return bstack111l1l_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪᬰ"), bstack111l1l_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᬱ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬲ")):
        return bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫᬳ"), bstack111l1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎ᬴ࠪ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬵ")):
        return bstack111l1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬶ"), bstack111l1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᬷ")
    elif fixture_name.startswith(bstack111l1l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭ᬸ")):
        return bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳࡭ࡰࡦࡸࡰࡪ࠭ᬹ"), bstack111l1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨᬺ")
    return None, None
def bstack11l111ll111_opy_(hook_name):
    if hook_name in [bstack111l1l_opy_ (u"࠭ࡳࡦࡶࡸࡴࠬᬻ"), bstack111l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࠩᬼ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111l1l11_opy_(hook_name):
    if hook_name in [bstack111l1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᬽ"), bstack111l1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡨࡸ࡭ࡵࡤࠨᬾ")]:
        return bstack111l1l_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡉࡆࡉࡈࠨᬿ")
    elif hook_name in [bstack111l1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࠪᭀ"), bstack111l1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡨࡲࡡࡴࡵࠪᭁ")]:
        return bstack111l1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡁࡍࡎࠪᭂ")
    elif hook_name in [bstack111l1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࠫᭃ"), bstack111l1l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡪࡺࡨࡰࡦ᭄ࠪ")]:
        return bstack111l1l_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡇࡄࡇࡍ࠭ᭅ")
    elif hook_name in [bstack111l1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡳ࡯ࡥࡷ࡯ࡩࠬᭆ"), bstack111l1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡣ࡭ࡣࡶࡷࠬᭇ")]:
        return bstack111l1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡆࡒࡌࠨᭈ")
    return hook_name
def bstack11l111l1ll1_opy_(node, scenario):
    if hasattr(node, bstack111l1l_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨᭉ")):
        parts = node.nodeid.rsplit(bstack111l1l_opy_ (u"ࠢ࡜ࠤᭊ"))
        params = parts[-1]
        return bstack111l1l_opy_ (u"ࠣࡽࢀࠤࡠࢁࡽࠣᭋ").format(scenario.name, params)
    return scenario.name
def bstack11l111ll11l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack111l1l_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫᭌ")):
            examples = list(node.callspec.params[bstack111l1l_opy_ (u"ࠪࡣࡵࡿࡴࡦࡵࡷࡣࡧࡪࡤࡠࡧࡻࡥࡲࡶ࡬ࡦࠩ᭍")].values())
        return examples
    except:
        return []
def bstack11l111l1l1l_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111ll1ll_opy_(report):
    try:
        status = bstack111l1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᭎")
        if report.passed or (report.failed and hasattr(report, bstack111l1l_opy_ (u"ࠧࡽࡡࡴࡺࡩࡥ࡮ࡲࠢ᭏"))):
            status = bstack111l1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭᭐")
        elif report.skipped:
            status = bstack111l1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ᭑")
        bstack11ll11111ll_opy_(status)
    except:
        pass
def bstack1llll11l1l_opy_(status):
    try:
        bstack11l111l11ll_opy_ = bstack111l1l_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᭒")
        if status == bstack111l1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ᭓"):
            bstack11l111l11ll_opy_ = bstack111l1l_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ᭔")
        elif status == bstack111l1l_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ᭕"):
            bstack11l111l11ll_opy_ = bstack111l1l_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭᭖")
        bstack11ll11111ll_opy_(bstack11l111l11ll_opy_)
    except:
        pass
def bstack11l111ll1l1_opy_(item=None, report=None, summary=None, extra=None):
    return
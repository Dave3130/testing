# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import re
from bstack_utils.bstack11111ll111_opy_ import bstack11ll1111l11_opy_
def bstack11l111l1l11_opy_(fixture_name):
    if fixture_name.startswith(bstack11l11l1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬜ")):
        return bstack11l11l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬝ")
    elif fixture_name.startswith(bstack11l11l1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬞ")):
        return bstack11l11l1_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬟ")
    elif fixture_name.startswith(bstack11l11l1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬠ")):
        return bstack11l11l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬡ")
    elif fixture_name.startswith(bstack11l11l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬢ")):
        return bstack11l11l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬣ")
def bstack11l111l1ll1_opy_(fixture_name):
    return bool(re.match(bstack11l11l1_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࠪࡩࡹࡳࡩࡴࡪࡱࡱࢀࡲࡵࡤࡶ࡮ࡨ࠭ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᬤ"), fixture_name))
def bstack11l111ll111_opy_(fixture_name):
    return bool(re.match(bstack11l11l1_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᬥ"), fixture_name))
def bstack11l111l11ll_opy_(fixture_name):
    return bool(re.match(bstack11l11l1_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᬦ"), fixture_name))
def bstack11l111ll11l_opy_(fixture_name):
    if fixture_name.startswith(bstack11l11l1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬧ")):
        return bstack11l11l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᬨ"), bstack11l11l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᬩ")
    elif fixture_name.startswith(bstack11l11l1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬪ")):
        return bstack11l11l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᬫ"), bstack11l11l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᬬ")
    elif fixture_name.startswith(bstack11l11l1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬭ")):
        return bstack11l11l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬮ"), bstack11l11l1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᬯ")
    elif fixture_name.startswith(bstack11l11l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬰ")):
        return bstack11l11l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬱ"), bstack11l11l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᬲ")
    return None, None
def bstack11l111ll1ll_opy_(hook_name):
    if hook_name in [bstack11l11l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᬳ"), bstack11l11l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ᬴")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111llll1_opy_(hook_name):
    if hook_name in [bstack11l11l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬵ"), bstack11l11l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᬶ")]:
        return bstack11l11l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᬷ")
    elif hook_name in [bstack11l11l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᬸ"), bstack11l11l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩᬹ")]:
        return bstack11l11l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᬺ")
    elif hook_name in [bstack11l11l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᬻ"), bstack11l11l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᬼ")]:
        return bstack11l11l1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᬽ")
    elif hook_name in [bstack11l11l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᬾ"), bstack11l11l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᬿ")]:
        return bstack11l11l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᭀ")
    return hook_name
def bstack11l111lll1l_opy_(node, scenario):
    if hasattr(node, bstack11l11l1_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᭁ")):
        parts = node.nodeid.rsplit(bstack11l11l1_opy_ (u"ࠨ࡛ࠣᭂ"))
        params = parts[-1]
        return bstack11l11l1_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢᭃ").format(scenario.name, params)
    return scenario.name
def bstack11l111ll1l1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11l11l1_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥ᭄ࠪ")):
            examples = list(node.callspec.params[bstack11l11l1_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨᭅ")].values())
        return examples
    except:
        return []
def bstack11l111l1l1l_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111lllll_opy_(report):
    try:
        status = bstack11l11l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᭆ")
        if report.passed or (report.failed and hasattr(report, bstack11l11l1_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᭇ"))):
            status = bstack11l11l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᭈ")
        elif report.skipped:
            status = bstack11l11l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᭉ")
        bstack11ll1111l11_opy_(status)
    except:
        pass
def bstack1l1lll1l1l_opy_(status):
    try:
        bstack11l111l1lll_opy_ = bstack11l11l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᭊ")
        if status == bstack11l11l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᭋ"):
            bstack11l111l1lll_opy_ = bstack11l11l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᭌ")
        elif status == bstack11l11l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ᭍"):
            bstack11l111l1lll_opy_ = bstack11l11l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ᭎")
        bstack11ll1111l11_opy_(bstack11l111l1lll_opy_)
    except:
        pass
def bstack11l111lll11_opy_(item=None, report=None, summary=None, extra=None):
    return
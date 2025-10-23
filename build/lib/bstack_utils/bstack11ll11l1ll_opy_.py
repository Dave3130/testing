# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import re
from bstack_utils.bstack1111ll1lll_opy_ import bstack11ll1111l11_opy_
def bstack11l111l1l11_opy_(fixture_name):
    if fixture_name.startswith(bstack11lll1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬣ")):
        return bstack11lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬤ")
    elif fixture_name.startswith(bstack11lll1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬥ")):
        return bstack11lll1_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬦ")
    elif fixture_name.startswith(bstack11lll1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬧ")):
        return bstack11lll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬨ")
    elif fixture_name.startswith(bstack11lll1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬩ")):
        return bstack11lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬪ")
def bstack11l111l11l1_opy_(fixture_name):
    return bool(re.match(bstack11lll1_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࠪࡩࡹࡳࡩࡴࡪࡱࡱࢀࡲࡵࡤࡶ࡮ࡨ࠭ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᬫ"), fixture_name))
def bstack11l111l1111_opy_(fixture_name):
    return bool(re.match(bstack11lll1_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᬬ"), fixture_name))
def bstack11l111ll1l1_opy_(fixture_name):
    return bool(re.match(bstack11lll1_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᬭ"), fixture_name))
def bstack11l111l111l_opy_(fixture_name):
    if fixture_name.startswith(bstack11lll1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬮ")):
        return bstack11lll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᬯ"), bstack11lll1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᬰ")
    elif fixture_name.startswith(bstack11lll1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬱ")):
        return bstack11lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᬲ"), bstack11lll1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᬳ")
    elif fixture_name.startswith(bstack11lll1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨ᬴ࠫ")):
        return bstack11lll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬵ"), bstack11lll1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᬶ")
    elif fixture_name.startswith(bstack11lll1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬷ")):
        return bstack11lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬸ"), bstack11lll1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᬹ")
    return None, None
def bstack11l111lll11_opy_(hook_name):
    if hook_name in [bstack11lll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᬺ"), bstack11lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᬻ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111ll111_opy_(hook_name):
    if hook_name in [bstack11lll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬼ"), bstack11lll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᬽ")]:
        return bstack11lll1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᬾ")
    elif hook_name in [bstack11lll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᬿ"), bstack11lll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩᭀ")]:
        return bstack11lll1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᭁ")
    elif hook_name in [bstack11lll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᭂ"), bstack11lll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᭃ")]:
        return bstack11lll1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌ᭄ࠬ")
    elif hook_name in [bstack11lll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᭅ"), bstack11lll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᭆ")]:
        return bstack11lll1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᭇ")
    return hook_name
def bstack11l111l1ll1_opy_(node, scenario):
    if hasattr(node, bstack11lll1_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᭈ")):
        parts = node.nodeid.rsplit(bstack11lll1_opy_ (u"ࠨ࡛ࠣᭉ"))
        params = parts[-1]
        return bstack11lll1_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢᭊ").format(scenario.name, params)
    return scenario.name
def bstack11l111l11ll_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11lll1_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᭋ")):
            examples = list(node.callspec.params[bstack11lll1_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨᭌ")].values())
        return examples
    except:
        return []
def bstack11l111ll11l_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111l1lll_opy_(report):
    try:
        status = bstack11lll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᭍")
        if report.passed or (report.failed and hasattr(report, bstack11lll1_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨ᭎"))):
            status = bstack11lll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ᭏")
        elif report.skipped:
            status = bstack11lll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ᭐")
        bstack11ll1111l11_opy_(status)
    except:
        pass
def bstack1111lll111_opy_(status):
    try:
        bstack11l111ll1ll_opy_ = bstack11lll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᭑")
        if status == bstack11lll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ᭒"):
            bstack11l111ll1ll_opy_ = bstack11lll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ᭓")
        elif status == bstack11lll1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ᭔"):
            bstack11l111ll1ll_opy_ = bstack11lll1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ᭕")
        bstack11ll1111l11_opy_(bstack11l111ll1ll_opy_)
    except:
        pass
def bstack11l111l1l1l_opy_(item=None, report=None, summary=None, extra=None):
    return
# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import re
from bstack_utils.bstack1l11l1llll_opy_ import bstack11ll1111ll1_opy_
def bstack11l111ll1l1_opy_(fixture_name):
    if fixture_name.startswith(bstack1l1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬜ")):
        return bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬝ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬞ")):
        return bstack1l1_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬟ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬠ")):
        return bstack1l1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬡ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬢ")):
        return bstack1l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬣ")
def bstack11l111l1l11_opy_(fixture_name):
    return bool(re.match(bstack1l1_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࠪࡩࡹࡳࡩࡴࡪࡱࡱࢀࡲࡵࡤࡶ࡮ࡨ࠭ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᬤ"), fixture_name))
def bstack11l111ll1ll_opy_(fixture_name):
    return bool(re.match(bstack1l1_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᬥ"), fixture_name))
def bstack11l111llll1_opy_(fixture_name):
    return bool(re.match(bstack1l1_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᬦ"), fixture_name))
def bstack11l111l1lll_opy_(fixture_name):
    if fixture_name.startswith(bstack1l1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬧ")):
        return bstack1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᬨ"), bstack1l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᬩ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬪ")):
        return bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᬫ"), bstack1l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᬬ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬭ")):
        return bstack1l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬮ"), bstack1l1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᬯ")
    elif fixture_name.startswith(bstack1l1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬰ")):
        return bstack1l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬱ"), bstack1l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᬲ")
    return None, None
def bstack11l111lllll_opy_(hook_name):
    if hook_name in [bstack1l1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᬳ"), bstack1l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ᬴")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111lll11_opy_(hook_name):
    if hook_name in [bstack1l1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬵ"), bstack1l1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᬶ")]:
        return bstack1l1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᬷ")
    elif hook_name in [bstack1l1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᬸ"), bstack1l1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩᬹ")]:
        return bstack1l1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᬺ")
    elif hook_name in [bstack1l1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᬻ"), bstack1l1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᬼ")]:
        return bstack1l1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᬽ")
    elif hook_name in [bstack1l1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᬾ"), bstack1l1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᬿ")]:
        return bstack1l1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᭀ")
    return hook_name
def bstack11l111l1l1l_opy_(node, scenario):
    if hasattr(node, bstack1l1_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᭁ")):
        parts = node.nodeid.rsplit(bstack1l1_opy_ (u"ࠨ࡛ࠣᭂ"))
        params = parts[-1]
        return bstack1l1_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢᭃ").format(scenario.name, params)
    return scenario.name
def bstack11l111ll11l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1l1_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥ᭄ࠪ")):
            examples = list(node.callspec.params[bstack1l1_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨᭅ")].values())
        return examples
    except:
        return []
def bstack11l111l1ll1_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111lll1l_opy_(report):
    try:
        status = bstack1l1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᭆ")
        if report.passed or (report.failed and hasattr(report, bstack1l1_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᭇ"))):
            status = bstack1l1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᭈ")
        elif report.skipped:
            status = bstack1l1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧᭉ")
        bstack11ll1111ll1_opy_(status)
    except:
        pass
def bstack111111ll1_opy_(status):
    try:
        bstack11l111ll111_opy_ = bstack1l1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᭊ")
        if status == bstack1l1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᭋ"):
            bstack11l111ll111_opy_ = bstack1l1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᭌ")
        elif status == bstack1l1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ᭍"):
            bstack11l111ll111_opy_ = bstack1l1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ᭎")
        bstack11ll1111ll1_opy_(bstack11l111ll111_opy_)
    except:
        pass
def bstack11l111l11ll_opy_(item=None, report=None, summary=None, extra=None):
    return
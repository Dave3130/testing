# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import re
from bstack_utils.bstack111111ll1_opy_ import bstack11ll111lll1_opy_
def bstack11l11l11lll_opy_(fixture_name):
    if fixture_name.startswith(bstack1lllll1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬇ")):
        return bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬈ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬉ")):
        return bstack1lllll1_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬊ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬋ")):
        return bstack1lllll1_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬌ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬍ")):
        return bstack1lllll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬎ")
def bstack11l11l1l111_opy_(fixture_name):
    return bool(re.match(bstack1lllll1_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࠪࡩࡹࡳࡩࡴࡪࡱࡱࢀࡲࡵࡤࡶ࡮ࡨ࠭ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᬏ"), fixture_name))
def bstack11l11l111l1_opy_(fixture_name):
    return bool(re.match(bstack1lllll1_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᬐ"), fixture_name))
def bstack11l11l11l11_opy_(fixture_name):
    return bool(re.match(bstack1lllll1_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᬑ"), fixture_name))
def bstack11l111llll1_opy_(fixture_name):
    if fixture_name.startswith(bstack1lllll1_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᬒ")):
        return bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᬓ"), bstack1lllll1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᬔ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᬕ")):
        return bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᬖ"), bstack1lllll1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᬗ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᬘ")):
        return bstack1lllll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᬙ"), bstack1lllll1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᬚ")
    elif fixture_name.startswith(bstack1lllll1_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬛ")):
        return bstack1lllll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬜ"), bstack1lllll1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᬝ")
    return None, None
def bstack11l11l11ll1_opy_(hook_name):
    if hook_name in [bstack1lllll1_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫᬞ"), bstack1lllll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨᬟ")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l11l1111l_opy_(hook_name):
    if hook_name in [bstack1lllll1_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨᬠ"), bstack1lllll1_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧᬡ")]:
        return bstack1lllll1_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᬢ")
    elif hook_name in [bstack1lllll1_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩᬣ"), bstack1lllll1_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩᬤ")]:
        return bstack1lllll1_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᬥ")
    elif hook_name in [bstack1lllll1_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪᬦ"), bstack1lllll1_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩᬧ")]:
        return bstack1lllll1_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᬨ")
    elif hook_name in [bstack1lllll1_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫᬩ"), bstack1lllll1_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫᬪ")]:
        return bstack1lllll1_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧᬫ")
    return hook_name
def bstack11l11l11l1l_opy_(node, scenario):
    if hasattr(node, bstack1lllll1_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧᬬ")):
        parts = node.nodeid.rsplit(bstack1lllll1_opy_ (u"ࠨ࡛ࠣᬭ"))
        params = parts[-1]
        return bstack1lllll1_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢᬮ").format(scenario.name, params)
    return scenario.name
def bstack11l11l11111_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1lllll1_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪᬯ")):
            examples = list(node.callspec.params[bstack1lllll1_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨᬰ")].values())
        return examples
    except:
        return []
def bstack11l111lllll_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111lll11_opy_(report):
    try:
        status = bstack1lllll1_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪᬱ")
        if report.passed or (report.failed and hasattr(report, bstack1lllll1_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨᬲ"))):
            status = bstack1lllll1_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬᬳ")
        elif report.skipped:
            status = bstack1lllll1_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪ᬴ࠧ")
        bstack11ll111lll1_opy_(status)
    except:
        pass
def bstack111lll11ll_opy_(status):
    try:
        bstack11l111lll1l_opy_ = bstack1lllll1_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧᬵ")
        if status == bstack1lllll1_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᬶ"):
            bstack11l111lll1l_opy_ = bstack1lllll1_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩᬷ")
        elif status == bstack1lllll1_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᬸ"):
            bstack11l111lll1l_opy_ = bstack1lllll1_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬᬹ")
        bstack11ll111lll1_opy_(bstack11l111lll1l_opy_)
    except:
        pass
def bstack11l11l111ll_opy_(item=None, report=None, summary=None, extra=None):
    return
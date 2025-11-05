# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import re
from bstack_utils.bstack1lll11111l_opy_ import bstack11ll1111111_opy_
def bstack11l1111ll1l_opy_(fixture_name):
    if fixture_name.startswith(bstack1lll11l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬸ")):
        return bstack1lll11l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬹ")
    elif fixture_name.startswith(bstack1lll11l_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬺ")):
        return bstack1lll11l_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬻ")
    elif fixture_name.startswith(bstack1lll11l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᬼ")):
        return bstack1lll11l_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡪࡺࡴࡣࡵ࡫ࡲࡲࠬᬽ")
    elif fixture_name.startswith(bstack1lll11l_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧᬾ")):
        return bstack1lll11l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬᬿ")
def bstack11l111l1ll1_opy_(fixture_name):
    return bool(re.match(bstack1lll11l_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࠪࡩࡹࡳࡩࡴࡪࡱࡱࢀࡲࡵࡤࡶ࡮ࡨ࠭ࡤ࡬ࡩࡹࡶࡸࡶࡪࡥ࠮ࠫࠩᭀ"), fixture_name))
def bstack11l111l1111_opy_(fixture_name):
    return bool(re.match(bstack1lll11l_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᭁ"), fixture_name))
def bstack11l111l111l_opy_(fixture_name):
    return bool(re.match(bstack1lll11l_opy_ (u"࠭࡞ࡠࡺࡸࡲ࡮ࡺ࡟ࠩࡵࡨࡸࡺࡶࡼࡵࡧࡤࡶࡩࡵࡷ࡯ࠫࡢࡧࡱࡧࡳࡴࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᭂ"), fixture_name))
def bstack11l111ll111_opy_(fixture_name):
    if fixture_name.startswith(bstack1lll11l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᭃ")):
        return bstack1lll11l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯᭄ࠩ"), bstack1lll11l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧᭅ")
    elif fixture_name.startswith(bstack1lll11l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪᭆ")):
        return bstack1lll11l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪᭇ"), bstack1lll11l_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩᭈ")
    elif fixture_name.startswith(bstack1lll11l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᭉ")):
        return bstack1lll11l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫᭊ"), bstack1lll11l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬᭋ")
    elif fixture_name.startswith(bstack1lll11l_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࡣ࡫࡯ࡸࡵࡷࡵࡩࠬᭌ")):
        return bstack1lll11l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲ࠲ࡳ࡯ࡥࡷ࡯ࡩࠬ᭍"), bstack1lll11l_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧ᭎")
    return None, None
def bstack11l1111ll11_opy_(hook_name):
    if hook_name in [bstack1lll11l_opy_ (u"ࠬࡹࡥࡵࡷࡳࠫ᭏"), bstack1lll11l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࠨ᭐")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111l1l11_opy_(hook_name):
    if hook_name in [bstack1lll11l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨ᭑"), bstack1lll11l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡧࡷ࡬ࡴࡪࠧ᭒")]:
        return bstack1lll11l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡈࡅࡈࡎࠧ᭓")
    elif hook_name in [bstack1lll11l_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࠩ᭔"), bstack1lll11l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡧࡱࡧࡳࡴࠩ᭕")]:
        return bstack1lll11l_opy_ (u"ࠬࡈࡅࡇࡑࡕࡉࡤࡇࡌࡍࠩ᭖")
    elif hook_name in [bstack1lll11l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࠪ᭗"), bstack1lll11l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡩࡹ࡮࡯ࡥࠩ᭘")]:
        return bstack1lll11l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡆࡃࡆࡌࠬ᭙")
    elif hook_name in [bstack1lll11l_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡲࡵࡤࡶ࡮ࡨࠫ᭚"), bstack1lll11l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤࡩ࡬ࡢࡵࡶࠫ᭛")]:
        return bstack1lll11l_opy_ (u"ࠫࡆࡌࡔࡆࡔࡢࡅࡑࡒࠧ᭜")
    return hook_name
def bstack11l111l1l1l_opy_(node, scenario):
    if hasattr(node, bstack1lll11l_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧ᭝")):
        parts = node.nodeid.rsplit(bstack1lll11l_opy_ (u"ࠨ࡛ࠣ᭞"))
        params = parts[-1]
        return bstack1lll11l_opy_ (u"ࠢࡼࡿࠣ࡟ࢀࢃࠢ᭟").format(scenario.name, params)
    return scenario.name
def bstack11l111l11l1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack1lll11l_opy_ (u"ࠨࡥࡤࡰࡱࡹࡰࡦࡥࠪ᭠")):
            examples = list(node.callspec.params[bstack1lll11l_opy_ (u"ࠩࡢࡴࡾࡺࡥࡴࡶࡢࡦࡩࡪ࡟ࡦࡺࡤࡱࡵࡲࡥࠨ᭡")].values())
        return examples
    except:
        return []
def bstack11l1111lll1_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111l11ll_opy_(report):
    try:
        status = bstack1lll11l_opy_ (u"ࠪࡪࡦ࡯࡬ࡦࡦࠪ᭢")
        if report.passed or (report.failed and hasattr(report, bstack1lll11l_opy_ (u"ࠦࡼࡧࡳࡹࡨࡤ࡭ࡱࠨ᭣"))):
            status = bstack1lll11l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ᭤")
        elif report.skipped:
            status = bstack1lll11l_opy_ (u"࠭ࡳ࡬࡫ࡳࡴࡪࡪࠧ᭥")
        bstack11ll1111111_opy_(status)
    except:
        pass
def bstack1ll1l1ll11_opy_(status):
    try:
        bstack11l1111llll_opy_ = bstack1lll11l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᭦")
        if status == bstack1lll11l_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨ᭧"):
            bstack11l1111llll_opy_ = bstack1lll11l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ᭨")
        elif status == bstack1lll11l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ᭩"):
            bstack11l1111llll_opy_ = bstack1lll11l_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ᭪")
        bstack11ll1111111_opy_(bstack11l1111llll_opy_)
    except:
        pass
def bstack11l111l1lll_opy_(item=None, report=None, summary=None, extra=None):
    return
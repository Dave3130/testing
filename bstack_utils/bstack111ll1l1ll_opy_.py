# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import re
from bstack_utils.bstack11ll111ll_opy_ import bstack11ll11111ll_opy_
def bstack11l111l1l1l_opy_(fixture_name):
    if fixture_name.startswith(bstack11ll1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᭃ")):
        return bstack11ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯᭄ࠩ")
    elif fixture_name.startswith(bstack11ll1l_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᭅ")):
        return bstack11ll1l_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩᭆ")
    elif fixture_name.startswith(bstack11ll1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩᭇ")):
        return bstack11ll1l_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩᭈ")
    elif fixture_name.startswith(bstack11ll1l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫᭉ")):
        return bstack11ll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩᭊ")
def bstack11l1111llll_opy_(fixture_name):
    return bool(re.match(bstack11ll1l_opy_ (u"ࠨࡠࡢࡼࡺࡴࡩࡵࡡࠫࡷࡪࡺࡵࡱࡾࡷࡩࡦࡸࡤࡰࡹࡱ࠭ࡤ࠮ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡽ࡯ࡲࡨࡺࡲࡥࠪࡡࡩ࡭ࡽࡺࡵࡳࡧࡢ࠲࠯࠭ᭋ"), fixture_name))
def bstack11l1111lll1_opy_(fixture_name):
    return bool(re.match(bstack11ll1l_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪᭌ"), fixture_name))
def bstack11l111l11ll_opy_(fixture_name):
    return bool(re.match(bstack11ll1l_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࡤ࡮ࡤࡷࡸࡥࡦࡪࡺࡷࡹࡷ࡫࡟࠯ࠬࠪ᭍"), fixture_name))
def bstack11l111ll11l_opy_(fixture_name):
    if fixture_name.startswith(bstack11ll1l_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᭎")):
        return bstack11ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭᭏"), bstack11ll1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫ᭐")
    elif fixture_name.startswith(bstack11ll1l_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᭑")):
        return bstack11ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࠭࡮ࡱࡧࡹࡱ࡫ࠧ᭒"), bstack11ll1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭᭓")
    elif fixture_name.startswith(bstack11ll1l_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᭔")):
        return bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨ᭕"), bstack11ll1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩ᭖")
    elif fixture_name.startswith(bstack11ll1l_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᭗")):
        return bstack11ll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡰࡳࡩࡻ࡬ࡦࠩ᭘"), bstack11ll1l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫ᭙")
    return None, None
def bstack11l111l11l1_opy_(hook_name):
    if hook_name in [bstack11ll1l_opy_ (u"ࠩࡶࡩࡹࡻࡰࠨ᭚"), bstack11ll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࠬ᭛")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l1111ll1l_opy_(hook_name):
    if hook_name in [bstack11ll1l_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࠬ᭜"), bstack11ll1l_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣࡲ࡫ࡴࡩࡱࡧࠫ᭝")]:
        return bstack11ll1l_opy_ (u"࠭ࡂࡆࡈࡒࡖࡊࡥࡅࡂࡅࡋࠫ᭞")
    elif hook_name in [bstack11ll1l_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡰࡦࡸࡰࡪ࠭᭟"), bstack11ll1l_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟ࡤ࡮ࡤࡷࡸ࠭᭠")]:
        return bstack11ll1l_opy_ (u"ࠩࡅࡉࡋࡕࡒࡆࡡࡄࡐࡑ࠭᭡")
    elif hook_name in [bstack11ll1l_opy_ (u"ࠪࡸࡪࡧࡲࡥࡱࡺࡲࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧ᭢"), bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥ࡭ࡦࡶ࡫ࡳࡩ࠭᭣")]:
        return bstack11ll1l_opy_ (u"ࠬࡇࡆࡕࡇࡕࡣࡊࡇࡃࡉࠩ᭤")
    elif hook_name in [bstack11ll1l_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡲࡨࡺࡲࡥࠨ᭥"), bstack11ll1l_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡦࡰࡦࡹࡳࠨ᭦")]:
        return bstack11ll1l_opy_ (u"ࠨࡃࡉࡘࡊࡘ࡟ࡂࡎࡏࠫ᭧")
    return hook_name
def bstack11l111l1l11_opy_(node, scenario):
    if hasattr(node, bstack11ll1l_opy_ (u"ࠩࡦࡥࡱࡲࡳࡱࡧࡦࠫ᭨")):
        parts = node.nodeid.rsplit(bstack11ll1l_opy_ (u"ࠥ࡟ࠧ᭩"))
        params = parts[-1]
        return bstack11ll1l_opy_ (u"ࠦࢀࢃࠠ࡜ࡽࢀࠦ᭪").format(scenario.name, params)
    return scenario.name
def bstack11l111l111l_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11ll1l_opy_ (u"ࠬࡩࡡ࡭࡮ࡶࡴࡪࡩࠧ᭫")):
            examples = list(node.callspec.params[bstack11ll1l_opy_ (u"࠭࡟ࡱࡻࡷࡩࡸࡺ࡟ࡣࡦࡧࡣࡪࡾࡡ࡮ࡲ࡯ࡩ᭬ࠬ")].values())
        return examples
    except:
        return []
def bstack11l111l1ll1_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l111ll111_opy_(report):
    try:
        status = bstack11ll1l_opy_ (u"ࠧࡧࡣ࡬ࡰࡪࡪࠧ᭭")
        if report.passed or (report.failed and hasattr(report, bstack11ll1l_opy_ (u"ࠣࡹࡤࡷࡽ࡬ࡡࡪ࡮ࠥ᭮"))):
            status = bstack11ll1l_opy_ (u"ࠩࡳࡥࡸࡹࡥࡥࠩ᭯")
        elif report.skipped:
            status = bstack11ll1l_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫ᭰")
        bstack11ll11111ll_opy_(status)
    except:
        pass
def bstack11l111l1ll_opy_(status):
    try:
        bstack11l111l1111_opy_ = bstack11ll1l_opy_ (u"ࠫ࡫ࡧࡩ࡭ࡧࡧࠫ᭱")
        if status == bstack11ll1l_opy_ (u"ࠬࡶࡡࡴࡵࡨࡨࠬ᭲"):
            bstack11l111l1111_opy_ = bstack11ll1l_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭᭳")
        elif status == bstack11ll1l_opy_ (u"ࠧࡴ࡭࡬ࡴࡵ࡫ࡤࠨ᭴"):
            bstack11l111l1111_opy_ = bstack11ll1l_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩ᭵")
        bstack11ll11111ll_opy_(bstack11l111l1111_opy_)
    except:
        pass
def bstack11l111l1lll_opy_(item=None, report=None, summary=None, extra=None):
    return
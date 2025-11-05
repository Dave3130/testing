# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import re
from bstack_utils.bstack11111111l_opy_ import bstack11l1llllll1_opy_
def bstack11l1111lll1_opy_(fixture_name):
    if fixture_name.startswith(bstack11ll1ll_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᭓")):
        return bstack11ll1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫ᭔")
    elif fixture_name.startswith(bstack11ll1ll_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡸ࡫ࡴࡶࡲࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᭕")):
        return bstack11ll1ll_opy_ (u"ࠬࡹࡥࡵࡷࡳ࠱ࡲࡵࡤࡶ࡮ࡨࠫ᭖")
    elif fixture_name.startswith(bstack11ll1ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡴࡦࡣࡵࡨࡴࡽ࡮ࡠࡨࡸࡲࡨࡺࡩࡰࡰࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᭗")):
        return bstack11ll1ll_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯࠯ࡩࡹࡳࡩࡴࡪࡱࡱࠫ᭘")
    elif fixture_name.startswith(bstack11ll1ll_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡪࡺࡴࡣࡵ࡫ࡲࡲࡤ࡬ࡩࡹࡶࡸࡶࡪ࠭᭙")):
        return bstack11ll1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫ᭚")
def bstack11l1111ll11_opy_(fixture_name):
    return bool(re.match(bstack11ll1ll_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟ࠩࡨࡸࡲࡨࡺࡩࡰࡰࡿࡱࡴࡪࡵ࡭ࡧࠬࡣ࡫࡯ࡸࡵࡷࡵࡩࡤ࠴ࠪࠨ᭛"), fixture_name))
def bstack11l1111l1ll_opy_(fixture_name):
    return bool(re.match(bstack11ll1ll_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬ᭜"), fixture_name))
def bstack11l1111l1l1_opy_(fixture_name):
    return bool(re.match(bstack11ll1ll_opy_ (u"ࠬࡤ࡟ࡹࡷࡱ࡭ࡹࡥࠨࡴࡧࡷࡹࡵࢂࡴࡦࡣࡵࡨࡴࡽ࡮ࠪࡡࡦࡰࡦࡹࡳࡠࡨ࡬ࡼࡹࡻࡲࡦࡡ࠱࠮ࠬ᭝"), fixture_name))
def bstack11l1111l11l_opy_(fixture_name):
    if fixture_name.startswith(bstack11ll1ll_opy_ (u"࠭࡟ࡹࡷࡱ࡭ࡹࡥࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᭞")):
        return bstack11ll1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵ࠳ࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨ᭟"), bstack11ll1ll_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭᭠")
    elif fixture_name.startswith(bstack11ll1ll_opy_ (u"ࠩࡢࡼࡺࡴࡩࡵࡡࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᭡")):
        return bstack11ll1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱ࠯ࡰࡳࡩࡻ࡬ࡦࠩ᭢"), bstack11ll1ll_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨ᭣")
    elif fixture_name.startswith(bstack11ll1ll_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᭤")):
        return bstack11ll1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪ᭥"), bstack11ll1ll_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫ᭦")
    elif fixture_name.startswith(bstack11ll1ll_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࡢࡪ࡮ࡾࡴࡶࡴࡨࠫ᭧")):
        return bstack11ll1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱ࠱ࡲࡵࡤࡶ࡮ࡨࠫ᭨"), bstack11ll1ll_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭᭩")
    return None, None
def bstack11l1111llll_opy_(hook_name):
    if hook_name in [bstack11ll1ll_opy_ (u"ࠫࡸ࡫ࡴࡶࡲࠪ᭪"), bstack11ll1ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴࠧ᭫")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l111l111l_opy_(hook_name):
    if hook_name in [bstack11ll1ll_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴ᭬ࠧ"), bstack11ll1ll_opy_ (u"ࠧࡴࡧࡷࡹࡵࡥ࡭ࡦࡶ࡫ࡳࡩ࠭᭭")]:
        return bstack11ll1ll_opy_ (u"ࠨࡄࡈࡊࡔࡘࡅࡠࡇࡄࡇࡍ࠭᭮")
    elif hook_name in [bstack11ll1ll_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠ࡯ࡲࡨࡺࡲࡥࠨ᭯"), bstack11ll1ll_opy_ (u"ࠪࡷࡪࡺࡵࡱࡡࡦࡰࡦࡹࡳࠨ᭰")]:
        return bstack11ll1ll_opy_ (u"ࠫࡇࡋࡆࡐࡔࡈࡣࡆࡒࡌࠨ᭱")
    elif hook_name in [bstack11ll1ll_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ᭲"), bstack11ll1ll_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮ࡠ࡯ࡨࡸ࡭ࡵࡤࠨ᭳")]:
        return bstack11ll1ll_opy_ (u"ࠧࡂࡈࡗࡉࡗࡥࡅࡂࡅࡋࠫ᭴")
    elif hook_name in [bstack11ll1ll_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡱࡴࡪࡵ࡭ࡧࠪ᭵"), bstack11ll1ll_opy_ (u"ࠩࡷࡩࡦࡸࡤࡰࡹࡱࡣࡨࡲࡡࡴࡵࠪ᭶")]:
        return bstack11ll1ll_opy_ (u"ࠪࡅࡋ࡚ࡅࡓࡡࡄࡐࡑ࠭᭷")
    return hook_name
def bstack11l1111ll1l_opy_(node, scenario):
    if hasattr(node, bstack11ll1ll_opy_ (u"ࠫࡨࡧ࡬࡭ࡵࡳࡩࡨ࠭᭸")):
        parts = node.nodeid.rsplit(bstack11ll1ll_opy_ (u"ࠧࡡࠢ᭹"))
        params = parts[-1]
        return bstack11ll1ll_opy_ (u"ࠨࡻࡾࠢ࡞ࡿࢂࠨ᭺").format(scenario.name, params)
    return scenario.name
def bstack11l111l1111_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11ll1ll_opy_ (u"ࠧࡤࡣ࡯ࡰࡸࡶࡥࡤࠩ᭻")):
            examples = list(node.callspec.params[bstack11ll1ll_opy_ (u"ࠨࡡࡳࡽࡹ࡫ࡳࡵࡡࡥࡨࡩࡥࡥࡹࡣࡰࡴࡱ࡫ࠧ᭼")].values())
        return examples
    except:
        return []
def bstack11l111l1l11_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l1111l111_opy_(report):
    try:
        status = bstack11ll1ll_opy_ (u"ࠩࡩࡥ࡮ࡲࡥࡥࠩ᭽")
        if report.passed or (report.failed and hasattr(report, bstack11ll1ll_opy_ (u"ࠥࡻࡦࡹࡸࡧࡣ࡬ࡰࠧ᭾"))):
            status = bstack11ll1ll_opy_ (u"ࠫࡵࡧࡳࡴࡧࡧࠫ᭿")
        elif report.skipped:
            status = bstack11ll1ll_opy_ (u"ࠬࡹ࡫ࡪࡲࡳࡩࡩ࠭ᮀ")
        bstack11l1llllll1_opy_(status)
    except:
        pass
def bstack1ll1l11l11_opy_(status):
    try:
        bstack11l111l11l1_opy_ = bstack11ll1ll_opy_ (u"࠭ࡦࡢ࡫࡯ࡩࡩ࠭ᮁ")
        if status == bstack11ll1ll_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᮂ"):
            bstack11l111l11l1_opy_ = bstack11ll1ll_opy_ (u"ࠨࡲࡤࡷࡸ࡫ࡤࠨᮃ")
        elif status == bstack11ll1ll_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᮄ"):
            bstack11l111l11l1_opy_ = bstack11ll1ll_opy_ (u"ࠪࡷࡰ࡯ࡰࡱࡧࡧࠫᮅ")
        bstack11l1llllll1_opy_(bstack11l111l11l1_opy_)
    except:
        pass
def bstack11l111l11ll_opy_(item=None, report=None, summary=None, extra=None):
    return
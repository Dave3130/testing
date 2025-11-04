# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import re
from bstack_utils.bstack11ll1l111l_opy_ import bstack11l1llll11l_opy_
def bstack11l1111ll11_opy_(fixture_name):
    if fixture_name.startswith(bstack11l1111_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᭒")):
        return bstack11l1111_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪ᭓")
    elif fixture_name.startswith(bstack11l1111_opy_ (u"ࠪࡣࡽࡻ࡮ࡪࡶࡢࡷࡪࡺࡵࡱࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᭔")):
        return bstack11l1111_opy_ (u"ࠫࡸ࡫ࡴࡶࡲ࠰ࡱࡴࡪࡵ࡭ࡧࠪ᭕")
    elif fixture_name.startswith(bstack11l1111_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡺࡥࡢࡴࡧࡳࡼࡴ࡟ࡧࡷࡱࡧࡹ࡯࡯࡯ࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᭖")):
        return bstack11l1111_opy_ (u"࠭ࡴࡦࡣࡵࡨࡴࡽ࡮࠮ࡨࡸࡲࡨࡺࡩࡰࡰࠪ᭗")
    elif fixture_name.startswith(bstack11l1111_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡩࡹࡳࡩࡴࡪࡱࡱࡣ࡫࡯ࡸࡵࡷࡵࡩࠬ᭘")):
        return bstack11l1111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡱࡴࡪࡵ࡭ࡧࠪ᭙")
def bstack11l1111llll_opy_(fixture_name):
    return bool(re.match(bstack11l1111_opy_ (u"ࠩࡡࡣࡽࡻ࡮ࡪࡶࡢࠬࡸ࡫ࡴࡶࡲࡿࡸࡪࡧࡲࡥࡱࡺࡲ࠮ࡥࠨࡧࡷࡱࡧࡹ࡯࡯࡯ࡾࡰࡳࡩࡻ࡬ࡦࠫࡢࡪ࡮ࡾࡴࡶࡴࡨࡣ࠳࠰ࠧ᭚"), fixture_name))
def bstack11l1111l1ll_opy_(fixture_name):
    return bool(re.match(bstack11l1111_opy_ (u"ࠪࡢࡤࡾࡵ࡯࡫ࡷࡣ࠭ࡹࡥࡵࡷࡳࢀࡹ࡫ࡡࡳࡦࡲࡻࡳ࠯࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠ࠰࠭ࠫ᭛"), fixture_name))
def bstack11l1111l11l_opy_(fixture_name):
    return bool(re.match(bstack11l1111_opy_ (u"ࠫࡣࡥࡸࡶࡰ࡬ࡸࡤ࠮ࡳࡦࡶࡸࡴࢁࡺࡥࡢࡴࡧࡳࡼࡴࠩࡠࡥ࡯ࡥࡸࡹ࡟ࡧ࡫ࡻࡸࡺࡸࡥࡠ࠰࠭ࠫ᭜"), fixture_name))
def bstack11l1111l1l1_opy_(fixture_name):
    if fixture_name.startswith(bstack11l1111_opy_ (u"ࠬࡥࡸࡶࡰ࡬ࡸࡤࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࡥࡦࡪࡺࡷࡹࡷ࡫ࠧ᭝")):
        return bstack11l1111_opy_ (u"࠭ࡳࡦࡶࡸࡴ࠲࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠧ᭞"), bstack11l1111_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬ᭟")
    elif fixture_name.startswith(bstack11l1111_opy_ (u"ࠨࡡࡻࡹࡳ࡯ࡴࡠࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫࡟ࡧ࡫ࡻࡸࡺࡸࡥࠨ᭠")):
        return bstack11l1111_opy_ (u"ࠩࡶࡩࡹࡻࡰ࠮࡯ࡲࡨࡺࡲࡥࠨ᭡"), bstack11l1111_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧ᭢")
    elif fixture_name.startswith(bstack11l1111_opy_ (u"ࠫࡤࡾࡵ࡯࡫ࡷࡣࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࡠࡨ࡬ࡼࡹࡻࡲࡦࠩ᭣")):
        return bstack11l1111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࠭ࡧࡷࡱࡧࡹ࡯࡯࡯ࠩ᭤"), bstack11l1111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪ᭥")
    elif fixture_name.startswith(bstack11l1111_opy_ (u"ࠧࡠࡺࡸࡲ࡮ࡺ࡟ࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࡡࡩ࡭ࡽࡺࡵࡳࡧࠪ᭦")):
        return bstack11l1111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰ࠰ࡱࡴࡪࡵ࡭ࡧࠪ᭧"), bstack11l1111_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡃࡏࡐࠬ᭨")
    return None, None
def bstack11l111l1111_opy_(hook_name):
    if hook_name in [bstack11l1111_opy_ (u"ࠪࡷࡪࡺࡵࡱࠩ᭩"), bstack11l1111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳ࠭᭪")]:
        return hook_name.capitalize()
    return hook_name
def bstack11l1111ll1l_opy_(hook_name):
    if hook_name in [bstack11l1111_opy_ (u"ࠬࡹࡥࡵࡷࡳࡣ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳ࠭᭫"), bstack11l1111_opy_ (u"࠭ࡳࡦࡶࡸࡴࡤࡳࡥࡵࡪࡲࡨ᭬ࠬ")]:
        return bstack11l1111_opy_ (u"ࠧࡃࡇࡉࡓࡗࡋ࡟ࡆࡃࡆࡌࠬ᭭")
    elif hook_name in [bstack11l1111_opy_ (u"ࠨࡵࡨࡸࡺࡶ࡟࡮ࡱࡧࡹࡱ࡫ࠧ᭮"), bstack11l1111_opy_ (u"ࠩࡶࡩࡹࡻࡰࡠࡥ࡯ࡥࡸࡹࠧ᭯")]:
        return bstack11l1111_opy_ (u"ࠪࡆࡊࡌࡏࡓࡇࡢࡅࡑࡒࠧ᭰")
    elif hook_name in [bstack11l1111_opy_ (u"ࠫࡹ࡫ࡡࡳࡦࡲࡻࡳࡥࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠨ᭱"), bstack11l1111_opy_ (u"ࠬࡺࡥࡢࡴࡧࡳࡼࡴ࡟࡮ࡧࡷ࡬ࡴࡪࠧ᭲")]:
        return bstack11l1111_opy_ (u"࠭ࡁࡇࡖࡈࡖࡤࡋࡁࡄࡊࠪ᭳")
    elif hook_name in [bstack11l1111_opy_ (u"ࠧࡵࡧࡤࡶࡩࡵࡷ࡯ࡡࡰࡳࡩࡻ࡬ࡦࠩ᭴"), bstack11l1111_opy_ (u"ࠨࡶࡨࡥࡷࡪ࡯ࡸࡰࡢࡧࡱࡧࡳࡴࠩ᭵")]:
        return bstack11l1111_opy_ (u"ࠩࡄࡊ࡙ࡋࡒࡠࡃࡏࡐࠬ᭶")
    return hook_name
def bstack11l1111l111_opy_(node, scenario):
    if hasattr(node, bstack11l1111_opy_ (u"ࠪࡧࡦࡲ࡬ࡴࡲࡨࡧࠬ᭷")):
        parts = node.nodeid.rsplit(bstack11l1111_opy_ (u"ࠦࡠࠨ᭸"))
        params = parts[-1]
        return bstack11l1111_opy_ (u"ࠧࢁࡽࠡ࡝ࡾࢁࠧ᭹").format(scenario.name, params)
    return scenario.name
def bstack11l111l11l1_opy_(node):
    try:
        examples = []
        if hasattr(node, bstack11l1111_opy_ (u"࠭ࡣࡢ࡮࡯ࡷࡵ࡫ࡣࠨ᭺")):
            examples = list(node.callspec.params[bstack11l1111_opy_ (u"ࠧࡠࡲࡼࡸࡪࡹࡴࡠࡤࡧࡨࡤ࡫ࡸࡢ࡯ࡳࡰࡪ࠭᭻")].values())
        return examples
    except:
        return []
def bstack11l111l11ll_opy_(feature, scenario):
    return list(feature.tags) + list(scenario.tags)
def bstack11l1111lll1_opy_(report):
    try:
        status = bstack11l1111_opy_ (u"ࠨࡨࡤ࡭ࡱ࡫ࡤࠨ᭼")
        if report.passed or (report.failed and hasattr(report, bstack11l1111_opy_ (u"ࠤࡺࡥࡸࡾࡦࡢ࡫࡯ࠦ᭽"))):
            status = bstack11l1111_opy_ (u"ࠪࡴࡦࡹࡳࡦࡦࠪ᭾")
        elif report.skipped:
            status = bstack11l1111_opy_ (u"ࠫࡸࡱࡩࡱࡲࡨࡨࠬ᭿")
        bstack11l1llll11l_opy_(status)
    except:
        pass
def bstack11l11l111_opy_(status):
    try:
        bstack11l111l111l_opy_ = bstack11l1111_opy_ (u"ࠬ࡬ࡡࡪ࡮ࡨࡨࠬᮀ")
        if status == bstack11l1111_opy_ (u"࠭ࡰࡢࡵࡶࡩࡩ࠭ᮁ"):
            bstack11l111l111l_opy_ = bstack11l1111_opy_ (u"ࠧࡱࡣࡶࡷࡪࡪࠧᮂ")
        elif status == bstack11l1111_opy_ (u"ࠨࡵ࡮࡭ࡵࡶࡥࡥࠩᮃ"):
            bstack11l111l111l_opy_ = bstack11l1111_opy_ (u"ࠩࡶ࡯࡮ࡶࡰࡦࡦࠪᮄ")
        bstack11l1llll11l_opy_(bstack11l111l111l_opy_)
    except:
        pass
def bstack11l111l1l11_opy_(item=None, report=None, summary=None, extra=None):
    return
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
from browserstack_sdk.bstack11111ll1_opy_ import bstack111111ll_opy_
from browserstack_sdk.bstack1l1l111l_opy_ import RobotHandler
def bstack111lll1l11_opy_(framework):
    if framework.lower() == bstack1l1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ≠"):
        return bstack111111ll_opy_.version()
    elif framework.lower() == bstack1l1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ≡"):
        return RobotHandler.version()
    elif framework.lower() == bstack1l1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ≢"):
        import behave
        return behave.__version__
    else:
        return bstack1l1_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࠬ≣")
def bstack1l11llll1l_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1l1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ≤"))
        framework_version.append(importlib.metadata.version(bstack1l1_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣ≥")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1l1_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫ≦"))
        framework_version.append(importlib.metadata.version(bstack1l1_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ≧")))
    except:
        pass
    return {
        bstack1l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ≨"): bstack1l1_opy_ (u"ࠪࡣࠬ≩").join(framework_name),
        bstack1l1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬ≪"): bstack1l1_opy_ (u"ࠬࡥࠧ≫").join(framework_version)
    }
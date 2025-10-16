# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
from browserstack_sdk.bstack1111l1l1_opy_ import bstack111111l1_opy_
from browserstack_sdk.bstack1l11ll1l_opy_ import RobotHandler
def bstack1ll1l1l11_opy_(framework):
    if framework.lower() == bstack1l_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ≋"):
        return bstack111111l1_opy_.version()
    elif framework.lower() == bstack1l_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ≌"):
        return RobotHandler.version()
    elif framework.lower() == bstack1l_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ≍"):
        import behave
        return behave.__version__
    else:
        return bstack1l_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࠬ≎")
def bstack11ll11lll_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1l_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ≏"))
        framework_version.append(importlib.metadata.version(bstack1l_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣ≐")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1l_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫ≑"))
        framework_version.append(importlib.metadata.version(bstack1l_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ≒")))
    except:
        pass
    return {
        bstack1l_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ≓"): bstack1l_opy_ (u"ࠪࡣࠬ≔").join(framework_name),
        bstack1l_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬ≕"): bstack1l_opy_ (u"ࠬࡥࠧ≖").join(framework_version)
    }
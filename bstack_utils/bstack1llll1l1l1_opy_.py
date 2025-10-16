# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
from browserstack_sdk.bstack11l11l11_opy_ import bstack1llll1l11_opy_
from browserstack_sdk.bstack1ll11l11_opy_ import RobotHandler
def bstack1ll1llll1l_opy_(framework):
    if framework.lower() == bstack1ll1ll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ≋"):
        return bstack1llll1l11_opy_.version()
    elif framework.lower() == bstack1ll1ll1_opy_ (u"ࠩࡵࡳࡧࡵࡴࠨ≌"):
        return RobotHandler.version()
    elif framework.lower() == bstack1ll1ll1_opy_ (u"ࠪࡦࡪ࡮ࡡࡷࡧࠪ≍"):
        import behave
        return behave.__version__
    else:
        return bstack1ll1ll1_opy_ (u"ࠫࡺࡴ࡫࡯ࡱࡺࡲࠬ≎")
def bstack1lll11111l_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1ll1ll1_opy_ (u"ࠬࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠧ≏"))
        framework_version.append(importlib.metadata.version(bstack1ll1ll1_opy_ (u"ࠨࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠣ≐")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1ll1ll1_opy_ (u"ࠧࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠫ≑"))
        framework_version.append(importlib.metadata.version(bstack1ll1ll1_opy_ (u"ࠣࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠧ≒")))
    except:
        pass
    return {
        bstack1ll1ll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧ≓"): bstack1ll1ll1_opy_ (u"ࠪࡣࠬ≔").join(framework_name),
        bstack1ll1ll1_opy_ (u"ࠫࡻ࡫ࡲࡴ࡫ࡲࡲࠬ≕"): bstack1ll1ll1_opy_ (u"ࠬࡥࠧ≖").join(framework_version)
    }
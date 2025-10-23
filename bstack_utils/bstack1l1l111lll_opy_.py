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
from browserstack_sdk.bstack11111l1l_opy_ import bstack1lllllll1_opy_
from browserstack_sdk.bstack1l11ll1l_opy_ import RobotHandler
def bstack11l11l11l1_opy_(framework):
    if framework.lower() == bstack11lll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭≥"):
        return bstack1lllllll1_opy_.version()
    elif framework.lower() == bstack11lll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭≦"):
        return RobotHandler.version()
    elif framework.lower() == bstack11lll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ≧"):
        import behave
        return behave.__version__
    else:
        return bstack11lll1_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࠪ≨")
def bstack1l1lll11l1_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11lll1_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ≩"))
        framework_version.append(importlib.metadata.version(bstack11lll1_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ≪")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11lll1_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩ≫"))
        framework_version.append(importlib.metadata.version(bstack11lll1_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ≬")))
    except:
        pass
    return {
        bstack11lll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ≭"): bstack11lll1_opy_ (u"ࠨࡡࠪ≮").join(framework_name),
        bstack11lll1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ≯"): bstack11lll1_opy_ (u"ࠪࡣࠬ≰").join(framework_version)
    }
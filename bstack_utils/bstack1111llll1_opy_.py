# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
from browserstack_sdk.bstack111ll11l_opy_ import bstack111l1lll_opy_
from browserstack_sdk.bstack11lll11l_opy_ import RobotHandler
def bstack1111ll1l11_opy_(framework):
    if framework.lower() == bstack111l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ≦"):
        return bstack111l1lll_opy_.version()
    elif framework.lower() == bstack111l1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ≧"):
        return RobotHandler.version()
    elif framework.lower() == bstack111l1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ≨"):
        import behave
        return behave.__version__
    else:
        return bstack111l1l_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࠫ≩")
def bstack1lll1l1l11_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack111l1l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭≪"))
        framework_version.append(importlib.metadata.version(bstack111l1l_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢ≫")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack111l1l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪ≬"))
        framework_version.append(importlib.metadata.version(bstack111l1l_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ≭")))
    except:
        pass
    return {
        bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭≮"): bstack111l1l_opy_ (u"ࠩࡢࠫ≯").join(framework_name),
        bstack111l1l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫ≰"): bstack111l1l_opy_ (u"ࠫࡤ࠭≱").join(framework_version)
    }
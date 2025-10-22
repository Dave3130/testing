# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
from browserstack_sdk.bstack1llllllll_opy_ import bstack1lll111l1_opy_
from browserstack_sdk.bstack1lll1ll1_opy_ import RobotHandler
def bstack1l1l1ll1l_opy_(framework):
    if framework.lower() == bstack1l111ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ≦"):
        return bstack1lll111l1_opy_.version()
    elif framework.lower() == bstack1l111ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ≧"):
        return RobotHandler.version()
    elif framework.lower() == bstack1l111ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ≨"):
        import behave
        return behave.__version__
    else:
        return bstack1l111ll_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࠫ≩")
def bstack11l1ll11l1_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1l111ll_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭≪"))
        framework_version.append(importlib.metadata.version(bstack1l111ll_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢ≫")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1l111ll_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪ≬"))
        framework_version.append(importlib.metadata.version(bstack1l111ll_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ≭")))
    except:
        pass
    return {
        bstack1l111ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭≮"): bstack1l111ll_opy_ (u"ࠩࡢࠫ≯").join(framework_name),
        bstack1l111ll_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫ≰"): bstack1l111ll_opy_ (u"ࠫࡤ࠭≱").join(framework_version)
    }
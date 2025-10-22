# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
from browserstack_sdk.bstack11111111_opy_ import bstack111ll11l_opy_
from browserstack_sdk.bstack1l1l1l1l_opy_ import RobotHandler
def bstack11ll1ll1l_opy_(framework):
    if framework.lower() == bstack1lllll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ≩"):
        return bstack111ll11l_opy_.version()
    elif framework.lower() == bstack1lllll1l_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ≪"):
        return RobotHandler.version()
    elif framework.lower() == bstack1lllll1l_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ≫"):
        import behave
        return behave.__version__
    else:
        return bstack1lllll1l_opy_ (u"࠭ࡵ࡯࡭ࡱࡳࡼࡴࠧ≬")
def bstack11l11l1111_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1lllll1l_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩ≭"))
        framework_version.append(importlib.metadata.version(bstack1lllll1l_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥ≮")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1lllll1l_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭≯"))
        framework_version.append(importlib.metadata.version(bstack1lllll1l_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ≰")))
    except:
        pass
    return {
        bstack1lllll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ≱"): bstack1lllll1l_opy_ (u"ࠬࡥࠧ≲").join(framework_name),
        bstack1lllll1l_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ≳"): bstack1lllll1l_opy_ (u"ࠧࡠࠩ≴").join(framework_version)
    }
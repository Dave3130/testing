# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from browserstack_sdk.bstack1111lll1_opy_ import bstack1llll1lll_opy_
from browserstack_sdk.bstack1l11ll1l_opy_ import RobotHandler
def bstack11ll11llll_opy_(framework):
    if framework.lower() == bstack1lllll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭≉"):
        return bstack1llll1lll_opy_.version()
    elif framework.lower() == bstack1lllll1_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭≊"):
        return RobotHandler.version()
    elif framework.lower() == bstack1lllll1_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ≋"):
        import behave
        return behave.__version__
    else:
        return bstack1lllll1_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࠪ≌")
def bstack1l1ll11111_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1lllll1_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ≍"))
        framework_version.append(importlib.metadata.version(bstack1lllll1_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ≎")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1lllll1_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩ≏"))
        framework_version.append(importlib.metadata.version(bstack1lllll1_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ≐")))
    except:
        pass
    return {
        bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ≑"): bstack1lllll1_opy_ (u"ࠨࡡࠪ≒").join(framework_name),
        bstack1lllll1_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ≓"): bstack1lllll1_opy_ (u"ࠪࡣࠬ≔").join(framework_version)
    }
# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
from browserstack_sdk.bstack1111ll1l_opy_ import bstack11l11ll1_opy_
from browserstack_sdk.bstack1ll111ll_opy_ import RobotHandler
def bstack1ll1llllll_opy_(framework):
    if framework.lower() == bstack1l1lll1_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ≆"):
        return bstack11l11ll1_opy_.version()
    elif framework.lower() == bstack1l1lll1_opy_ (u"ࠫࡷࡵࡢࡰࡶࠪ≇"):
        return RobotHandler.version()
    elif framework.lower() == bstack1l1lll1_opy_ (u"ࠬࡨࡥࡩࡣࡹࡩࠬ≈"):
        import behave
        return behave.__version__
    else:
        return bstack1l1lll1_opy_ (u"࠭ࡵ࡯࡭ࡱࡳࡼࡴࠧ≉")
def bstack1l1ll1l1l_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1l1lll1_opy_ (u"ࠧࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠩ≊"))
        framework_version.append(importlib.metadata.version(bstack1l1lll1_opy_ (u"ࠣࡵࡨࡰࡪࡴࡩࡶ࡯ࠥ≋")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1l1lll1_opy_ (u"ࠩࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹ࠭≌"))
        framework_version.append(importlib.metadata.version(bstack1l1lll1_opy_ (u"ࠥࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠢ≍")))
    except:
        pass
    return {
        bstack1l1lll1_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ≎"): bstack1l1lll1_opy_ (u"ࠬࡥࠧ≏").join(framework_name),
        bstack1l1lll1_opy_ (u"࠭ࡶࡦࡴࡶ࡭ࡴࡴࠧ≐"): bstack1l1lll1_opy_ (u"ࠧࡠࠩ≑").join(framework_version)
    }
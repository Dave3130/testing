# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
from browserstack_sdk.bstack1llll111l_opy_ import bstack111l1l11_opy_
from browserstack_sdk.bstack1lll11l1_opy_ import RobotHandler
def bstack1l111lll1l_opy_(framework):
    if framework.lower() == bstack1ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ≃"):
        return bstack111l1l11_opy_.version()
    elif framework.lower() == bstack1ll1l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ≄"):
        return RobotHandler.version()
    elif framework.lower() == bstack1ll1l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ≅"):
        import behave
        return behave.__version__
    else:
        return bstack1ll1l_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࠫ≆")
def bstack1l1ll1l11_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1ll1l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭≇"))
        framework_version.append(importlib.metadata.version(bstack1ll1l_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢ≈")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1ll1l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪ≉"))
        framework_version.append(importlib.metadata.version(bstack1ll1l_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ≊")))
    except:
        pass
    return {
        bstack1ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭≋"): bstack1ll1l_opy_ (u"ࠩࡢࠫ≌").join(framework_name),
        bstack1ll1l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫ≍"): bstack1ll1l_opy_ (u"ࠫࡤ࠭≎").join(framework_version)
    }
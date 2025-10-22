# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
from browserstack_sdk.bstack1lll11l11_opy_ import bstack1lllll11l_opy_
from browserstack_sdk.bstack1llll11l_opy_ import RobotHandler
def bstack1l1ll11l1l_opy_(framework):
    if framework.lower() == bstack11l1l11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭≥"):
        return bstack1lllll11l_opy_.version()
    elif framework.lower() == bstack11l1l11_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭≦"):
        return RobotHandler.version()
    elif framework.lower() == bstack11l1l11_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ≧"):
        import behave
        return behave.__version__
    else:
        return bstack11l1l11_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࠪ≨")
def bstack1lll11l1ll_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11l1l11_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ≩"))
        framework_version.append(importlib.metadata.version(bstack11l1l11_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ≪")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11l1l11_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩ≫"))
        framework_version.append(importlib.metadata.version(bstack11l1l11_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ≬")))
    except:
        pass
    return {
        bstack11l1l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ≭"): bstack11l1l11_opy_ (u"ࠨࡡࠪ≮").join(framework_name),
        bstack11l1l11_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ≯"): bstack11l1l11_opy_ (u"ࠪࡣࠬ≰").join(framework_version)
    }
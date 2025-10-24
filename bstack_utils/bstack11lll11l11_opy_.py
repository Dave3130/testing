# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
from browserstack_sdk.bstack1111l11l_opy_ import bstack1lll1ll1l_opy_
from browserstack_sdk.bstack1llll1l1_opy_ import RobotHandler
def bstack1l111l1l11_opy_(framework):
    if framework.lower() == bstack11l11l1_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ≟"):
        return bstack1lll1ll1l_opy_.version()
    elif framework.lower() == bstack11l11l1_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ≠"):
        return RobotHandler.version()
    elif framework.lower() == bstack11l11l1_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ≡"):
        import behave
        return behave.__version__
    else:
        return bstack11l11l1_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࠫ≢")
def bstack1lll111111_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11l11l1_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭≣"))
        framework_version.append(importlib.metadata.version(bstack11l11l1_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢ≤")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11l11l1_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪ≥"))
        framework_version.append(importlib.metadata.version(bstack11l11l1_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ≦")))
    except:
        pass
    return {
        bstack11l11l1_opy_ (u"ࠨࡰࡤࡱࡪ࠭≧"): bstack11l11l1_opy_ (u"ࠩࡢࠫ≨").join(framework_name),
        bstack11l11l1_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫ≩"): bstack11l11l1_opy_ (u"ࠫࡤ࠭≪").join(framework_version)
    }
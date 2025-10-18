# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
from browserstack_sdk.bstack111l111l_opy_ import bstack1lll11lll_opy_
from browserstack_sdk.bstack11llll11_opy_ import RobotHandler
def bstack1111l1111l_opy_(framework):
    if framework.lower() == bstack11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ≭"):
        return bstack1lll11lll_opy_.version()
    elif framework.lower() == bstack11ll_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ≮"):
        return RobotHandler.version()
    elif framework.lower() == bstack11ll_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ≯"):
        import behave
        return behave.__version__
    else:
        return bstack11ll_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࠫ≰")
def bstack1lll111lll_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11ll_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭≱"))
        framework_version.append(importlib.metadata.version(bstack11ll_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢ≲")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11ll_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪ≳"))
        framework_version.append(importlib.metadata.version(bstack11ll_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ≴")))
    except:
        pass
    return {
        bstack11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭≵"): bstack11ll_opy_ (u"ࠩࡢࠫ≶").join(framework_name),
        bstack11ll_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫ≷"): bstack11ll_opy_ (u"ࠫࡤ࠭≸").join(framework_version)
    }
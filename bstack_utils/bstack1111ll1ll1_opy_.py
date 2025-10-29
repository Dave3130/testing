# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
from browserstack_sdk.bstack11111ll1_opy_ import bstack1llll1lll_opy_
from browserstack_sdk.bstack1ll111l1_opy_ import RobotHandler
def bstack1l1l1l1l11_opy_(framework):
    if framework.lower() == bstack11l11ll_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ⊆"):
        return bstack1llll1lll_opy_.version()
    elif framework.lower() == bstack11l11ll_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ⊇"):
        return RobotHandler.version()
    elif framework.lower() == bstack11l11ll_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭⊈"):
        import behave
        return behave.__version__
    else:
        return bstack11l11ll_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࠨ⊉")
def bstack111l1llll_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11l11ll_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪ⊊"))
        framework_version.append(importlib.metadata.version(bstack11l11ll_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦ⊋")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11l11ll_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧ⊌"))
        framework_version.append(importlib.metadata.version(bstack11l11ll_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ⊍")))
    except:
        pass
    return {
        bstack11l11ll_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ⊎"): bstack11l11ll_opy_ (u"࠭࡟ࠨ⊏").join(framework_name),
        bstack11l11ll_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ⊐"): bstack11l11ll_opy_ (u"ࠨࡡࠪ⊑").join(framework_version)
    }
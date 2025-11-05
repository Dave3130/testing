# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
from browserstack_sdk.bstack1lllllll1_opy_ import bstack1lll111l1_opy_
from browserstack_sdk.bstack1ll1l11l_opy_ import RobotHandler
def bstack1ll111ll1l_opy_(framework):
    if framework.lower() == bstack11ll1ll_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭⊝"):
        return bstack1lll111l1_opy_.version()
    elif framework.lower() == bstack11ll1ll_opy_ (u"ࠧࡳࡱࡥࡳࡹ࠭⊞"):
        return RobotHandler.version()
    elif framework.lower() == bstack11ll1ll_opy_ (u"ࠨࡤࡨ࡬ࡦࡼࡥࠨ⊟"):
        import behave
        return behave.__version__
    else:
        return bstack11ll1ll_opy_ (u"ࠩࡸࡲࡰࡴ࡯ࡸࡰࠪ⊠")
def bstack111l11111l_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11ll1ll_opy_ (u"ࠪࡷࡪࡲࡥ࡯࡫ࡸࡱࠬ⊡"))
        framework_version.append(importlib.metadata.version(bstack11ll1ll_opy_ (u"ࠦࡸ࡫࡬ࡦࡰ࡬ࡹࡲࠨ⊢")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11ll1ll_opy_ (u"ࠬࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠩ⊣"))
        framework_version.append(importlib.metadata.version(bstack11ll1ll_opy_ (u"ࠨࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠥ⊤")))
    except:
        pass
    return {
        bstack11ll1ll_opy_ (u"ࠧ࡯ࡣࡰࡩࠬ⊥"): bstack11ll1ll_opy_ (u"ࠨࡡࠪ⊦").join(framework_name),
        bstack11ll1ll_opy_ (u"ࠩࡹࡩࡷࡹࡩࡰࡰࠪ⊧"): bstack11ll1ll_opy_ (u"ࠪࡣࠬ⊨").join(framework_version)
    }
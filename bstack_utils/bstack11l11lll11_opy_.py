# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
from browserstack_sdk.bstack11111l11_opy_ import bstack1llll1111_opy_
from browserstack_sdk.bstack11llll1l_opy_ import RobotHandler
def bstack1l1ll1l11l_opy_(framework):
    if framework.lower() == bstack111111l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩ∾"):
        return bstack1llll1111_opy_.version()
    elif framework.lower() == bstack111111l_opy_ (u"ࠪࡶࡴࡨ࡯ࡵࠩ∿"):
        return RobotHandler.version()
    elif framework.lower() == bstack111111l_opy_ (u"ࠫࡧ࡫ࡨࡢࡸࡨࠫ≀"):
        import behave
        return behave.__version__
    else:
        return bstack111111l_opy_ (u"ࠬࡻ࡮࡬ࡰࡲࡻࡳ࠭≁")
def bstack1l1111l1ll_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack111111l_opy_ (u"࠭ࡳࡦ࡮ࡨࡲ࡮ࡻ࡭ࠨ≂"))
        framework_version.append(importlib.metadata.version(bstack111111l_opy_ (u"ࠢࡴࡧ࡯ࡩࡳ࡯ࡵ࡮ࠤ≃")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack111111l_opy_ (u"ࠨࡲ࡯ࡥࡾࡽࡲࡪࡩ࡫ࡸࠬ≄"))
        framework_version.append(importlib.metadata.version(bstack111111l_opy_ (u"ࠤࡳࡰࡦࡿࡷࡳ࡫ࡪ࡬ࡹࠨ≅")))
    except:
        pass
    return {
        bstack111111l_opy_ (u"ࠪࡲࡦࡳࡥࠨ≆"): bstack111111l_opy_ (u"ࠫࡤ࠭≇").join(framework_name),
        bstack111111l_opy_ (u"ࠬࡼࡥࡳࡵ࡬ࡳࡳ࠭≈"): bstack111111l_opy_ (u"࠭࡟ࠨ≉").join(framework_version)
    }
# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
from browserstack_sdk.bstack111llll1_opy_ import bstack11111l11_opy_
from browserstack_sdk.bstack1ll1lll1_opy_ import RobotHandler
def bstack111l111ll_opy_(framework):
    if framework.lower() == bstack11l1l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ≁"):
        return bstack11111l11_opy_.version()
    elif framework.lower() == bstack11l1l11_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ≂"):
        return RobotHandler.version()
    elif framework.lower() == bstack11l1l11_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ≃"):
        import behave
        return behave.__version__
    else:
        return bstack11l1l11_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࠩ≄")
def bstack1l1ll1l1l_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11l1l11_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ≅"))
        framework_version.append(importlib.metadata.version(bstack11l1l11_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧ≆")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11l1l11_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨ≇"))
        framework_version.append(importlib.metadata.version(bstack11l1l11_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ≈")))
    except:
        pass
    return {
        bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ≉"): bstack11l1l11_opy_ (u"ࠧࡠࠩ≊").join(framework_name),
        bstack11l1l11_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ≋"): bstack11l1l11_opy_ (u"ࠩࡢࠫ≌").join(framework_version)
    }
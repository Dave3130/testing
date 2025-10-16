# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
from browserstack_sdk.bstack1lll1llll_opy_ import bstack111l11l1_opy_
from browserstack_sdk.bstack1l1ll1l1_opy_ import RobotHandler
def bstack1l11lllll_opy_(framework):
    if framework.lower() == bstack1ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ≈"):
        return bstack111l11l1_opy_.version()
    elif framework.lower() == bstack1ll11_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ≉"):
        return RobotHandler.version()
    elif framework.lower() == bstack1ll11_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ≊"):
        import behave
        return behave.__version__
    else:
        return bstack1ll11_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࠩ≋")
def bstack11ll111111_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1ll11_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ≌"))
        framework_version.append(importlib.metadata.version(bstack1ll11_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧ≍")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1ll11_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨ≎"))
        framework_version.append(importlib.metadata.version(bstack1ll11_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ≏")))
    except:
        pass
    return {
        bstack1ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ≐"): bstack1ll11_opy_ (u"ࠧࡠࠩ≑").join(framework_name),
        bstack1ll11_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ≒"): bstack1ll11_opy_ (u"ࠩࡢࠫ≓").join(framework_version)
    }
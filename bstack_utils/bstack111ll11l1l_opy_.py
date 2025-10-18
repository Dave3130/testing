# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
from browserstack_sdk.bstack1lll1ll1l_opy_ import bstack111lll11_opy_
from browserstack_sdk.bstack1ll11111_opy_ import RobotHandler
def bstack1ll1l11ll1_opy_(framework):
    if framework.lower() == bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ≫"):
        return bstack111lll11_opy_.version()
    elif framework.lower() == bstack11l111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ≬"):
        return RobotHandler.version()
    elif framework.lower() == bstack11l111_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ≭"):
        import behave
        return behave.__version__
    else:
        return bstack11l111_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࠩ≮")
def bstack111lll1l1l_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11l111_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ≯"))
        framework_version.append(importlib.metadata.version(bstack11l111_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧ≰")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11l111_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨ≱"))
        framework_version.append(importlib.metadata.version(bstack11l111_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ≲")))
    except:
        pass
    return {
        bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ≳"): bstack11l111_opy_ (u"ࠧࡠࠩ≴").join(framework_name),
        bstack11l111_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ≵"): bstack11l111_opy_ (u"ࠩࡢࠫ≶").join(framework_version)
    }
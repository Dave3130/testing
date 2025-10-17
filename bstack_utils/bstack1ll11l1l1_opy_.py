# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
from browserstack_sdk.bstack1lll1ll11_opy_ import bstack11l111ll_opy_
from browserstack_sdk.bstack1ll1ll1l_opy_ import RobotHandler
def bstack111l1l1l1_opy_(framework):
    if framework.lower() == bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ∹"):
        return bstack11l111ll_opy_.version()
    elif framework.lower() == bstack11111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ∺"):
        return RobotHandler.version()
    elif framework.lower() == bstack11111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭∻"):
        import behave
        return behave.__version__
    else:
        return bstack11111_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࠨ∼")
def bstack1l1l11ll11_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11111_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪ∽"))
        framework_version.append(importlib.metadata.version(bstack11111_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦ∾")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧ∿"))
        framework_version.append(importlib.metadata.version(bstack11111_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ≀")))
    except:
        pass
    return {
        bstack11111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ≁"): bstack11111_opy_ (u"࠭࡟ࠨ≂").join(framework_name),
        bstack11111_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ≃"): bstack11111_opy_ (u"ࠨࡡࠪ≄").join(framework_version)
    }
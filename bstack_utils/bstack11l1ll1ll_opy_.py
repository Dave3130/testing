# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
from browserstack_sdk.bstack11111l11_opy_ import bstack1111l1l1_opy_
from browserstack_sdk.bstack1l1l111l_opy_ import RobotHandler
def bstack11ll11l1l_opy_(framework):
    if framework.lower() == bstack11l111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ∹"):
        return bstack1111l1l1_opy_.version()
    elif framework.lower() == bstack11l111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ∺"):
        return RobotHandler.version()
    elif framework.lower() == bstack11l111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭∻"):
        import behave
        return behave.__version__
    else:
        return bstack11l111_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࠨ∼")
def bstack1lllll11l1_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11l111_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪ∽"))
        framework_version.append(importlib.metadata.version(bstack11l111_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦ∾")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11l111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧ∿"))
        framework_version.append(importlib.metadata.version(bstack11l111_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ≀")))
    except:
        pass
    return {
        bstack11l111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ≁"): bstack11l111_opy_ (u"࠭࡟ࠨ≂").join(framework_name),
        bstack11l111_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ≃"): bstack11l111_opy_ (u"ࠨࡡࠪ≄").join(framework_version)
    }
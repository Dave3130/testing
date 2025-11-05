# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
from browserstack_sdk.bstack1lll1llll_opy_ import bstack1llllll1l_opy_
from browserstack_sdk.bstack1ll1llll_opy_ import RobotHandler
def bstack1llll11l1l_opy_(framework):
    if framework.lower() == bstack11111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ⊜"):
        return bstack1llllll1l_opy_.version()
    elif framework.lower() == bstack11111_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ⊝"):
        return RobotHandler.version()
    elif framework.lower() == bstack11111_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ⊞"):
        import behave
        return behave.__version__
    else:
        return bstack11111_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࠩ⊟")
def bstack1ll1lll111_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11111_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ⊠"))
        framework_version.append(importlib.metadata.version(bstack11111_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧ⊡")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11111_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨ⊢"))
        framework_version.append(importlib.metadata.version(bstack11111_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ⊣")))
    except:
        pass
    return {
        bstack11111_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ⊤"): bstack11111_opy_ (u"ࠧࡠࠩ⊥").join(framework_name),
        bstack11111_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ⊦"): bstack11111_opy_ (u"ࠩࡢࠫ⊧").join(framework_version)
    }
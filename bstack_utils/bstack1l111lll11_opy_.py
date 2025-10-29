# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
from browserstack_sdk.bstack1llll1lll_opy_ import bstack1111llll_opy_
from browserstack_sdk.bstack1ll1ll1l_opy_ import RobotHandler
def bstack11111l1111_opy_(framework):
    if framework.lower() == bstack11ll1l_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ⊇"):
        return bstack1111llll_opy_.version()
    elif framework.lower() == bstack11ll1l_opy_ (u"࠭ࡲࡰࡤࡲࡸࠬ⊈"):
        return RobotHandler.version()
    elif framework.lower() == bstack11ll1l_opy_ (u"ࠧࡣࡧ࡫ࡥࡻ࡫ࠧ⊉"):
        import behave
        return behave.__version__
    else:
        return bstack11ll1l_opy_ (u"ࠨࡷࡱ࡯ࡳࡵࡷ࡯ࠩ⊊")
def bstack1l1l1l1l1l_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11ll1l_opy_ (u"ࠩࡶࡩࡱ࡫࡮ࡪࡷࡰࠫ⊋"))
        framework_version.append(importlib.metadata.version(bstack11ll1l_opy_ (u"ࠥࡷࡪࡲࡥ࡯࡫ࡸࡱࠧ⊌")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11ll1l_opy_ (u"ࠫࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠨ⊍"))
        framework_version.append(importlib.metadata.version(bstack11ll1l_opy_ (u"ࠧࡶ࡬ࡢࡻࡺࡶ࡮࡭ࡨࡵࠤ⊎")))
    except:
        pass
    return {
        bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫ⊏"): bstack11ll1l_opy_ (u"ࠧࡠࠩ⊐").join(framework_name),
        bstack11ll1l_opy_ (u"ࠨࡸࡨࡶࡸ࡯࡯࡯ࠩ⊑"): bstack11ll1l_opy_ (u"ࠩࡢࠫ⊒").join(framework_version)
    }
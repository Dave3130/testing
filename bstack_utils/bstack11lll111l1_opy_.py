# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
from browserstack_sdk.bstack1llllllll_opy_ import bstack1111l111_opy_
from browserstack_sdk.bstack1ll1l1ll_opy_ import RobotHandler
def bstack1111ll11l_opy_(framework):
    if framework.lower() == bstack1lll11l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ⊂"):
        return bstack1111l111_opy_.version()
    elif framework.lower() == bstack1lll11l_opy_ (u"ࠨࡴࡲࡦࡴࡺࠧ⊃"):
        return RobotHandler.version()
    elif framework.lower() == bstack1lll11l_opy_ (u"ࠩࡥࡩ࡭ࡧࡶࡦࠩ⊄"):
        import behave
        return behave.__version__
    else:
        return bstack1lll11l_opy_ (u"ࠪࡹࡳࡱ࡮ࡰࡹࡱࠫ⊅")
def bstack11111ll11_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack1lll11l_opy_ (u"ࠫࡸ࡫࡬ࡦࡰ࡬ࡹࡲ࠭⊆"))
        framework_version.append(importlib.metadata.version(bstack1lll11l_opy_ (u"ࠧࡹࡥ࡭ࡧࡱ࡭ࡺࡳࠢ⊇")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack1lll11l_opy_ (u"࠭ࡰ࡭ࡣࡼࡻࡷ࡯ࡧࡩࡶࠪ⊈"))
        framework_version.append(importlib.metadata.version(bstack1lll11l_opy_ (u"ࠢࡱ࡮ࡤࡽࡼࡸࡩࡨࡪࡷࠦ⊉")))
    except:
        pass
    return {
        bstack1lll11l_opy_ (u"ࠨࡰࡤࡱࡪ࠭⊊"): bstack1lll11l_opy_ (u"ࠩࡢࠫ⊋").join(framework_name),
        bstack1lll11l_opy_ (u"ࠪࡺࡪࡸࡳࡪࡱࡱࠫ⊌"): bstack1lll11l_opy_ (u"ࠫࡤ࠭⊍").join(framework_version)
    }
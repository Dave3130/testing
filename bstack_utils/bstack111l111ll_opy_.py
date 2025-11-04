# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
from browserstack_sdk.bstack1111l1l1_opy_ import bstack1lllll111_opy_
from browserstack_sdk.bstack11lll111_opy_ import RobotHandler
def bstack11l1ll1111_opy_(framework):
    if framework.lower() == bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫ⊛"):
        return bstack1lllll111_opy_.version()
    elif framework.lower() == bstack11l1111_opy_ (u"ࠬࡸ࡯ࡣࡱࡷࠫ⊜"):
        return RobotHandler.version()
    elif framework.lower() == bstack11l1111_opy_ (u"࠭ࡢࡦࡪࡤࡺࡪ࠭⊝"):
        import behave
        return behave.__version__
    else:
        return bstack11l1111_opy_ (u"ࠧࡶࡰ࡮ࡲࡴࡽ࡮ࠨ⊞")
def bstack1l1ll11lll_opy_():
    import importlib.metadata
    framework_name = []
    framework_version = []
    try:
        from selenium import webdriver
        framework_name.append(bstack11l1111_opy_ (u"ࠨࡵࡨࡰࡪࡴࡩࡶ࡯ࠪ⊟"))
        framework_version.append(importlib.metadata.version(bstack11l1111_opy_ (u"ࠤࡶࡩࡱ࡫࡮ࡪࡷࡰࠦ⊠")))
    except:
        pass
    try:
        import playwright
        framework_name.append(bstack11l1111_opy_ (u"ࠪࡴࡱࡧࡹࡸࡴ࡬࡫࡭ࡺࠧ⊡"))
        framework_version.append(importlib.metadata.version(bstack11l1111_opy_ (u"ࠦࡵࡲࡡࡺࡹࡵ࡭࡬࡮ࡴࠣ⊢")))
    except:
        pass
    return {
        bstack11l1111_opy_ (u"ࠬࡴࡡ࡮ࡧࠪ⊣"): bstack11l1111_opy_ (u"࠭࡟ࠨ⊤").join(framework_name),
        bstack11l1111_opy_ (u"ࠧࡷࡧࡵࡷ࡮ࡵ࡮ࠨ⊥"): bstack11l1111_opy_ (u"ࠨࡡࠪ⊦").join(framework_version)
    }
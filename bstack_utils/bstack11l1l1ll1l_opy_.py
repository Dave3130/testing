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
import threading
import logging
import bstack_utils.accessibility as bstack11l11lll_opy_
from bstack_utils.helper import bstack1ll1ll11_opy_
logger = logging.getLogger(__name__)
def bstack11l1l1l11l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack11111l1l1_opy_(context, *args):
    tags = getattr(args[0], bstack1ll11_opy_ (u"ࠫࡹࡧࡧࡴࠩᬹ"), [])
    bstack111lll1ll1_opy_ = bstack11l11lll_opy_.bstack1llllll1l1_opy_(tags)
    threading.current_thread().isA11yTest = bstack111lll1ll1_opy_
    try:
      bstack11l1111l11_opy_ = threading.current_thread().bstackSessionDriver if bstack11l1l1l11l_opy_(bstack1ll11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫᬺ")) else context.browser
      if bstack11l1111l11_opy_ and bstack11l1111l11_opy_.session_id and bstack111lll1ll1_opy_ and bstack1ll1ll11_opy_(
              threading.current_thread(), bstack1ll11_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬᬻ"), None):
          threading.current_thread().isA11yTest = bstack11l11lll_opy_.bstack111l1lll1l_opy_(bstack11l1111l11_opy_, bstack111lll1ll1_opy_)
    except Exception as e:
       logger.debug(bstack1ll11_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡤ࠵࠶ࡿࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧ࠽ࠤࢀࢃࠧᬼ").format(str(e)))
def bstack1llll11l1l_opy_(bstack11l1111l11_opy_):
    if bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬᬽ"), None) and bstack1ll1ll11_opy_(
      threading.current_thread(), bstack1ll11_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᬾ"), None) and not bstack1ll1ll11_opy_(threading.current_thread(), bstack1ll11_opy_ (u"ࠪࡥ࠶࠷ࡹࡠࡵࡷࡳࡵ࠭ᬿ"), False):
      threading.current_thread().a11y_stop = True
      bstack11l11lll_opy_.bstack1lllll1ll_opy_(bstack11l1111l11_opy_, name=bstack1ll11_opy_ (u"ࠦࠧᭀ"), path=bstack1ll11_opy_ (u"ࠧࠨᭁ"))
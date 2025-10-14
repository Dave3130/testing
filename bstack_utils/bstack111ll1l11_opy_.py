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
import threading
import logging
import bstack_utils.accessibility as bstack111l1lll_opy_
from bstack_utils.helper import bstack11lll111_opy_
logger = logging.getLogger(__name__)
def bstack11ll1lll11_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack111l1111ll_opy_(context, *args):
    tags = getattr(args[0], bstack11l1l11_opy_ (u"ࠫࡹࡧࡧࡴࠩᬲ"), [])
    bstack1lll111111_opy_ = bstack111l1lll_opy_.bstack111111l1l_opy_(tags)
    threading.current_thread().isA11yTest = bstack1lll111111_opy_
    try:
      bstack111l111l1l_opy_ = threading.current_thread().bstackSessionDriver if bstack11ll1lll11_opy_(bstack11l1l11_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫᬳ")) else context.browser
      if bstack111l111l1l_opy_ and bstack111l111l1l_opy_.session_id and bstack1lll111111_opy_ and bstack11lll111_opy_(
              threading.current_thread(), bstack11l1l11_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱ᬴ࠬ"), None):
          threading.current_thread().isA11yTest = bstack111l1lll_opy_.bstack11l111111_opy_(bstack111l111l1l_opy_, bstack1lll111111_opy_)
    except Exception as e:
       logger.debug(bstack11l1l11_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡤ࠵࠶ࡿࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧ࠽ࠤࢀࢃࠧᬵ").format(str(e)))
def bstack11ll11111l_opy_(bstack111l111l1l_opy_):
    if bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬᬶ"), None) and bstack11lll111_opy_(
      threading.current_thread(), bstack11l1l11_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᬷ"), None) and not bstack11lll111_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠪࡥ࠶࠷ࡹࡠࡵࡷࡳࡵ࠭ᬸ"), False):
      threading.current_thread().a11y_stop = True
      bstack111l1lll_opy_.bstack11l11l1l_opy_(bstack111l111l1l_opy_, name=bstack11l1l11_opy_ (u"ࠦࠧᬹ"), path=bstack11l1l11_opy_ (u"ࠧࠨᬺ"))
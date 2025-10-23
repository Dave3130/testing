# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1llll111l_opy_
from bstack_utils.helper import bstack1lll111l_opy_
logger = logging.getLogger(__name__)
def bstack1l111lll1l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack11111ll11_opy_(context, *args):
    tags = getattr(args[0], bstack111111l_opy_ (u"ࠨࡶࡤ࡫ࡸ࠭ᬯ"), [])
    bstack11lll1ll11_opy_ = bstack1llll111l_opy_.bstack11l11ll11l_opy_(tags)
    threading.current_thread().isA11yTest = bstack11lll1ll11_opy_
    try:
      bstack11l11l1lll_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111lll1l_opy_(bstack111111l_opy_ (u"ࠩࡥࡷࡹࡧࡣ࡬ࡕࡨࡷࡸ࡯࡯࡯ࡆࡵ࡭ࡻ࡫ࡲࠨᬰ")) else context.browser
      if bstack11l11l1lll_opy_ and bstack11l11l1lll_opy_.session_id and bstack11lll1ll11_opy_ and bstack1lll111l_opy_(
              threading.current_thread(), bstack111111l_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᬱ"), None):
          threading.current_thread().isA11yTest = bstack1llll111l_opy_.bstack1l111111l1_opy_(bstack11l11l1lll_opy_, bstack11lll1ll11_opy_)
    except Exception as e:
       logger.debug(bstack111111l_opy_ (u"ࠫࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡶࡤࡶࡹࠦࡡ࠲࠳ࡼࠤ࡮ࡴࠠࡣࡧ࡫ࡥࡻ࡫࠺ࠡࡽࢀࠫᬲ").format(str(e)))
def bstack1l11l111l_opy_(bstack11l11l1lll_opy_):
    if bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠬ࡯ࡳࡂ࠳࠴ࡽ࡙࡫ࡳࡵࠩᬳ"), None) and bstack1lll111l_opy_(
      threading.current_thread(), bstack111111l_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱ᬴ࠬ"), None) and not bstack1lll111l_opy_(threading.current_thread(), bstack111111l_opy_ (u"ࠧࡢ࠳࠴ࡽࡤࡹࡴࡰࡲࠪᬵ"), False):
      threading.current_thread().a11y_stop = True
      bstack1llll111l_opy_.bstack1lllllll1_opy_(bstack11l11l1lll_opy_, name=bstack111111l_opy_ (u"ࠣࠤᬶ"), path=bstack111111l_opy_ (u"ࠤࠥᬷ"))
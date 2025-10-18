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
import threading
import logging
import bstack_utils.accessibility as bstack1111l11l_opy_
from bstack_utils.helper import bstack1l1lll11_opy_
logger = logging.getLogger(__name__)
def bstack111l1l11l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack111l11l1ll_opy_(context, *args):
    tags = getattr(args[0], bstack11l111_opy_ (u"ࠫࡹࡧࡧࡴࠩ᭜"), [])
    bstack111l11ll1_opy_ = bstack1111l11l_opy_.bstack1llll111ll_opy_(tags)
    threading.current_thread().isA11yTest = bstack111l11ll1_opy_
    try:
      bstack111111l11_opy_ = threading.current_thread().bstackSessionDriver if bstack111l1l11l_opy_(bstack11l111_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫ᭝")) else context.browser
      if bstack111111l11_opy_ and bstack111111l11_opy_.session_id and bstack111l11ll1_opy_ and bstack1l1lll11_opy_(
              threading.current_thread(), bstack11l111_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬ᭞"), None):
          threading.current_thread().isA11yTest = bstack1111l11l_opy_.bstack111llll11_opy_(bstack111111l11_opy_, bstack111l11ll1_opy_)
    except Exception as e:
       logger.debug(bstack11l111_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡤ࠵࠶ࡿࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧ࠽ࠤࢀࢃࠧ᭟").format(str(e)))
def bstack111ll1lll1_opy_(bstack111111l11_opy_):
    if bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬ᭠"), None) and bstack1l1lll11_opy_(
      threading.current_thread(), bstack11l111_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨ᭡"), None) and not bstack1l1lll11_opy_(threading.current_thread(), bstack11l111_opy_ (u"ࠪࡥ࠶࠷ࡹࡠࡵࡷࡳࡵ࠭᭢"), False):
      threading.current_thread().a11y_stop = True
      bstack1111l11l_opy_.bstack1lllllll1_opy_(bstack111111l11_opy_, name=bstack11l111_opy_ (u"ࠦࠧ᭣"), path=bstack11l111_opy_ (u"ࠧࠨ᭤"))
# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1lll11l11_opy_
from bstack_utils.helper import bstack1l1l1ll1_opy_
logger = logging.getLogger(__name__)
def bstack1llll111ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack11111l1l11_opy_(context, *args):
    tags = getattr(args[0], bstack11ll1ll_opy_ (u"ࠫࡹࡧࡧࡴࠩᮆ"), [])
    bstack1ll111l11l_opy_ = bstack1lll11l11_opy_.bstack11llll11ll_opy_(tags)
    threading.current_thread().isA11yTest = bstack1ll111l11l_opy_
    try:
      bstack1l11l1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1llll111ll_opy_(bstack11ll1ll_opy_ (u"ࠬࡨࡳࡵࡣࡦ࡯ࡘ࡫ࡳࡴ࡫ࡲࡲࡉࡸࡩࡷࡧࡵࠫᮇ")) else context.browser
      if bstack1l11l1l11l_opy_ and bstack1l11l1l11l_opy_.session_id and bstack1ll111l11l_opy_ and bstack1l1l1ll1_opy_(
              threading.current_thread(), bstack11ll1ll_opy_ (u"࠭ࡡ࠲࠳ࡼࡔࡱࡧࡴࡧࡱࡵࡱࠬᮈ"), None):
          threading.current_thread().isA11yTest = bstack1lll11l11_opy_.bstack1ll1ll1l11_opy_(bstack1l11l1l11l_opy_, bstack1ll111l11l_opy_)
    except Exception as e:
       logger.debug(bstack11ll1ll_opy_ (u"ࠧࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡹࡧࡲࡵࠢࡤ࠵࠶ࡿࠠࡪࡰࠣࡦࡪ࡮ࡡࡷࡧ࠽ࠤࢀࢃࠧᮉ").format(str(e)))
def bstack1ll1l11l1l_opy_(bstack1l11l1l11l_opy_):
    if bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠨ࡫ࡶࡅ࠶࠷ࡹࡕࡧࡶࡸࠬᮊ"), None) and bstack1l1l1ll1_opy_(
      threading.current_thread(), bstack11ll1ll_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᮋ"), None) and not bstack1l1l1ll1_opy_(threading.current_thread(), bstack11ll1ll_opy_ (u"ࠪࡥ࠶࠷ࡹࡠࡵࡷࡳࡵ࠭ᮌ"), False):
      threading.current_thread().a11y_stop = True
      bstack1lll11l11_opy_.bstack111ll1l1_opy_(bstack1l11l1l11l_opy_, name=bstack11ll1ll_opy_ (u"ࠦࠧᮍ"), path=bstack11ll1ll_opy_ (u"ࠧࠨᮎ"))
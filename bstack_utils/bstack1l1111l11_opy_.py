# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1lll1ll1l_opy_
from bstack_utils.helper import bstack1l1l1l1l_opy_
logger = logging.getLogger(__name__)
def bstack1lll11ll1l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack11l1ll11l_opy_(context, *args):
    tags = getattr(args[0], bstack1l1lll1_opy_ (u"ࠧࡵࡣࡪࡷࠬᬵ"), [])
    bstack11lll11l1_opy_ = bstack1lll1ll1l_opy_.bstack1ll11111l1_opy_(tags)
    threading.current_thread().isA11yTest = bstack11lll11l1_opy_
    try:
      bstack1111l1111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1lll11ll1l_opy_(bstack1l1lll1_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧᬶ")) else context.browser
      if bstack1111l1111l_opy_ and bstack1111l1111l_opy_.session_id and bstack11lll11l1_opy_ and bstack1l1l1l1l_opy_(
              threading.current_thread(), bstack1l1lll1_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᬷ"), None):
          threading.current_thread().isA11yTest = bstack1lll1ll1l_opy_.bstack11lllll111_opy_(bstack1111l1111l_opy_, bstack11lll11l1_opy_)
    except Exception as e:
       logger.debug(bstack1l1lll1_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡧ࠱࠲ࡻࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࡀࠠࡼࡿࠪᬸ").format(str(e)))
def bstack1111lll11l_opy_(bstack1111l1111l_opy_):
    if bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨᬹ"), None) and bstack1l1l1l1l_opy_(
      threading.current_thread(), bstack1l1lll1_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫᬺ"), None) and not bstack1l1l1l1l_opy_(threading.current_thread(), bstack1l1lll1_opy_ (u"࠭ࡡ࠲࠳ࡼࡣࡸࡺ࡯ࡱࠩᬻ"), False):
      threading.current_thread().a11y_stop = True
      bstack1lll1ll1l_opy_.bstack1111lll1_opy_(bstack1111l1111l_opy_, name=bstack1l1lll1_opy_ (u"ࠢࠣᬼ"), path=bstack1l1lll1_opy_ (u"ࠣࠤᬽ"))
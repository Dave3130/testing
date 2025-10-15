# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1lllllll1_opy_
from bstack_utils.helper import bstack1l1l1l1l_opy_
logger = logging.getLogger(__name__)
def bstack1l111111ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1ll111llll_opy_(context, *args):
    tags = getattr(args[0], bstack1ll1l_opy_ (u"࠭ࡴࡢࡩࡶ᬴ࠫ"), [])
    bstack11llllll1_opy_ = bstack1lllllll1_opy_.bstack1l11l1llll_opy_(tags)
    threading.current_thread().isA11yTest = bstack11llllll1_opy_
    try:
      bstack1ll1l1l11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l111111ll_opy_(bstack1ll1l_opy_ (u"ࠧࡣࡵࡷࡥࡨࡱࡓࡦࡵࡶ࡭ࡴࡴࡄࡳ࡫ࡹࡩࡷ࠭ᬵ")) else context.browser
      if bstack1ll1l1l11l_opy_ and bstack1ll1l1l11l_opy_.session_id and bstack11llllll1_opy_ and bstack1l1l1l1l_opy_(
              threading.current_thread(), bstack1ll1l_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧᬶ"), None):
          threading.current_thread().isA11yTest = bstack1lllllll1_opy_.bstack1lll11ll11_opy_(bstack1ll1l1l11l_opy_, bstack11llllll1_opy_)
    except Exception as e:
       logger.debug(bstack1ll1l_opy_ (u"ࠩࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡹࡴࡢࡴࡷࠤࡦ࠷࠱ࡺࠢ࡬ࡲࠥࡨࡥࡩࡣࡹࡩ࠿ࠦࡻࡾࠩᬷ").format(str(e)))
def bstack11l1llllll_opy_(bstack1ll1l1l11l_opy_):
    if bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠪ࡭ࡸࡇ࠱࠲ࡻࡗࡩࡸࡺࠧᬸ"), None) and bstack1l1l1l1l_opy_(
      threading.current_thread(), bstack1ll1l_opy_ (u"ࠫࡦ࠷࠱ࡺࡒ࡯ࡥࡹ࡬࡯ࡳ࡯ࠪᬹ"), None) and not bstack1l1l1l1l_opy_(threading.current_thread(), bstack1ll1l_opy_ (u"ࠬࡧ࠱࠲ࡻࡢࡷࡹࡵࡰࠨᬺ"), False):
      threading.current_thread().a11y_stop = True
      bstack1lllllll1_opy_.bstack1lllll111_opy_(bstack1ll1l1l11l_opy_, name=bstack1ll1l_opy_ (u"ࠨࠢᬻ"), path=bstack1ll1l_opy_ (u"ࠢࠣᬼ"))
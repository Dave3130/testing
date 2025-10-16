# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1lll1lll1_opy_
from bstack_utils.helper import bstack1lll1l11_opy_
logger = logging.getLogger(__name__)
def bstack1111l1l11l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack111ll1lll1_opy_(context, *args):
    tags = getattr(args[0], bstack1lllll1_opy_ (u"ࠬࡺࡡࡨࡵࠪᬺ"), [])
    bstack111111111_opy_ = bstack1lll1lll1_opy_.bstack11l1ll1lll_opy_(tags)
    threading.current_thread().isA11yTest = bstack111111111_opy_
    try:
      bstack11l1l1l111_opy_ = threading.current_thread().bstackSessionDriver if bstack1111l1l11l_opy_(bstack1lllll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬᬻ")) else context.browser
      if bstack11l1l1l111_opy_ and bstack11l1l1l111_opy_.session_id and bstack111111111_opy_ and bstack1lll1l11_opy_(
              threading.current_thread(), bstack1lllll1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭ᬼ"), None):
          threading.current_thread().isA11yTest = bstack1lll1lll1_opy_.bstack1111lll1l_opy_(bstack11l1l1l111_opy_, bstack111111111_opy_)
    except Exception as e:
       logger.debug(bstack1lllll1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡥ࠶࠷ࡹࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨ࠾ࠥࢁࡽࠨᬽ").format(str(e)))
def bstack1l111llll1_opy_(bstack11l1l1l111_opy_):
    if bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭ᬾ"), None) and bstack1lll1l11_opy_(
      threading.current_thread(), bstack1lllll1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩᬿ"), None) and not bstack1lll1l11_opy_(threading.current_thread(), bstack1lllll1_opy_ (u"ࠫࡦ࠷࠱ࡺࡡࡶࡸࡴࡶࠧᭀ"), False):
      threading.current_thread().a11y_stop = True
      bstack1lll1lll1_opy_.bstack1111l1ll_opy_(bstack11l1l1l111_opy_, name=bstack1lllll1_opy_ (u"ࠧࠨᭁ"), path=bstack1lllll1_opy_ (u"ࠨࠢᭂ"))
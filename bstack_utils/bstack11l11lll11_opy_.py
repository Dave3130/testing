# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack111llll1_opy_
from bstack_utils.helper import bstack1ll11l1l_opy_
logger = logging.getLogger(__name__)
def bstack1l1lll1ll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1111ll11ll_opy_(context, *args):
    tags = getattr(args[0], bstack11l11l1_opy_ (u"ࠬࡺࡡࡨࡵࠪ᭏"), [])
    bstack1l1lllll1_opy_ = bstack111llll1_opy_.bstack11l1l1l1l_opy_(tags)
    threading.current_thread().isA11yTest = bstack1l1lllll1_opy_
    try:
      bstack1ll1lll11l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lll1ll_opy_(bstack11l11l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ᭐")) else context.browser
      if bstack1ll1lll11l_opy_ and bstack1ll1lll11l_opy_.session_id and bstack1l1lllll1_opy_ and bstack1ll11l1l_opy_(
              threading.current_thread(), bstack11l11l1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭᭑"), None):
          threading.current_thread().isA11yTest = bstack111llll1_opy_.bstack11l111ll1l_opy_(bstack1ll1lll11l_opy_, bstack1l1lllll1_opy_)
    except Exception as e:
       logger.debug(bstack11l11l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡥ࠶࠷ࡹࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨ࠾ࠥࢁࡽࠨ᭒").format(str(e)))
def bstack1l111111ll_opy_(bstack1ll1lll11l_opy_):
    if bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭᭓"), None) and bstack1ll11l1l_opy_(
      threading.current_thread(), bstack11l11l1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ᭔"), None) and not bstack1ll11l1l_opy_(threading.current_thread(), bstack11l11l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡡࡶࡸࡴࡶࠧ᭕"), False):
      threading.current_thread().a11y_stop = True
      bstack111llll1_opy_.bstack111ll11l_opy_(bstack1ll1lll11l_opy_, name=bstack11l11l1_opy_ (u"ࠧࠨ᭖"), path=bstack11l11l1_opy_ (u"ࠨࠢ᭗"))
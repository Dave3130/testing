# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack11l1111l_opy_
from bstack_utils.helper import bstack11lll111_opy_
logger = logging.getLogger(__name__)
def bstack11llll1ll1_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1l11l111ll_opy_(context, *args):
    tags = getattr(args[0], bstack1l1_opy_ (u"ࠬࡺࡡࡨࡵࠪ᭏"), [])
    bstack11l1l1l1l_opy_ = bstack11l1111l_opy_.bstack1lll1111ll_opy_(tags)
    threading.current_thread().isA11yTest = bstack11l1l1l1l_opy_
    try:
      bstack1l1ll1l1ll_opy_ = threading.current_thread().bstackSessionDriver if bstack11llll1ll1_opy_(bstack1l1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ᭐")) else context.browser
      if bstack1l1ll1l1ll_opy_ and bstack1l1ll1l1ll_opy_.session_id and bstack11l1l1l1l_opy_ and bstack11lll111_opy_(
              threading.current_thread(), bstack1l1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭᭑"), None):
          threading.current_thread().isA11yTest = bstack11l1111l_opy_.bstack1l111111l_opy_(bstack1l1ll1l1ll_opy_, bstack11l1l1l1l_opy_)
    except Exception as e:
       logger.debug(bstack1l1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡥ࠶࠷ࡹࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨ࠾ࠥࢁࡽࠨ᭒").format(str(e)))
def bstack1l1llllll1_opy_(bstack1l1ll1l1ll_opy_):
    if bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭᭓"), None) and bstack11lll111_opy_(
      threading.current_thread(), bstack1l1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ᭔"), None) and not bstack11lll111_opy_(threading.current_thread(), bstack1l1_opy_ (u"ࠫࡦ࠷࠱ࡺࡡࡶࡸࡴࡶࠧ᭕"), False):
      threading.current_thread().a11y_stop = True
      bstack11l1111l_opy_.bstack111ll11l_opy_(bstack1l1ll1l1ll_opy_, name=bstack1l1_opy_ (u"ࠧࠨ᭖"), path=bstack1l1_opy_ (u"ࠨࠢ᭗"))
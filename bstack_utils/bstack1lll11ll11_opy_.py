# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1lllll1l1_opy_
from bstack_utils.helper import bstack1l111l1l_opy_
logger = logging.getLogger(__name__)
def bstack1l11ll1l11_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1111l1llll_opy_(context, *args):
    tags = getattr(args[0], bstack11l1l11_opy_ (u"ࠬࡺࡡࡨࡵࠪ᭖"), [])
    bstack1l1l11ll1_opy_ = bstack1lllll1l1_opy_.bstack1l111lll11_opy_(tags)
    threading.current_thread().isA11yTest = bstack1l1l11ll1_opy_
    try:
      bstack1l111l111l_opy_ = threading.current_thread().bstackSessionDriver if bstack1l11ll1l11_opy_(bstack11l1l11_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ᭗")) else context.browser
      if bstack1l111l111l_opy_ and bstack1l111l111l_opy_.session_id and bstack1l1l11ll1_opy_ and bstack1l111l1l_opy_(
              threading.current_thread(), bstack11l1l11_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭᭘"), None):
          threading.current_thread().isA11yTest = bstack1lllll1l1_opy_.bstack11l111111_opy_(bstack1l111l111l_opy_, bstack1l1l11ll1_opy_)
    except Exception as e:
       logger.debug(bstack11l1l11_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡥ࠶࠷ࡹࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨ࠾ࠥࢁࡽࠨ᭙").format(str(e)))
def bstack111lllll11_opy_(bstack1l111l111l_opy_):
    if bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭᭚"), None) and bstack1l111l1l_opy_(
      threading.current_thread(), bstack11l1l11_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ᭛"), None) and not bstack1l111l1l_opy_(threading.current_thread(), bstack11l1l11_opy_ (u"ࠫࡦ࠷࠱ࡺࡡࡶࡸࡴࡶࠧ᭜"), False):
      threading.current_thread().a11y_stop = True
      bstack1lllll1l1_opy_.bstack1111l111_opy_(bstack1l111l111l_opy_, name=bstack11l1l11_opy_ (u"ࠧࠨ᭝"), path=bstack11l1l11_opy_ (u"ࠨࠢ᭞"))
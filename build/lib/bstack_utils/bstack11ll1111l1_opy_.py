# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack111ll11l_opy_
from bstack_utils.helper import bstack1lll111l_opy_
logger = logging.getLogger(__name__)
def bstack11lll1111_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack11111lll1_opy_(context, *args):
    tags = getattr(args[0], bstack11lll1_opy_ (u"ࠬࡺࡡࡨࡵࠪ᭖"), [])
    bstack11ll111l11_opy_ = bstack111ll11l_opy_.bstack11111l1ll_opy_(tags)
    threading.current_thread().isA11yTest = bstack11ll111l11_opy_
    try:
      bstack11l1l1l1l1_opy_ = threading.current_thread().bstackSessionDriver if bstack11lll1111_opy_(bstack11lll1_opy_ (u"࠭ࡢࡴࡶࡤࡧࡰ࡙ࡥࡴࡵ࡬ࡳࡳࡊࡲࡪࡸࡨࡶࠬ᭗")) else context.browser
      if bstack11l1l1l1l1_opy_ and bstack11l1l1l1l1_opy_.session_id and bstack11ll111l11_opy_ and bstack1lll111l_opy_(
              threading.current_thread(), bstack11lll1_opy_ (u"ࠧࡢ࠳࠴ࡽࡕࡲࡡࡵࡨࡲࡶࡲ࠭᭘"), None):
          threading.current_thread().isA11yTest = bstack111ll11l_opy_.bstack1l11ll1l1_opy_(bstack11l1l1l1l1_opy_, bstack11ll111l11_opy_)
    except Exception as e:
       logger.debug(bstack11lll1_opy_ (u"ࠨࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸࡺࡡࡳࡶࠣࡥ࠶࠷ࡹࠡ࡫ࡱࠤࡧ࡫ࡨࡢࡸࡨ࠾ࠥࢁࡽࠨ᭙").format(str(e)))
def bstack1ll111l11l_opy_(bstack11l1l1l1l1_opy_):
    if bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠩ࡬ࡷࡆ࠷࠱ࡺࡖࡨࡷࡹ࠭᭚"), None) and bstack1lll111l_opy_(
      threading.current_thread(), bstack11lll1_opy_ (u"ࠪࡥ࠶࠷ࡹࡑ࡮ࡤࡸ࡫ࡵࡲ࡮ࠩ᭛"), None) and not bstack1lll111l_opy_(threading.current_thread(), bstack11lll1_opy_ (u"ࠫࡦ࠷࠱ࡺࡡࡶࡸࡴࡶࠧ᭜"), False):
      threading.current_thread().a11y_stop = True
      bstack111ll11l_opy_.bstack1lll1lll1_opy_(bstack11l1l1l1l1_opy_, name=bstack11lll1_opy_ (u"ࠧࠨ᭝"), path=bstack11lll1_opy_ (u"ࠨࠢ᭞"))
# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack1111111l_opy_
from bstack_utils.helper import bstack1llll11l_opy_
logger = logging.getLogger(__name__)
def bstack111l11l1l_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack111l1ll1ll_opy_(context, *args):
    tags = getattr(args[0], bstack11l1111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᮅ"), [])
    bstack11l111ll11_opy_ = bstack1111111l_opy_.bstack1l11l11ll1_opy_(tags)
    threading.current_thread().isA11yTest = bstack11l111ll11_opy_
    try:
      bstack1ll1ll111_opy_ = threading.current_thread().bstackSessionDriver if bstack111l11l1l_opy_(bstack11l1111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪᮆ")) else context.browser
      if bstack1ll1ll111_opy_ and bstack1ll1ll111_opy_.session_id and bstack11l111ll11_opy_ and bstack1llll11l_opy_(
              threading.current_thread(), bstack11l1111_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫᮇ"), None):
          threading.current_thread().isA11yTest = bstack1111111l_opy_.bstack111111ll11_opy_(bstack1ll1ll111_opy_, bstack11l111ll11_opy_)
    except Exception as e:
       logger.debug(bstack11l1111_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡣ࠴࠵ࡾࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦ࠼ࠣࡿࢂ࠭ᮈ").format(str(e)))
def bstack1111ll1111_opy_(bstack1ll1ll111_opy_):
    if bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫᮉ"), None) and bstack1llll11l_opy_(
      threading.current_thread(), bstack11l1111_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧᮊ"), None) and not bstack1llll11l_opy_(threading.current_thread(), bstack11l1111_opy_ (u"ࠩࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࠬᮋ"), False):
      threading.current_thread().a11y_stop = True
      bstack1111111l_opy_.bstack1lll1l111_opy_(bstack1ll1ll111_opy_, name=bstack11l1111_opy_ (u"ࠥࠦᮌ"), path=bstack11l1111_opy_ (u"ࠦࠧᮍ"))
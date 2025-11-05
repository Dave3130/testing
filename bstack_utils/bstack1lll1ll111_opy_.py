# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack111111l1_opy_
from bstack_utils.helper import bstack1lll1lll_opy_
logger = logging.getLogger(__name__)
def bstack11l111llll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack1ll1ll111_opy_(context, *args):
    tags = getattr(args[0], bstack11111_opy_ (u"ࠪࡸࡦ࡭ࡳࠨᮅ"), [])
    bstack11l11111ll_opy_ = bstack111111l1_opy_.bstack1llll1ll11_opy_(tags)
    threading.current_thread().isA11yTest = bstack11l11111ll_opy_
    try:
      bstack11lll1111l_opy_ = threading.current_thread().bstackSessionDriver if bstack11l111llll_opy_(bstack11111_opy_ (u"ࠫࡧࡹࡴࡢࡥ࡮ࡗࡪࡹࡳࡪࡱࡱࡈࡷ࡯ࡶࡦࡴࠪᮆ")) else context.browser
      if bstack11lll1111l_opy_ and bstack11lll1111l_opy_.session_id and bstack11l11111ll_opy_ and bstack1lll1lll_opy_(
              threading.current_thread(), bstack11111_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫᮇ"), None):
          threading.current_thread().isA11yTest = bstack111111l1_opy_.bstack11l1lll11_opy_(bstack11lll1111l_opy_, bstack11l11111ll_opy_)
    except Exception as e:
       logger.debug(bstack11111_opy_ (u"࠭ࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡸࡦࡸࡴࠡࡣ࠴࠵ࡾࠦࡩ࡯ࠢࡥࡩ࡭ࡧࡶࡦ࠼ࠣࡿࢂ࠭ᮈ").format(str(e)))
def bstack1l1ll1l1l1_opy_(bstack11lll1111l_opy_):
    if bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠧࡪࡵࡄ࠵࠶ࡿࡔࡦࡵࡷࠫᮉ"), None) and bstack1lll1lll_opy_(
      threading.current_thread(), bstack11111_opy_ (u"ࠨࡣ࠴࠵ࡾࡖ࡬ࡢࡶࡩࡳࡷࡳࠧᮊ"), None) and not bstack1lll1lll_opy_(threading.current_thread(), bstack11111_opy_ (u"ࠩࡤ࠵࠶ࡿ࡟ࡴࡶࡲࡴࠬᮋ"), False):
      threading.current_thread().a11y_stop = True
      bstack111111l1_opy_.bstack1lll1l1ll_opy_(bstack11lll1111l_opy_, name=bstack11111_opy_ (u"ࠥࠦᮌ"), path=bstack11111_opy_ (u"ࠦࠧᮍ"))
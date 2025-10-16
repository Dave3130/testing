# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import threading
import logging
import bstack_utils.accessibility as bstack11111ll1_opy_
from bstack_utils.helper import bstack1llll11l_opy_
logger = logging.getLogger(__name__)
def bstack1l1lllllll_opy_(key_name):
  return True if key_name in threading.current_thread().__dict__.keys() else False
def bstack11l11llll_opy_(context, *args):
    tags = getattr(args[0], bstack1l_opy_ (u"ࠧࡵࡣࡪࡷࠬᬼ"), [])
    bstack111lll1ll1_opy_ = bstack11111ll1_opy_.bstack111l11l11_opy_(tags)
    threading.current_thread().isA11yTest = bstack111lll1ll1_opy_
    try:
      bstack1l111l1ll1_opy_ = threading.current_thread().bstackSessionDriver if bstack1l1lllllll_opy_(bstack1l_opy_ (u"ࠨࡤࡶࡸࡦࡩ࡫ࡔࡧࡶࡷ࡮ࡵ࡮ࡅࡴ࡬ࡺࡪࡸࠧᬽ")) else context.browser
      if bstack1l111l1ll1_opy_ and bstack1l111l1ll1_opy_.session_id and bstack111lll1ll1_opy_ and bstack1llll11l_opy_(
              threading.current_thread(), bstack1l_opy_ (u"ࠩࡤ࠵࠶ࡿࡐ࡭ࡣࡷࡪࡴࡸ࡭ࠨᬾ"), None):
          threading.current_thread().isA11yTest = bstack11111ll1_opy_.bstack1111l111l1_opy_(bstack1l111l1ll1_opy_, bstack111lll1ll1_opy_)
    except Exception as e:
       logger.debug(bstack1l_opy_ (u"ࠪࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡵࡣࡵࡸࠥࡧ࠱࠲ࡻࠣ࡭ࡳࠦࡢࡦࡪࡤࡺࡪࡀࠠࡼࡿࠪᬿ").format(str(e)))
def bstack1ll111l111_opy_(bstack1l111l1ll1_opy_):
    if bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"ࠫ࡮ࡹࡁ࠲࠳ࡼࡘࡪࡹࡴࠨᭀ"), None) and bstack1llll11l_opy_(
      threading.current_thread(), bstack1l_opy_ (u"ࠬࡧ࠱࠲ࡻࡓࡰࡦࡺࡦࡰࡴࡰࠫᭁ"), None) and not bstack1llll11l_opy_(threading.current_thread(), bstack1l_opy_ (u"࠭ࡡ࠲࠳ࡼࡣࡸࡺ࡯ࡱࠩᭂ"), False):
      threading.current_thread().a11y_stop = True
      bstack11111ll1_opy_.bstack111l1ll1_opy_(bstack1l111l1ll1_opy_, name=bstack1l_opy_ (u"ࠢࠣᭃ"), path=bstack1l_opy_ (u"ࠣࠤ᭄"))